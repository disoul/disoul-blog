from django.http import HttpResponse,HttpResponseForbidden,HttpResponseBadRequest
from add_article.py import main
import shlex,subprocess


def webhook(request):
    webhook_pw = '32d64b959c130e7eac89f643d632578'
    if request.method == 'POST':
        post = request.POST
        if post[hook][config][secret] == webhook_pw:
            update_work()
            return HttpResponse("ok")
        else:
            return HttpResponseForbidden('error secret')
    else:
        return HttpResponseBadRequest('bad request')


def update_work():
    git = subprocess.Popen(shlex.split("git pull origin master"))
    update_article = subprocess.Popen(shlex.split("python 'add_article.py'"))
