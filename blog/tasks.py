from celery import task
import shlex,subprocess

@task
def update_work():
    git = subprocess.Popen(shlex.split("git pull origin master"))
    update = subprocess.Popen(shlex.split("python /usr/disoul/works/disoul-blog/add_article.py"))
    static = subprocess.Popen(shlex.split("python /usr/disoul/works/disoul-blog/manage.py collectstatic"),stdin=subprocess.PIPE)
    static.stdin.write('yes\n')
    uwsgi = subprocess.Popen(shlex.split("/usr/disoul/works/disoul-blog/uwsgi_control.sh restart"))
    return git.wait()+update.wait()+static.wait()+uwsgi.wait()
