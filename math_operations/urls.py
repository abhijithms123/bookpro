"""math_operations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from calculation import views
from book import views as bv
from mobile import views as mv
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('operations/add', views.add),
    path('operations/sub', views.sub),
    path('operations/mul', views.mul),
    path('operations/div', views.div),
    path('operations/vowels', views.get_vowels),
    path('operations/prime', views.get_prime),
    path('operations/wordcount', views.word_count),
    path('operations/cbv/add', views.AddView.as_view(), name="addition"),
    path('operations/cbv/sub', views.SubView.as_view(), name="subtraction"),
    path('operations/cbv/mul', views.MulView.as_view(), name="multiplication"),
    path('operations/cbv/div', views.DivView.as_view(), name="division"),
    path('', views.IndexView.as_view(), name="index"),
    path('books/add',bv.BookView.as_view(), name="addbook"),
    path('books/all', bv.BookList.as_view(), name="allbooks"),
    path('books/<int:id>', bv.BookDetailView.as_view(), name="bookdetail"),
    path('books/change/<int:id>',bv.ChangeBook.as_view(),name="bookchange"),
    path('mobiles/add', mv.MobileView.as_view(), name = "addmobile"),
    path('books/remove/<int:id>',bv.BookDeleteView.as_view(),name="bookdelete"),
    path("customers/",include("customer.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

