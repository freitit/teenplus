from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
import json

from .models_from_db import Entity, HealthPost
from .forms import EntityForm

@login_required(login_url="login")
def index(request):
    list_post_id = getTopPostID(5)
    title = []
    content = []
    image = []
    for post_id in list_post_id:
        post = getPost(post_id)
        title.append(post["title"])
        content.append(post["content"])
        image.append(post["image"])

    post_list = zip(title, content, image)
    return render(request, "web3/index.html", context = {'a_post':post_list, 'username':request.user.username, 'userid':request.user.id})

def getPost(post_id):
    result = Entity.objects.get(entity_id = post_id)
    context = {
        'title': result.title,
        'content': result.content,
        'image': result.image,
    }
    return context

def getTopPostID(topNum):
    results = Entity.objects.all().order_by('-created_date')[:topNum]
    list = []
    for result in results:
        list.append(result.entity_id)
    return list

# def increaseActionNumber(request):
#     record = Ajjaxdemoo.objects.get(user="abc")
#     record.likee += 1
#     record.save()
#     return HttpResponse("success")

# def getActionNumber(request):
#     record = Ajjaxdemoo.objects.get(user="abc")
#     data = {
#         'user': record.user,
#         'likenumber':record.likee,
#     }
#     return HttpResponse(record.likee, content_type="text/plain")


# Views related to Posts of a user
def showPost(request, user_id = 1):
    posts = Entity.objects.filter(user_id = user_id)
    return render(request, "web3/show.html", {'posts':posts})

def addPost(request):
    if request.method == "POST":
        form = EntityForm(request.POST, request.FILES)
        if form.is_valid():
            try: 
                form.save()  
                return redirect('/web3')  
            except:  
                pass
    else:
        form = EntityForm()
    return render(request,'web3/addPost.html',{'form':form, 'userid':request.user.id})

def editPost(request, id):  
    post = Entity.objects.get(entity_id=id)  
    return render(request,'web3/updatePost.html', {'post':post})

def updatePost(request, id):
    post = Entity.objects.get(entity_id=id)  
    form = EntityForm(request.POST, instance=post)  
    if form.is_valid(): 
        form.save()
        return redirect("/web3/show")  
    return render(request, 'web3/updatePost.html', {'post': post})  

def removePost(request, id):
    post = Entity.objects.get(entity_id = id)
    post.delete()
    return redirect("/web3/show")

def save_uploaded_file_to_media_root(f):
    with open('%s%s' % (settings.MEDIA_ROOT,f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)