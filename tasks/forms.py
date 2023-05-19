from django import forms
from django.forms import ValidationError
from django.utils import timezone
from tasks.models import Task

PRIORITIES = [
    ("L", "Prioridad baja"),
    ("N", "Prioridad normal"),
    ("H", "Prioridad alta"),
]


class SearchForm(forms.Form):
    query = forms.CharField(label="Buscar")
    priority = forms.MultipleChoiceField(
        label="Prioridad",
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=PRIORITIES,
    )
    urgent = forms.BooleanField(required=False, label="Urgente")


def fecha_en_futuro(value):
    if value:
        if value < timezone.now().date():
            raise ValidationError("La fecha de entrega debe ser en el futuro")


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "subject", "due_date", "priority", "urgent"]

    due_date = forms.DateField(
        validators=[
            fecha_en_futuro,
        ]
    )


class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "subject", "due_date", "priority", "urgent"]

    # def clean_due_date(self):
    #    due_date = self.cleaned_data["due_date"]
    #    fecha_en_futuro(due_date)
    #    return due_date

    def clean(self):
        cleaned_data = super().clean()
        due_date = self.cleaned_data["due_date"]
        fecha_en_futuro(due_date)
        return cleaned_data
