from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import LenderCreate
from .models import Lender

def calculate(request):
    clas = request.POST['clas']
    budget = request.POST['budget']
    duration = request.POST['duration']
    noloans = request.POST['loans']
    base = Lender.objects.get(Class=clas)
    install= int(base.Installments)
    dur=int(base.Duration)
    min=int(base.Amount)
    loan=int(noloans)
    dura=int(duration)
    bud=int(budget)
    i=1
    rem=bud-(loan*min)
    while i<=dura:
        if i==dur:
            rem=rem+(loan*(min/dur))
            res=rem/(min/dur)
            break
            return render(request ,"lenders/result.html",{"result":res})
        rem=rem+(loan*(min/dur))
        i=i+1
    res=rem/(min/dur)
    if (bud < min):
        res= " Doesn't meet minimum amount !"
        return render(request ,"lenders/result.html",{"result":res})
    if (bud < min*loan):
        res= "Not enough budget !"
        return render(request ,"lenders/result.html",{"result":res})
    return render(request ,"lenders/result.html",{"result":res})


def index(request):
    base = Lender.objects.all()
    return render(request, 'lenders/data.html', {'base': base})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request , user)
            return redirect("lenders:index")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
    form = UserCreationForm
    return render(request , 'lenders/register.html' , {'form' : form})

def login_request(request):
    if request.method == 'POST':
        form=AuthenticationForm(request , data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user=authenticate(username=username , password=password)
            if user is not None:
                login(request , user)
                return redirect("lenders:index")
    form = AuthenticationForm()
    return render(request , "lenders/login.html" , {"form":form})



def logout_request(request):
    logout(request)
    return redirect("lenders:index")


def upload(request):
    upload = LenderCreate()
    if request.method == 'POST':
        upload = LenderCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'lenders/upload_form.html', {'upload_form':upload})

def update_lender(request, lender_id):
    lender_id = int(lender_id)
    try:
        lender_sel = Lender.objects.get(id = lender_id)
    except Lender.DoesNotExist:
        return redirect('index')
    lender_form = LenderCreate(request.POST or None, instance = lender_sel)
    if lender_form.is_valid():
       lender_form.save()
       return redirect('index')
    return render(request, 'lenders/upload_form.html', {'upload_form':lender_form})


def delete_lender(request, lender_id):
    lender_id = int(lender_id)
    try:
        lender_sel = Lender.objects.get(id = lender_id)
    except Lender.DoesNotExist:
        return redirect('index')
    lender_sel.delete()
    return redirect('index')