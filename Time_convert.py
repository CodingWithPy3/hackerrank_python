s='07:05:45PM'

l=s.split(':')
a=l[2][2].upper()
if(a=='P'):
    hr=int(l[0])
    if(hr<12):
        hr=int(l[0])+12
    if(hr>24):
       hr=hr-24
       res=str(hr)+':'+l[1]+':'+l[2][0]+l[2][1]
    elif(hr==24):
       hr=00
       res=str(hr)*2+':'+l[1]+':'+l[2][0]+l[2][1]
    else:
       res=str(hr)+':'+l[1]+':'+l[2][0]+l[2][1] 
    pass

else:
   hr=l[0]
   if(l[0]=='12'):
       hr='00'
   res=hr+':'+l[1]+':'+l[2][0]+l[2][1]

print(res)
