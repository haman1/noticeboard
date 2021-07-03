from django.shortcuts import render, redirect
from . models import Notice
from .forms import NoticeForm
# Create your views here.


def home(request):
    notices = Notice.objects.order_by('-date_added')
    context = {'notices': notices}
    return render(request, 'notices/home.html', context)


def nform(request):
    if request.method== 'POST':
        form = NoticeForm(request.POST)

        if form.is_valid():
            new_req = Notice(noticeTitle=request.POST[''], noticedesc=request.POST['noticedesc'])
            new_req.save()
            return redirect('home')
    else:
        form = NoticeForm()

    context = {'form': form}

    return render(request, 'notices/nform.html', context)



