
from django.urls import path
from AppSnake import views

urlpatterns= [
            path('',views.inicio,name= 'Inicio'),
            path('kinesiologo/', views.kinesiologo,name='Kinesiologos'),
            path('masajistas/',views.masajista,name="Masajistas"),
            path('proyecto/',views.proyecto, name='Proyecto'),
            path('masajistaFormulario/',views.masajistaFormulario, name='masajistaFormulario'),
            path('masajistaBusqueda/',views.masajistaBusqueda, name='masajistaBusqueda'),
            path('buscar/',views.buscar),
            path('kinesiologosFormulario/',views.kinesiologoFormulario,name='kinesiologoFormulario'),
            path('kinesiologosBusqueda/',views.kinesiologoBusqueda,name='kinesiologoBusqueda'),
            path('proyectoFormulario/',views.proyectoFormulario,name="proyectoFormulario"),
            path('buscar2/',views.buscar2),
            
            ]