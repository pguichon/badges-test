from django import forms

from .models import Model


class ModelCreateForm(forms.ModelForm):
    name = forms.CharField(max_length=48, required=False)

    class Meta:
        model = Model
        fields = ['file']
        exclude = ('user',)

    def save(self, commit=True):
        model = super(ModelCreateForm, self).save(commit)
        model.name = self.cleaned_data['name'] or self.cleaned_data['file'].name

        return model
