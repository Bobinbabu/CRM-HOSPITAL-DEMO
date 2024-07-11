from django.urls import path
from .import views


urlpatterns = [
    path("", views.signs, name="sign"),
    path("dash", views.dash, name="dash"),
    path("signup", views.signup, name="signup"),
    path("signin", views.signin, name="signin"),
    path("logout", views.logout, name="logout"), 
    path("tic", views.ticket, name="ticket"),
    path('twc', views.ticket_wc, name="tikwc"),
    path('cust', views.customer, name='cust'),
    path('newcustomer', views.newcustomer, name="newcustomer"),
    path('delecustomer/<int:id>', views.delecustomer, name='delecustomer'), #delete customer table
    path('editcustomer/<int:id>', views.editcustomer, name='editcustomer'), #edit customer table
    path("newcus", views.newcust, name="newcus"),
    path("customf", views.customFeild, name="customf"),
    path("billship", views.billandShip, name="billship"),
    path('lead', views.leads, name='lead'),
    path("newlead", views.newleads, name="newlead"),
    path('Leads1', views.Leads1, name='Leads1'),
    path('deleleads/<int:id>', views.deleleads, name='deleleads'), #delete leads table
    path('editleads/<int:id>', views.editleads, name='editleads'), #edit leads table
    path('flup', views.followups, name='followup'),
    path('sac', views.searchAndCall, name='sac'),
    path("s&c", views.sandc, name="s&c"),
    path('searchid/<int:id>', views.searchid, name="searchid"),
    path('newdoctor1', views.newdoctor1, name='newdoctor1'),
    path("newdoc", views.new_doc, name="newdoc"),
    path('deledoctor/<int:id>', views.deledoctor, name='deledoctor'), #delete doctor table
    path('editdoctor/<int:id>', views.editdoctor, name='editdoctor'), # edit doctor table
    path("newpro", views.new_pro, name="newpro"),
    path("product1", views.product1, name="product1"),
    path("deleproduct/<int:id>", views.deleproduct, name="deleproduct"), #delete product table
    path("newstaff", views.newstaff, name="newstaff"),
    path("stafform", views.stafform, name="stafform"),
    path("setup", views.setup, name="setup"),
    path('editstaff/<int:id>', views.editstaff, name="editstaff"), #edit staff table
    path('delestaff/<int:id>', views.delestaff, name="delestaff"), #delete staff table
]