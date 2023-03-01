from django.shortcuts import render

from django.http import HttpResponse
from joblib import load 
model =load('./savedModels/model_d.joblib')
# Create your views here.
def predictor(request):
    return render(request,"page.html")

def form_info(request):
    CreditScore=request.GET['cs']
    MIP=request.GET['mip']
    OrigUPB=request.GET['origupb']
    IsFirstTime =request.GET['isfirsttime']
    CreditRange_Excellent=request.GET['crex']
    CreditRange_Poor=request.GET['crpoor']
    y_pred =model.predict([[CreditScore,MIP,OrigUPB,IsFirstTime,CreditRange_Excellent,CreditRange_Poor]])
    print(y_pred)
    if y_pred[0]==1:
        y_pred='Ever Delinquent'
    else :
        y_pred='Not Ever Delinquent'
    return render(request,'result.html',{'result':y_pred})