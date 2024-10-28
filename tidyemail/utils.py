import imaplib
import email
import os
from email.header import decode_header
import re
import json

def connect_to_imap_server(imap_server, imap_port, username, password, verbose=None):
    """
    Connect to the ProtonMail Bridge server and login.

    Args:
        imap_server (str): The IMAP server address
        imap_port (int): The IMAP server port
        username (str): The username from your ProtonMail Bridge account
        password (str): The password from your ProtonMail Bridge account
        verbose (bool, optional): Whether to print the email content. Defaults to None.

    Returns:
        IMAP4: An instance of the IMAP4 class for the server connection.
    """
    try:
        # Connect to the server
        mail = imaplib.IMAP4(imap_server, imap_port)
        if verbose: print("Connected to the server.")
        # Login to your account
        mail.login(username, password)
        if verbose: print("Logged in successfully.")
        return mail
    except imaplib.IMAP4.error as e:
        print(f"IMAP error: {e}")
        return

def fetch_emails(mail, start_date, end_date, folder_name="INBOX", search_criteria=None, max_emails=20, verbose=None):
    """
    Fetch emails from the specified folder on the ProtonMail Bridge server based on the search criteria.

    Args:
        mail (IMAP4): The IMAP4 connection object
        folder_name (str, optional): The name of the folder to fetch emails from. Defaults to "INBOX".
        start_date (str): The start date for the search in 'dd-MMM-yyyy' format
        end_date (str): The end date for the search in 'dd-MMM-yyyy' format
        search_criteria (str, optional): The search criteria for fetching emails. Defaults to None.
        max_emails (int, optional): The maximum number of emails to fetch. Defaults to 20.
        verbose (bool, optional): Whether to print the email content. Defaults to None.

    Returns:
        list: A list of email IDs and their corresponding messages.
    """
    try:
        # Select the specified folder
        mail.select(f'"{folder_name.replace("\"", "\\\"")}"')
        if verbose: print(f"Selected folder: {folder_name}")

        # Set default search criteria if not provided
        if not search_criteria:
            search_criteria = f'(UNSEEN SINCE {start_date} BEFORE {end_date})'
        else:
            search_criteria = f'({search_criteria} SINCE {start_date} BEFORE {end_date})'

        # Search for emails based on the search criteria
        status, messages = mail.search(None, search_criteria)
        if status != "OK":
            if verbose: print("No emails found.")
            return []

        # Convert messages to a list of email IDs
        email_ids = messages[0].split()
        email_ids = email_ids[:max_emails]  # Limit to max_emails

        emails = []
        # Loop through each email
        for email_id in email_ids:
            # Fetch the email by ID
            status, msg_data = mail.fetch(email_id, "(RFC822)")
            
            # Get the email content
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    if verbose:
                        # Print all available fields of the email
                        for header in msg.keys():
                            header_value = msg[header]
                            if header.lower() == "subject":
                                # Decode the email subject
                                subject, encoding = decode_header(header_value)[0]
                                if isinstance(subject, bytes):
                                    subject = subject.decode(encoding if encoding else "utf-8")
                                header_value = subject
                            print(f"{header}: {header_value}")
                        print("\n")
                    emails.append((email_id, msg))

        return emails

    except imaplib.IMAP4.error as e:
        print(f"IMAP error: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def mark_emails_as_read(mail, email_ids, verbose=None):
    """
    Mark emails as read on the ProtonMail Bridge server.

    Args:
        mail (IMAP4): The IMAP4 connection object
        email_ids (list): A list of email IDs to mark as read
        verbose (bool, optional): Whether to print the email content. Defaults to None.
    """
    try:
        # Loop through each email ID and mark as read
        for email_id in email_ids:
            mail.store(email_id, '+FLAGS', '\\Seen')
            if verbose: print(f"Marked email {email_id} as read.")

    except imaplib.IMAP4.error as e:
        print(f"IMAP error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


### Combined Function

def fetch_and_mark_emails(username, password, imap_server, imap_port, start_date, end_date, max_emails=20, verbose=None):
    """
    Fetch unread emails from the ProtonMail Bridge server and mark them as read.

    Args:
        username (str): The username from your ProtonMail Bridge account
        password (str): The password from your ProtonMail Bridge account
        imap_server (str): The IMAP server address
        imap_port (int): The IMAP server port
        start_date (str): The start date for the search in 'dd-MMM-yyyy' format
        end_date (str): The end date for the search in 'dd-MMM-yyyy' format
        max_emails (int, optional): The maximum number of emails to fetch. Defaults to 20.
        verbose (bool, optional): Whether to print the email content. Defaults to None.
    """
    # Connect to the server
    mail = connect_to_imap_server(imap_server, imap_port, username, password, verbose)
    if not mail:
        return

    # Fetch emails
    emails = fetch_emails(mail, start_date, end_date, max_emails, verbose)

    # Extract email IDs
    email_ids = [email_id for email_id, msg in emails]

    # Mark emails as read
    mark_emails_as_read(mail, email_ids, verbose)

    # Logout and close the connection
    mail.logout()
    if verbose: print("Logged out successfully.")

def list_folders(mail, verbose=None):
    """
    List all available folders on the IMAP server.

    Args:
        mail (IMAP4): The IMAP4 connection object
        verbose (bool, optional): Whether to print the folder names. Defaults to None.

    Returns:
        list: A list of folder names.
    """
    status, folders = mail.list()
    if status != "OK":
        print("Failed to list folders.")
        return []

    folder_names = []
    for folder in folders:
        folder_name = folder.decode().split(' "/" ')[-1]
        folder_names.append(folder_name)
        if verbose:
            print(f"Folder: {folder_name}")

    return folder_names

def move_emails(mail, email_ids, target_folder, verbose=None):
    """
    Move emails to the specified target folder on the ProtonMail Bridge server.

    Args:
        mail (IMAP4): The IMAP4 connection object
        email_ids (list): A list of email IDs to move
        target_folder (str): The name of the target folder
        verbose (bool, optional): Whether to print the email content. Defaults to None.
    """
    try:
        # Quote the target folder name to handle special characters and spaces
        # Loop through each email ID and move to the target folder
        for email_id in email_ids:
            mail.copy(email_id, f'"{target_folder.replace("\"", "\\\"")}"')
            mail.store(email_id, '+FLAGS', '\\Deleted')
            if verbose: print(f"Moved email {email_id} to {target_folder}.")

        # Expunge deleted emails
        mail.expunge()
        if verbose: print("Expunged deleted emails.")

    except imaplib.IMAP4.error as e:
        print(f"IMAP error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def domains_criteria(loc=None,bind="FROM"):
    """
    Build the search criteria string for the specified domains.

    Args:
        None

    Returns:
        str: The search criteria string.
    """
    if loc is None:
        with open(os.environ["CRITERIA_FILE"], 'r') as file:
            domains = json.load(file).get("domains", [])
    else:
        with open(loc, 'r') as file:
            domains = json.load(file).get("domains", [])
    # Start with the first domain
    if bind is None: bind = "FROM"
    criteria = f'{bind} {domains[0]}'
    
    # Combine the rest of the domains using nested OR
    for domain in domains[1:]:
        criteria = f'OR ({bind} {domain}) ({criteria})'
    
    return criteria