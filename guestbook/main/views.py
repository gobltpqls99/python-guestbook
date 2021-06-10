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



# 댓글 생성하기 
# def reply 로 request, pk 받아오기 
# posting 으로 pk=pk인 것 가져오기
# posting.html에 있는 form에 있는 input name = name, pw, reply 받아와서 넣기
# posting.coments.create 를 related_name의 comments로 create하기
# 저장 후, redirect로 posting페이지 + pk 가게 하기

def reply(request, pk):
    posting = Post.objects.get(pk=pk)
    name = request.POST['reply_name']
    pw = request.POST['reply_pw']
    reply = request.POST['reply']
    posting.comments.create(name=name, pw=pw, reply=reply)
    posting.save()
    return redirect('main:posting', pk)

# 댓글 삭제하기
# def reply_delete 로 request, pk 받기
# POST로 받는 경우
# Reply로 pk=pk 받기
# 그냥 pk로 하는 경우 Post의 pk로 받기 때문에 다른 이름을 지정하고 Reply.posting.pk 하기
# pw 받아오기
# pw가 reply의 pk가 맞을 경우 = 삭제 후, posting페이지와 pk를 지정한 이름으로 redirect하기
# GET으로 받는 경우 = delete 페이지로 가기

def reply_delete(request, pk):
    if request.method =="POST":
        reply = Reply.objects.get(pk=pk)
        post_pk = Reply.posting.pk
        pw = request.POST["reply_pw"]
        if pw == reply.pw:
            reply.delete()
            return redirect("main:posting", post_pk)
    else:
        return render(request, "main/delete.html")





def login(request):
    return render(request, "main/login.html")

def signin(request):
    return render(request, "main/signin.html")