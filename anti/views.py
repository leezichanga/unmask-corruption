from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import category, report
from .forms import CommentForm

# Create your views here.
def welcome(request):
      return render(request, 'welcome.html')


@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    return render(request, 'index.html')

def about(request):
      return render(request, 'about.html')

def comment(request):
      return render(request, 'comment.html')

@login_required(login_url="/accounts/login/")
def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = category.find_category(search_term)
        message = search_term

        return render(request,'search.html',{"message":message,"category":searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def view_category(request):
    current_user = request.user
    category = Category.get_category()
    return render(request,'category.html',{"current_user":current_user,
                                           "category":category})

@login_required(login_url='/accounts/login/')
def new_comment(request):
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.save()
            return render(request,'report.html',{"message":message})

    else:
        form = CommentForm()
        return
        render(request,'report.html',{"comment_form":comment_form})

# @login_required(login_url='/accounts/login/')
# def new_comment(request):
#     current_user = request.user
#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST,request.FILES)
#         if comment_form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.editor = user
#             comment.save()
#             return redirect(index)
#         else:
#             comment_form = CommentForm()
#             return render(request,'report.html',{"comment_form":comment_form})
