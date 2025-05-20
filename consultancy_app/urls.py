from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('book-consultation/', views.book_consultation, name='book_consultation'),
    path('united-kingdom/', views.united_kingdom, name='united_kingdom'),
    path('australia/', views.australia, name='australia'),
    path('canada/', views.canada, name='canada'),
    path('usa/', views.usa, name='usa'),
    path('france/', views.france, name='france'),
    path('malta/', views.malta, name='malta'),
    path('denmark/', views.denmark, name='denmark'),
    path('south-korea/', views.south_korea, name='south_korea'),
    path('hungary/', views.hungary, name='hungary'),
    path('germany/', views.germany, name='germany'),
    path('location/', views.location, name='location'),
    path('blogs/', views.blogs, name='blogs'),
    path('faqs/', views.faqs, name='faqs'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
    path('submit-contact/', views.submit_contact, name='submit_contact'),
    path('become-a-partner/', views.become_a_partner, name='become_a_partner'),
]