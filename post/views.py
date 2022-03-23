from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from .form import PostForm
from .models import Tag

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post_post = form.save(commit=False)
            post_post.author = request.user
            post_post.save()
            post_post.tag_set.add(*post_post.extract_tag_list())
            messages.success(request,"포스팅을 저장했습니다")
            return redirect("/")
    else:
        form=PostForm()

    return render(request,"post/post_form.html",{
        "form":form,
    })