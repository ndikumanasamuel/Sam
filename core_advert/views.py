from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import (InkoranyaForm,UbukweForm,ImbyinoForm,IbikoreshoForm,UbuhinziForm,
IndamukanyoForm,AmasanoForm,IkibonezamvugoForm,UmurageForm,HuguraForm)
from .models import (Inkoranya,Ubukwe,Imbyino,Ibikoresho,Ubuhinzi,Indamukanyo,
Amasano,Ikibonezamvugo,Umurage,Hugura)


def index(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'home.html')

def inkoranya(request):
    inkoranya=Inkoranya.objects.all()
    return render(request, 'inkoranya.html',{ 'inkoranya':inkoranya })


def upload_inkoranya(request):
    if request.method == 'POST':
        form=InkoranyaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inkoranya')
    else:
        form= InkoranyaForm()

    return render(request, 'upload_inkoranya.html',{'form':form})

def ubukwe(request):
    ubukwe=Ubukwe.objects.all()
    return render(request, 'ubukwe.html',{ 'ubukwe':ubukwe })

def upload_ubukwe(request):
    if request.method == 'POST':
        form=UbukweForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ubukwe')
    else:
        form= UbukweForm()

    return render(request, 'upload_ubukwe.html',{'form':form})

def imbyino(request):
    imbyino=Imbyino.objects.all()
    return render(request, 'imbyino.html',{ 'imbyino':imbyino })

def upload_imbyino(request):
    if request.method == 'POST':
        form=ImbyinoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('imbyino')
    else:
        form= ImbyinoForm()

    return render(request, 'upload_imbyino.html',{'form':form})


def ibikoresho(request):
    ibikoresho=Ibikoresho.objects.all()
    return render(request, 'ibikoresho.html',{ 'ibikoresho':ibikoresho })

def upload_ibikoresho(request):
    if request.method == 'POST':
        form=IbikoreshoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ibikoresho')
    else:
        form= IbikoreshoForm()

    return render(request, 'upload_ibikoresho.html',{'form':form})


def ubuhinzi(request):
    ubuhinzi=Ubuhinzi.objects.all()
    return render(request, 'ubuhinzi.html',{ 'ubuhinzi':ubuhinzi})

def upload_ubuhinzi(request):
    if request.method == 'POST':
        form=UbuhinziForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ubuhinzi')
    else:
        form= UbuhinziForm()

    return render(request, 'upload_ubuhinzi.html',{'form':form})


def indamukanyo(request):
    indamukanyo=Indamukanyo.objects.all()
    return render(request, 'indamukanyo.html',{ 'indamukanyo':indamukanyo})

def upload_indamukanyo(request):
    if request.method == 'POST':
        form=IndamukanyoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('indamukanyo')
    else:
        form= IndamukanyoForm()

    return render(request, 'upload_indamukanyo.html',{'form':form})


def amasano(request):
    amasano=Amasano.objects.all()
    return render(request, 'amasano.html',{ 'amasano':amasano})

def upload_amasano(request):
    if request.method == 'POST':
        form=AmasanoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('amasano')
    else:
        form= AmasanoForm()
    return render(request, 'upload_amasano.html',{'form':form})

def search(request):
    if request.method == 'GET':
        q= request.GET['q']
        try:
            inkoranya=Inkoranya.objects.filter(name__icontains=q)
            return render(request, 'search.html', {'inkoranyas': inkoranya})
        except:
            return render(request, 'search.html', {})
    else:
        return render(request, 'inkoranya.html', {})

def ikibonezamvugo(request):
    ikibonezamvugo=Ikibonezamvugo.objects.all()
    return render(request, 'ikibonezamvugo.html',{ 'ikibonezamvugo':ikibonezamvugo})

def upload_ikibonezamvugo(request):
    if request.method == 'POST':
        form=IkibonezamvugoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ikibonezamvugo')
    else:
        form= IkibonezamvugoForm()
    return render(request, 'upload_ikibonezamvugo.html',{'form':form})


def umurage(request):
    umurage=Umurage.objects.all()
    return render(request, 'umurage.html',{ 'umurage':umurage})

def upload_umurage(request):
    if request.method == 'POST':
        form=UmurageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('umurage')
    else:
        form= UmurageForm()
    return render(request, 'upload_umurage.html',{'form':form})


def hugura(request):
    hugura=Hugura.objects.all()
    return render(request, 'hugura.html',{ 'hugura':hugura})

def upload_hugura(request):
    if request.method == 'POST':
        form=HuguraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('hugura')
    else:
        form= HuguraForm()
    return render(request, 'upload_hugura.html',{'form':form})


def register(request):
    if request.method == 'POST':
        First_name= request.POST['first_name']
        Second_name= request.POST['second_name']
        Username= request.POST['username']
        Email= request.POST['email']
        Password1= request.POST['password1']
        Password2= request.POST['password2']

        if Password1==Password2:
            if User.objects.filter(username=Username).exists():
                messages.info(request,"username yarafashwe")
                return render(request,'register.html')
            else:
              user= User.objects.create_user(username= Username,email=Email, password= Password1,first_name=First_name,last_name=Second_name)
              user.save();
              messages.info(request,"kwiyandikisha byagenze neza")
              return render(request, 'login')

        else:
            messages.info(request,"Amagambo banga ntahura")
            return render(request,'register.html')

        # return render(request, 'home.html')

    else:
         return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        Username= request.POST['username']
        Password= request.POST['password']

        user = auth.authenticate(username=Username, password=Password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'home.html')

        else:
            messages.info(request," imyirondoro ntihura ")
            
            return render(request, 'login.html')

    else:
       return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return render('home')

