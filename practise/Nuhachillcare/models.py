from django.db import models

# Create your models here.

brand_category=[
    ('Daikin','daikin'),('Samsung','samsung'),('Bluestar','bluestar'),('Whirlpool','whirlpool'),('Others','others')
]

issues=[
    ('Cooling Issues','cooling_issues'),('Electrical Problems','electrical problems') ,('Water Leakage','water leakage'),('Noisy Operation','noisy operation'),('Others','others')
]


class bhaiimodel(models.Model):
    para_name=models.CharField(max_length=20,blank=True,null=True)
    para_address=models.TextField(blank=True,null=True)
    para_ph_no=models.IntegerField(null=True)
    para_ac_brand=models.CharField(blank=True,null=True,max_length=30,choices=brand_category)
    para_ac_issue=models.CharField(blank=True,null=True,max_length=30,choices=issues)
    para_service_charges=models.IntegerField(null=True)
    para_service_date=models.DateField(null=True,blank=True)
    para_nxt_service_date=models.DateField(null=True,blank=True)


