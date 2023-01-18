from django.urls import path
from appestudiantes.views import (
    listar_estudiantes, listar_profesores, listar_cursos,
    crear_curso, buscar_cursos, crear_estudiante, crear_profesor
)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('alumnos/', listar_estudiantes, name="listar_alumnos"),
    path('crear-estudiante/', crear_estudiante, name="crear_estudiante"),
    path('profesores/', listar_profesores, name="listar_profesores"),
    path('crear-profesor/', crear_profesor, name="crear_profesor"),
    path('cursos/', listar_cursos, name="listar_cursos"),
    path('crear-curso/', crear_curso, name="crear_curso"),
    path('buscar-cursos/', buscar_cursos, name="buscar_cursos"),
]

urlpatterns += staticfiles_urlpatterns()