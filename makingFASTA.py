nam=open("Downloads/name.txt",'r')
for n in nam:
    n=n.rstrip()
    k=0
    
    if n[0]=='N'and n[-1]=='n':#Negetive trainning
        m="Downloads/dataset2/"+n+".txt"
        n="Downloads/dataset1/"+n+".txt"
        fileRead=open(n,'r')
        wr=open(m,'w+')
        for f in fileRead:
            
            if k==0:
                f=f.rstrip()
                wr.write(f+"|"+"0"+"|"+"training"+"\n")
                k=1
            else:
                wr.write(f)
                k=0
        wr.close()
        
    elif n[0]=='N'and n[-1]=='t':#Negetive testing
        m="Downloads/dataset2/"+n+".txt"
        n="Downloads/dataset1/"+n+".txt"
        fileRead=open(n,'r')
        wr=open(m,'w+')
        for f in fileRead:
            
            if k==0:
                f=f.rstrip()
                wr.write(f+"|"+"0"+"|"+"testing"+"\n")
                k=1
            else:
                wr.write(f)
                k=0
        wr.close()
        
    elif n[0]=='P'and n[-1]=='n':#Positive trainning
        m="Downloads/dataset2/"+n+".txt"
        n="Downloads/dataset1/"+n+".txt"
        fileRead=open(n,'r')
        wr=open(m,'w+')
        for f in fileRead:
            
            if k==0:
                f=f.rstrip()
                wr.write(f+"|"+"1"+"|"+"training"+"\n")
                k=1
            else:
                wr.write(f)
                k=0
        wr.close()
        
    elif n[0]=='P'and n[-1]=='t':#Positive testing
        m="Downloads/dataset2/"+n+".txt"
        n="Downloads/dataset1/"+n+".txt"
        fileRead=open(n,'r')
        wr=open(m,'w+')
        for f in fileRead:
            
            if k==0:
                f=f.rstrip()
                wr.write(f+"|"+"1"+"|"+"testing"+"\n")
                k=1
            else:
                wr.write(f)
                k=0
        wr.close()

