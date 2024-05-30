from django import forms
from django.core.exceptions import ValidationError

from main.models import Category, Todo


class TodoItemForm(forms.ModelForm):
    deadline = forms.DateTimeField(widget=forms.SelectDateWidget)
    class Meta:
        model = Todo
        fields = ['category', 'body', 'deadline']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data['name']
        if Category.objects.filter(name=name).exists():
            raise ValidationError("Category with this name already exists!")
        return name

