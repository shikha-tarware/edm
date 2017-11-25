from django import forms
from django.conf import settings
from .models import *

class AddCustomerForm(forms.ModelForm):
    Salutation          = forms.CharField(max_length=100)
    FirstName           = forms.CharField(max_length=100)
    LastName            = forms.CharField(max_length=100)
	Email               = forms.EmailField(max_length=100)
    PhoneNumber         = forms.CharField(max_length=15)
    StreetAddress       = forms.CharField(max_length=100)
    City                = forms.CharField(max_length=100)
    State               = forms.CharField(max_length=100)
    Zip                 = forms.CharField(max_length=100)
    CustomerType        = forms.CharField(max_length=2,required=False)

    class Meta:
        model = Customer
        fields = '__all__'
		
class AddVolunteerForm(forms.ModelForm):
    Salutation          = forms.CharField(max_length=100)
    FirstName           = forms.CharField(max_length=100)
    LastName            = forms.CharField(max_length=100)
	Email               = forms.EmailField(max_length=100)
    PhoneNumber         = forms.CharField(max_length=15)

    class Meta:
        model = Volunteer
        fields = '__all__'
		
class ServicesForm(forms.ModelForm):

    class Meta:
        model = Services
        fields = '__all__'
		
		
class ServicesReviewForm(forms.ModelForm):
	FirstName           = forms.CharField(max_length=100)
    LastName            = forms.CharField(max_length=100)
    ServiceOne          = forms.CharField(max_length=100)
	ServiceTwo          = forms.CharField(max_length=100)
	ServiceThree        = forms.CharField(max_length=100)
    DescriptionOne      = forms.CharField(max_length=100)
	DescriptionTwo      = forms.CharField(max_length=100)
	DescriptionThree    = forms.CharField(max_length=100)
	ServiceRatingOne    = forms.CharField(max_length=100)
	ServiceRatingTwo    = forms.CharField(max_length=100)
	ServiceRatingThree  = forms.CharField(max_length=100)
	ServiceRatingFour   = forms.CharField(max_length=100)
	ServiceRatingFive   = forms.CharField(max_length=100)
	ServiceDate         = forms.DateField(initial=datetime.date.today)

    class Meta:
        model = ServicesReview
        fields = '__all__'
	
class ServicesDetailsForm(forms.ModelForm):
	ServiceDetailOne          = forms.CharField(max_length=100)
	ServiceDetailTwo          = forms.CharField(max_length=100)
	ServiceDetailThree        = forms.CharField(max_length=100)
	ServiceTakenDate          = forms.DateField()
	ReviewDate         	  	  = forms.DateField(initial=datetime.date.today)

    class Meta:
        model = ServicesDetails
        fields = '__all__'

class AddDonorForm(forms.ModelForm):
    OrganizationName    = forms.CharField(max_length=100)
    Salutation          = forms.CharField(max_length=100)
    FirstName           = forms.CharField(max_length=100)
    LastName            = forms.CharField(max_length=100)
    Email               = forms.EmailField(max_length=100)
    PhoneNumber         = forms.CharField(max_length=15)
    Comments            = forms.CharField(max_length=100,required=False)
    StreetAddress       = forms.CharField(max_length=100)
    City                = forms.CharField(max_length=100)
    State               = forms.CharField(max_length=100)
    Zip                 = forms.CharField(max_length=100)
    ICS                 = forms.CharField(max_length=2,required=False)

    class Meta:
        model = Donors
        fields = '__all__'

class SearchDonorForm(forms.ModelForm):
    SearchQuery = forms.CharField(max_length=255)

    class Meta:
        model = SearchDonor
        fields = '__all__'
