from django.shortcuts import redirect, render
# from django.utils import timezone
from .models import Post
# Create your views here.



def index(request):
    postlist = Post.objects.all()
    return render(request, 'main/index.html', {'postlist': postlist})
# def index 로 Post 받아오기, index 페이지 보여주기



def write(request):
    if request.method == "POST":
    # method를 POST로 받을 경우
        pk = request.GET.get("pk",None)
        if pk is None :
        # 새 글일 경우, 글쓰기 화면으로 넘어가서 새로 만들기
            title = request.POST['title']
            name = request.POST['name']
            content = request.POST['content']
            pw = request.POST['pw']
            # POST에서 가져오기
            new_posting = Post.objects.create(postTitle=title, name=name, content=content, pw=pw)
            # new_posting에 Post create 넣고 만들기 
            new_posting.save()
            return redirect("main:posting", new_posting.pk)
            # posting 페이지로 넘어가고 pk번호 붙이기
        else:
        # 기존 글일 경우
            posting = Post.objects.get(pk=pk)
            # posting에 넣어놓은 Post의 pk=pk 일 경우
            title = request.POST['title']
            name = request.POST['name']
            content = request.POST['content']
            pw = request.POST['pw']
            # Post의 title, name, content, pw 불러오기
            posting.postTitle = title
            posting.content = content
            # 불러온 posting을 각각 postTitle, name, content 에 넣기
            if pw == posting.pw:
            # 비밀번호가 맞을 경우
                posting.save()
                return redirect("main:posting", pk)
                #수정 후 저장
            else :
            # 비밀번호 틀린 경우, index화면으로 넘어가기
                return redirect("main:index")
    elif request.method == "GET":
    #method를 GET으로 받을 경우 
        pk = request.GET.get("pk", None)
        if pk is None:
        # 새 글일 경우, 글쓰기 페이지로 이동
            return render(request, 'main/write.html')
        else:
        # 존재하는 글일 경우, 수정페이지로 이동
            posting = Post.objects.get(pk=pk)
            return render(request, 'main/write.html', {'posting':posting})



def posting(request, pk):
    posting = Post.objects.get(pk=pk)
    return render(request, 'main/posting.html', {'posting':posting})
    # posting 페이지로 넘어가게 하기



def delete_posting(request,pk):
    if request.method == "POST":
    # method를 POST로 받을 경우
        posting = Post.objects.get(pk=pk)
        # posting에 Post pk값 받아오기
        pw = request.POST['pw']
        # pw받아오기
        if pw == posting.pw:
        # pw 가 일치한 경우
            posting.delete()
        return redirect("main:index")
        # 삭제 후, index화면으로 넘어가기
    else:
        return render(request, 'main/delete.html')
        # 비밀번호 틀린경우, delete페이지 보내기



###
    # def write(request):
    #     if request.method == "POST":
    #         pk = request.GET.get("pk", None)
    #         if pk is None:
    #             title = request.POST['title']
    #             name = request.POST['name']
    #             pw = request.POST['pw']
    #             content = request.POST['content']
    #             new_posting = Post.objects.create(title=title, name=name, pw=pw, content=content)
    #             new_posting.save()
    #             return redirect("main:write", new_posting.pk)
    #         else:
    #             posting = Post.objects.get(pk=pk)
    #             title = request.POST['title']
    #             name = request.POST['name']
    #             pw = request.POST['pw']
    #             content = request.POST['content']
    #             posting.postTitle = title
    #             posting.content = content
    #             if  pw == posting.pw:
    #                 posting.save()
    #                 return redirect("main:posting", pk)
    #             else:
    #                 return redirect("main:index")
    #     elif request.method == "GET":
    #         pk = request.GET.get("pk", None)
    #         if pk is None:
    #             return render("main/write.html")
    #         else:
    #             posting = Post.objects.get(pk=pk)
    #             return render("mani/write.html", {'posting': posting})