from django.db import models

# Create your models here.
class Register(models.Model):
    Username = models.CharField(max_length=50)
    Email = models.EmailField()
    Password = models.CharField(max_length=20)
    def __str__(self):
        return self.Username
    
class Login(models.Model):
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=20)    
    def __str__(self):
        return self.Username 
    
class NewTickets(models.Model):
    tags = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    cc = models.CharField(max_length=100)
    assign = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    ipr = models.CharField(max_length=100)
    ikbl = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    attach = models.FileField()
    
    def _str_(self):
        return self.name
    
class Newproduct1(models.Model):
    Productname = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Type = models.CharField(max_length=100)   

class NewDoctor(models.Model):
    Title = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
    Phone = models.CharField(max_length=15)
    Clinicname = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)
    Specialization = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Callstatus = models.CharField(max_length=50) 

class NewCustomer(models.Model):
    Clinic3 = models.CharField(max_length=50)
    VATnumber3 = models.CharField(max_length=50)
    Phone3 = models.CharField(max_length=50)
    Website3 = models.CharField(max_length=50)
    Group3 = models.CharField(max_length=50)
    Currency3 = models.CharField(max_length=50)
    Language3 = models.CharField(max_length=50)
    Address3 = models.CharField(max_length=50)
    City3 = models.CharField(max_length=50)
    State3 = models.CharField(max_length=50)
    Zipcode3 = models.CharField(max_length=50)
    Country3 = models.CharField(max_length=50)

class NewLeads(models.Model):
    Status2 = models.CharField(max_length=50)
    Specialisation2 = models.CharField(max_length=100)
    Assigned2 = models.CharField(max_length=50)
    Tags2 = models.CharField(max_length=50)
    Name2 = models.CharField(max_length=50)
    Address2 = models.CharField(max_length=100)
    Position2 = models.CharField(max_length=50)
    City2 = models.CharField(max_length=50)
    Email2 = models.EmailField(unique=True)
    State2 = models.CharField(max_length=50)
    Website2 = models.URLField(max_length=200, blank=True)
    Company2 = models.CharField(max_length=50)
    Phone2 = models.CharField(max_length=15)
    Country2 = models.CharField(max_length=50)
    Zipcode2 = models.CharField(max_length=50)
    Language2 = models.CharField(max_length=50)
    Description2 = models.TextField(max_length=200)
    Public2 = models.BooleanField(default=False)
    ContactedToday2 = models.BooleanField(default=False)
    Priority2 = models.CharField(max_length=50)
    Remark2 = models.TextField(max_length=200)

    
class Staff(models.Model):
    Profile = models.ImageField(upload_to='profiles/', blank=True)
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Position = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)
    Direction = models.CharField(max_length=100, blank=True)
    State = models.CharField(max_length=100)
    Phonenumber = models.CharField(max_length=20)
    Facebook = models.URLField(max_length=200, blank=True)
    Linkedin = models.URLField(max_length=200, blank=True)
    Skype = models.CharField(max_length=100, blank=True)
    Language = models.CharField(max_length=100)
    Emailsignature = models.TextField(blank=True)
    Departments = models.CharField(max_length=100)
    Administrator = models.BooleanField(default=False)
    SWE = models.BooleanField(default=False)
    Password = models.CharField(max_length=100)