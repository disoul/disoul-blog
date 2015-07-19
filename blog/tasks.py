from celery import task
import shlex,subprocess

@task
def update_work():
    git = subprocess.Popen(shlex.split("git pull origin master"))
    set_ev = subprocess.Popen(shlex.split('export DJANGO_SETTINGS_MODULE="disoul_blog.settings"'))
    update = subprocess.Popen(shlex.split("python ../add_article.py"))
    return git.wait()+set_ev.wait()+update.wait()
