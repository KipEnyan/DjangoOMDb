from django import forms

class TitleForm(forms.Form):
    movie_title = forms.CharField(label="Title:", max_length=255)
    movie_year = forms.CharField(label="Year:",max_length=4, required=False)