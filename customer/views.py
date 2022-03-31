from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,ListView
from book.models import Book
from customer.forms import UserRegistrationForm,LoginForm,PasswordResetForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from customer.models import Cart
# Create your views here.


class CustomerIndex(ListView):
    model = Book
    template_name = "custhome.html"
    context_object_name = "books"
    # def get(self, request, *args, **kwargs):
    #     qs = Book.objects.all()
    #     return render(request, "custhome.html",{"books":qs})


class SignUpView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "signup.html"
    success_url = reverse_lazy("signin")
    # def get(self,request, *args,**kwargs):
    #     form = UserRegistrationForm()
    #     return render(request,"signup.html",{"form":form})
    #
    # def post(self,request,*args,**kwargs):
    #     form = UserRegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("signin")
    #     else:
    #         return render(request,"signup.html",{"form":form})


class SignInView(View):
    def get(self,request,*args,**kwargs):
        form = LoginForm()
        return render(request,"signin.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username,password)
            user = authenticate(request,username=username,password=password)
            print(user)
            if user:
                print("login success")
                login(request,user)
                return redirect("custhome")
            else:
                print("login failed")
                return render(request,"signin.html",{"form":form})


def signout(request):
    logout(request)
    return redirect("signin")

class PasswordResetView(View):
    def get(self,request):
        form = PasswordResetForm()
        return render(request,"password_reset.html",{"form":form})
    def post(self,request):
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            oldpassword = form.cleaned_data.get("oldpassword")
            newpassword = form.cleaned_data.get("newpassword")
            user = authenticate(request,username=request.user,password=oldpassword)
            if user:
                user.set_password(newpassword)
                user.save()
                return redirect("signin")
            else:
                return render(request, "password_reset.html", {"form": form})
        else:
            return render(request, "password_reset.html", {"form": form})

# class AddToCart(View):
#     def post(self,request,*args,**kwargs):
#         book = Book.objects.get(id=kwargs["id"])
#         user = request.user
#         cart = Cart(product=book,user=user)
#         return redirect("custhome")
def add_to_cart(request,id):
    book = Book.objects.get(id=id)
    user = request.user
    cart = Cart(product=book,
                user=user)
    cart.save()
    return redirect("custhome")


class ViewMyCart(ListView):
    model = Cart
    template_name = "mycart.html"
    context_object_name = "carts"

