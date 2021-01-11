from django.contrib import admin
from django.urls import path
from schoofi import views

urlpatterns = [
    path("", views.index,name="home"),
    path("about", views.about,name="about"),
    path("contact", views.contact,name="contact"),
    path("services", views.services,name="services"),
    path("loginsystem", views.loginsystem,name="loginsystem"),
    path("signup", views.signup,name="signup"),
    path("classifiadmin", views.classifiadmin,name="classifiadmin"),
    path("assignments", views.assignments,name="assignments"),
    path("logoutsystem", views.logoutsystem,name="logoutsystem"),
    path("attendance", views.attendance,name="attendance"),
    path("profile", views.profile,name="profile"),
]

