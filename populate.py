import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'souravjobs.settings')
import django
django.setup()
from testapp.models import BangaloreJobs,PuneJobs,HydJobs
from faker import Faker
import random
fake = Faker()
def generate_random_mobile_number():
    # Choose the country code based on your requirements
    country_code = "+1"  # Replace with the desired country code
    # Generate the rest of the mobile number (10 digits)
    rest_of_number = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    # Concatenate the country code and the rest of the number
    mobile_number = country_code + rest_of_number
    return mobile_number
def populate(n):
    for _ in range(n):
        fname = fake.company()
        ftitle = fake.random_element(['Dont limit yourself.', 'Make your name web-friendly.', 'Be memorable but not too unique.'])
        frole = fake.random_element(['HR', 'Manager', 'Assistant Manager', 'CEO'])
        fdate = fake.date()
        fphno = generate_random_mobile_number()
        faddr = fake.address()
        #HydJobs.objects.get_or_create(name=fname, title=ftitle, role=frole, date=fdate, phno=fphno, address=faddr)
        #PuneJobs.objects.get_or_create(name=fname, title=ftitle, role=frole, date=fdate, phno=fphno, address=faddr)
        BangaloreJobs.objects.get_or_create(name=fname, title=ftitle, role=frole, date=fdate, phno=fphno, address=faddr)
n = int(input("Enter how many jobs to insert: "))
populate(n)
print(f'{n} no. of jobs inserted!')
