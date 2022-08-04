from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.db.models import Q
from .form import UserImageForm  


from .models import Genre,Movie,User

def home(request):
    query=request.GET.get('query') if request.GET.get('query') != None else ''
    movies=Movie.objects.filter(Q(genre__name__icontains=query)|Q(title__icontains=query))
    genre=Genre.objects.all()
    content={"Movie":movies,"Genre":genre}
    return render(request,'index.html',content)


def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    return render(request, 'registration/signup.html', {'form': form})


def singleMovie(request,id):
    movie=Movie.objects.get(id=id)
    movies=Movie.objects.filter(genre=movie.genre)
    context={"movie":movie,"similar":movies}
    return render(request,'viewMovie.html',context)


 

def addMovie(request):
    genre=Genre.objects.all()
    
    if request.method=='POST':
        movie=Movie()
        movie.user=User.objects.get(id=request.POST.get('genre'))
        movie.genre=Genre.objects.get(id=request.POST.get('genre'))
        movie.actors=request.POST.get('actor')
        movie.title=request.POST.get('title')
        movie.description=request.POST.get('description')
        movie.release_date=request.POST.get('rdate')
        movie.trailer=request.POST.get('trailer')
        movie.poster=request.FILES['poster']
        movie.save()
        # return redirect('/')

    context={"genre":genre}    
    return render(request,'addMovie.html',context)


def image_request(request):  
    if request.method == 'POST':  
        form = UserImageForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
  
            # Getting the current instance object to display in the template  
            img_object = form.instance  
              
            return render(request, 'addMovie.html.html', {'form': form, 'img_obj': img_object})  
    else:  
        form = UserImageForm()  
  
    return render(request, 'addMovie.html.html', {'form': form})  