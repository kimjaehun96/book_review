from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm, UserForm
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
# Create your views here.
@csrf_exempt

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', { 'posts': posts })

@login_required
def new(request):
    if request.method == 'POST':
        # POST Get 차이
        form = PostForm(request.POST, request.FILES)
        post = form.save(commit=False)
        post.author= request.user.get_username()
        post.save() 
        #여기가 post.save인지 form.save인지?>>post.save 포스트를 데이터베이스에 저장!!
        return redirect('detail', post.pk)
       # return redirect('home')
    else: 
        form = PostForm()
    return render(request, 'new.html', { 'form' :  form })
        #render 넣을 땐 앞에 request

def detail(request, post_pk):
    post = Post.objects.get(pk = post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        comment = form.save(commit=False) 
        comment.post = post #이게 뭔뜻이지?
        comment.save()

        return redirect('detail', post.pk)
    else:
        # post= Post.objects.get(pk = post_pk)
        form = CommentForm()
        
        return render(request, 'detail.html', {'post': post, 'form' : form })

@login_required
def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    comment.delete()
    return redirect('detatil', post_pk)

@login_required
def edit(request, post_pk):
    post = Post.objects.get(pk= post_pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        form.save()
        return redirect('detail', post.pk)
    else:
        form = PostForm(instance = post)
    return render(request, 'edit.html', { 'form' : form })

def delete(request, post_pk):
    post= Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('home')

#auth
def signup(request):
    if request.method =='POST':
        form =UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)  #정체를 모르겠음.
            
            auth.login(request, new_user)
            return redirect('home')
        else:
            form = UserForm()
            error = "아이디가 이미 존재합니다"
            return render(request, 'registration/signup.html', {'form': form}, {'error':error})
    else:
        form = UserForm()
        
        return render(request, 'registration/signup.html', {'form': form})