import csv
import os
import sys
import requests

JIRA_BASE_URL = os.environ['JIRA_BASE_URL']
JIRA_API_TOKEN = os.environ['JIRA_API_TOKEN']
JIRA_USER_EMAIL = os.environ['JIRA_USER_EMAIL']

def offboard_user(email):
    url = f"{JIRA_BASE_URL}/rest/api/3/user"
    headers = {
        "Accept": "application/json"
    }
    params = {
        "accountId": email
    }
    response = requests.delete(
        url,
        auth=(JIRA_USER_EMAIL, JIRA_API_TOKEN),
        headers=headers,
        params=params
    )
    if response.status_code == 204:
        print(f"Successfully offboarded user: {email}")
    else:
        print(f"Failed to offboard user: {email}. Status code: {response.status_code}")

def main(csv_file):
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            offboard_user(row['email'])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python offboard_users.py <csv_file>")
        sys.exit(1)
    main(sys.argv[1])