from django.http import HttpResponse, JsonResponse
from django.template import loader

from .models import Ajjaxdemoo

def index(request):
    likenum = Ajjaxdemoo.objects.get(user="abc")
    template = loader.get_template('web3/index.html')
    context = {
        'likenumber': likenum.likee,
    }
    return HttpResponse(template.render(context, request))

def increaseActionNumber(request):
    record = Ajjaxdemoo.objects.get(user="abc")
    record.likee += 1
    record.save()
    return HttpResponse("success")

def getActionNumber(request):
    record = Ajjaxdemoo.objects.get(user="abc")
    data = {
        'user': record.user,
        'likenumber':record.likee,
    }
    return HttpResponse(record.likee, content_type="text/plain")