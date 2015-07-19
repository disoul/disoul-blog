from celery import task
import shlex,subprocess

@task()
def update_work():
    git = subprocess.Popen(shlex.split("git pull origin master"))              
    update_article = subprocess.Popen(shlex.split("python '../add_article.py'"))
    return git.wait()+update_article.wait()
    
