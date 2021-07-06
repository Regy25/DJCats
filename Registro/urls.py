from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from Registro import views
from rest_framework.authtoken.views import obtain_auth_token  

urlpatterns = [

    # listar las gatos de la bd
    path('listar_cats', views.listar_cats, name="listar_cats"),
        
    # agregar un gato 
    path('add_cat', views.add_cat, name="add_cat"),

    # editar un gato
    path('editar_cat/<int:id_cat>', views.editar_cat ,name="editar_cat"),

    # borrar un gato
    path('borrar_cat/<int:id_cat>', views.borrar_cat, name="borrar_cat"),

    # pagina principal
    path('home', views.home,  name="home"),
    
    # redirecciona a la pagina principal
    path('', views.redir_home, name="redirect_home"),

    #este manda a la pagina principal cuando se presiona el logout
    path('logout', views.logout_view, name="logout"),
]

urlpatterns += [
    #api
    path('cat/',  views.cat_collection , name='cat_collection'),
    path('cat/<int:pk>/', views.cat_element ,name='cat_element'),
    #token
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

urlpatterns = format_suffix_patterns(urlpatterns)