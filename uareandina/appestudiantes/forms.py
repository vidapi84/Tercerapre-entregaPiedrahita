from django import forms


class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=64)
    curso = forms.IntegerField(required=True)

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    apellido = forms.CharField(required=True, max_length=64)
    dni = forms.IntegerField(required=True)
    email = forms.CharField(required=True, max_length=64)

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    apellido = forms.CharField(required=True, max_length=64)
    dni = forms.IntegerField(required=True)
    email = forms.CharField(required=True, max_length=64)
    profesion = forms.CharField(required=True, max_length=64)