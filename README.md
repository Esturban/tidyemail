# TidyEmail

TidyEmail is a Python-based tool for managing and organizing emails using the ProtonMail Bridge. It provides functionalities to move emails to specified folders and build search criteria based on domains.

## Features

- Move emails to specified folders
- Build search criteria for emails based on domains

## Project Structure

- `data/`: Contains JSON files with email-related data.
- `examples/`: Example scripts demonstrating how to use TidyEmail.
- `tidyemail/`: Main package containing utility functions.
- `.devcontainer/`: Configuration for development container.
- `.github/`: GitHub-specific configurations and workflows.

## Usage

Refer to the example scripts in the `examples/` directory to see how to use the functionalities provided by TidyEmail.

## Installation

1. Clone the repository.
2. Set up a virtual environment:
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. copy and update `env.local`:

```sh
cp env.local .env
```

Then you'll have to update your corresponding environment variables in the process to make sure it's able to connect to your imap server.

4. Open in a devcontainer and test:

```sh
/workspaces/tidyemail # python examples/3_categorize_emails_multiple_folders.py 
Connected to the server.
Logged in successfully.
```

## License

This project is licensed under the MIT License.