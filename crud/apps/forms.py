from django import forms
from crud.apps.models import Asignatura

class addAsignaturaForm(forms.Form):
	nombre 			= forms.CharField(widget=forms.TextInput())
	pesoAsignatura 	= forms.IntegerField(required=True)
	activo          = forms.BooleanField(required=False, initial=True)

	def clean(self):
		return self.cleaned_data
	





