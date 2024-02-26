from django.shortcuts import render
def galactic(request):
    if(request.method=="POST"):
        data=request.POST
        alpha=data.get('textalpha')
        delta=data.get('textdelta')
        u=data.get('textu')
        g=data.get('textg')
        r=data.get('textr')
        i=data.get('texti')
        z=data.get('textz')
        runid=data.get('textrunid')
        rerunid=data.get('textrerunid')
        camcol=data.get('textcamcol')
        fieldid=data.get('textfieldid')
        specobj=data.get('textspecobj')
        redshift=data.get('textredshift')
        plate=data.get('textplate')
        mjd=data.get('textmjd')
        fiberid=data.get('textfiberid')
        if('buttonpredict' in request.POST):
            import pandas as pd
            path="C:\\Users\\shara\\OneDrive\\Desktop\\Sanjana\\train_dataset.csv"
            data=pd.read_csv(path)
            inputs=data.drop('class',axis=1)
            output=data['class']
            import sklearn
            from sklearn.model_selection import train_test_split
            x_train,x_test,y_train,y_test=train_test_split(inputs,output,test_size=0.2)
            import sklearn
            from sklearn.ensemble import RandomForestClassifier
            model=RandomForestClassifier(n_estimators=100)
            model.fit(x_train,y_train)
            y_pred=model.predict(x_test)
            result=model.predict([[float(alpha),float(delta),float(u),float(g),float(r),float(i),float(z),int(runid),int(rerunid),int(camcol),int(fieldid),float(specobj or 0),float(redshift or 0),int(plate),int(mjd),int(fiberid)]])
            return render(request,'galactic.html',context={'result':result})
    return render(request,'galactic.html')