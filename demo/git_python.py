# https://pygithub.readthedocs.io/en/stable/introduction.html
# https://medium.com/clarusway/how-to-use-git-github-without-asking-for-authentication-always-passwordless-usage-of-private-git-8c32489bc2e9

from git import Repo
import pathlib
import shutil
import os


def remove_directory(path):
    if os.path.exists(path):
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                file_path = os.path.join(root, name)
                os.remove(file_path)
            for name in dirs:
                dir_path = os.path.join(root, name)
                os.rmdir(dir_path)
        os.rmdir(path)


folder_path_base = str(pathlib.Path(__file__).parents[0].resolve().as_posix()) # .replace('/', '\\')
folder_path_git_clone = folder_path_base + '/git_clone'
print(folder_path_git_clone)

rd_path = folder_path_git_clone.replace('/', '\\')
os.system(f'''rd /s/q {rd_path}''')

# os.system(f'rd /s/q git_clone')
# Remove directory recursively
# remove_directory(folder_path_git_clone)

# shutil.rmtree(folder_path_git_clone, ignore_errors=False)
# os.rmdir(folder_path_git_clone)

#
repo_url = "https://github.com/p-d-h/python_portable.git"
repo = Repo.clone_from(repo_url, folder_path_git_clone)

gui_path = (folder_path_git_clone + '/demo/gui/call_gui.bat').replace('/', '\\')
print(gui_path)
os.system(f'''call {gui_path}''')
