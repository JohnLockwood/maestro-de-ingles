from django.urls import path

from . import views

app_name = 'polls'  # Namespaces the views

urlpatterns = [
    # This was how the old non-generic views worked.
    #path('', views.index, name='index'),
    #path('<int:question_id>/', views.detail, name='detail'),
    #path('<int:question_id>/results/', views.results, name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),

    # Note For generic detail views <int:pk> is needed
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]