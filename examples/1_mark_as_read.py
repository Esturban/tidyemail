import os
import sys
from dotenv import load_dotenv
from datetime import datetime, timedelta
# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tidyemail import fetch_emails, connect_to_imap_server, list_folders, mark_emails_as_read

if __name__ == "__main__":
    load_dotenv()
    # Account credentials from ProtonMail Bridge
    username = os.environ['BRIDGE_USER']
    password = os.environ['BRIDGE_TOKEN']
    imap_server = os.environ['IMAP_SERVER']
    imap_port = int(os.environ['IMAP_PORT'])  # IMAP over ProtonMail Bridge
    # Specify the start and end dates
    start_date = (datetime.now() - timedelta(days=365*2)).strftime("%d-%b-%Y")
    end_date = datetime.now().strftime("%d-%b-%Y")  # Today
    verbose=None
    # Connect to the server
    mail = connect_to_imap_server(imap_server, imap_port, username, password, verbose=verbose)
    if not mail:
        exit()

    # List available folders
    folders = list_folders(mail)
    folder_name = os.environ['FOLDER']
    #print(folders)
    # Fetch and mark emails
    emails = fetch_emails(mail, start_date, end_date, folder_name=folder_name, max_emails = 1000, verbose=verbose)
    email_ids = [email_id for email_id, msg in emails]

    # Mark emails as read
    mark_emails_as_read(mail, email_ids, verbose=verbose)
    
    # Logout and close the connection
    mail.logout()
    print(f"{len(email_ids)} email(s) marked as read.")
    print("Logged out successfully.")