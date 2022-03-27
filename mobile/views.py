from django.shortcuts import render
from django.views.generic import View
from mobile.forms import MobileForm

# Create your views here.

class MobileView(View):
    def get(self,request):
        form = MobileForm()
        return render(request, "mobiles.html",{"form":form})
    def post(self,request):
        form = MobileForm(request.POST)
        return render(request, "mobiles.html", {"form":form})
