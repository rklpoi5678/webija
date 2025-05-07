from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment

# Create your views here.

#base

#-post
def post_list(request):
    order = request.GET.get('order', 'new')
    if order == 'popular':
        posts = Post.objects.all().order_by('-views')
    else:
        posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        comment = Comment.objects.create(post=post, author=request.user, content=content)
        return redirect('post_detail', pk=post.pk)
    else:
        return render(request, 'blog/add_comment_to_post.html',{'post':post})

#-choiceChipsAdd
def choice_chips_view(request):
    return render(request, 'choice_chips.html')