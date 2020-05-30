from django.urls import path
from . import views
from .views import (
    ListForms,
    CreateForm,
    FormDetails
)

urlpatterns = [
    path('', ListForms.as_view(), name='home'),
    path('form/<int:pk>/', FormDetails.as_view(), name='form-details'),
    path('form/create/', CreateForm.as_view(), name='form-create'),
    #path('form/<int:pk>/update/', FormUpdateView.as_view(), name='form-update'),
    path('form/<int:pk>/line/add/', VatCreateView.as_view(), name='line-create'),
    #path('form/<int:pk>/view-pdf/', views.view_as_pdf, name='finance-view_as_pdf'),
    #path('form/<int:pk>/pdf-download/', views.force_download_pdf, name='finance-download-view_as_pdf')
]
