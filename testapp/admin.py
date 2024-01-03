from django.contrib import admin
from testapp.models import HydJobs,BangaloreJobs,PuneJobs
from testapp.models import Contact
# Register your models here.
class HydJobsAdmin(admin.ModelAdmin):
  list_display=['name','title','role','date','address']
class BangaloreJobsAdmin(admin.ModelAdmin):
  list_display=['name','title','role','date','address']
class PuneJobsAdmin(admin.ModelAdmin):
  list_display=['name','title','role','date','address']    
admin.site.register(HydJobs,HydJobsAdmin)  
admin.site.register(BangaloreJobs,BangaloreJobsAdmin)  
admin.site.register(PuneJobs,PuneJobsAdmin)  

class ContactAdmin(admin.ModelAdmin):
  list_display=['id','name','email','msg']
admin.site.register(Contact,ContactAdmin)  