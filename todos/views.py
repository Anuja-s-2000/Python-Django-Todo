from django.shortcuts import render, get_object_or_404,get_list_or_404, redirect,reverse
from django.views import generic
from todos.models import Todo,Users
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect

def home(request):
    return render(request,'login.html')

def login(request):
    username = request.POST['content']
    password=request.POST['pass']
    try:
        user = get_object_or_404(Users, username=username, password=password)
        uid=user.id
        return redirect(reverse('todos:index', kwargs={ 'uid': uid })) 
    except:
        return redirect('todos:home')

def signin(request):
    username = request.POST['content']
    password=request.POST['pass'] 
    if len(username)>0 and len(password)>0:
        user = Users.objects.filter(username=username)
        userid=0
        for i in user:
            userid=i.id
            userpass=i.password
        if userid==0:
            Users.objects.create(username=username,password=password)
            user = get_object_or_404(Users,username=username, password=password)
            uid = user.id
            return redirect(reverse('todos:index', kwargs={ 'uid': uid }))
        else:
            if userpass==password:
                return redirect(reverse('todos:index', kwargs={ 'uid': userid }))
            else:
                return redirect('todos:home')     
    else:
        return redirect('todos:home')

def index(request,uid):
    user = get_object_or_404(Users,pk=uid)
    todo_list = Todo.objects.filter(user_id=uid)
    context = {
        'user':user,
        'todo_list': todo_list
    }
    return render(request, 'todo.html', context)

@csrf_protect    
def add(request,uid):
    title = request.POST['title']
    if title:
        Todo.objects.create(user_id=uid,title=title)
    return redirect(reverse('todos:index', kwargs={ 'uid': uid }))

def delete(request,uid, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id,user_id=uid)
    todo.delete()
    return redirect(reverse('todos:index', kwargs={ 'uid': uid }))

def update(request,uid, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id,user_id=uid)
    todo.complete = not(todo.complete)
    todo.save()
    return redirect(reverse('todos:index', kwargs={ 'uid': uid }))

@csrf_protect
def search(request,uid):
    try:
        title = request.POST['title']
        stodo = get_object_or_404(Todo,user_id=uid, title=title)
        print(stodo.id)
        context = { 'stodo': stodo  }
        return render(request, 'search-todo.html', context)
    except:
        return redirect(reverse('todos:index', kwargs={ 'uid': uid })) 