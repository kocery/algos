import shutil
import subprocess
import tempfile

from git import Repo
import os


def bisect(path_to_repo, start_hash, end_hash, command):
    check_path_to_repo(path_to_repo)
    check_hash(start_hash)
    check_hash(end_hash)
    check_command(command)

    # Инициализация

    temp_dir = create_temp_dir()
    repo = clone_repo(path_to_repo, temp_dir)

    # Поиск

    while start_hash != end_hash:
        middle_hash = get_middle_hash(start_hash, end_hash)

        # repo reset(middle_hash, hard=True)
        # https://gitpython.readthedocs.io/en/stable/reference.html?highlight=reset#module-git.refs.head

        if check_command_with_error_code(command):
            end_hash = middle_hash
        else:
            start_hash = middle_hash

    # Вывод

    print(start_hash)
    delete_temp_dir(temp_dir)

    # return start_hash


def create_temp_dir():
    temp_dir = tempfile.mkdtemp()
    return temp_dir


def delete_temp_dir(temp_dir):
    shutil.rmtree(temp_dir, ignore_errors=True)


def get_middle_hash(start_hash, end_hash):
    ## middle_hash
    return middle_hash


def check_path_to_repo(path_to_repo):
    if not os.path.isdir(path_to_repo):
        raise ValueError(f"{path_to_repo} is not a directory")

    if not os.path.exists(os.path.join(path_to_repo, ".git")):
        raise ValueError(f"{path_to_repo} is not a Git repository")

    return True


def check_command(command):
    if not os.path.isfile(command):
        raise ValueError(f"{command} is not an executable file")

    if not os.access(command, os.X_OK):
        raise ValueError(f"{command} is not executable")

    return True


def check_hash(hash):
    if not len(hash) == 40:
        raise ValueError(f"{hash} is not a valid commit hash")
    return True


def check_command_with_error_code(command):
    try:
        subprocess.check_call(command, shell=True)
        return False
    except subprocess.CalledProcessError:
        return True


def clone_repo(path_to_repo, temp_dir):
    repo = Repo.clone_from(path_to_repo, temp_dir)
    return repo
