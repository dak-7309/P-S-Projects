import csv
from math import *

csv.register_dialect('myDialect',
delimiter = ';',
skipinitialspace=True)

with open('scimagojr_journal.csv', 'r') as csvFile, open('EDITED1.csv', 'w') as csvFile2:
    reader = csv.reader(csvFile, dialect='myDialect')
    c=0
    sum_h=0
    sum_im=0
    sum_cov=0
    sum_var_x=0
    sum_var_y=0
    num=0
    count=-1
    P=0
    for roww in reader:
        if P>0:
            if int(roww[12])>0:
                count+=1
        P+=1
    COUNT=floor(0.8*count)

with open('scimagojr_journal.csv', 'r') as csvFile, open('EDITED1.csv', 'w') as csvFile2:
    reader = csv.reader(csvFile, dialect='myDialect')
    LIST_orig=[]
    for roww in reader:
        if c==0:
            data=[roww[2], roww[7],"Impact Factor"]
            writer = csv.writer(csvFile2)
            writer.writerow(data)

        elif c>0 and c<COUNT and int(roww[12])>0 :
            imp=int(roww[11])/int(roww[12])
            data=[roww[2], roww[7],round(imp,5)]
            writer = csv.writer(csvFile2)
            writer.writerow(data)
                        
            sum_h+=int(roww[7])
            sum_im+=imp
            sum_cov+=int(roww[7])*imp
            sum_var_x+=int(roww[7])**2
            sum_var_y+=imp**2
            num+=1
            
        elif c>=COUNT and int(roww[12])>0:
            imp=int(roww[11])/int(roww[12])
            LIST_orig.append(round(imp,5))
            data=[roww[2], roww[7],-10]
            writer = csv.writer(csvFile2)
            writer.writerow(data)
            
        c+=1

    mean_h=round(sum_h/num,5)
    mean_im=round(sum_im/num,5)
    summation=(sum_cov)/num-(mean_h*mean_im)
    var_x=(sum_var_x/num)-((mean_h)**2)
    var_y=(sum_var_y/num)-((mean_im)**2)
    a=summation/var_x
    coeff=summation/((var_x**0.5)*(var_y**.5))
    print("a= ",round(a,5))
    b=mean_im-(a*mean_h)
    print("b= ",round(b,5))
    print("correlation coeffecient= ",round(coeff,5))


csvFile.close()
csvFile2.close()
    
with open('EDITED1.csv', 'r') as csvFile3, open('JOURNAL_final.csv', 'w') as csvFile4:
    reader = csv.reader(csvFile3)
    q=0
    LIST_fin=[]
    for roww in reader:
        if q==0:
            data=["Title","H Index","Impact Factor"]
            writer = csv.writer(csvFile4)
            writer.writerow(data)

        if q>0 and q%2==0 and roww[2]=='-10':
        
            data=[roww[0],roww[1], round(a*int(roww[1])+b,5)]
            LIST_fin.append (round(a*int(roww[1])+b,5))
            writer = csv.writer(csvFile4)
            writer.writerow(data)
        
        elif q>0 and q%2==0 and roww[2]!='-10':
            data=[roww[0],roww[1],roww[2]]
            writer = csv.writer(csvFile4)
            writer.writerow(data)
        q+=1 

SUM_error=0
for i in range(len(LIST_orig)):
    SUM_error+=(LIST_fin[i]-LIST_orig[i])**2

MEAN_FINALE=SUM_error/len(LIST_fin)
print("Mean square error value= ",round(MEAN_FINALE,5))
print("Root Mean square error value= ",round((MEAN_FINALE)**.5,5))


csvFile3.close()
csvFile4.close()

with open('scimagojr_conference.csv', 'r') as File1, open('CONFERENCE_final.csv', 'w') as File2:
    reader = csv.reader(File1, dialect='myDialect')
    c=0
    for roww in reader:
        if c==0:
            data=[roww[2], roww[7],"Impact Factor"]
            writer = csv.writer(File2)
            writer.writerow(data)

        elif c>0 and int(roww[12])>0 :
            
            data=[roww[2], roww[7],round(a*int(roww[7])+b,5)]
            writer = csv.writer(File2)
            writer.writerow(data)
        c+=1  

File1.close()
File2.close()