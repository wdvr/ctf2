#!/usr/bin/env python3

from github_utils import gh_post_pr_comment
from gitutils import get_git_remote_name, get_git_repo_dir, GitRepo

def parse_args():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("pr_num", type=int)
    return parser.parse_args()

def main():
    args = parse_args()
    repo = GitRepo(get_git_repo_dir(), get_git_remote_name())
    org, project = repo.gh_owner_and_name()
    gh_post_pr_comment(org, project, args.pr_num, "Thanks for your PR!")


if __name__ == "__main__":
    print("testtest")
    main()
