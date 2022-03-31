from django.shortcuts import render,redirect
from book.forms import BookForm
from django.urls import reverse_lazy
from django.views.generic import View,ListView,CreateView,DetailView,UpdateView
from book.models import Book

# Create your views here.


class BookView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "book_add.html"
    success_url = reverse_lazy("allbooks")
    # def get(self, request):
    #     form = BookForm()
    #     return render(request, "book_add.html", {"form": form})
    #
    # def post(self,request):
    #     form = BookForm(request.POST,files=request.FILES)
    #     if form.is_valid():
    #         # print(form.cleaned_data)
    #         # print(form.cleaned_data.get("book_name"))
    #         # qs = Book(book_name=form.cleaned_data.get("book_name"),Author=form.cleaned_data.get("author"),
    #         #           copies=form.cleaned_data.get("copies"),amount=form.cleaned_data.get("price"))
    #         # qs.save()
    #         form.save()
    #
    #         return redirect("allbooks")
    #     else:
    #         return render(request, "book_add.html", {"form": form})

class BookList(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "books"
    # def get(self, request):
    #     qs = Book.objects.all()
    #     return render(request, "book_list.html", {"books":qs})

class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"
    context_object_name = "book"
    pk_url_kwarg = "id"
    # def get(self, request,*args,**kwargs):
    #     #pass
    #     #kwargs={'id':3}
    #     qs=Book.objects.get(id=kwargs.get("id"))
    #     return render(request,"book_detail.html",{"book":qs})

class BookDeleteView(View):
    def get(self, request,*args,**kwargs):
        qs=Book.objects.get(id=kwargs.get("id"))
        qs.delete()
        return redirect("allbooks")

class ChangeBook(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "book_edit.html"
    success_url = reverse_lazy("allbooks")
    pk_url_kwarg = "id"
    # def get(self, request,*args,**kwargs):
    #     qs = Book.objects.get(id=kwargs.get("id"))
    #     form = BookForm(instance=qs)
    #     return render(request,"book_edit.html",{"form":form})
    # def post(self, request,*args,**kwargs):
    #     qs = Book.objects.get(id=kwargs.get("id"))
    #     form = BookForm(request.POST,instance=qs,files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #     return redirect("allbooks")


