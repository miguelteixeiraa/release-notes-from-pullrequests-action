import os
from github import Github

from src.release_notes_from_pullrequests import contruct_release_notes


def main():
    next_tag = os.environ['NEXT_RELEASE_TAG']
    repo_name = os.environ['GITHUB_REPOSITORY']
    token = os.environ['GITHUB_TOKEN']
    if not next_tag or not repo_name or not token:
        raise ValueError(
            'Bad environment variables. Invalid GITHUB_REPOSITORY, GITHUB_TOKEN or NEXT_RELEASE_TAG'
        )

    g = Github(token)
    repo = g.get_repo(repo_name)

    release_notes = contruct_release_notes(repo, next_tag)
    print(release_notes)


if __name__ == '__main__':
    main()
