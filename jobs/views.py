from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Jobs, Job
from django.http import HttpResponse
from django.utils.translation import gettext as _


def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            job = Job()
            job.title = request.POST['title']
            job.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                job.url = request.POST['url']
            else:
                job.url = 'http://' + request.POST['url']
            print("request.FILES==>")
            print(request.FILES)
            job.icon = request.FILES['icon']
            job.image = request.FILES['image']
            job.pub_date = timezone.datetime.now()
            job.user = request.user
            job.save()
            return redirect('/home')
            # return redirect('/jobs/' + str(job.id))

        else:
            return render(request, 'jobs/create.html',{'error':'All fields are required.'})
    else:
        return render(request, 'jobs/create.html')

def detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html',{'job':job})

@login_required(login_url="/accounts/signup")
def update(request, job_id):
    if request.method == 'POST':
        job = get_object_or_404(Job, pk=job_id)
        job.votes_total += 1
        job.save()
        return redirect('/jobs/' + str(job.id))

def my_view(request):
    words = ['Welcome', 'to', 'my', 'site.']
    output = _(' '.join(words))
    return HttpResponse(output)
