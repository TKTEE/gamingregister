from django.shortcuts import render, redirect
from .models import Register


def displayindex(request):
    data = Register.objects.all()
    context = {"data": data}
    return render(request, 'index.html', context)


def inserData(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        team = request.POST.get('team')
        age = request.POST.get('age')
        number = request.POST.get('number')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        password = request.POST.get('password')

        query = Register(name=name, email=email, team=team, age=age, number=number, gender=gender, country=country, password=password)
        query.save()
        return redirect('/')
    return render(request, 'index.html')

def deleteData(request, id):
    d = Register.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "index.html")

def updateData(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        team = request.POST.get('team')
        age = request.POST.get('age')
        number = request.POST.get('number')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        password = request.POST.get('password')

        edit = Register.objects.get(id=id)
        edit.name = name
        edit.email = email
        edit.team = team
        edit.age = age
        edit.number = number
        edit.gender = gender
        edit.country = country
        edit.password = password
        edit.save()
        return redirect("/")
    d = Register.objects.get(id=id)
    context = {"d":d}
    return render(request, "edit.html", context)
