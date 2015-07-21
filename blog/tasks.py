from celery import task
import shlex,subprocess

@task
def update_work():
    git = subprocess.Popen(shlex.split("git pull origin master"))
    git.wait()
    update = subprocess.Popen(shlex.split("/usr/disoul/works/disoul-blog/add_article.py"))
    update.wait()
    return 1
