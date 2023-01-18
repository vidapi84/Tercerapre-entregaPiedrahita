from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from appestudiantes.models import Estudiante, Profesor, Curso
from appestudiantes.forms import CursoFormulario, EstudianteFormulario, ProfesorFormulario


def inicio(request):
    return render(
        request=request,
        template_name='appestudiantes/inicio.html',
    )


def listar_estudiantes(request):
    ## Aqui iria la validacion del permiso lectura estudiantes
    contexto = {
        'estudiantes': Estudiante.objects.all()
    }
    return render(
        request=request,
        template_name='appestudiantes/lista_estudiantes.html',
        context=contexto,
    )


def listar_profesores(request):
    contexto = {
        'profesores': Profesor.objects.all()
    }
    return render(
        request=request,
        template_name='appestudiantes/lista_profesores.html',
        context=contexto,
    )


def listar_cursos(request):
    contexto = {
        'cursos': Curso.objects.all()
    }
    return render(
        request=request,
        template_name='appestudiantes/lista_cursos.html',
        context=contexto,
    )

def crear_curso(request):
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            curso = Curso(nombre=data['nombre'], curso=data['curso'])
            curso.save()
            url_exitosa = reverse('listar_cursos')
            return redirect(url_exitosa)
    else:  # GET
        formulario = CursoFormulario()
    return render(
        request=request,
        template_name='appestudiantes/formulario_curso.html',
        context={'formulario': formulario},
    )

def crear_estudiante(request):
    if request.method == "POST":
        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            estudiante = Estudiante(nombre=data['nombre'], apellido=data['apellido'], dni=data['dni'], email=data['email'])
            estudiante.save()
            url_exitosa = reverse('listar_cursos')
            return redirect(url_exitosa)
    else:  # GET
        formulario = EstudianteFormulario()
    return render(
        request=request,
        template_name='appestudiantes/formulario_estudiante.html',
        context={'formulario': formulario},
    )

def crear_profesor(request):
    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            profesor = Profesor(nombre=data['nombre'], apellido=data['apellido'], dni=data['dni'], email=data['email'], profesion=data['profesion'])
            profesor.save()
            url_exitosa = reverse('listar_cursos')
            return redirect(url_exitosa)
    else:  # GET
        formulario = ProfesorFormulario()
    return render(
        request=request,
        template_name='appestudiantes/formulario_profesores.html',
        context={'formulario': formulario},
    )

def buscar_cursos(request):
    if request.method == "POST":
        data = request.POST
        cursos = Curso.objects.filter(
            Q(curso__contains=data['busqueda']) | Q(curso__exact=data['busqueda'])
        )
        contexto = {
            'cursos': cursos
        }
        return render(
            request=request,
            template_name='appestudiantes/lista_cursos.html',
            context=contexto,
        )
