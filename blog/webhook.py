from django.http import HttpResponse,HttpResponseForbidden,HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import shlex,subprocess

@csrf_exempt
def updatehook(request):
    if request.method == 'POST':
        post = request.POST
        if post['repository']['name'] == 'disoul-blog' and post['commits']['committer']['name'] == 'disoul':
            update_work()
            return HttpResponse("ok")
        else:
            return HttpResponseForbidden('error secret')
    else:
        return HttpResponseBadRequest('bad request')


def update_work():
    git = subprocess.Popen(shlex.split("git pull origin master"))
    update_article = subprocess.Popen(shlex.split("python '../add_article.py'"))
