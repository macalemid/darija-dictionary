from django import forms

class WordForm(forms.Form):
	darija = forms.CharField(label='Darija', max_length=201)
	arabic = forms.CharField(label='Arabic', max_length=201)
	english = forms.CharField(label='English', max_length=201)
	explanation = forms.CharField(label='explanation', max_length=10000)

