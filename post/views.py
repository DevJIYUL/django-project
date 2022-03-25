from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,redirect,render
from .form import PostForm
from .models import Post

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            post.tag_set.add(*post.extract_tag_list())
            messages.success(request,"포스팅을 저장했습니다")
            return redirect(post)
    else:
        form=PostForm()

    return render(request,"post/post_form.html",{
        "form":form,
    })


def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,"post/post_detail.html",{
        "post":post,
    })

def user_page(request,username):
    page_user = get_object_or_404(get_user_model(), username= username, is_active=True)
    post_list = Post.objects.filter(author=page_user)
    post_list_count = post_list.count() # 실제 데이터베이스에 count쿼리를 던진다
    # len(post_list) post_list를 메모리에 올린 후 메모리상 리스트 개수를 반환 post갯수가 많아지면 느려질수 있다.
    return render(request,'post/user_page.html',{
        "page_user":page_user,
        "post_list":post_list,
    })