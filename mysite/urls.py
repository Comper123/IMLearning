from django.urls import path

from . import views


urlpatterns = [
    # path("", views.main, name="main"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("courses", views.courses, name="index"),
    path('loadsolution', views.load_solution)
]
