from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from COLLEGE_APP.models import CourseModel, StudentModel, TeacherModel

# Create your views here.
def home(request):
    return render(request,'home.html')
def signuppage(request):
    course= CourseModel.objects.all()
    return render(request,'signup.html',{'course':course})
def signinpage(request):
    return render(request,'signin.html')
@login_required(login_url='login')
def admin_home(request):
    return render(request,'admin_home.html')

@login_required(login_url='login')
def student(request):
    course= CourseModel.objects.all()
    return render(request,'student.html',{'course':course})

@login_required(login_url='login')
def teacher_home(request):
    # usrname=request.POST['uname']
    # user= User.objects.get(username=usrname)
    # data=User.objects.get(id=pk)
    # usr= request.
    # tchr= TeacherModel.objects.get(User=data.id)
    return render(request,'teacher_home.html')

def signin(request):
    if request.method== 'POST':
        usrname=request.POST['uname']
        pswd=request.POST['pwd']
        user = auth.authenticate(username=usrname, password=pswd)
        # teacher= TeacherModel.objects.get(id=user.id)
        if user is not None:
            if user.is_staff:
                auth.login(request, user)
                return redirect('admin_home')
            else:
                auth.login(request, user)
                return redirect('teacher_home')
        else:
            messages.info(request, 'Invalid Username or Password. Try Again.')
            return redirect('signinpage')
    else:
         return redirect('signinpage')
def signup(request):
    if request.method=='POST':
        print("hello")
        fname=request.POST['fname']
        print(fname)
        lname=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']
        age=request.POST['age']
        phone=request.POST['phone']
        adrs=request.POST['address']
        print(adrs)
        # select=request.POST['select']
        select=request.POST['select']
        course= CourseModel.objects.get(id=select)
        print(select)
        # course=CourseModel.objects.get(id=select)
        image=request.FILES.get('file')
        pwd=request.POST['pwd']
        cpwd=request.POST['cpwd']
        
        if pwd==cpwd:
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'This User Already Exists')
                return redirect('signuppage')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This User Already Exists')
                return redirect('signuppage')
            else:
                user= User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=pwd)
                user.save()
                data=User.objects.get(id=user.id)
                teacher=TeacherModel(Course=course,User=data,Address=adrs,Age=age,Phone=phone,Image=image)
                teacher.save()
                messages.success(request, 'Registered successfully')
                return redirect('signinpage')
        else:
            messages.info(request, 'Password Mismatch')
            return redirect('signuppage')
    else:
         return redirect('signuppage')
        
@login_required(login_url='login')    
def course(request):
    return render(request,'course.html')

def addcourse(request):
    if request.method=='POST':
        cname=request.POST['coursename']
        cfee=request.POST['coursefees']
        course = CourseModel(Course_Name=cname,Course_Fees=cfee)
        course.save()
        return redirect('course')
    

def logout(request):
	auth.logout(request)
	return redirect('home')
@login_required(login_url='login')
def editpage(request,pk):
    usr = User.objects.get(id=pk)
    tchr=TeacherModel.objects.get(User=usr.id)
    course= CourseModel.objects.all()
    context = {'tchr':tchr,'course':course}
    return render(request,'editpage.html',context)
def edit(request,pk):
    tch=TeacherModel.objects.get(id=pk)
    usr=User.objects.get(id=tch.User.id)
    if request.method == 'POST':
        new=request.FILES.get('file')
        old= tch.Image
        if old!=None and new==None:
            tch.Image=old
        else:
            tch.Image=new
        usr.first_name=request.POST['fname']
        usr.last_name=request.POST['lname']
        usr.username=request.POST['uname']
        usr.email=request.POST['email']
        usr.save()
        tch.Age=request.POST['age']
        tch.Phone=request.POST['phone']
        tch.Address=request.POST['address']
        select=request.POST['select']
        course= CourseModel.objects.get(id=select)
        tch.Course=course
        tch.User=usr
        tch.save()

        return redirect('teacher_home')
    return render(request,'editpage.html')

def addstudent(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        phone=request.POST['phone']
        adrs=request.POST['address']
        select=request.POST['select']
        course= CourseModel.objects.get(id=select)
       

        student= StudentModel(std_fname=fname,
                                std_lname=lname,
                                std_email=email,
                                std_phone=phone,
                                std_address=adrs,
                                std_course=course,
                                )
        student.save()
        return redirect('admin_home')
    else:
        return redirect('student')

@login_required(login_url='login')    
def student_data(request):
    data= StudentModel.objects.all()
    return render(request,'studentdata.html',{'sdata':data})

@login_required(login_url='login')
def user_data(request):
    data= TeacherModel.objects.all()
    return render(request,'userdata.html',{'udata':data})

def userdelete(request,pk):
    data= TeacherModel.objects.get(id=pk)
    data.delete()
    return redirect('user_data')
def studentdelete(request,pk):
    data= StudentModel.objects.get(id=pk)
    data.delete()
    return redirect('student_data')
def user_view(request,pk):
    data= TeacherModel.objects.get(id=pk)
    return render(request,'userview.html',{'u':data})
def std_editpage(request,pk):
    stud=StudentModel.objects.get(id=pk)
    c=CourseModel.objects.all()
    return render(request,'studentedit.html',{'std':stud,'crs':c})
def std_edit(request,pk):
    stud=StudentModel.objects.get(id=pk)
    if request.method == 'POST':
        stud.std_fname = request.POST.get('fname')
        stud.std_lname = request.POST.get('lname')
        stud.std_email = request.POST.get('email')
        stud.std_phone = request.POST.get('phone')
        stud.std_address = request.POST.get('address')
        select = request.POST.get('select')
        course= CourseModel.objects.get(id=select)
        stud.std_course=course
        stud.save()
        return redirect('student_data')
    return render(request,'studentedit.html')