from django.urls import path
from myapp import views
urlpatterns=[
    path('index/',views.index,name='index'),
    path('addgenre/',views.addgenre,name='addgenre'),
    path('savegenre/', views.savegenre, name='savegenre'),
    path('displaygenre/',views.displaygenre,name='displaygenre'),
    path('editgenre/<int:dataid>',views.editgenre,name='editgenre'),
    path('updategenre/<int:dataid>',views.updategenre,name='updategenre'),
    path('deletegenre/<int:dataid>',views.deletegenre,name='deletegenre'),
    path('addbooks/',views.addbooks,name='addbooks'),
    path('savebooks/',views.savebooks,name='savebooks'),
    path('displaybooks/',views.displaybooks,name='displaybooks'),
    path('editbooks/<int:dataid>',views.editbooks,name='editbooks'),
    path('updatebooks/<int:dataid>',views.updatebooks,name='updatebooks'),
    path('deletebooks/<int:dataid>',views.deletebooks,name='deletebooks'),
    path('loginfun/', views.loginfun, name='loginfun'),
    path('adminauth/', views.adminauth, name='adminauth'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),
    path('displaycontact/', views.displaycontact, name='displaycontact'),
    path('deletecontact/<int:dataid>', views.deletecontact, name='deletecontact'),

]