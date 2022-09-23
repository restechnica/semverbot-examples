import subprocess
import pathlib
from invoke import task


@task
def get_version(c):
    current_dir = pathlib.Path(__file__).parent.resolve()
    with open(f"{current_dir}/src/settings/version.py", "w") as file:
        version = subprocess.run(["sbot", "get" ,"version"], stdout=subprocess.PIPE)
        file.write(f'VERSION = "{version.stdout.decode().strip()}"')


@task 
def deploy(c):
    #do stuff 
    print("Deployed!")