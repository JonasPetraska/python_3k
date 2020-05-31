from django.urls import path
from . import views
from .views import (
    ListForms,
    CreateForm,
    FormDetails,
    CreateFormLine,
    EditForm
)

urlpatterns = [
    path('', ListForms.as_view(), name='home'),
    path('form/<int:pk>/', FormDetails.as_view(), name='form-details'),
    path('form/create/', CreateForm.as_view(), name='form-create'),
    path('form/<int:pk>/edit/', EditForm.as_view(), name='form-edit'),
    path('form/<int:pk>/line/add/', CreateFormLine.as_view(), name='line-create'),
    path('form/<int:pk>/pdf-view/', views.form_as_pdf, name='form-pdf-view')
]
