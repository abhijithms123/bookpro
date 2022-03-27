from django.shortcuts import render
from django.views.generic import View
from calculation.forms import OperationForm

# Create your views here.


class AddView(View):
    def get(self, request):
        form = OperationForm()
        return render(request, "add.html", {"form": form})

    def post(self, request):
        # n1 = int(request.POST.get("num1"))
        # n2 = int(request.POST.get("num2"))
        form = OperationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            n1 = int(form.cleaned_data.get("num1"))
            n2 = int(form.cleaned_data.get("num2"))
            result = n1 + n2
            return render(request, "add.html", {"result":result})
        else:
            return render(request, "add.html", {"form":form})


class SubView(View):
    def get(self, request):
        form = OperationForm()
        return render(request, "sub.html", {"form": form})
    def post(self,request):
        # n1 = int(request.POST.get("num1"))
        # n2 = int(request.POST.get("num2"))
        form = OperationForm(request.POST)
        if form.is_valid():
            n1 = int(form.cleaned_data.get("num1"))
            n2 = int(form.cleaned_data.get("num2"))
            result = n1 - n2
            return render(request, "sub.html", {"result":result})
        else:
            return render(request, "sub.html", {"form": form})


class MulView(View):
    def get(self,request):
        form = OperationForm()
        return render(request, "mul.html", {"form":form})
    def post(self,request):
        # n1 = int(request.POST.get("num1"))
        # n2 = int(request.POST.get("num2"))
        form = OperationForm(request.POST)
        if form.is_valid():
            n1 = int(form.cleaned_data.get("num1"))
            n2 = int(form.cleaned_data.get("num2"))
            result = n1 * n2
            return render(request, "mul.html", {"result": result})

class DivView(View):
    def get(self,request):
        form = OperationForm()
        return render(request, "div.html", {"form": form})
    def post(self,request):
        # n1 = int(request.POST.get("num1"))
        # n2 = int(request.POST.get("num2"))
        form = OperationForm(request.POST)
        if form.is_valid():
            n1 = int(form.cleaned_data.get("num1"))
            n2 = int(form.cleaned_data.get("num2"))
            result = n1 / n2
            return render(request, "div.html", {"result": result})


class IndexView(View):
    def get(self,request):
        return render(request, "home.html")
def add(request):
    print(request.method)
    if request.method == "POST":
        n1 = int(request.POST.get("num1"))
        n2 = int(request.POST.get("num2"))
        result = n1 + n2
        return render(request, "add.html", {"result": result})
    return render(request, "add.html")


def sub(request):
    if request.method == "POST":
        n1 = int(request.POST.get("num1"))
        n2 = int(request.POST.get("num2"))
        result = n1 - n2
        return render(request, "sub.html", {"result": result})
    return render(request, "sub.html")


def mul(request):
    if request.method == "POST":
        n1 = int(request.POST.get("num1"))
        n2 = int(request.POST.get("num2"))
        result = n1 * n2
        return render(request, "mul.html", {"result": result})
    return render(request, "mul.html")


def div(request):
    if request.method == "POST":
        n1 = int(request.POST.get("num1"))
        n2 = int(request.POST.get("num2"))
        result = n1 / n2
        return render(request, "div.html", {"result": result})
    return render(request, "div.html")


def get_vowels(request):
    if request.method == "POST":
        word = request.POST.get("word")
        vowels = [char for char in word if char in ["a", "e", "i", "o", "u"]]
        return render(request, "getvow.html", {"result": vowels})
    return render(request, "getvow.html")


def get_prime(request):
    if request.method == "POST":
        initial = int(request.POST.get("initial"))
        final = int(request.POST.get("final"))
        prime = []
        for i in range(initial,final):
            for n in range(2,final):
                if i % 2 == 0:
                    break
            else:
                prime.append(i)
        return render(request, "prime.html", {"result": prime})
    return render(request, "prime.html")

def word_count(request):
    if request.method == "POST":
        words = request.POST.get("word")
        word_list = words.split(" ")
        word_count = len(word_list)
        return render(request, "word_count.html", {"result": word_count})
    return render(request, "word_count.html")



