# https://pygithub.readthedocs.io/en/stable/introduction.html
# https://medium.com/clarusway/how-to-use-git-github-without-asking-for-authentication-always-passwordless-usage-of-private-git-8c32489bc2e9

from git import Repo
import pathlib
import shutil
import os
from registry import RegistryPythonPortable, RegistryGui


folder_path_base = str(pathlib.Path(__file__).parents[0].resolve().as_posix()) # .replace('/', '\\')
folder_path_git_clone = folder_path_base + '/git_clone'
print(folder_path_git_clone)

rd_path = folder_path_git_clone.replace('/', '\\')
os.system(f'''rd /s/q {rd_path}''')



repo_url = "https://github.com/p-d-h/python_portable.git"
repo = Repo.clone_from(repo_url, folder_path_git_clone)


registry_gui = RegistryGui()

registry_gui.gui_path = (folder_path_git_clone + '/demo/gui').replace('/', '\\')
print(registry_gui.gui_path)

# gui_path = (folder_path_git_clone + '/demo/gui/call_gui.bat').replace('/', '\\')
# print(gui_path)
# os.system(f'''call {gui_path}''')
