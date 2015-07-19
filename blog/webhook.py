from django.http import HttpResponse,HttpResponseForbidden,HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from blog.tasks import update_work
import shlex,subprocess

@csrf_exempt
def updatehook(request):
    return HttpResponse("ok")
    webhook_pw = '32d64b959c130e7eac89f643d632578'
    if request.method == 'POST':
        post = request.POST
        if post['hook']['config']['secret'] == webhook_pw:
            update_work.delay()
            return HttpResponse("ok")
        else:
            return HttpResponseForbidden('error secret')
    else:
        return HttpResponseBadRequest('bad request')
