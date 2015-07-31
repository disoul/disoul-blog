from celery import task
import shlex,subprocess

@task
def update_work():
    shell = subprocess.Popen(shlex.split("/usr/disoul/works/disoul-blog/blog/pushtask.sh"))
    return shell.wait()
