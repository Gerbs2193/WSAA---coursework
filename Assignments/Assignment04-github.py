
from git import Repo 
import os
import shutil

REPO_URL = 'git@github.com:Gerbs2193/WSAA---coursework.git'
FILE_PATH = 'Assignments/Andrew.txt'
YOUR_NAME = 'Ger'

# Remove the temporary directory if it already exists
if os.path.exists('/tmp/repo'):
    shutil.rmtree('/tmp/repo')

repo = Repo.clone_from(REPO_URL, '/tmp/repo')

with open(os.path.join('/tmp/repo', FILE_PATH), 'r') as file:
    filedata = file.read()

filedata = filedata.replace('Andrew', YOUR_NAME)

with open(os.path.join('/tmp/repo', FILE_PATH), 'w') as file:
    file.write(filedata)

try:
    repo.git.add(FILE_PATH)
    repo.git.commit('-m', 'Replace Andrew with ger')
    repo.git.push()
    print("Changes pushed successfully!")
except Exception as e:
    print(f'An error has occurred: {e}')

repo.close()
shutil.rmtree('/tmp/repo')

