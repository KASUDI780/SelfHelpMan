from django import forms
from .models import Member
from .models import Contribution


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields='__all__'
    def __init__(self,*args,**kwargs):
        super(MemberForm,self).__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields='__all__'
    def __init__(self,*args,**kwargs):
        super(ContributionForm,self).__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
