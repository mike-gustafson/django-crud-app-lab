from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('systems/', views.systems_index, name='systems_index'),
    path('systems/create/', views.systems_create, name='systems_create'),
    path('systems/<int:system_id>/', views.systems_detail, name='systems_detail'),
    path('systems/<int:system_id>/games/create/', views.games_create, name='games_create'),
    path('games/<int:game_id>/', views.games_detail, name='games_detail'),
    path('games/<int:game_id>/update/', views.games_update, name='games_update'),
    path('games/<int:game_id>/delete/', views.games_delete, name='games_delete'),
    path('systems/<int:system_id>/accessories/create/', views.accessories_create, name='accessories_create'),
    path('accessories/<int:accessory_id>/', views.accessories_detail, name='accessories_detail'),
    path('accessories/<int:accessory_id>/update/', views.accessories_update, name='accessories_update'),
    path('accessories/<int:accessory_id>/delete/', views.accessories_delete, name='accessories_delete'),
    path('account/', views.account, name='account'),
]