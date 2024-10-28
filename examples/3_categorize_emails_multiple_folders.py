import os
import sys
from dotenv import load_dotenv
from datetime import datetime, timedelta
import json
# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tidyemail import fetch_emails, connect_to_imap_server, list_folders, move_emails,domains_criteria

if __name__ == "__main__":
    load_dotenv()
    # Account credentials from ProtonMail Bridge
    username = os.environ['BRIDGE_USER']
    password = os.environ['BRIDGE_TOKEN']
    imap_server = 'host.docker.internal' if os.path.exists('/.dockerenv') else os.environ['IMAP_SERVER']
    imap_port = int(os.environ['IMAP_PORT'])  # IMAP over ProtonMail Bridge

    # Specify the start and end dates
    start_date = (datetime.now() - timedelta(days=365*8)).strftime("%d-%b-%Y")
    end_date = datetime.now().strftime("%d-%b-%Y")  # Today
    verbose=None

    # Connect to the server
    mail = connect_to_imap_server(imap_server, imap_port, username, password, verbose=True)
    if not mail:
        exit()
    # List available folders
    #folders = list_folders(mail)
    folder_name = os.environ['FOLDER']
    
    criteria = [item.strip() for item in os.environ['CRITERIA_FILES'].split(',')]
    target_folders = [item.strip() for item in os.environ['TARGET_FOLDERS'].split(',')]
    for i in range(len(criteria)):
        # Fetch emails from a specific sender
        emails = fetch_emails(mail, start_date, end_date, folder_name=folder_name,search_criteria=domains_criteria(loc = criteria[i],bind = 'FROM'), max_emails = 1500, verbose=verbose)
        email_ids = [email_id for email_id, msg in emails]
        
        
        # Move emails to the target folder
        move_emails(mail, email_ids, target_folders[i], verbose=verbose)
        print(f"{len(email_ids)} email(s) moved to target {i}.")
        
    # Logout and close the connection
    mail.logout()
    print(f"{len(email_ids)} email(s) moved to target.")
    print("Logged out successfully.")