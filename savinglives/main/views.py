from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from twilio.rest import TwilioRestClient
from main.models import Operation, SendText, SendCall, LookUpNearestWorker, EnterNewWorker
from main.forms import sendText, sendCall, lookUpNearestWorker, enterNewWorker
import subprocess
def mainIndex(request):
       context = RequestContext(request)
       operationsList = Operation.objects.all()
       context_dict = {'operations':operationsList}
       return render_to_response('main/index.html',context_dict,context)
def send(request):
   context = RequestContext(request)
   if request.method == 'POST':
        form = sendText(request.POST)
        if form.is_valid():
            form.save(commit=True)
            account_sid = "AC5b4554ce206c4d06dd07b282e8b07790"
            auth_token  = "dc0b2014b6f566b7f5f88c802e283305"
            client = TwilioRestClient(account_sid, auth_token)
            message = client.sms.messages.create(body="Yo this Twilio actually works",
              to="+17706174766",    # Replace with your phone number
              from_="+19199487371") # Replace with your Twilio number
            return mainIndex(request)
        else:
            print form.errors
   else:
        form = sendText()
   return render_to_response('main/send.html', {'form': form}, context)
def texts(request):
       context = RequestContext(request)
       account_sid = "AC5b4554ce206c4d06dd07b282e8b07790"
       auth_token  = "dc0b2014b6f566b7f5f88c802e283305"
       client = TwilioRestClient(account_sid, auth_token)
       messages = client.messages.list()
       olations = []
       for message in messages:
              olations.append(message.body)
       context_dict = {'finito': olations}
       return render_to_response('main/texts.html', context_dict,context)
def call(request):
   context = RequestContext(request)
   if request.method == 'POST':
        form = sendCall(request.POST)
        if form.is_valid():
            form.save(commit=True)
            p = subprocess.Popen(['ruby', 'callPy.rb'], cwd='/Users/manavdutta/Downloads/savinglives/main', shell=False, stdout=subprocess.PIPE)                               
            output, errors = p.communicate()                        
            return mainIndex(request)
        else:
            print form.errors
   else:
        form = sendCall()
   return render_to_response('main/call.html', {'form': form}, context)
def data(request):
      context = RequestContext(request)
      context_dict = {'calif':"verdy"}
      return render_to_response('main/data.html', context_dict,context)
def viewNear(request):
   context = RequestContext(request)
   if request.method == 'POST':
      nearestWorker = None
      xLoc = LookUpNearestWorker.objects.all()[0].xLocation
      yLoc = LookUpNearestWorker.objects.all()[0].yLocation
      if (EnterNewWorker.objects.all() != None):
             for worker in EnterNewWorker.objects.all():
                    if (nearestWorker == None):
                           nearestWorker = worker
                    else:
                      a = [xLoc,yLoc]
                      b = [worker.xLocation,worker.yLocation]
                      c = [nearestWorker.xLocation,nearestWorker.yLocation]
                      old_dist = math.sqrt(math.pow((a[0]-b[0]),2)+math.pow((a[0]-b[0]),2))
                      new_dist = math.sqrt(math.pow((a[0]-c[0]),2)+math.pow((a[0]-c[0]),2))
                      if old_dist < new_dist:
                             nearestWorker = worker

      return render_to_response('main/returnNearest.html', {'phone': nearestWorker.phoneNumber}, context)
   else:
      return mainIndex(request)      
def findNear(request):    
   context = RequestContext(request)
   if request.method == 'POST':
        form = lookUpNearestWorker(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return viewNear(request)
        else:
            print form.errors
   else:
        form = lookUpNearestWorker()
   return render_to_response('main/enterNearest.html', {'form': form}, context)
def enterNew(request):
   print "access enterNew"
   listIdeal = EnterNewWorker.objects.all()
   for item in listIdeal:
          print item.name
   context = RequestContext(request)
   if request.method == 'POST':
        form = enterNewWorker(request.POST)
        if form.is_valid():
            form.save(commit=True)
            
            return mainIndex(request)
        else:
            print form.errors
   else:
        form = enterNewWorker()
   return render_to_response('main/addNewWorker.html', {'form': form}, context)
                            
