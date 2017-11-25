# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render_to_response, render
from django.core.urlresolvers import reverse
from django.template import Context
import datetime
from django.http import HttpResponse
import re

from .forms import *
from .models import *


def health(request):
    return HttpResponse("3")

#@login_required(login_url="login/")
def index(request):
    template_name = 'ics_tool/home.html'

    if request.method == "GET":
        return render(request, template_name)

    form = SearchDataForm(request.POST)
    if form.is_valid():

      results = 'Welcome'

      return render(request,'ics_tool/home.html',{'Results' : results})

    print(form.errors)

    return render(request,'ics_tool/home.html',{})

def add_donor(request):
    template_name = 'ics_tool/add_donor.html'

    if request.method == "GET":
        return render(request, template_name)

    form = AddDonorForm(request.POST)
    if form.is_valid():
      OrganizationName = request.POST.get('OrganizationName', '')
      Salutation       = request.POST.get('Salutation', '')
      FirstName        = request.POST.get('FirstName', '')
      LastName         = request.POST.get('LastName', '')
      Email            = request.POST.get('Email', '')
      PhoneNumber      = request.POST.get('PhoneNumber', '')
      Comments         = request.POST.get('Comments', '')
      StreetAddress    = request.POST.get('StreetAddress', '')
      City             = request.POST.get('City', '')
      State            = request.POST.get('State', '')
      Zip              = request.POST.get('Zip', '')
      ICS              = request.POST.get('ICS', '')

      LoadDonorObj = Donors(OrganizationName=OrganizationName,Salutation=Salutation,FirstName=FirstName,LastName=LastName,
                            Email=Email,PhoneNumber=PhoneNumber,Comments=Comments,StreetAddress=StreetAddress,City=City,State=State,Zip=Zip,ICS=ICS)
      LoadDonorObj.save()

      return render(request,'ics_tool/donor_success.html',{})

    print(form.errors)

    return render(request,'ics_tool/add_donor.html',{})

def search_donor(request):

    template_name = 'ics_tool/search_donor.html'

    if request.method == "GET":
        return render(request, template_name)

    form = SearchDonorForm(request.POST)
    if form.is_valid():
      SearchQuery = request.POST.get('SearchQuery', '')

      results = Donors.objects.filter(Q(FirstName__icontains=SearchQuery)).values()

      return render(request,'ics_tool/donor_results.html',{'Results' : results})

    print(form.errors)

    return render(request,'ics_tool/search_donor.html',{})
	
def add_customer(request):
    template_name = 'ics_tool/add_customer.html'

    if request.method == "GET":
        return render(request, template_name)

    form = AddCustomerForm(request.POST)
    if form.is_valid():
      Salutation       = request.POST.get('Salutation', '')
      FirstName        = request.POST.get('FirstName', '')
      LastName         = request.POST.get('LastName', '')
      Email            = request.POST.get('Email', '')
      PhoneNumber      = request.POST.get('PhoneNumber', '')
      Comments         = request.POST.get('Comments', '')
      StreetAddress    = request.POST.get('StreetAddress', '')
      City             = request.POST.get('City', '')
      State            = request.POST.get('State', '')
      Zip              = request.POST.get('Zip', '')
      CustomerType     = request.POST.get('CustomerType', '')

      LoadCustomerObj = Customer(Salutation=Salutation,FirstName=FirstName,LastName=LastName,Email=Email,PhoneNumber=PhoneNumber,Comments=Comments,StreetAddress=StreetAddress,City=City,State=State,Zip=Zip,CustomerType=CustomerType)
      LoadCustomerObj.save()

      return render(request,'ics_tool/add_customer.html',{})

    print(form.errors)

    return render(request,'ics_tool/home.html',{})
	
def add_volunteer(request):
    template_name = 'ics_tool/add_volunteer.html'

    if request.method == "GET":
        return render(request, template_name)

    form = AddVolunteerForm(request.POST)
    if form.is_valid():
      Salutation       = request.POST.get('Salutation', '')
      FirstName        = request.POST.get('FirstName', '')
      LastName         = request.POST.get('LastName', '')
      Email            = request.POST.get('Email', '')
      PhoneNumber      = request.POST.get('PhoneNumber', '')
      
      LoadVolunteerObj = Volunteer(Salutation=Salutation,FirstName=FirstName,LastName=LastName,Email=Email,PhoneNumber=PhoneNumber)
      LoadVolunteerObj.save()

      return render(request,'ics_tool/add_volunteer.html',{})

    print(form.errors)

    return render(request,'ics_tool/home.html',{})
	
def add_service_review(request):
    template_name = 'ics_tool/add_service_review.html'

    if request.method == "GET":
        return render(request, template_name)

    form = ServicesReviewForm(request.POST)
    if form.is_valid():
      FirstName        = request.POST.get('FirstName', '')
      LastName         = request.POST.get('LastName', '')
      ServiceOne       = request.POST.get('ServiceOne', '')
	  ServiceTwo       = request.POST.get('ServiceTwo', '')
	  ServiceThree     = request.POST.get('ServiceThree', '')
	  DescriptionOne   = request.POST.get('DescriptionOne', '')
	  DescriptionTwo   = request.POST.get('DescriptionTwo', '')
	  DescriptionThree = request.POST.get('DescriptionThree', '')
      ServiceRatingOne = request.POST.get('ServiceRatingOne', '')
	  ServiceRatingTwo = request.POST.get('ServiceRatingTwo', '')
	  ServiceRatingThree = request.POST.get('ServiceRatingThree', '')
	  ServiceRatingFour = request.POST.get('ServiceRatingFour', '')
	  ServiceRatingFive = request.POST.get('ServiceRatingFive', '')
	  ServiceDate	   = request.POST.get('ServiceDate', '')
	
      LoadServicesReviewObj = ServicesReview(FirstName=FirstName,LastName=LastName,ServiceOne=ServiceOne,ServiceTwo=ServiceTwo,ServiceThree=ServiceThree,DescriptionOne=DescriptionOne,DescriptionTwo=DescriptionTwo,DescriptionThree=DescriptionThree,ServiceRatingOne=ServiceRatingOne,ServiceRatingTwo=ServiceRatingTwo,ServiceRatingThree=ServiceRatingThree,ServiceRatingFour=ServiceRatingFour,ServiceRatingFive=ServiceRatingFive,ServiceDate=ServiceDate)
      LoadServicesReviewObj.save()

      return render(request,'ics_tool/add_service_review.html',{})

    print(form.errors)

    return render(request,'ics_tool/home.html',{})

def add_service_details_form(request):
    template_name = 'ics_tool/add_service_details_form.html'

    if request.method == "GET":
        return render(request, template_name)

    form = ServicesReviewForm(request.POST)
    if form.is_valid():
      ServiceDetailOne       = request.POST.get('ServiceDetailOne', '')
	  ServiceDetailTwo       = request.POST.get('ServiceDetailTwo', '')
	  ServiceDetailThree     = request.POST.get('ServiceDetailThree', '')
	  ServiceTakenDate  	 = request.POST.get('ServiceTakenDate', '')
	  ReviewDate  	 		 = request.POST.get('ReviewDate', '')
	
      LoadServicesDetailsObj = ServicesDetails(ServiceDetailOne=ServiceDetailOne,ServiceDetailTwo=ServiceDetailTwo,ServiceDetailThree=ServiceDetailThree,ServiceTakenDate=ServiceTakenDate,ReviewDate=ReviewDate)
      LoadServicesDetailsObj.save()

      return render(request,'ics_tool/add_service_details_form.html',{})

    print(form.errors)

    return render(request,'ics_tool/home.html',{})

def add_item_donation(request):
    template_name = 'ics_tool/add_item_donation.html'

    if request.method == "GET":
        return render(request, template_name)

    form = ItemDonationForm(request.POST)
    if form.is_valid():
      ItemDescription        = request.POST.get('ItemDescription', '')
	  ACKstatus		         = request.POST.get('ACKstatus', '')
	  DonatedItemValue       = request.POST.get('DonatedItemValue', '')
	
      LoadItemDonationObj = ItemDonation(ItemDescription=ItemDescription,ACKstatus=ACKstatus,DonatedItemValue=DonatedItemValue)
      LoadItemDonationObj.save()

      return render(request,'ics_tool/add_item_donation.html',{})

    print(form.errors)

    return render(request,'ics_tool/home.html',{})
	
def add_monetary_donation(request):
    template_name = 'ics_tool/add_monetary_donation.html'

    if request.method == "GET":
        return render(request, template_name)

    form = MonetaryDonationForm(request.POST)
    if form.is_valid():
      ModeOfPayment        = request.POST.get('ModeOfPayment', '')
	  DonationValue	       = request.POST.get('DonationValue', '')
	
      LoadMoneyDonationObj = ItemDonation(ModeOfPayment=ModeOfPayment,DonationValue=DonationValue)
      LoadMoneyDonationObj.save()

      return render(request,'ics_tool/add_monetary_donation.html',{})

    print(form.errors)

    return render(request,'ics_tool/home.html',{})