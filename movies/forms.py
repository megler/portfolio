from django import forms


class Movie_Title(forms.Form):
    movie_title = forms.CharField(
        required=True, widget=forms.TextInput(attrs={"class": "form-control"}))


class Movie_Rating(forms.Form):
    movie_rating = forms.FloatField(widget=forms.NumberInput(
        attrs={
            "class": "form-control",
            "min": 0,
            "max": 10,
            "type": "number"
        }))
    movie_review = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control"}))
