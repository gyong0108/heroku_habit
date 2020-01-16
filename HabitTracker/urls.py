"""HabitTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""
from django.contrib import admin
from django.urls import path, include
admin.autodiscover()

import Habit.views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.Habit_show, name = "Habit_show"),
	path("addhabit/", views.Add_Habit, name = "Add_Habit"),
	path("edithabit/", views.Edit_Habit, name = "Edit_Habit"),
	path("deletehabit/", views.Delete_Habit, name = "Delete_Habit"),
	path("modifyhabit/", views.Modify_Habit, name = "Modify_Habit"),
	path("chartshow/", views.Chart_show, name= "Chart_show"),
]
