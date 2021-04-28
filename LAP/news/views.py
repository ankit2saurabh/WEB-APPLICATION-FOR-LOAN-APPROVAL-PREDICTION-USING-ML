from project.models import Project
from .models import News
from django.http.response import HttpResponse
from django.shortcuts import render, get_list_or_404, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import datetime

site = Project.objects.get(pk=2)
# Calling name from session
def sessioncallcunction(request):
    b=request.session['member_fname']
    return b

# Show the news in detialed view
def news_detail(request,id):
    b = sessioncallcunction(request)
    news = News.objects.get(pk=id)
    return render(request,'front/news_detail.html',{'site':site, 'news':news,'user':b}) #{'sitename':sitename},{'news':news}

# Show the news list
def news_list(request):
    b = sessioncallcunction(request)
    news = News.objects.all()
    if not request.user.is_superuser:
        return redirect('login')
    else:
        return render(request, 'user/news_list.html',{'news':news,'user':b})
   
# Add News into database   
def add_news(request):
    b = sessioncallcunction(request)
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    if len(str(day)) == 1:
        day = "0" + str(day)
    if len(str(month)) == 1:
        month = "0" + str(month)
    today = str(year) + "/" + str(month) + "/" + str(day)

    if not request.user.is_superuser:
        return redirect('login')
    else:
        if request.method == 'POST':
            title = request.POST.get('newstitle')
            newscat = request.POST.get('news_cat')
            shortText = request.POST.get('short_text')
            longText = request.POST.get('long_text')
            writer = request.POST.get('writername')

            if title == "" or newscat == "" or shortText == "" or longText == "":
                error = "All fields are required"
                return render(request, 'back/error.html',{'error':error,'user':b})
            try:
                myfile = request.FILES['imgfile']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                url = fs.url(filename)
                
                # if str(myfile.content_type).startswith('image'):
                if myfile.size < 5000000:
                        b = News(name=title, short_txt=shortText, body_txt=longText, date=today,picname=filename, picurl=url, Writer=writer, category=newscat, categoryid=0, show=0)
                        b.save()
                        return redirect('news_list')
                else:
                        fs.delete(filename)
                        error = "Size must be less than 5 MB..."
                        return render(request, 'user/error.html',{'error':error,'user':b})
                # else:
                #     fs.delete(filename)
                #     error = "Image type not supported by us"
                #     return render(request, 'back/error.html',{'error':error,'user':b})
            except:
                error = "Please select image"
                return render(request, 'user/error.html',{'error':error,'user':b})

        return render(request, 'user/add_news.html',{'user':b})

# Delete the news
def news_delete(request,pk):
    if not request.user.is_superuser:
        return redirect('login')
    else:
        b = News.objects.filter(pk=pk)
        b.delete()
        return redirect('news_list')

# Call news edit page
def news_edit(request,pk):
    b = sessioncallcunction(request)
    if not request.user.is_superuser:
        return redirect('login')
    else:
        global identity
        identity = pk
        news = News.objects.get(pk=pk)
        return render(request, 'user/news_edit.html',{'pk':pk, 'news':news,'user':b})

# Edit news or changes into anything into news and save that
def editData(request):
    b = sessioncallcunction(request)
    news = News.objects.get(pk=identity)
    if request.method == 'POST':
        title = request.POST.get('newstitle')
        newscat = request.POST.get('news_cat')
        shortText = request.POST.get('short_text')
        longText = request.POST.get('long_text')

        if title == "" or newscat == "" or shortText == "" or longText == "":
            error = "All fields are required"
            return render(request, 'back/error.html',{'error':error,'user':b})
        try:
            myfile = request.FILES['imgfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)
            
            # if str(myfile.content_type).startswith('image'):
            if myfile.size < 5000000:
                b = News.objects.get(pk=identity)
                fss = FileSystemStorage()
                fss.delete(b.picname)
                b.category = newscat
                b.short_txt = shortText
                b.body_txt = longText
                b.picname = filename
                b.picurl = url
                # b = News(name=title, short_txt=shortText, body_txt=longText, date=today,picname=filename, picurl=url, Writer='Ankit JI', category=newscat, categoryid=0, show=0)
                b.save()
                return redirect('news_list')
            else:
                fs.delete(filename)
                error = "Size must be less than 5 MB..."
                return render(request, 'back/error.html',{'error':error,'user':b})
            # else:
            #     fs.delete(filename)
            #     error = "Image type not supported by us"
            #     return render(request, 'back/error.html',{'error':error,'user':b})
        except:
            b = News.objects.get(pk=identity)
            b.name = title
            b.category = newscat
            b.short_txt = shortText
            b.body_txt = longText
            # b = News(name=title, short_txt=shortText, body_txt=longText, date=today,picname=filename, picurl=url, Writer='Ankit JI', category=newscat, categoryid=0, show=0)
            b.save()
            return redirect('news_list')
    news = News.objects.all()
    return render(request, 'back/news_list.html',{'news':news,'user':b})