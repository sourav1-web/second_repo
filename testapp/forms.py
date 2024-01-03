from django.forms import ModelForm
from django.contrib.auth.models import User
from testapp.models import HydJobs,BangaloreJobs,PuneJobs,Contact
class SignUpForm(ModelForm):
  class Meta:
    model=User
    fields=['first_name','last_name','email','username','password']


class HydUpdateForm(ModelForm):
  class Meta:
    model=HydJobs
    fields='__all__'

class BangaloreUpdateForm(ModelForm):
  class Meta:
    model=BangaloreJobs
    fields='__all__'   


class PuneUpdateForm(ModelForm):
  class Meta:
    model=PuneJobs
    fields='__all__'      

class contactusForm(ModelForm):
  class Meta:
    model=Contact
    fields='__all__'   
    