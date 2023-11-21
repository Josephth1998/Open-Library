from django.urls import path
from library import views
urlpatterns=[
    path('libindex/',views.libindex,name='libindex'),
    path('displaycategoryfun/<itemcat>/',views.displaycategoryfun,name='displaycategoryfun'),
    path('booksinglefun/<int:dataid>/',views.booksinglefun,name='booksinglefun'),
    path('',views.userreg,name='userreg'),
    path('registersave/',views.registersave,name='registersave'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('userloginsave/',views.userloginsave,name='userloginsave'),
    path('userlogout/',views.userlogout,name='userlogout'),
    path('contact/',views.contact,name='contact'),
    path('contactsave/',views.contactsave,name='contactsave'),
]