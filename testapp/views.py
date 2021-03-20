from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import UserForm

# def index(request):
#     header = "User Data"
#     user = {"name": "Oleg", "age": 21}
#     address = ("Юбилейная", 42, 36)
#     email = ["w223@gmail.com", "gh39483@yandex.ru"]
#     # email = []
#     num_reg = 10000
#
#     data = {"header": header, "user": user,
#             "address": address, "email": email, "num_reg": num_reg}
#     return render(request, "index.html", context=data)


def index(request):
    userform = UserForm()
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            return HttpResponse("<h2>Hello, {0}</h2>".format(name))
    return render(request, "index.html", {"form": userform})


# def about(request):
#     return HttpResponse("<h2>О компании</h2>")
#
#
# def contacts(request):
#     return HttpResponse("<h2>Контакты</h2>")


def categories(request, category_id):
    title = request.GET.get("title", "")
    output = f"<h2>Category {category_id}  Title: {title}</h2>"
    return HttpResponse(output)


def clients(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Admin")
    output = f"<h2>Client</h2><h3>id: {id}  name: {name}</h3>"
    return HttpResponse(output)
