from django import forms


class searchForm(forms.Form):
    search_input = forms.CharField(max_length=100)
