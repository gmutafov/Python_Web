from django.urls import path, include

from urlsAndViews.departments import views


urlpatterns = [
    path('', views.index, name='home'),
    path('redirect-to-views/', views.redirect_to_view, name='redirect-view'),
    path('softuni/', views.redirect_to_softuni),
    path('numbers/', include([
        path('<int:pk>/', views.view_with_int_pk),
        path('<int:pk>/<slug:slug>/', views.view_with_slug),
    ])),

    path('<variable>/', views.view_with_name),
    path('<path:variable>', views.view_with_name),
]