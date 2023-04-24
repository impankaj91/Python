from jira import JIRA

# Jira server information
JIRA_SERVER = "https://your-jira-server-url"
JIRA_USERNAME = "your-jira-username"
JIRA_PASSWORD = "your-jira-password"

# Issue information
ISSUE_TYPE = 'issuetype in ("Bug", "Improvement")'
LABEL = "Unit Tested"
NEW_STATUS = "Ready to Sit"

# List of Jira issues to update
X = ["JIRA-1", "JIRA-2", "JIRA-3"]

# Connect to Jira
jira = JIRA(server=JIRA_SERVER, basic_auth=(JIRA_USERNAME, JIRA_PASSWORD))

# Find all issues with the given issue type and label
query = f'{ISSUE_TYPE} and labels="{LABEL}"'
issues = jira.search_issues(query)

# Update the status of each issue in the list to the new status
for issue_key in X:
    issue = jira.issue(issue_key)
    if issue in issues:
        issue.update(fields={"status": {"name": NEW_STATUS}})
        print(f"Updated status of {issue.key} to '{NEW_STATUS}'")
    else:
        print(f"Could not find {issue.key} in the list of issues to update")
