from django import forms
from crud.apps.models import Asignatura

class addAsignaturaForm(forms.Form):
	nombre 			= forms.CharField(widget=forms.TextInput(),required=True)
	pesoAsignatura 	= forms.IntegerField(required=True)

	def clean(self):
		return self.cleaned_data
	





