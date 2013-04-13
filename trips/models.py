from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

PRICINGPLANS = (
  (1, 'Basic'),(2, 'Premium'),(2, 'Enterprise')
  )


class Company(models.Model):
  STATUSES = (
    (1, 'Active'),(2, 'Cancel'),
    )
  PEOPLE = (
    (1, 'ME'),(2, 'Company Admins'),(3,'Other'),
    )
  created_by = models.ForeignKey(User, editable=True)
  name = models.CharField('Name', max_length=300, null=False,blank=False)
  tripscanner_email=models.EmailField("TripScanner Email",max_length=100, null=False,blank=False)
  address1 = models.CharField('Address1', max_length=200, null=True)
  address2 = models.CharField('Address2', max_length=200, null=True)
  city = models.CharField('City', max_length=50, null=True)
  state = models.CharField('State', max_length=50, null=True)
  zip = models.CharField('Zip', max_length=20, null=True)
  industry = models.CharField('Industry', max_length=200, null=True)
  status=models.PositiveSmallIntegerField(choices=STATUSES,default=1)
  alert_who = models.SmallIntegerField(choices=PEOPLE,default=1)
  created_at=models.DateTimeField(auto_now_add=True)
  class Meta:
    verbose_name_plural = 'Company'

  def __unicode__(self):
    return self.name

class UserProfile(models.Model):
  CHOICES = (
    (1, 'Primary'),(2, 'Regular'),
    )
  user = models.OneToOneField(User, related_name='profile')
  company = models.ForeignKey(Company, editable=True)
  company_name = models.CharField('Company', max_length=200, null=True)
  type = models.SmallIntegerField(choices=CHOICES,default=2)

  class Meta:
    verbose_name_plural = 'User Profile'

  def __unicode__(self):
    return "%s,%s %s,%s" % (self.user, self.user.first_name, self.user.last_name, self.user.email)
class CompanyStatusLog(models.Model):
  user = models.ForeignKey(User, editable=True)
  company = models.ForeignKey(Company, editable=True)
  status=models.PositiveSmallIntegerField(choices=Company.STATUSES,default=1)
  reason=models.CharField('Reason', max_length=500, null=True)
  exit_interview = models.BooleanField(default=False)
  contact= models.BooleanField(default=False)
  created_at=models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'Company Status Log'

  def __unicode__(self):
    return self.company.name

class CompanyUser(models.Model):
  user = models.ForeignKey(User, editable=True)
  company = models.ForeignKey(Company, editable=True)
  created_by=models.ForeignKey(User, editable=True,related_name='created_by')
  type = models.SmallIntegerField(choices=UserProfile.CHOICES,default=2)
  first_name= models.CharField(max_length=100,null=False)
  last_name = models.CharField(max_length=100,null=False)
  email=models.EmailField("Email",max_length=100,null=False)
  created_at=models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'Company User'

  def __unicode__(self):
    return self.first_name

class Pricing(models.Model):
  user = models.ForeignKey(User, editable=True)
  name= models.CharField(max_length=100,null=False)
  itineraries= models.CharField(max_length=100,null=False)
  alerts=models.CharField("Trip Alerts",max_length=100,null=False)
  reporting=models.CharField("Reporting",max_length=200,null=False)
  created_at=models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'Company User'

  def __unicode__(self):
    return self.first_name

class CompanyPricing(models.Model):
  user = models.ForeignKey(User, editable=True)
  company = models.ForeignKey(Company, editable=True)
  pricing=models.ForeignKey(Pricing, editable=True)
  created_at=models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'Company Pricing'

  def __unicode__(self):
    return self.company.name
class CompanyPricingLog(models.Model):
  user = models.ForeignKey(User, editable=True)
  company = models.ForeignKey(Company, editable=True)
  pricing=models.ForeignKey(Pricing, editable=True)
  created_at=models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'Company Pricing Log'

  def __unicode__(self):
    return self.company.name
class CompanyBilling(models.Model):
  user = models.ForeignKey(User, editable=True)
  company = models.ForeignKey(Company, editable=True)
  pricing=models.ForeignKey(Pricing, editable=True)
  amount=models.DecimalField(null=True,decimal_places=2,max_digits=10)
  created_at=models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'Company Billing'

  def __unicode__(self):
    return self.company.name

class AlertTaker(models.Model):
  user = models.ForeignKey(User, editable=True)
  company = models.ForeignKey(Company, editable=True)
  email=models.EmailField(null=False)
  created_at=models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'Alert Taker'

  def __unicode__(self):
    return self.email

class FlightAlerts(models.Model):
  ALERTCHOICES = (
    (1, 'Never'),(2, 'Always'),(2, 'Only'),
    )
  user = models.ForeignKey(User, editable=True)
  company = models.ForeignKey(Company, editable=True)
  alert_when=models.SmallIntegerField(choices=ALERTCHOICES)
  airfare_greater=models.BooleanField(default=False)
  airfare_amount=models.DecimalField(null=True,decimal_places=2,max_digits=10)
  international=models.BooleanField(default=False)
  bf_class=models.BooleanField(default=False)
  adv_bf_class=models.BooleanField(default=False)
  adv_bf_hours=models.DecimalField(null=True,decimal_places=2,max_digits=10)
  adv_airfare_dom=models.BooleanField(default=False)
  adv_airfare_dom_amount=models.DecimalField(null=True,decimal_places=2,max_digits=10)
  adv_airfare_int=models.BooleanField(default=False)
  adv_airfare_int_amount=models.DecimalField(null=True,decimal_places=2,max_digits=10)
  adv_flight_booked=models.BooleanField(default=False)
  adv_flight_booked_days=models.SmallIntegerField(null=True)

  created_at=models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'Flight Alerts'

  def __unicode__(self):
    return self.comany.name

class HotelAlerts(models.Model):
  ALERTCHOICES = (
    (1, 'Never'),(2, 'Always'),(2, 'Only'),
    )
  user = models.ForeignKey(User, editable=True)
  company = models.ForeignKey(Company, editable=True)
  alert_when=models.SmallIntegerField(choices=ALERTCHOICES)
  rate_greater=models.BooleanField(default=False)
  rate_amount=models.DecimalField(null=True,decimal_places=2,max_digits=10)

  adv_rate_cost_cities=models.BooleanField(default=False)
  adv_rate_cost_cities_amount=models.DecimalField(null=True,decimal_places=2,max_digits=10)
  adv_rate_other_cities=models.BooleanField(default=False)
  adv_rate_other_cities_amount=models.DecimalField(null=True,decimal_places=2,max_digits=10)
  created_at=models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'Hotel Alerts'

  def __unicode__(self):
    return self.comany.name


class CarAlerts(models.Model):
  ALERTCHOICES = (
    (1, 'Never'),(2, 'Always'),(2, 'Only'),
    )
  user = models.ForeignKey(User, editable=True)
  company = models.ForeignKey(Company, editable=True)
  alert_when=models.SmallIntegerField(choices=ALERTCHOICES)
  rate_greater=models.BooleanField(default=False)
  rate_amount=models.DecimalField(null=True,decimal_places=2,max_digits=10)
  car_size=models.BooleanField(default=False)
  car_size_amount=models.SmallIntegerField()
  created_at=models.DateTimeField(auto_now_add=True)
  class Meta:
    verbose_name_plural = 'Hotel Alerts'

  def __unicode__(self):
    return self.comany.name

class RailAlerts(models.Model):
  ALERTCHOICES = (
    (1, 'Never'),(2, 'Always'),(2, 'Only'),
    )
  user = models.ForeignKey(User, editable=True)
  company = models.ForeignKey(Company, editable=True)
  alert_when=models.SmallIntegerField(choices=ALERTCHOICES)
  ticket_cost_greater=models.BooleanField(default=False)
  ticket_amount=models.DecimalField(null=True,decimal_places=2,max_digits=10)
  bf_class=models.BooleanField(default=False)
  created_at=models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'Rail Alerts'

  def __unicode__(self):
    return self.comany.name

