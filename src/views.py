from django.shortcuts import render,redirect
import pandas as pd
import joblib

# Create your views here.
def index(request):
    return render(request,'index.html')

def form(request):
    return render(request,'form.html')

def result(request):
    try:
        if request.method == 'POST':
            age=int(request.POST['age'])
            sex=int(request.POST['sex'])
            cp=int(request.POST['cp'])
            trestbps=int(request.POST['trestbps'])
            chol=int(request.POST['chol'])
            fbs=int(request.POST['fbs'])
            restecg=int(request.POST['restecg'])
            thalach=int(request.POST['thalach'])
            exang=int(request.POST['exang'])
            oldpeak=float(request.POST['oldpeak'])
            slope=int(request.POST['slope'])
            ca=int(request.POST['ca'])
            thal=int(request.POST['thal'])

            arr = {
                'age':age,
                'sex':sex,
                'cp':cp,
                'trestbps':trestbps,
                'chol':chol,
                'fbs':fbs,
                'restecg':restecg,
                'thalach':thalach,
                'exang':exang,
                'oldpeak':oldpeak,
                'slope':slope,
                'ca':ca,
                'thal':thal
            }

            reg = joblib.load('model.joblib')
            predictions = reg.predict(pd.DataFrame(arr,index=[0]))
            # print(predictions[0])
            return render(request,'result.html',{'predictions':predictions[0]})
    except Exception as e:
        return redirect('form')
        