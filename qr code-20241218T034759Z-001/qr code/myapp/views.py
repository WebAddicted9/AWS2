# # views.py
from django.shortcuts import render, redirect,HttpResponse
from .forms import Custom_Form,Login_form
import qrcode
from io import BytesIO
from django.core.files import File
from .models import myuser
from django.contrib.auth import authenticate , login , logout

def form_view(request):
    if request.method == 'POST':
        form = Custom_Form(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            
            # data = f"tel:{form_instance.mobile_no},username:{form_instance.username}"
            # print(user,'>>>>user')
            uname = request.POST['username']
            passw = request.POST['password1']
            print(uname,passw,'>>>>>>>>>>>>')
            user = authenticate(username=uname,password=passw)
            print(user,'>>>>>>>>>>')
            data =  f"http://192.168.29.57:8000//call/{user.id}/"
            qr_img = qrcode.make(data)
            buffer = BytesIO()
            qr_img.save(buffer, format='PNG')
            filename = f'qrcodes/{form_instance.mobile_no}.png'
            form_instance.qr_code.save(filename, File(buffer), save=True)
            form_instance.save()
            return redirect('/')
    else:
        form = Custom_Form()
    return render(request, 'signup.html', {'form': form})


def login_view(request):

    if request.method == "POST":

        login_data =  Login_form(request=request, data=request.POST)
        if login_data.is_valid():
            uname = login_data.cleaned_data['username']
            passw = login_data.cleaned_data['password']
    
            user = authenticate(username = uname,password = passw)
            print(user,'>>>>>>>>>')

            if user is not None:
                login(request,user)
                return redirect('/detail/')
    else:

        login_data = Login_form()
    return render(request,'login.html',{'data':login_data})
    
def logouthandel(request):
    logout(request)
    return redirect('/')

    
def detail_view(request):
    data = myuser.objects.get(username=request.user)
    return render(request,'detail.html',{'data':data})

def call(request):
    data = myuser.objects.get(username=request.user)
    print(data,'>>>>>>>>>>>>>>')
    return render(request,'call.html',{'data':data})




# from twilio.rest import Client
# from django.http import JsonResponse

# def make_call(request):
#     # Your Twilio credentials
#     account_sid = 'AC3e1176a4e568ff0c1e0e55f71175a041'
#     auth_token = '7205b0f05f9d6735ef6b6c0b7847ed82'
#     client = Client(account_sid, auth_token)

#     # Make a call
#     call = client.calls.create(
#         to='+919024285527',  # Replace with the recipient's phone number
#         from_='+19896070312',  # Replace with your Twilio phone number
#         url='http://example.com/twiml/'  # URL for TwiML, explained below
#     )

#     # You can return a JSON response or redirect the user to a success page
#     return JsonResponse({'status': 'Call initiated successfully'})


