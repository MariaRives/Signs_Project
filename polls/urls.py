from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),   
    path("demographics/", views.demographics, name="demographics"),     
    path("rt/<str:id>/<str:part>", views.rt, name="firstPartRender"),
    path("preference/<str:id>/<int:counter>", views.preference, name="preference"),    
    path("importance/<str:id>", views.importance, name="importance"),
    path("training/<str:id>", views.training, name="training"),    
    path("intro/<str:id>/<str:part>",views.intro, name="intro"),
    #API Calls
    path("trainSings", views.firstPartTraining, name="trainSings"),
    path("getSigns1", views.getSigns1, name="firstPartJS"),
    path("getSigns2", views.getSigns2, name="firstPartJS"),
    path("saveRT", views.getSigns1, name="saveRT"),
    path("saveComp", views.saveComp, name="saveComp")

]
