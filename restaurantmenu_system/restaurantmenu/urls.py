"""
URL configuration for restaurantmenu_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# restaurantmenu/urls.py

from django.urls import path
from .views import upload_and_process_pdf  # Import the view you wrote in Step 4
from django.urls import path
from .views import upload_pdf_form, upload_and_process_pdf

urlpatterns = [
    path("upload-pdf/", upload_and_process_pdf, name="upload_pdf"),  # URL for PDF upload
]

urlpatterns = [
    path("upload-pdf/", upload_and_process_pdf, name="upload_pdf"),
    path("upload-form/", upload_pdf_form, name="upload_pdf_form"),
]
