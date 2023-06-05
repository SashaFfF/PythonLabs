from django import forms
from  .models import *


class AddDealForm(forms.ModelForm):
    def __input__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['Owner'].empty_label = "Владелец не выбран"
    class Meta:
        model=Deal
        fields = '__all__'