from django.shortcuts import redirect, render
from .models import Post, Reply



def index(request):
    postlist = Post.objects.all()
    return render(request, 'main/index.html', {'postlist': postlist})



def write(request):
    if request.method == "POST":
        pk = request.GET.get("pk",None)
        if pk is None :
            title = request.POST['title']
            name = request.POST['name']
            content = request.POST['content']
            pw = request.POST['pw']
            new_posting = Post.objects.create(postTitle=title, name=name, content=content, pw=pw)
            new_posting.save()
            return redirect("main:posting", new_posting.pk)
        else:
            posting = Post.objects.get(pk=pk)
            title = request.POST['title']
            name = request.POST['name']
            content = request.POST['content']
            pw = request.POST['pw']
            posting.postTitle = title
            posting.name = name
            posting.content = content
            if pw == posting.pw:
                posting.save()
                return redirect("main:posting", pk)
            else :
                return redirect("main:index")
    elif request.method == "GET":
        pk = request.GET.get("pk", None)
        if pk is None:
            return render(request, 'main/write.html')
        else:
            posting = Post.objects.get(pk=pk)
            return render(request, 'main/write.html', {'posting':posting})



def posting(request, pk):
    posting = Post.objects.get(pk=pk)
    return render(request, 'main/posting.html', {'posting':posting})



def delete_posting(request,pk):
    if request.method == "POST":
        posting = Post.objects.get(pk=pk)
        pw = request.POST['pw']
        if pw == posting.pw:
            posting.delete()
        return redirect("main:index")
    else:
        return render(request, 'main/delete.html')



def reply(request, pk):
    posting = Post.objects.get(pk=pk)
    name = request.POST['reply_name']
    pw = request.POST['reply_pw']
    reply = request.POST['reply']
    posting.comments.create(name=name, pw=pw, reply=reply)
    posting.save()
    return redirect('main:posting', pk)


def reply_delete(request, pk):
    if request.method == "POST":
        reply = Reply.objects.get(pk=pk)
        post_pk = reply.posting.pk
        pw = request.POST['pw']
        if pw == reply.pw:
            reply.delete()
        return redirect("main:posting", post_pk)
    else:
        return render(request, 'main/delete.html')


