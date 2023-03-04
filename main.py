a=[5,10,6,4,2,7,3,4,1]

def mean():
    sum=0

    for i in range(0,len(a)):
        sum+=a[i]
    mean_val=sum/len(a)
    return round(mean_val,4)

def variance():
    var=0
    for i in range(0,len(a)):
         var+=(a[i]-mean())**2
    var_val=var/len(a)
    return round(var_val,4)

def sv():
    sv_val=variance()**0.5
    return round(sv_val,4)

