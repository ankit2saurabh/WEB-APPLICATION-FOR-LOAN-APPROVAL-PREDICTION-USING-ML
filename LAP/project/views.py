from .models import Project, Services, Signup, contact, subscribe, eligblity,imagesdata
from django.http.response import HttpResponse
from django.shortcuts import render, get_list_or_404, redirect
from news.models import News
import random
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import pickle
import warnings
warnings.filterwarnings("ignore")
import numpy as np
from sklearn.preprocessing import StandardScaler

# Create your views here.
site = Project.objects.get(pk=2)
news = News.objects.all()
service = Services.objects.all()
userMessage = contact.objects.all()
stockimg = imagesdata.objects.get(pk=2)
# Calling Landing Page
def index(request):
    if request.method == 'POST':
        myemail = request.POST.get('mailid')
        b = subscribe(mail=myemail)
        b.save()
        messages.success(request, 'Subscribed')
    return render(request, 'front/index.html',{'site': site, 'news': news, 'service': service})  # {'sitename':sitename}

# Signup Page
def signup(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        fatName = request.POST.get('fatherName')
        dofb = request.POST.get('dob')
        mno = request.POST.get('mno')
        mail = request.POST.get('mail')
        cpass = request.POST.get('cpass')

        # To register in a local Database
        b = Signup(fname=firstname, lname=lastname, fathername=fatName, dob=dofb, mobnum=mno, email=mail, password=cpass)
        b.save()
        # To register in Admin
        user = User.objects.create_user(mail, mail, cpass)
        user.is_staff = True
        user.save()
        messages.success(request, 'Registration Successful.')
        return redirect('index')

#! Checking loan Eligblity
def checkloan(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        mailid = request.POST.get('emailid')
        state = request.POST.get('state')
        city = request.POST.get('city')
        zipcode = request.POST.get('zipcode')
        gen = request.POST.get('gender')
        maritialstatus = request.POST.get('maritialstatus')
        familyDependent = request.POST.get('familyDependent')
        job = request.POST.get('job')
        ed = request.POST.get('education')
        propertyType = request.POST.get('propertyType')
        takenLoan = request.POST.get('takenLoan')
        income = request.POST.get('income')
        coNetIncome = request.POST.get('coNetIncome')
        creditAmount = request.POST.get('creditAmount')
        creditduration = request.POST.get('creditduration')
        panNo = request.POST.get('panNo')
        typeofcheck = request.POST.get('checktype')
        

        b = eligblity(fname = fname, lname = lname, email = mailid, state = state, city = city, zip = zipcode, gender = gen, Marital = maritialstatus, Dependents = familyDependent, profession = job, education = ed, property = propertyType, takenLoan = takenLoan, aincome = income, cincome = coNetIncome, loanamount = creditAmount, duration = creditduration, pan = panNo)
        if (b.save()):
            print("Success")
        else:
            print("Not ")

    #These are values which will come from website form
    #check dataset to see what each of them can hold
    gender=gen
    married=maritialstatus
    dependents=int(familyDependent)
    education=ed
    self_employed=job
    applicantincome=int(income)
    coapplicantincome=int(coNetIncome)
    loanamount=int(creditAmount)
    loanamounterm=int(creditduration)
    credithistory=int(takenLoan)
    propertyarea=propertyType
    successmsg = "We are excited to tell you that your Loan Application is Acceptable in Any bank"
    errormsg = "Bank not Accepts Your Loan Application"
    tempname = str(fname+" "+lname)
    if (loanamount > applicantincome*4):
        return render(request,'front/status.html',{'name':tempname,'msg':errormsg,'img':stockimg})
    # elif ((loanamount > applicantincome*4) and (coapplicantincome > loanamount*4)):
    #     messages.info(request,"As per the income of Co-Applicant Your loan will be approved")
    #     return render(request,'front/status.html',{'name':tempname,'msg':successmsg,'img':stockimg})
    else:
        x=[gender, married, dependents, education, self_employed, applicantincome, coapplicantincome, loanamount, loanamounterm, credithistory, propertyarea]
        data=Preprocess(x)
        valp = random.randint(0,1)
        # rdf, adb, dtm, ensm, knn, ldm, lgm, nv, svm
        if (typeofcheck=="rdf"):
            temp = pickle.load(open('RandomForest_model.sav','rb'))
            rnd = temp.predict(data)
            print(rnd[0])
            if (rnd[0]==1 and valp==1):
                messages.info(request,"You selected Random Forest Model")
                return render(request,'front/status.html',{'name':tempname,'msg':successmsg,'img':stockimg})
            else:
                return render(request,'front/status.html',{'name':tempname,'msg':errormsg,'img':stockimg})
        elif (typeofcheck=="adb"):
            temp = pickle.load(open('AdaBoost_model.sav','rb'))
            adaboost = temp.predict(data)
            print(adaboost[0])
            if (adaboost[0]==1 and valp==1):
                messages.info(request,"You Selected AdaBoost Model")
                return render(request,'front/status.html',{'name':tempname,'msg':successmsg,'img':stockimg})
            else:
                return render(request,'front/status.html',{'name':tempname,'msg':errormsg,'img':stockimg})
        elif (typeofcheck=="dtm"):
            temp = pickle.load(open('DecisionTree_model.sav','rb'))
            decision = temp.predict(data)
            print(decision[0])
            if (decision[0]==1 and valp==1):
                messages.info(request,"You selected Decision Tree Model")
                return render(request,'front/status.html',{'name':tempname,'msg':successmsg,'img':stockimg})
            else:
                return render(request,'front/status.html',{'name':tempname,'msg':errormsg,'img':stockimg})
        elif (typeofcheck=="ensm"):
            temp = pickle.load(open('ensemble_model.sav','rb'))
            ensemble = temp.predict(data)
            print(ensemble[0])
            if (ensemble[0]==1 and valp==1):
                messages.info(request,"You selected Ensemble Model")
                return render(request,'front/status.html',{'name':tempname,'msg':successmsg,'img':stockimg})
            else:
                return render(request,'front/status.html',{'name':tempname,'msg':errormsg,'img':stockimg})
        elif (typeofcheck=="knn"):
            temp = pickle.load(open('KNN_model.sav','rb'))
            kn = temp.predict(data)
            print(kn[0])
            if (kn[0]==1 and valp==1):
                messages.info(request,"You selected KNN Model")
                return render(request,'front/status.html',{'name':tempname,'msg':successmsg,'img':stockimg})
            else:
                return render(request,'front/status.html',{'name':tempname,'msg':errormsg,'img':stockimg})
        elif (typeofcheck=="ldm"):
            temp = pickle.load(open('LinearDiscriminant_model.sav','rb'))
            lineardiscriminant = temp.predict(data)
            print(lineardiscriminant[0])
            if (lineardiscriminant[0]==1 and valp==1):
                messages.info(request,"You selected Linear Discriminant Model")
                return render(request,'front/status.html',{'name':tempname,'msg':successmsg,'img':stockimg})
            else:
                return render(request,'front/status.html',{'name':tempname,'msg':errormsg,'img':stockimg})
        elif (typeofcheck=="lgm"):
            temp = pickle.load(open('Logistic_model.sav','rb'))
            logistic = temp.predict(data)
            print(logistic[0])
            if (logistic[0]==1 and valp==1):
                messages.info(request,"You selected logistic Regression Model")
                return render(request,'front/status.html',{'name':tempname,'msg':successmsg,'img':stockimg})
            else:
                return render(request,'front/status.html',{'name':tempname,'msg':errormsg,'img':stockimg})
        elif (typeofcheck=="nv"):
            temp = pickle.load(open('NB_model.sav','rb'))
            naive = temp.predict(data)
            print(naive[0])
            if (naive[0]==1 and valp==1):
                messages.info(request,"You selected Naive Base Model")
                return render(request,'front/status.html',{'name':tempname,'msg':successmsg,'img':stockimg})
            else:
                return render(request,'front/status.html',{'name':tempname,'msg':errormsg,'img':stockimg})
        elif (typeofcheck=="svm"):
            temp = pickle.load(open('svm_model.sav','rb'))
            sv = temp.predict(data)
            print(sv[0])
            if (sv[0]==1 and valp==1):
                messages.info(request,"You selected Support Vector Machine Model")
                return render(request,'front/status.html',{'name':tempname,'msg':successmsg,'img':stockimg})
            else:
                return render(request,'front/status.html',{'name':tempname,'msg':errormsg,'img':stockimg})



# User Login
def userlogin(request):
    if request.method == 'POST':
        unam = request.POST.get('usernam')
        upass = request.POST.get('userpass')
        print(unam,upass)
        try:
            user = authenticate(username=unam, password=upass)
            if user != None:
                b = Signup.objects.get(email = unam)
                login(request, user) #Login Method Called
                request.session['member_fname'] = b.fname
                if request.user.is_superuser:
                    return redirect('adminUser')
                else:
                    return redirect('panel')
            else:
                messages.error(request, 'Wrong Password')
                return render(request, 'front/login.html')
        except:
            messages.error(request, 'Something went Wrong')
            return render(request, 'front/login.html')
    return redirect('index')

# TODO: After loan Process redirect to status page
def status(request):
    return render(request,'front/status.html')


# Generate OTP
def randomNumberOTP(request):
    global otp, fmail, fmno
    if request.method == 'POST':
        tempfmail = request.POST.get('forgetEmail')
        fmail = tempfmail
        tempfmno = request.POST.get('forgetMobile')
        fmno = tempfmno
    temp = random.randint(10000, 99999)
    otp = temp
    print(fmno, fmail)
    messages.info(request, 'Your OTP is ' + str(otp))
    return render(request, 'master/forgetPassword.html', {'site': site})


# Change Password
def changePassword(request):
    print(otp, fmno)
    if request.method == 'POST':
        validateOTP = request.POST.get('validateOTP')
        cnfPass = request.POST.get('cnfPass')
        if (str(validateOTP) == str(otp)):
            try:
                b = Signup.objects.get(email=fmail)
                b.password = cnfPass
                b.save()
                u = User.objects.get(email=fmail)
                u.set_password(cnfPass)
                u.save()
                messages.info(request, 'Your Password Changed Successfully... Now you can Login')
                return render(request, 'master/forgetPassword2.html', {'site': site})
            except:
                b = Signup.objects.get(email=fmail)
                b.password = cnfPass
                b.save()
                messages.error(request, 'Your Mobile Number is not registered with us.'.format(fmno))
                return render(request, 'master/forgetPassword.html', {'site': site})
        else:
            print(validateOTP)
            messages.error(request, 'Wrong OTP')
            return render(request, 'master/forgetPassword2.html', {'site': site})
    return render(request, 'front/index.html',
                  {'site': site, 'news': news, 'service': service})


#TODO: services page html
def services(request):
    return render(request, 'front/services.html', {'site': site, 'service': service})

#TODO: Our Team page HTML
def ourteam(request):
    return render(request, 'front/team.html', {'site': site})

#TODO: About page HTML
def about(request):
    return render(request, 'front/about.html', {'site': site})

#TODO: Contact page request
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name,email,subject,message)
    try:
        b = contact(name=name, email=email, subject=subject,issues=message)
        b.save()
        messages.success(request, 'We received your query. we will contact your through your mail')
        return render(request, 'front/contacts.html', {'site': site})
    except:
        return render(request, 'front/contacts.html', {'site': site})

def cont(request):
    contacts(request)
    return render(request, 'front/contacts.html', {'site': site})


# TODO: page is Under Maintainence
def maintainence(request):
    return render(request, 'front/maintainence.html', {'site': site})


# TODO: Check Loan status of active user status
def check_detail(request):
    return render(request, 'front/check_status.html', {'site': site})

# TODO: Error pages in HTML
def error(request):
    print(otp)
    return render(request, 'front/error.html', {'site': site})

# TODO: User Login Pages
def panel(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        b=request.session['member_fname']
        return render(request, 'back/index.html',{'user':b})

# TODO: User Login Pages
def adminUser(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        b=request.session['member_fname']
        return render(request, 'user/index.html',{'user':b})

# TODO: User Logout Page
def userlogout(request):
    try:
        del request.session['member_fname']
        logout(request)
        return redirect('index')
    except KeyError:
        return redirect('panel')

# TODO: registerd user check their loan requirement Page
def checkStatus(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        b=request.session['member_fname']
        return render(request, 'back/index2.html',{'user':b})


# TODO: Forget Password Second Page
def forgetPassword(request):
    return render(request, 'master/forgetPassword.html', {'site': site})


# TODO: Forget Password Second Page
def forgetPassword2(request):
    return render(request, 'master/forgetPassword2.html', {'site': site})


# TODO: User Login Page
def userloginpage(request):
    return render(request, 'front/login.html')


#! Loan Approval Predictoin user data process 
def Preprocess(x):
    mrdict={'No': 0, 'Yes': 1}
    gndict={'Female': 0, 'Male': 1}
    eddict={'Graduate': 0, 'Not Graduate': 1}
    sedict={'No': 0, 'Yes': 1}
    padict={'Rural': 0, 'Semiurban': 1, 'Urban': 2}
    x[0]=gndict[x[0]]
    x[1]=mrdict[x[1]]
    x[3]=eddict[x[3]]
    x[4]=sedict[x[4]]
    x[10]=padict[x[10]]
    x=np.asarray(x)
    x=x.reshape(1,-1)
    StSc = StandardScaler()
    x = StSc.fit_transform(x)
    return x

# TODO Admin read messages
# def messageRead(request):
#     b=request.session['member_fname']
#     return render(request, 'user/index2.html',{'userMessage':userMessage,'user':b})