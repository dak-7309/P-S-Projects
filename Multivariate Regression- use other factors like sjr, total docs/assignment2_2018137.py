import csv
from math import *
import numpy
from itertools import combinations

def obtain_constants(Y,X):
    return numpy.dot(numpy.dot(numpy.linalg.pinv(numpy.dot(numpy.transpose(X),X)),numpy.transpose(X)),Y)

csv.register_dialect('myDialect',
delimiter = ';',
skipinitialspace=True)

with open('scimagojr_journal.csv', 'r') as csvFile, open('TEMP1.csv', 'w') as csvFile2:
    reader = csv.reader(csvFile, dialect='myDialect')
    P=0
    c=0
    count=0
    for roww in reader:
        if P>0:
            if int(roww[12])>0:
                count+=1
        P+=1
    COUNT=floor(0.8*count)

with open('scimagojr_journal.csv', 'r') as csvFile, open('TEMP1.csv', 'w') as csvFile2:
    reader = csv.reader(csvFile, dialect='myDialect')
    LIST_orig=[]
    for roww in reader:
        if c==0:
            data=[roww[2],roww[5],roww[7],roww[8],roww[9],roww[10],roww[11],roww[12],roww[13],roww[14],"Impact Factor"]
            writer = csv.writer(csvFile2)
            writer.writerow(data)

        elif c>0 and c<COUNT and int(roww[12])>0 :
            imp=int(roww[11])/int(roww[12])
            roww[5]=roww[5].replace(",",".")
            roww[12]=roww[12].replace(",",".")
            roww[13]=roww[13].replace(",",".")
            roww[14]=roww[14].replace(",",".")
           
            data=[roww[2],float(roww[5]),int(roww[7]),int(roww[8]),int(roww[9]),int(roww[10]),int(roww[11]),float(roww[12]),float(roww[13]),float(roww[14]),round(imp,5)]
            writer = csv.writer(csvFile2)
            writer.writerow(data)
          
        elif c>=COUNT and int(roww[12])>0:
            imp=int(roww[11])/int(roww[12])
            LIST_orig.append(round(imp,5))
            
            roww[5]=roww[5].replace(",",".")
            roww[12]=roww[12].replace(",",".")
            roww[13]=roww[13].replace(",",".")
            roww[14]=roww[14].replace(",",".")

            data=[roww[2],float(roww[5]),int(roww[7]),int(roww[8]),int(roww[9]),int(roww[10]),int(roww[11]),float(roww[12]),float(roww[13]),float(roww[14]),float(-10)]
            writer = csv.writer(csvFile2)
            writer.writerow(data)
        c+=1

csvFile.close()
csvFile2.close()
    
with open('TEMP1.csv', 'r') as csvFile3:
    reader = csv.reader(csvFile3)
    q=0
    LIST_1=[]
    LIST_2=[]
    LIST_3=[]
    LIST_4=[]
    LIST_5=[]
    LIST_6=[]
    LIST_7=[]
    LIST_8=[]
    LIST_9=[]
    LIST_imp_fac=[]
    
    LIST_1_testing=[]
    LIST_2_testing=[]
    LIST_3_testing=[]
    LIST_4_testing=[]
    LIST_5_testing=[]
    LIST_6_testing=[]
    LIST_7_testing=[]
    LIST_8_testing=[]
    LIST_9_testing=[]

    for roww in reader:
        if q>0 and q%2==0 and float(roww[10])!=-10.0:
            LIST_1.append(float(roww[1]))  
            LIST_2.append(int(roww[2]))  
            LIST_3.append(int(roww[3]))  
            LIST_4.append(int(roww[4]))  
            LIST_5.append(int(roww[5]))
            LIST_6.append(int(roww[6]))
            LIST_7.append(float(roww[7]))
            LIST_8.append(float(roww[8]))
            LIST_9.append(float(roww[9]))
            LIST_imp_fac.append(float(roww[10])) 

        elif q>0 and q%2==0 and float(roww[10])==-10.0:
            LIST_1_testing.append(float(roww[1]))  
            LIST_2_testing.append(int(roww[2]))  
            LIST_3_testing.append(int(roww[3]))  
            LIST_4_testing.append(int(roww[4]))  
            LIST_5_testing.append(int(roww[5]))
            LIST_6_testing.append(int(roww[6]))
            LIST_7_testing.append(float(roww[7]))
            LIST_8_testing.append(float(roww[8]))
            LIST_9_testing.append(float(roww[9]))
        q+=1 
csvFile3.close()

totality_list=[]
totality_list.append(LIST_1)
totality_list.append(LIST_2)
totality_list.append(LIST_3)
totality_list.append(LIST_4)
totality_list.append(LIST_5)
totality_list.append(LIST_6)
totality_list.append(LIST_7)
totality_list.append(LIST_8)
totality_list.append(LIST_9)

totality_list_testing=[]
totality_list_testing.append(LIST_1_testing)
totality_list_testing.append(LIST_2_testing)
totality_list_testing.append(LIST_3_testing)
totality_list_testing.append(LIST_4_testing)
totality_list_testing.append(LIST_5_testing)
totality_list_testing.append(LIST_6_testing)
totality_list_testing.append(LIST_7_testing)
totality_list_testing.append(LIST_8_testing)
totality_list_testing.append(LIST_9_testing)

COMBOS=sum([list(map(list,combinations(totality_list,i)))for i in range(len(totality_list)+1)],[])
COMBOS.remove([])
addo=[1]*461
addo_testing=[1]*117

COMBOS_testing=sum([list(map(list,combinations(totality_list_testing,i)))for i in range(len(totality_list_testing)+1)],[])
COMBOS_testing.remove([])

for i in range(len(COMBOS)):
    COMBOS[i].insert(0,addo)

for i in range(len(COMBOS_testing)):
    COMBOS_testing[i].insert(0,addo_testing)

all_combinations=[]
all_combinations_testing=[]

for i in range(len(COMBOS)):
    all_combinations.append(numpy.transpose(COMBOS[i]))

for i in range(len(COMBOS_testing)):
    all_combinations_testing.append(numpy.transpose(COMBOS_testing[i]))

temp=[]
temp.append(LIST_imp_fac)
Y_impact=numpy.transpose(temp)

constants_all=[]
for i in range(len(all_combinations)):
    constants_all.append(obtain_constants(Y_impact,all_combinations[i]))

predicted_Y=[]
for i in range(len(all_combinations_testing)):
    predicted_Y.append(numpy.dot(all_combinations_testing[i],constants_all[i]))

a=[]
for i in range(len(predicted_Y)):   
    a.append(numpy.transpose(predicted_Y[i]))

b=[]
for i in range(len(predicted_Y)):
    b.append(a[i][0])

ERROR_list=[]
MAE=[]
for i in range(len(b)):
    SUM=0
    abso=0
    for j in range(len(b[0])):
        SUM+=(b[i][j]-LIST_orig[j])**2
        abso+=abs(b[i][j]-LIST_orig[j])
    MEAN_E=SUM/len(LIST_orig)
    abso_E=abso/len(LIST_orig)
    MAE.append(abso_E)
    ERROR_list.append(MEAN_E)

w=sorted(ERROR_list)
w2=sorted(MAE)


dictionary=["SJR","H Index","Total Docs(2017)","Total Docs(3years)","Total Refs","Total Cites(3years)","Citable Docs(3years)","Cites/Doc(2years)","Ref/Doc"]
which_combi = sum([list(map(list, combinations(dictionary, i))) for i in range(len(dictionary) + 1)], [])
which_combi.remove([])

with open('ERRORS_all.csv','w') as File1:
    data=["Combination no","Combination","Mean Absolute Error", "Mean Squared error","Root Mean Squared Error"]
    writer = csv.writer(File1)
    writer.writerow(data)

    for i in range(len(w)):
        if "Cites/Doc(2years)" not in str(which_combi[i])[1:-1]: 
            data=[i+1,str(which_combi[i])[1:-1], MAE[i], ERROR_list[i] ,ERROR_list[i]**.5  ]
            writer = csv.writer(File1)
            writer.writerow(data)
File1.close


with open('RMSE_min.csv', 'w') as File2:
        data=["Combination no","Combination","Mean Squared error","Root Mean Squared Error"]
        writer = csv.writer(File2)
        writer.writerow(data)

        for i in range(len(w)):
            if "Cites/Doc(2years)" not in str(which_combi[ERROR_list.index(w[i])])[1:-1]: 
                data=[ERROR_list.index(w[i])+1,str(which_combi[ERROR_list.index(w[i])])[1:-1],w[i] ,w[i]**.5  ]
                writer = csv.writer(File2)
                writer.writerow(data)
File2.close

with open('MAE_min.csv','w') as File3:
    data=["Combination no","Combination","Mean Absolute Error"]
    writer = csv.writer(File3)
    writer.writerow(data)

    for i in range(len(w)):
        if "Cites/Doc(2years)" not in str(which_combi[MAE.index(w2[i])])[1:-1]: 
            data=[MAE.index(w2[i])+1,str(which_combi[MAE.index(w2[i])])[1:-1],w2[i]  ]
            writer = csv.writer(File3)
            writer.writerow(data)

File3.close