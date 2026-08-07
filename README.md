
# GitHub User Activity

Implementation of Project idea https://roadmap.sh/projects/github-user-activity on Roadmap.sh

Overview
--------

This repository contains two small Python scripts that fetch and print a GitHub user's recent public events using the GitHub Events API:

- `main.py`: command-line entry point. Reads a username argument and prints human-readable messages for several event types.
- `request.py`: handles the HTTP request to GitHub and returns parsed JSON.

Key behavior
------------

- `main.py` expects a single positional argument (the GitHub username). If none is provided it prints "Github name was not provided".
- `main.py` calls `getData(username)` from `request.py`, prints the returned status message, and iterates events (if any). It recognizes these event types and prints concise messages:
	- `PushEvent` — prints that the user pushed to a repo
	- `PullRequestEvent` — prints PR number
	- `CreateEvent` — prints created ref type and name
	- `IssueCommentEvent` — prints commented issue number
- If `getData` returns an empty list, `main.py` prints "No data found" and exits with code 1.

Implementation details
----------------------

- `request.py` uses `urllib.request.urlopen` and `json.loads` to fetch `https://api.github.com/users/{username}/events` and return `(data, message)`.
- The code does not use the `requests` library or any third-party dependency.
- Because `request.py` does not send authentication headers, it is subject to GitHub's unauthenticated rate limits (usually 60 requests per hour per IP). HTTP errors are caught and cause `getData` to return `(None, "Data not fetched successfully")`.

Requirements
------------

- Python 3.10 or newer (uses the `match` statement and `|` union typing).
- No external packages required.

Usage
-----

Run the script from the repository root:

```powershell
python main.py <github-username>
```

Examples
--------

```powershell
python main.py octocat
```
