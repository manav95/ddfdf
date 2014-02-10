from django import forms
from main.models import Operation, SendText, SendCall, LookUpNearestWorker, EnterNewWorker

class sendText(forms.ModelForm):
     phoneNumber = forms.CharField(max_length=128, help_text="Enter the phone number.")
     message = forms.CharField(max_length=128, help_text="Enter what message you want to send")
     class Meta:
        model = SendText
class sendCall(forms.ModelForm):
         phoneNumber = forms.CharField(max_length=128, help_text="Enter the phone number.")
         class Meta:
            model = SendCall
class lookUpNearestWorker(forms.ModelForm):         
       xLocation = forms.IntegerField(help_text="Enter x location of ASHA worker")
       yLocation = forms.IntegerField(help_text="Enter y location of ASHA worker")
       class Meta:
         model = LookUpNearestWorker
class enterNewWorker(forms.ModelForm):
       phoneNumber = forms.CharField(max_length=128, help_text="Enter the phone number of ASHA worker.")
       name = forms.CharField(max_length=128, help_text="Enter the name of ASHA worker.")
       xLocation = forms.IntegerField(help_text="Enter x location of ASHA worker")
       yLocation = forms.IntegerField(help_text="Enter y location of ASHA worker")
       class Meta:
           model = EnterNewWorker
