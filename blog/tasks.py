from celery import task
import subprocess

@task
def update_work():
    shell = subprocess.Popen("/usr/disoul/works/disoul-blog/blog/pushtask.sh",shell=True)
    return shell.wait()
