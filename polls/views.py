import json
import random
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .models import *



# Starting page
def index(request):
    return render(request, "polls/index.html")

#This view is to gather demographics for the subjects
def demographics(request):
    if request.method == "POST":
        age = request.POST["age"]
        gender = request.POST["gender"]
        nationality = request.POST["nationality"]
        driversLicense = request.POST["DL"]
        yearsXP = request.POST["YOE"]
        subject = Subject(
            age=age,
            gender=gender,
            nationality=nationality,
            driversLicense=driversLicense,
            yearsXP=yearsXP,
        )
        subject.save()
        return render(request, "polls/intro.html", {"id":subject.id, "part": "training"})
    else:
        return render(request, "polls/demographics.html")  

#View for the first experiment of the survey
def training (request, id):
    return render(request, "polls/training.html", {"id":id})

def intro(request, id, part):
    return render(request, "polls/intro.html", {"id":id, "part": f"part{part}"})

def rt (request, id, part):
    return render(request, "polls/reactionTime.html", {"id":id, "part": part}) 

def firstPartTraining(request):
    commonSymbols = list(Signal.objects.filter(signalType="Training"))
    return JsonResponse([sign.serialize() for sign in commonSymbols], safe=False)

def getSigns1(request):
    if request.method == "GET":
        commonSymbols = list(Signal.objects.filter(signalType="Symbol", frequency="Common"))
        uncommonSymbols =list(Signal.objects.filter(signalType="Symbol", frequency="Uncommon"))
        symbols =  commonSymbols + uncommonSymbols
        random.shuffle(symbols)  
        return JsonResponse([sign.serialize() for sign in symbols], safe=False)
    else:
        data = json.loads(request.body)
        subject = Subject.objects.get(id=data.get("subjectID"))
        rT = data.get("rT")
        sign = Signal.objects.get(id=data.get("signID"))
        rT_toSave = Reaction_Time (
            subject = subject,
            signal = sign,
            reactionTime = rT
        )
        rT_toSave.save()
        return JsonResponse({"message": "RT saved"}, status=201)
    
def getSigns2(request):
    if request.method == "GET":
        textCommon = list(Signal.objects.filter(signalType="Text", frequency="Common"))
        bothCommon = list(Signal.objects.filter(signalType="Both", frequency="Common"))
        textUncommon = list(Signal.objects.filter(signalType="Text", frequency="Uncommon"))
        bothUncommon = list(Signal.objects.filter(signalType="Both", frequency="Uncommon"))
        signals = textCommon + bothUncommon + bothCommon + textUncommon  
        random.shuffle(signals)  
        return JsonResponse([sign.serialize() for sign in signals], safe=False)
    else:
        data = json.loads(request.body)
        subject = Subject.objects.get(id=data.get("subjectID"))
        rT = data.get("rT")
        sign = Signal.objects.get(id=data.get("signID"))
        rT_toSave = Reaction_Time (
            subject = subject,
            signal = sign,
            reactionTime = rT
        )
        rT_toSave.save()
        return JsonResponse({"message": "RT saved"}, status=201)
    
def saveComp (request):
    data = json.loads(request.body)
    subject = Subject.objects.get(id=data.get("subjectID"))
    answer = data.get("answer")
    sign = Signal.objects.get(id=data.get("signID"))
    comprehension = Identify(
        subject = subject,
        signal = sign,
        guess = answer
    )
    comprehension.save()
    return JsonResponse({"message": "Comprehension saved"}, status=201)

#View for the first experiment of the survey

def preference(request, id, counter):
    symbols =  list(Signal.objects.filter(signalType="Preference").values())
    if counter == len(symbols):   
        return render(request, "polls/intro.html", {"id":id, "part": "importance"})
    data = {
            "id": id,
            "symbol": symbols[counter],
            "counter": counter
        }      
    if request.method == "GET":
        return render(request, "polls/preferences.html", {"data": data})
    else:
        preference = request.POST["signal"]
        signal = Signal.objects.get(id = request.POST["signalID"])
        subject = Subject.objects.get(id=id)

        pref = Preference(
            subject = subject,
            signal = signal,
            preference = preference
        )
        pref.save()

        return render(request, "polls/preferences.html", {"data": data} )
    
    
def importance (request, id):
    symbols = list(Signal.objects.filter(signalType="Symbol").values())
    data = {
            "id": id,
            "symbols": symbols,            
        }
    if request.method == "GET":
        return render(request, "polls/importance.html", {"data": data} )
    else:
        subject = Subject.objects.get(id=id)        
        for key in request.POST:
            if key.startswith('signal'):
                id = request.POST[key].replace('signal','')
                signal = Signal.objects.get(id=id)
                signal_importance = request.POST[key]
                importance = Importance(
                    subject = subject,
                    signal = signal,
                    importance = signal_importance
                )
                importance.save()
        return render(request, "polls/end.html")

