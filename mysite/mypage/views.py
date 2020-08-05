from django.shortcuts import render, HttpResponse
from mypage.models import User
from django.contrib import messages
import datetime
import sweetify
# Create your views here.

def index(request):
    #return HttpResponse("This is my page")
    if request.method == 'POST':
        name = request.POST.get('name')
        print("request input -> ",name)
    context = {
        'var':"This is a input from the user"
    }
    # return HttpResponse("index function")
    return render(request,'index.html', context)

    

def about(request):
   # return HttpResponse("This is About my page")
#    if request.method == 'POST':
#        name = request.POST.get('name')
#        password = request.POST.get('password')
#        index = Index(name = name , password = password, date = date.today())
   return render(request,'about.html')

def reply(request):
    if request.method == 'POST':
       name = request.POST.get('name')
       password = request.POST.get('password')
       index = Index(name = name , password = password, date = date.today())
       print(index)
    return render(request,'reply.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phn = request.POST.get('phone')
        password = request.POST.get('pass')
        confirm_password = request.POST.get('con_pass')
        date_time = datetime.datetime.now()
        if password == confirm_password:
            user = User(name=name,email=email,phone=phn,password=password, date_time=date_time)
            user.save()
            messages.success(request, 'Profile details updated.')
        else:
            messages.error(request, 'Password does not match')

        print("Name -> ",name,", Email ->",email,", Phone -> ",phn)
        
        
    # context = {
    #     'var':"This is a input from the user"
    # }
    # return HttpResponse("index function")
    return render(request,'register.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("pass")
        response = User.objects.raw('SELECT id,name,phone,email FROM mypage_user WHERE email = %s', [email])

        
        try:
            response2 = User.objects.get(email = email)
            print("----------------------")
            print(str(response2).split('`~`'))
            print("----------------------")
            x = str(response2).split('`~`')
            if password == x[3]:
                context = {'name':x[0] , 'email': x[1], 'phn': x[2] }
                return render(request,'dashboard.html',context)
            else:
                context = {'response':"Incorrect password"}
                messages.error(request, 'Incorrect password')
                return render(request,'login.html')
            # return HttpResponse("name : "+x[0]+" phone : "+x[2])
        except:
            context = {'response':"User Not found!"}
            messages.error(request, 'User Not found!')
            return render(request,'login.html',context)

        
    else:
        sweetify.success(request, 'You did it', text='Good job! You successfully showed a SweetAlert message', persistent='Hell yeah')
        return render(request,'login.html')
    
