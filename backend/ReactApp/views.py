from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def web_index(request):
    info_dict = {
        "home_page": "Some homepage info regarding bot"
    }
    return render(request, "ReactApp/index.html", context=info_dict)


def contact_page(request):
    contact_info = {
        "name": "Troy Kirin",
        "phone_number": "206-702-5022",
        "email": "troy.kirin@outlook.com"
    }
    return render(request, "ReactApp/contact_page.html", context=contact_info)
