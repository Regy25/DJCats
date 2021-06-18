from django.urls import path, include
from . import views

urlpatterns = [

    # listar las gatos de la bd
    path('listar_cats', views.listar_cats, name="listar_cats"),
        
    # agregar un gato 
    path('add_cat', views.add_cat, name="add_cat"),

    # editar un gato
    path('editar_cat/<int:id_cat>', views.editar_cat ,name="editar_cat"),

    # borrar un gato
    path('borrar_cat/<int:id_cat>', views.borrar_cat, name="borrar_cat"),

]
