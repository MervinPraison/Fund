from django.db import models

class data_fund(models.Model):
    fund_id = models.IntegerField(primary_key=True)
    fund_name = models.CharField(max_length=40)
    def __str__(self):
        return self.fund_name

class data_commitment(models.Model):
    commitment_id = models.AutoField(primary_key=True)  
    fund_id = models.ForeignKey(data_fund, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.IntegerField()

class data_call(models.Model):
    call_id = models.AutoField(primary_key=True) 
    #call_id = models.IntegerField()
    date = models.DateField()
    investment_name = models.CharField(max_length=40)
    capital_requirement = models.IntegerField()
    def __str__(self):
        return self.investment_name

class data_fund_investment(models.Model):
    id = models.AutoField(primary_key=True) 
    call_id = models.ForeignKey(data_call, on_delete=models.CASCADE)
    commitment_id = models.ForeignKey(data_commitment, on_delete=models.CASCADE)
    fund_id = models.ForeignKey(data_fund, on_delete=models.CASCADE)
