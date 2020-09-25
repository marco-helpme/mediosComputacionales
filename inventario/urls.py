from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bocinas', views.bocinasList, name='bocinasList'),
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
# ex: /polls/
    # ex: /polls/5/
    path('<int:id>/', views.detail, name='detail'),
    path('pc/<int:id>/', views.pc_component, name='pc_component'),
    path('region/<int:id>/', views.region_detail, name='region_detail'),
    path('area/<int:id>/', views.area_detail, name='area_detail'),
    path('pc/list', views.pc_list, name='pc_list'),
    # ex: /polls/5/results/
    # path('<int:pc_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    # path('<int:pc_id>/vote/', views.vote, name='vote'),
]