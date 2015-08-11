from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from magazine.forms import PostForm, CommentForm
from magazine.models import Post, Comment
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    post_list = Post.objects.all()
    return render(request, 'magazine/index.html', {
            'post_list' : post_list,
        })


def detail(request, pk):
    post = get_object_or_404(Post,pk=pk)
    messages.info(request, "새 글이 등록되었습니다.")
    return render(request, 'magazine/detail.html',{
            'post': post,
        })

@csrf_exempt
def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('magazine:index')
    else:
            form = PostForm()
    return render(request, 'magazine/forms.html',{
                'form': form,
            })

def comment_new(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            messages.info(request, "새 댓글이 등록되었습니다")
            comment.post = post
            comment.save()

            return redirect('magazine:detail',pk)
    else:
            form = CommentForm()
    return render(request, "magazine/forms.html", {
                'form':form,
        })

def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('magazine:index')
    else:
        form = PostForm(instance=post)
    return render(request, 'magazine/forms.html', {
            'form':form,
        })

def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('magazine:index')
    return render(request, 'magazine/post_delete_confirm.html', {
        })
