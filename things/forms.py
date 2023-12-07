"""Forms of the project."""
from django import forms  
from things.models import Thing  

# Create your forms here.

  
class ThingForm(forms.ModelForm):  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["description"].widget = forms.Textarea(attrs={"maxlength": 120})
        self.fields["quantity"].widget = forms.NumberInput()

    class Meta:  
        model = Thing  
        exclude = ('created_at',)