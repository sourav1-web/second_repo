from django.shortcuts import render,redirect
from testapp.models import HydJobs,BangaloreJobs,PuneJobs
from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpForm,HydUpdateForm,BangaloreUpdateForm,PuneUpdateForm
from django.http import HttpResponseRedirect
# Create your views here.
def HomeView(request):
  return render(request, 'testapp/index.html')

@login_required
def HydearbadJobsView(request):
  hydjobs=HydJobs.objects.all()
  type='hyd'
  return render(request,'testapp/jobs.html',{'hydjobs':hydjobs,'type':type})
@login_required
def BangaloreJobsView(request):
  bangaloreJobs=BangaloreJobs.objects.all()
  type='bangalore'
  return render(request,'testapp/jobs.html',{'bangalorejobs':bangaloreJobs,'type':type})
@login_required
def PuneJobsView(request):
  puneJobs=PuneJobs.objects.all()
  type='pune'
  return render(request,'testapp/jobs.html',{'punejobs':puneJobs,'type':type})

def LogoutView(request):
  return render(request,'testapp/logout.html')

def SignupForm(request):
    if request.user.is_authenticated:
        # If user is already logged in, redirect to some other view or template
        return redirect('/')
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request, 'testapp/signup.html', {'form': form})

def HydDeleteRecord(request,id):
   job=HydJobs.objects.get(id=id)
   job.delete()
   return redirect('/hyd')

def HydUpdateRecord(request,id):
    jobs = HydJobs.objects.get(id=id)
    form = HydUpdateForm(instance =jobs)
    if request.method == 'POST':
        form = HydUpdateForm(request.POST,instance =jobs)
        if form.is_valid():
            form.save()
        return redirect('/hyd')
    return render(request,'testapp/update.html',{'form':form})

def BangaloreDeleteRecord(request,id):
   job=BangaloreJobs.objects.get(id=id)
   job.delete()
   return redirect('/bng')

def BangaloreUpdateRecord(request,id):
    jobs = BangaloreJobs.objects.get(id=id)
    form = BangaloreUpdateForm(instance =jobs)
    if request.method == 'POST':
        form = BangaloreUpdateForm(request.POST,instance =jobs)
        if form.is_valid():
            form.save()
        return redirect('/bng')
    return render(request,'testapp/update.html',{'form':form})

def PuneDeleteRecord(request,id):
   job=PuneJobs.objects.get(id=id)
   job.delete()
   return redirect('/pune')

def PuneUpdateRecord(request,id):
    jobs = PuneJobs.objects.get(id=id)
    form = PuneUpdateForm(instance =jobs)
    if request.method == 'POST':
        form = PuneUpdateForm(request.POST,instance =jobs)
        if form.is_valid():
            form.save()
        return redirect('/pune')
    return render(request,'testapp/update.html',{'form':form})


from .forms import contactusForm  # Import your form class

def contact_us_view(request):
    cform = contactusForm()  # Use the correct form class name
    if request.method == "POST":
       cform=contactusForm(request.POST)
       if cform.is_valid():
          cform.save()
          return redirect('/')
    return render(request, 'testapp/contact.html', {'cform': cform})

   


