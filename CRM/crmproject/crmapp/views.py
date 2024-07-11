from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
from .models import *
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.
def dash(request):
    if 'id' in request.session:
        x = request.session['id']
        y = Register.objects.filter(Username=x)
        return render(request, 'dash.html', {"data": y})
    else:
        return redirect(dash)
    # return render(request, 'dash.html')
    


def signs(request): 
    return render(request, "signin_signup.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        data = Register.objects.create(
            Username = username,
            Email = email, 
            Password = password
        )
        data.save()
        data1 = Login.objects.create(
            Username = username,
            Password = password
        )
        data1.save()
        return redirect(signin)
    return render(request, 'signin_signup.html')
    
def signin(request):
    abc = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            data = Login.objects.filter(Username = username, Password = password).exists()
            if data:
                request.session['id'] = username
                return redirect(dash)
            else:
                abc['key'] = 'Password Incorrect'
                return render(request, 'signin_signup.html', abc)
        except Exception:
            abc['key1'] = 'Username Incorrect'
            return render(request, 'signin_signup.html', abc)    
    return render(request, 'signin_signup.html')

def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(signs) 
    
def ticket(request):
    tick = NewTickets.objects.all()
    return render(request, "ticket.html", {'tick':tick})


def ticket_wc(request):
    if request.method == "POST":
        tags = request.POST['tags']
        subject = request.POST['subject']
        contact = request.POST['contact']
        name = request.POST['name']
        email = request.POST['email']
        department = request.POST['department']
        cc = request.POST['cc']
        assign = request.POST['assign']
        priority = request.POST['priority']
        service = request.POST['service']
        ipr = request.POST['ipr']
        ikbl = request.POST['ikbl']
        content = request.POST['content']
        attach = request.POST['attach']
        tickets = NewTickets(tags=tags, subject=subject, contact=contact,
                             name=name,email=email,department=department,
                             cc=cc, assign=assign, priority=priority, service=service,
                             ipr=ipr,ikbl=ikbl, content=content, attach=attach )
        tickets.save()
        return redirect('/tic')
    return render(request, "ticket_wc.html")

def customer(request):
    cust = NewCustomer.objects.all()
    return render(request, "customer.html", {'cust1':cust})

def newcustomer(request):
    if request.method == 'POST':
        custclinic = request.POST['Clinic2']
        custvatnumber  = request.POST['VATnumber2']
        custphone = request.POST['Phone2']
        custwebsite = request.POST['Website2']
        custgroup = request.POST['Group2']
        custcurrency = request.POST['Currency2']
        custlanguage = request.POST['Language2']
        custaddress = request.POST['Address2']
        custcity = request.POST['City2']
        custstate = request.POST['State2']
        custzipcode = request.POST['Zipcode2']
        custcountry = request.POST['Country2']
        customer1 = NewCustomer(
            Clinic3 = custclinic,
            VATnumber3 = custvatnumber,
            Phone3 = custphone,
            Website3 = custwebsite,
            Group3 = custgroup,
            Currency3 = custcurrency,
            Language3 = custlanguage,
            Address3 = custaddress,
            City3 = custcity,
            State3 = custstate,
            Zipcode3 = custzipcode,
            Country3 = custcountry
        )
        customer1.save()
        return redirect('/cust')
    
def editcustomer(request,id):
    Cedit = get_object_or_404(NewCustomer, id=id)
    if request.method == 'POST':
        custclinic = request.POST['Clinic2']
        custvatnumber  = request.POST['VATnumber2']
        custphone = request.POST['Phone2']
        custwebsite = request.POST['Website2']
        custgroup = request.POST['Group2']
        custcurrency = request.POST['Currency2']
        custlanguage = request.POST['Language2']
        custaddress = request.POST['Address2']
        custcity = request.POST['City2']
        custstate = request.POST['State2']
        custzipcode = request.POST['Zipcode2']
        custcountry = request.POST['Country2']
        Cedit.Clinic3 = custclinic
        Cedit.VATnumber3 = custvatnumber
        Cedit.Phone3 = custphone
        Cedit.Website3 = custwebsite
        Cedit.Group3 = custgroup
        Cedit.Currency3 = custcurrency
        Cedit.Language3 = custlanguage
        Cedit.Address3 = custaddress
        Cedit.City3 = custcity
        Cedit.State3 = custstate
        Cedit.Zipcode3 = custzipcode
        Cedit.Country3 = custcountry
        Cedit.save()
        return redirect('/cust')
    return render(request, 'editcust.html', {'Cedit':Cedit})

    
def delecustomer(request,id):
    custdele = NewCustomer.objects.get(id=id)
    custdele.delete()
    return redirect('/cust')

def newcust(request):
    return render(request, "newcust.html")

def customFeild(request):
    return render(request, "customFeild.html")

def billandShip(request):
    return render(request, "bill&ship.html")

def followups(request):
    return render(request, "followups.html")

def new_doc(request):
    return render(request, "new_doc.html")

def newdoctor1(request):
    if request.method == 'POST':
        title = request.POST['Title']
        name = request.POST['Name']
        phone = request.POST['Phone']
        clinicname = request.POST['Clinic_name']
        email = request.POST['Email']
        specialization = request.POST['Specialization']
        state = request.POST['State']
        city = request.POST['City']
        callstatus = request.POST['Call_status']
        doctor = NewDoctor(
            Title = title,
            Name = name,
            Phone = phone,
            Clinicname = clinicname,
            Email = email,
            Specialization = specialization,
            State = state,
            City = city,
            Callstatus = callstatus
        )
        doctor.save()
        return redirect('/sac')
    
def searchAndCall(request):
    doc = NewDoctor.objects.all()
    return render(request, "searchAndCall.html", {'doct':doc})

def deledoctor(request,id):
    docdele = NewDoctor.objects.get(id=id)
    docdele.delete()
    return redirect('/sac')

def editdoctor(request, id):
    editdoc = get_object_or_404(NewDoctor, id=id)
    if request.method == 'POST':
        title = request.POST['Title']
        name = request.POST['Name']
        phone = request.POST['Phone']
        clinicname = request.POST['Clinic_name']
        email = request.POST['Email']
        specialization = request.POST['Specialization']
        state = request.POST['State']
        city = request.POST['City']
        callstatus = request.POST['Call_status']
        editdoc.Title = title,
        editdoc.Name = name,
        editdoc.Phone = phone,
        editdoc.Clinicname = clinicname,
        editdoc.Email = email,
        editdoc.Specialization = specialization,
        editdoc.State = state,
        editdoc.City = city,
        editdoc.Callstatus = callstatus
        editdoc.save()
        return redirect('/sac')
    return render(request, 'editdoctor.html', {'docedit': editdoc})

def searchid(request, id):
    search = NewDoctor.objects.get(id=id)
    return render(request, 's&c.html', {'search':search})

def new_pro(request):
    pro = Newproduct1.objects.all()
    return render(request, "newproduct.html", {'prod':pro})

def product1(request):
    if request.method == 'POST':
        productname = request.POST['Product_name']
        price = request.POST['Price']
        type = request.POST['Type']
        product = Newproduct1(
            Productname = productname,
            Price = price,
            Type = type
        )
        product.save()
        return redirect('/newpro')
    
def deleproduct(request,id):
    productdele = Newproduct1.objects.get(id=id)
    productdele.delete()
    return redirect('/newpro')    


def leads(request):
    lea = NewLeads.objects.all()
    return render(request, "leads.html", {'lead':lea})

def newleads(request):
    return render(request, "new_leads.html")

def Leads1(request):
    if request.method == "POST":
        status = request.POST['Status1']
        specialisation = request.POST['Specialisation1']
        assigned = request.POST['Assigned1']
        tags = request.POST['Tags1']
        name = request.POST['Name1']
        address = request.POST['Address1']
        position = request.POST['Position1']
        city = request.POST['City1']
        email = request.POST['Email1']
        state = request.POST['State1']
        website = request.POST['Website1']
        company = request.POST['Company1']
        phone = request.POST['Phone1']
        country = request.POST['Country1']
        zipcode = request.POST['Zipcode1']
        language = request.POST['Language1']
        description = request.POST['Description1']
        options = request.POST.get('Options1') == 'on'
        options2 = request.POST.get('Options2') == 'on'
        priority = request.POST['Priority1']
        remark = request.POST['Remark1']
        leadss = NewLeads(
            Status2 = status,
            Specialisation2 = specialisation,
            Assigned2 = assigned,
            Tags2 = tags,
            Name2 = name, 
            Address2 = address,
            Position2 = position,
            City2 = city,
            Email2 = email,
            State2 = state,
            Website2 = website,
            Company2 = company,
            Phone2 = phone,
            Country2 = country,
            Zipcode2 = zipcode,
            Language2 = language,
            Description2 = description,
            Public2 = options,
            ContactedToday2 = options2,
            Priority2 = priority,
            Remark2 = remark
        )
        leadss.save()
        return redirect('/lead')
    
def editleads (request, id):
    Ledit = get_object_or_404(NewLeads, id=id)
    if request.method == 'POST':
        status = request.POST['Status1']
        specialisation = request.POST['Specialisation1']
        assigned = request.POST['Assigned1']
        tags = request.POST['Tags1']
        name = request.POST['Name1']
        address = request.POST['Address1']
        position = request.POST['Position1']
        city = request.POST['City1']
        email = request.POST['Email1']
        state = request.POST['State1']
        website = request.POST['Website1']
        company = request.POST['Company1']
        phone = request.POST['Phone1']
        country = request.POST['Country1']
        zipcode = request.POST['Zipcode1']
        language = request.POST['Language1']
        description = request.POST['Description1']
        options = request.POST.get('Options1') == 'on'
        options2 = request.POST.get('Options2') == 'on'
        priority = request.POST['Priority1']
        remark = request.POST['Remark1']
        Ledit.Status2 = status,
        Ledit.Specialisation2 = specialisation
        Ledit.Assigned2 = assigned
        Ledit.Tags2 = tags
        Ledit.Name2 = name 
        Ledit.Address2 = address
        Ledit.Position2 = position
        Ledit.City2 = city
        Ledit.Email2 = email
        Ledit.State2 = state
        Ledit.Website2 = website
        Ledit.Company2 = company
        Ledit.Phone2 = phone
        Ledit.Country2 = country
        Ledit.Zipcode2 = zipcode
        Ledit.Language2 = language
        Ledit.Description2 = description
        Ledit.Public2 = options
        Ledit.ContactedToday2 = options2
        Ledit.Priority2 = priority
        Ledit.Remark2 = remark
        Ledit.save()
        return redirect('/lead')
    return render(request, 'leadsedit.html', {'Ledit':Ledit})

def deleleads(request, id):
    leaddele = NewLeads.objects.get(id=id)
    leaddele.delete()
    return redirect('/lead')

def newstaff(request):
    return render(request, "newstaff.html")

def stafform(request):
    if request.method == 'POST':
        profile = request.POST['image']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        position = request.POST['position']
        city = request.POST['city']
        email = request.POST['email']
        direction = request.POST['direction']
        state = request.POST['state']
        phonenumber = request.POST['phone_number']
        facebook = request.POST['facebook']
        linkedin = request.POST['linkedin']
        skype = request.POST['skype']
        language = request.POST['language']
        esigna = request.POST['email_signature']
        departments = request.POST['department']
        administrator = request.POST.get('Aoptions') == 'on'
        swe = request.POST.get('Soptions') == 'on'
        password = request.POST['password1']
        c_password = request.POST['password2']
        if password == c_password:
            staf = Staff(
                Profile=profile, 
                Firstname=firstname, 
                Lastname=lastname,
                Position=position,
                City=city, 
                Email=email,
                Direction=direction,
                State=state,
                Phonenumber=phonenumber,
                Facebook=facebook, 
                Linkedin=linkedin, 
                Skype=skype, 
                Language=language, 
                Emailsignature=esigna, 
                Departments=departments,
                Administrator=administrator, 
                SWE=swe, 
                Password=password
            )
            staf.save()
            return redirect('/setup')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('/newstaff')

def setup(request):
    a = Staff.objects.all()
    return render(request, "setup.html", {'st':a})

def editstaff(request, id):
    edit = get_object_or_404(Staff, id=id) 
    if request.method == 'POST':
        profile = request.FILES.get('image1')  # Use request.FILES for file uploads
        firstname = request.POST['first_name1']
        lastname = request.POST['last_name1']
        position = request.POST['position1']
        city = request.POST['city1']
        email = request.POST['email1']
        direction = request.POST['direction1']
        state = request.POST['state1']
        phonenumber = request.POST['phone_number1']
        facebook = request.POST['facebook1']
        linkedin = request.POST['linkedin1']
        skype = request.POST['skype1']
        language = request.POST['language1']
        esigna = request.POST['email_signature1']
        departments = request.POST['department1']
        administrator = request.POST.get('Aoptions1') == 'on'
        swe = request.POST.get('Soptions1') == 'on'
        password = request.POST['password12']
        c_password = request.POST['password21']
        # Assign values without the trailing comma
        edit.Profile = profile
        edit.Firstname = firstname
        edit.Lastname = lastname
        edit.Position = position
        edit.City = city
        edit.Email = email
        edit.Direction = direction
        edit.State = state
        edit.Phonenumber = phonenumber
        edit.Facebook = facebook
        edit.Linkedin = linkedin
        edit.Skype = skype
        edit.Language = language
        edit.Emailsignature = esigna
        edit.Departments = departments
        edit.Administrator = administrator
        edit.SWE = swe
        edit.Password = password
        edit.Password = c_password
        edit.save()
        return redirect('/setup')
    return render(request, 'staffedit.html', {'edit': edit})

def delestaff(request,id):
    ds = Staff.objects.get(id=id)
    ds.delete()
    return redirect('/setup')

def sandc(request):
    return render(request, "s&c.html")