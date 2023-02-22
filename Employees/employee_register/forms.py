from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['full_name', 'phone_number', 'emp_code',  'position']  # __all__ for all
        labels = {
            'full_name': 'Full name',
            'emp_code': 'Employee code'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['phone_number'].required = False
