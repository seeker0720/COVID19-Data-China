import os
import time
import git


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def git_init():
    git.Repo.init(path=BASE_DIR)

def git_push():
    repo = git.Repo(path=BASE_DIR)
    if len(repo.untracked_files) > 0:
        repo.index.add(items=repo.untracked_files)
        commit_info = 'add new file' 
        repo.index.commit(commit_info)
    if repo.is_dirty:
        my_git = repo.git
        my_git.add('.')
        repo.index.commit('update repo, add new data')
    remote = repo.remote()
    remote.push()
    
