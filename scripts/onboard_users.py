import csv
import os
import sys
import requests

JIRA_BASE_URL = os.environ['JIRA_BASE_URL']
JIRA_API_TOKEN = os.environ['JIRA_API_TOKEN']
JIRA_USER_EMAIL = os.environ['JIRA_USER_EMAIL']

def onboard_user(email, name):
    url = f"{JIRA_BASE_URL}/rest/api/3/user"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = {
        "emailAddress": email,
        "displayName": name
    }
    response = requests.post(
        url,
        json=payload,
        auth=(JIRA_USER_EMAIL, JIRA_API_TOKEN),
        headers=headers
    )
    if response.status_code == 201:
        print(f"Successfully onboarded user: {email}")
    else:
        print(f"Failed to onboard user: {email}. Status code: {response.status_code}")

def main(csv_file):
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            onboard_user(row['email'], row['name'])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python onboard_users.py <csv_file>")
        sys.exit(1)
    main(sys.argv[1])