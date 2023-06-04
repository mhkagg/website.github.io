from django.urls import path
from . import views


urlpatterns = [
    path('page1/', views.page1, name='page1'),
    path('page2', views.page2, name='page2'),
    path('page3', views.page3, name='page3'),
    path('page4/', views.page4, name='page4'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),


    path('blogs/', views.blogs, name='blogs'),

    path('login/', views.login, name='login'),
  



    path('UttarPradesh/', views.UttarPradesh, name='UttarPradesh'),
    path('Uttrakhand/', views.Uttrakhand, name='Uttrakhand'),
    path('WestBangal/', views.WestBangal, name='WestBangal'),

    
    path('blogs/<int:blog_id>/edit/', views.edit_blog, name='edit_blog'),
    path('blogs/<int:blog_id>/delete/', views.delete_blog, name='delete_blog'),
      path('pune/', views.pune, name='pune'),
    path('delhi/', views.delhi, name='delhi'),
    path('manali/', views.manali, name='manali'),
    path('assam/', views.assam, name='assam'),
    path('mumbai/', views.mumbai, name='mumbai'),
    path('kerala/', views.kerala, name='kerala'),
    path('Sikkim/', views.Sikkim, name='Sikkim'),
    path('Andaman/', views.Andaman, name='Andaman'),
    path('AndraPradesh/', views.AndraPradesh, name='AndraPradesh'),
    path('ArunachalPradesh/', views.ArunachalPradesh, name='ArunachalPradesh'),
    path('Bihar/', views.Bihar, name='Bihar'),
    path('Gujarat/', views.Gujarat, name='Gujarat'),
    path('Haryana/', views.Haryana, name='Haryana'),

    path('Jammu/', views.Jammu, name='Jammu'),
    path('karnataka/', views.karnataka, name='karnataka'),
    path('kerala/', views.kerala, name='kerala'),
    path('Lakhak/', views.Lakhak, name='Lakhak'),
    path('Lakshadweep/', views.Lakshadweep, name='Lakshadweep'),
    path('MadhayaPradesh/', views.MadhayaPradesh, name='MadhayaPradesh'),
    path('Meghalaya/', views.Meghalaya, name='Meghalaya'),
    path('manali/', views.manali, name='manali'),
    
    path('Mizoram/', views.Mizoram, name='Mizoram'),
    path('mumbai/', views.mumbai, name='mumbai'),
    path('Nagaland/', views.Nagaland, name='Nagaland'),
    path('Lakhak/', views.Lakhak, name='Lakhak'),
    path('Odisha/', views.Odisha, name='Odisha'),
    path('Punjab/', views.Punjab, name='Punjab'),
    path('Rajasthan/', views.Rajasthan, name='Rajasthan'),
]
