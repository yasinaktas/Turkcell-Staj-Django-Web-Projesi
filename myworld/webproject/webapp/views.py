from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages


@login_required
def BASE(request):
    return render(request, 'base.html')

def LOGIN(request):
    return render(request, 'login.html')

def BLANK(request):
    return render(request, 'blank.html')

def TABLES(request):
    return render(request, 'tables.html')

def user_list(request):
    users = User.objects.all().values('id', 'name', 'age', 'id_admin', 'id_deleted')
    return JsonResponse({'data': list(users)})

@csrf_exempt
@require_http_methods(["POST"])
def add_user(request):
    data = json.loads(request.body)
    user = User.objects.create(
        name=data['name'],
        age=data['age'],
        id_admin=1 if data.get('is_admin') else 0,
        id_deleted=0
    )
    return JsonResponse({'id': user.id})

@csrf_exempt
@require_http_methods(["PUT"])
def update_user(request, user_id):
    data = json.loads(request.body)
    user = get_object_or_404(User, id=user_id)
    user.name = data.get('name', user.name)
    user.age = data.get('age', user.age)
    user.id_admin = data.get('is_admin', user.id_admin)
    user.save()
    return JsonResponse({'id': user.id})

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return JsonResponse({'result': 'User deleted'})

def create_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        
        if password == password_confirmation:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'User created successfully!')
                return redirect('login')
            except:
                messages.error(request, 'Username already exists!')
        else:
            messages.error(request, 'Passwords do not match!')
    
    return redirect('login')
