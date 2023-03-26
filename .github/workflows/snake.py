import os
from datetime import datetime, timedelta
from github import Github

# Get GitHub token from environment variable
token = os.environ['GITHUB_TOKEN']

# Create a PyGithub object using the token
g = Github(token)

# Get the authenticated user
user = g.get_user()

# Get the current date and the date one year ago
today = datetime.today().strftime('%Y-%m-%d')
last_year = (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')

# Loop through each day in the last year
for date in (datetime.strptime(last_year, '%Y-%m-%d') + timedelta(n) for n in range(366)):
    # Get the number of commits on this day
    num_commits = len(list(user.get_commits(since=date, until=(date + timedelta(days=1)))))

    # Create the contribution string for this day
    if num_commits > 0:
        contribution = 'H' * min(num_commits // 2, 4)
        if num_commits % 2 == 1:
            contribution += 'h'
    else:
        contribution = ' '

    # Update the contribution graph for this day
    user.create_repository_invitation("snake",date);
    g.get_repo(user.login+"/snake").create_file("README.md","Update README.md",contribution,branch="main",committer={'name': 'Snake Bot', 'email': 'snakebot@github.com'},author={'name': 'Snake Bot', 'email': 'snakebot@github.com'})

