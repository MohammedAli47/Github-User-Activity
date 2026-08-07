import sys
from request import getData


def printUserEvents(username: str):
    events, msg = getData(username)
    print(msg)
    if events is not None:
        if len(events) == 0:
            print("No data found")
            sys.exit(1)
        for event in events:
            event_type = event["type"]
            match event_type:
                case "PushEvent":
                    print(f"{username} pushed to {event['repo']['name']}")
                case "PullRequestEvent":
                    print(f"{username} created pull request {event['payload']['pull_request']['number']}")
                case "CreateEvent":
                    print(f"{username} created {event['payload']['ref_type']} {event['payload']['ref']}")
                case "IssueCommentEvent":
                    print(f"{username} commented on issue {event['payload']['issue']['number']}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        printUserEvents(sys.argv[1])
    else:
        print("Github name was not provided")
