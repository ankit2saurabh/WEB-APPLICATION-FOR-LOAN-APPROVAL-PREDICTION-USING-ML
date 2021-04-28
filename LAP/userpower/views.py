from project.models import Project, Services, Signup, contact, subscribe, eligblity
from django.http.response import HttpResponse
from django.shortcuts import render, get_list_or_404, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import datetime

userMessage = contact.objects.all()
alluserchechedloan = eligblity.objects.all()
userreg = Signup.objects.all()
# TODO Admin check how many user chek their eligblity
def eligblityUser(request):
    b=request.session['member_fname']
    return render(request, 'user/eligble.html',{'people':alluserchechedloan,'user':b})

# TODO Admin check how many user registered
def existuser(request):
    b=request.session['member_fname']
    return render(request, 'user/registereduser.html',{'reg_user':userreg,'user':b})

# TODO Admin read messages
def messageRead(request):
    b=request.session['member_fname']
    return render(request, 'user/index2.html',{'userMessage':userMessage,'user':b})


# Delete message
def message_delete(request,pk):
    if not request.user.is_superuser:
        return redirect('login')
    else:
        b = contact.objects.filter(pk=pk)
        b.delete()
        return redirect('messageRead')

# Call news edit page
def user_edit(request,pk):
    b = request.session['member_fname']
    if not request.user.is_superuser:
        return redirect('login')
    else:
        global identity
        identity = pk
        userdata = Signup.objects.get(pk=pk)
        return render(request, 'user/useredit.html',{'pk':pk, 'userdata':userdata,'user':b})

# Edit news or changes into anything into news and save that
def edituserData(request):
    print(identity)
    b = request.session['member_fname']
    user = Signup.objects.get(pk=identity)
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        fatName = request.POST.get('fatherName')
        dofb = request.POST.get('dob')
        mno = request.POST.get('mno')
        mail = request.POST.get('mail')

        if firstname == "" or lastname == "" or fatName == "" or dofb == "" or mno == "" or mail == "":
            error = "All fields are required"
            return render(request, 'user/error.html',{'error':error,'user':b})
        else:
            b = Signup.objects.get(pk=identity)
            b.fname = firstname
            b.lname = lastname
            b.fathername = fatName
            b.dob = dofb
            b.mobnum = mno
            b.email = mail
            passworduser = b.password
            # To update user in a local Database
            b = Signup(fname=firstname, lname=lastname, fathername=fatName, dob=dofb, mobnum=mno, email=mail, password=passworduser)
            b.save()
            return redirect('existuser')


def user_delete(request,pk):
    if not request.user.is_superuser:
        return redirect('login')
    else:
        b = Signup.objects.filter(pk=pk)
        b.delete()
        return redirect('existuser')