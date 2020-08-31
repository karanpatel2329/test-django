import random
import re

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import CustomUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout

def generate_session_token  (length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97,123)]+[str(i) for i in range(10)]) for _ in range(length))

@csrf_exempt
def signin(request):
    
    if not request.method == 'POST':
        return JsonResponse({'erro':'Send a post request with valid information'})
    
    username = request.POST['emails']
<<<<<<< HEAD
    
    
    password = request.POST['password']
=======
    password = request.POST.get("password")
>>>>>>> d2bba5c5b63b0c5575c13502b29b34e57ae5701a

    if not re.match("/\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b/gi", username):
        return JsonResponse({'error': 'Enter valid email id'})

    if len(password) <8:
        return JsonResponse({'error':'ENter more charater in password'})
    
    UserModel =get_user_model()

    try:
        user=UserModel.object.get(emails=username)

        if user.check_password(password):
            user_dict= UserModel.object.filter(emails=username).values().first()
            user_dict.pop('password')

            if user.session_token != "0":
                user.session_token = "0"
                user.save()
                return JsonResponse({'error': 'Previous session exists'})
            
            token = generate_session_token()
            user.session_token = token
            user.save()
            login(request, user)
            return JsonResponse({'token':token, 'user':user_dict})
        
        else:
            return JsonResponse({'error':'Invalid Password'})

    except UserModel.DoesNotExist:
        return JsonResponse({'error':'Invalid Email'})

def signout(request, id):
    #logout(request)

    UserModel = get_user_model()

    try:
        user = UserModel.object.get(pk=id)
        user.session_token = "0"
        user.save()
        logout(request)
    except UserModel.DoesNotExist:
        return JsonResponse({'error':'Invalid id'})

    return JsonResponse({'success':'Logout Successful'})


class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create':[AllowAny]}

    queryset= CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer
    
    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]] 
        except KeyError:
            return [permission() for permission in self.permission_classes] 
