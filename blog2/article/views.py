from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PostForm
from .models import Article


@login_required
def post_create(request):
		
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		# message success
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)

@login_required
def post_detail(request, pk=None):
	instance = get_object_or_404(Article, pk=pk)

	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "post_detail.html", context)


@login_required
def post_list(request):
	queryset_list = Article.objects.all()
	
	paginator = Paginator(queryset_list, 8) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)


	context = {
		"object_list": queryset, 
		"title": "List",
		"page_request_var": page_request_var,
	}
	return render(request, "post_list.html", context)




@login_required
def post_update(request, pk=None):

	instance = get_object_or_404(Article, pk=pk)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, "post_form.html", context)


@login_required
def post_delete(request, pk=None):

	instance = get_object_or_404(Article, pk=pk)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("posts:list")


@login_required
def users_list(request):

	instance = User.objects.all()

	return render(request, "users_list.html", {"instance": instance})

@login_required
def user_article(request, pk=None):

	instance = Article.objects.filter(user=pk)

	return render(request, "user_article.html", {'instance': instance})
