
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Destination
from .serializers import DestinationSerializer
from rest_framework import viewsets
from .serializers import DestinationSerializer
from .models import Destination
from django.contrib.auth import authenticate,login,logout
from .forms import CustomUserForm
from django.shortcuts import render,redirect
from django.contrib import messages




class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

@csrf_exempt
def destination_list(request):
    if request.method == 'GET':
        destinations = Destination.objects.all()
        serializer = DestinationSerializer(destinations, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DestinationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def destination_edit(request, id):
    try:
        destination = Destination.objects.get(id=id)
    except Destination.DoesNotExist:
        return JsonResponse({'error': 'Destination not found.'}, status=404)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DestinationSerializer(destination, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


def destination_delete(request, id):
    try:
        destination = Destination.objects.get(id=id)
    except Destination.DoesNotExist:
        return JsonResponse({'error': 'Destination not found.'}, status=404)

    if request.method == 'DELETE':
        destination.delete()
        return JsonResponse({'message': 'Destination deleted successfully.'}, status=204)


def destination_detail(request, id):
    try:
        destination = Destination.objects.get(id=id)
    except Destination.DoesNotExist:
        return JsonResponse({'error': 'Destination not found.'}, status=404)

    if request.method == 'GET':
        serializer = DestinationSerializer(destination)
        return JsonResponse(serializer.data, safe=False)




def register(request):
    form=CustomUserForm()
    if request.method=="POST":
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Register sucess")
            return redirect('/login_page')
        

    return render(request,'register.html',{'form':form})



def login_page(request):
    if request.user.is_authenticated:
        return redirect('destination') 

    if request.method == "POST":
        name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successfully")
            return redirect('destination') 
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('login_page') 
    return render(request, 'login.html')


def destination(request):
    
    destinations = Destination.objects.all()
    
    return render(request, 'destination_list.html', {'destinations': destinations})



def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'Logout sucessfully')
    return redirect('/')