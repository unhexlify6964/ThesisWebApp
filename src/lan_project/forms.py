from django import forms
from .models import UserProject


# Model Form is a form that is bound(connected) to a model.
# a modelForm knows where to store that data .
class LanModelForm(forms.ModelForm):
    checkbox_port_choices = (('common', "scan common ports"),
                             ('all', "wider port scan"))

    port_options = forms.ChoiceField(label='Select what ports will be scanned', choices=checkbox_port_choices)
    update_db_option = forms.BooleanField(label='Update CVE database', required=False)

    class Meta:
        model = UserProject
        widgets = {
            'subnet': forms.TextInput(attrs={'placeholder': '192.168.1.0/24'}),
        }
        fields = ['project_name',
                  'subnet',
                  'port_options',
                  'update_db_option'
                  ]


class ArpSpoofForm(forms.Form):
    victim_ip = forms.GenericIPAddressField(label='Victim\'s IP:', required=True)
    host_ip = forms.GenericIPAddressField(label='Host\'s IP:', required=True)


