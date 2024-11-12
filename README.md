# Jira User Management

This repository contains scripts and workflows for automating the onboarding and offboarding of users in Jira using GitHub Actions.

## Usage

1. Create a new issue using the "User Management" template.
2. In the issue comments, use one of the following commands:
   - `/onboard filename.csv` to onboard users
   - `/offboard filename.csv` to offboard users

Replace `filename.csv` with the name of your CSV file containing user information.

## CSV File Format

The CSV file should have the following columns:
- `email`: The user's email address
- `name`: The user's full name (for onboarding only)

## Setup

1. Set up the following secrets in your GitHub repository:
   - `JIRA_BASE_URL`: Your Jira instance URL
   - `JIRA_API_TOKEN`: Your Jira API token
   - `JIRA_USER_EMAIL`: The email associated with your Jira account

2. Ensure your CSV files are accessible to the GitHub Actions runner.

## Workflows

The `.github/workflows/user_management.yaml` file contains the workflow that processes the commands and runs the appropriate scripts.

## Scripts

- `scripts/onboard_users.py`: Handles the onboarding process
- `scripts/offboard_users.py`: Handles the offboarding process

These scripts interact with the Jira API to add or remove users based on the provided CSV file.