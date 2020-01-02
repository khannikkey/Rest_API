from django import forms
from testapp.models import Employee

class EmployeeForm(forms.ModelForm):
    def clean_esal(self):
        inputsal = self.cleaned_data['esal']
        if inputsal<5000:
            raise forms.ValidationError('Salary Must be Greater Then 5000')
        return inputsal

    #it is based on Employee Model thats why we are using Meta
    class Meta:
        model = Employee
        fields= '__all__'
