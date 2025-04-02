from django.shortcuts import render
from django.utils import timezone
from .models import Volonteer
from django.shortcuts import render, get_object_or_404
def post_list(request):
    posts = Volonteer.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Volonteer, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})