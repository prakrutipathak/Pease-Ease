from decimal import Context
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import DayDescriptionForm
from textblob import TextBlob
from statistics import mean
import datetime
from .utils import paginateTracks


from .decorators import  allowed_users

# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['User'])
def tracker(request):
    profile = request.user.profile
    
    dates = []
    sentiment_values = []
    tracks = profile.tracks.filter(owner = profile)
    desc = []

    for track in tracks:
        dates.append(track.date) 
        desc.append(track.body)
        sentiment_values.append(TextBlob(track.body).sentiment.polarity)
        
    if len(sentiment_values)==0 or len(dates)==0:
        total_entries = 0
        streak = 0
        sentimental_change = 0
        avg_sentimental = 0
        latest_subject = ''
        lastest_desc = ''
    
    else:

        count = 0
        x = len(dates)
        m=0

        while x:
            if datetime.date.today() == dates[x-1]:
                x-=1
                continue
            m = int(float(str(datetime.date.today() - dates[x-1]).split()[0]))
            count+=1
            if m!=count:
                m=0
                break
            x-=1
        if datetime.date.today() in dates:
            m+=1
        total_entries = len(dates)
        streak = m
        if len(sentiment_values)==1:
            sentimental_change=0
        else:
            sentimental_change = round(sentiment_values[-1]-sentiment_values[-2],2)

        avg_sentimental = round(mean(sentiment_values), 2)
        latest_subject = tracks[len(tracks)-1].subject
        lastest_desc = tracks[len(tracks)-1].body
    
    context = {'dates':dates,'sentiment_values':sentiment_values,'total_entries':total_entries,'streak':streak,'sentimental_change':sentimental_change,'avg_sentimental':avg_sentimental,'latest_subject':latest_subject,'lastest_desc':lastest_desc,'desc':desc}
    return render(request,'tracker/tracker.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['User'])
def trackerForm(request):
    profile = request.user.profile
    form = DayDescriptionForm()
    already_submitted = False
    today_date = datetime.date.today()
    dates = []
    tracks = profile.tracks.filter(owner = profile)
    for track in tracks:
        dates.append(track.date)
    
    if today_date in dates:
        already_submitted = True
    
    if already_submitted:
        messages.error(request,'You have already submitted your day description')
        return redirect('tracker')
        
    if request.method == 'POST':
        form = DayDescriptionForm(request.POST)
        
        if form.is_valid():
            day_description = form.save(commit=False)
            day_description.owner = profile
            day_description.save()
            messages.success(request,'Your Day Description was successfully submitted')
            return redirect('tracker')
        
    context={'form':form}
    return render(request,'tracker/tracker_form.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['User'])
def dayDescriptions(request):
    profile = request.user.profile
    tracks = profile.tracks.filter(owner = profile).order_by('-date')
    custom_range, tracks = paginateTracks(request, tracks, 4)
    context={'tracks':tracks,'custom_range': custom_range}
    return render(request,'tracker/trackerDescriptions.html',context)