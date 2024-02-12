import subprocess
import os
import argparse

from git import Repo, BadName


def bisect(path_to_repo, start_hash, end_hash, command):
    check_path_to_repo(path_to_repo)
    os.chdir(path_to_repo)
    repo = Repo("D:\\PyCharmProjects\\test_for_bisect")

    check_hash(start_hash, repo)
    check_hash(end_hash, repo)

    commits = get_previous_commits(path_to_repo, end_hash)

    last_bug = str()

    l, r = 0, len(commits) - 1

    while l + 1 != r:
        pivot = (l + r) // 2
        repo.git.reset(commits[pivot])
        repo.git.checkout('.')
        if exec_command(command):
            l = pivot
        else:
            r = pivot
            last_bug = commits[pivot]

    repo.git.reset(end_hash)
    repo.git.checkout('.')

    return last_bug


def get_previous_commits(repo_path, commit_hash):
    repo = Repo(repo_path)
    commit = repo.commit(commit_hash)

    previous_commits_hashes = [commit.hexsha]
    while commit.parents:
        commit = commit.parents[0]
        previous_commits_hashes.append(commit.hexsha)

    return previous_commits_hashes[::-1]


def check_path_to_repo(path_to_repo):
    if not os.path.isdir(path_to_repo):
        raise ValueError(f"{path_to_repo} is not a directory")

    if not os.path.exists(os.path.join(path_to_repo, ".git")):
        raise ValueError(f"{path_to_repo} is not a Git repository")

    return True


def check_hash(hash, repo):
    try:
        commit = repo.commit(hash)
    except BadName:
        raise ValueError(f"Commit hash - {hash} is not valid")

    return True


def exec_command(command):
    try:
        subprocess.check_call(command, shell=True, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False


parser = argparse.ArgumentParser()
parser.add_argument('path_to_repo')
parser.add_argument('start_hash')
parser.add_argument('end_hash')
parser.add_argument('command', nargs='+')
args = parser.parse_args()

print("First bad commit - ", bisect(args.path_to_repo, args.start_hash, args.end_hash, args.command))
