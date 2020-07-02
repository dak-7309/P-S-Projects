with open("tic-tac-toe.data.txt") as f:
    content = f.read().splitlines()
    line=[]
    for i in range(len(content)):
        line.append(content[i].split(','))

    count_baap=0
    count_desirable=0

    for i in range(len(line)):
        count_pos=0
        count_neg=0
        count_total=0
        for n in range(len(line)):
            if line[n][-1]=='positive' and n!=i:
                count_pos=count_pos+1
            if line[n][-1]=='negative' and n!=i: 
                count_neg=count_neg+1
            if n!=i:
                count_total=count_total+1
        P_Final_pos=count_pos/count_total
        P_Final_neg=count_neg/count_total

        count_baap=count_baap+1
        testing= line[i]
        training=line[:i]+line[i+1:]
        list_each_pos=[0]*9
        list_each_neg=[0]*9
        for j in range(len(training)):
            for k in range(9):
                if training[j][-1]=="positive" and (testing[k]==training[j][k]):
                   list_each_pos[k]=list_each_pos[k]+1
                if training[j][-1]=="negative" and (testing[k]==training[j][k]):
                        list_each_neg[k]=list_each_neg[k]+1
        for q in range(len(list_each_pos)):
                list_each_pos[q]=(list_each_pos[q])/(count_pos)
                list_each_neg[q]=(list_each_neg[q])/(count_neg)

        for q in range(len(list_each_pos)):
                P_Final_pos=P_Final_pos*list_each_pos[q]
                P_Final_neg=P_Final_neg*list_each_neg[q]
        # print(P_Final_pos,P_Final_neg)
        if testing[-1]=="positive" and P_Final_pos>P_Final_neg:
            count_desirable=count_desirable+1
        elif testing[-1]=="negative" and P_Final_neg>P_Final_pos:
            count_desirable=count_desirable+1
f.close()
OUTPUT1=(count_desirable/count_baap)
# "___________________________________________________________________________________________________"

with open("SPECT.train.txt") as f, open("SPECT.test.txt") as g:
    
    content1 = f.read().splitlines()
    training=[]
    testing=[]
    for i in range(len(content1)):
        training.append(content1[i].split(','))

    content2 = g.read().splitlines()
    for i in range(len(content2)):
        testing.append(content2[i].split(','))
    
    count_1=0
    count_0=0
    count_total=0
    for i in range(len(training)):
        if training[i][0]=='1':
            count_1=count_1+1
        elif training[i][0]=='0': 
            count_0=count_0+1
        count_total=count_total+1
    
    P_1=count_1/count_total
    P_0=count_0/count_total
    count_desirable=0

    for i in range(len(testing)):
        a=[0]
        list_each_1=a*22
        list_each_0=a*22
           
        for j in range(len(training)):
            for k in range(22):
                if training[j][0]=="1" and testing[i][k+1]==training[j][k+1]:
                    list_each_1[k]=list_each_1[k]+1
                elif training[j][0]=="0" and testing[i][k+1]==training[j][k+1]:
                    list_each_0[k]=list_each_0[k]+1
        for q in range(len(list_each_1)):
            list_each_1[q]=(list_each_1[q])/count_1
            list_each_0[q]=(list_each_0[q])/count_0
        P_Final_1=P_1
        P_Final_0=P_0

        for z in range(len(list_each_1)):
            P_Final_1=P_Final_1*list_each_1[z]
            P_Final_0=P_Final_0*list_each_0[z]

        if testing[i][0]=="1" and P_Final_1>P_Final_0:
            count_desirable=count_desirable+1
        elif testing[i][0]=="0" and P_Final_0>P_Final_1:
            count_desirable=count_desirable+1
    OUTPUT2=(count_desirable/len(testing))
f.close()
g.close()
# "___________________________________________________________________________________________________"


with open("soybean-small.data.txt") as f:
    content = f.read().splitlines()
    line=[]
    for i in range(len(content)):
        line.append(content[i].split(','))
    count_D1=0
    count_D2=0
    count_D3=0
    count_D4=0

    count_baap=0
    count_desirable=0

    for i in range(len(line)):
        count_D1=0
        count_D2=0
        count_D3=0
        count_D4=0
        count_total=0

        for n in range(len(line)):
            if line[n][-1]=='D1' and n!=i:
                count_D1=count_D1+1
            elif line[n][-1]=='D2' and n!=i: 
                count_D2=count_D2+1
            elif line[n][-1]=='D3' and n!=i: 
                count_D3=count_D3+1
            elif line[n][-1]=='D4' and n!=i: 
                count_D4=count_D4+1
            if n!=i:
                count_total=count_total+1
        P_D1=count_D1/count_total
        P_D2=count_D2/count_total
        P_D3=count_D3/count_total
        P_D4=count_D4/count_total
      
        count_baap=count_baap+1
        testing= line[i]
        training=line[:i]+line[i+1:]
        a=[0]
        list_each_D1=a*35
        list_each_D2=a*35
        list_each_D3=a*35
        list_each_D4=a*35
        
        for j in range(len(training)):
            for k in range(35):
                if training[j][-1]=="D1" and (testing[k]==training[j][k]):
                    list_each_D1[k]=list_each_D1[k]+1
                if training[j][-1]=="D2" and (testing[k]==training[j][k]):
                    list_each_D2[k]=list_each_D2[k]+1
                if training[j][-1]=="D3" and (testing[k]==training[j][k]):
                    list_each_D3[k]=list_each_D3[k]+1
                if training[j][-1]=="D4" and (testing[k]==training[j][k]):
                    list_each_D4[k]=list_each_D4[k]+1
        
        for q in range(len(list_each_D1)):
                list_each_D1[q]=(list_each_D1[q])/(count_D1)
                list_each_D2[q]=(list_each_D2[q])/(count_D2)
                list_each_D3[q]=(list_each_D3[q])/(count_D3)
                list_each_D4[q]=(list_each_D4[q])/(count_D4)
        P_Final_D1=P_D1
        P_Final_D2=P_D2
        P_Final_D3=P_D3
        P_Final_D4=P_D4

        for q in range(len(list_each_D1)):
                P_Final_D1=P_Final_D1*list_each_D1[q]
                P_Final_D2=P_Final_D2*list_each_D2[q]
                P_Final_D3=P_Final_D3*list_each_D3[q]
                P_Final_D4=P_Final_D4*list_each_D4[q]
    
        if testing[-1]=="D1" and P_Final_D1>P_Final_D2 and P_Final_D1>P_Final_D3 and P_Final_D1>P_Final_D4 :
            count_desirable=count_desirable+1
        elif testing[-1]=="D2" and P_Final_D2>P_Final_D1 and P_Final_D2>P_Final_D3 and P_Final_D2>P_Final_D4:
            count_desirable=count_desirable+1
        elif testing[-1]=="D3" and P_Final_D3>P_Final_D1 and P_Final_D3>P_Final_D2 and P_Final_D3>P_Final_D4:
            count_desirable=count_desirable+1
        elif testing[-1]=="D4" and P_Final_D4>P_Final_D1 and P_Final_D4>P_Final_D2 and P_Final_D4>P_Final_D3:
            count_desirable=count_desirable+1
OUTPUT3=(count_desirable/count_baap)
f.close()
# "___________________________________________________________________________________________________"


with open("shuttle-landing-control.data.txt") as f:
    content = f.read().splitlines()
    line=[]
    for i in range(len(content)):
        line.append(content[i].split(','))
    count_baap=0
    count_desirable=0
    for i in range(len(line)):
        count_1=0
        count_2=0
        count_total=0

        for n in range(len(line)):
            if line[n][0]=='1' and n!=i:
                count_1=count_1+1
            elif line[n][0]=='2' and n!=i: 
                count_2=count_2+1
            if n!=i:
                count_total=count_total+1

        P_1=count_1/count_total
        P_2=count_2/count_total
        count_baap=count_baap+1
        testing= line[i]
        training=line[:i]+line[i+1:]
        list_each_1=[]
        list_each_2=[]
        for m in range(len(testing)-1):
            if testing[m+1]!="*":
                list_each_1.append(0)
                list_each_2.append(0)
            else:
                list_each_1.append(-1)
                list_each_2.append(-1)
        for j in range(len(training)):
            for k in range(6):
                if training[j][0]=="1" and list_each_1[k]!=-1 and (testing[k+1]==training[j][k+1] or training[j][k+1]=="*"):
                    list_each_1[k]=list_each_1[k]+1
                
                if training[j][0]=="2" and list_each_2[k]!=-1 and (testing[k+1]==training[j][k+1] or training[j][k+1]=="*"):
                    list_each_2[k]=list_each_2[k]+1

        for q in range(len(list_each_1)):
            if list_each_1[q]!=-1:
                list_each_1[q]=(list_each_1[q])/(count_1)
                list_each_2[q]=(list_each_2[q])/(count_2)
        
        P_Final_1=P_1
        P_Final_2=P_2

        for q in range(len(list_each_1)):
            if list_each_1[q]!=-1:
                P_Final_1=P_Final_1*list_each_1[q]
                P_Final_2=P_Final_2*list_each_2[q]
        if testing[0]=="1" and P_Final_1>P_Final_2:
            count_desirable=count_desirable+1
        elif testing[0]=="2" and P_Final_2>P_Final_1:
            count_desirable=count_desirable+1
OUTPUT4=(count_desirable/count_baap)
f.close()
# "________________________________________________________________________________________"


with open("monks-1.train.txt") as f, open("monks-1.test.txt") as g:
    
    content1 = f.read().splitlines()
    training=[]
    testing=[]
    for i in range(len(content1)):
        training.append(content1[i].split(' '))
    content2 = g.read().splitlines()
    for i in range(len(content2)):
        testing.append(content2[i].split(' '))
    
    for i in range(len(training)):
        training[i]=training[i][1:-1]
    
    for i in range(len(testing)):
        testing[i]=testing[i][1:-1]

    count_1=0
    count_0=0
    count_total=0

    for i in range(len(training)):
        if training[i][0]=='1':
            count_1=count_1+1
        elif training[i][0]=='0': 
            count_0=count_0+1
        count_total=count_total+1
    P_1=count_1/count_total
    P_0=count_0/count_total
    count_desirable=0
   
    for i in range(len(testing)):
        a=[0]
        list_each_1=a*6
        list_each_0=a*6
           
        for j in range(len(training)):
            for k in range(6):
                if training[j][0]=="1" and testing[i][k+1]==training[j][k+1]:
                    list_each_1[k]=list_each_1[k]+1
                
                elif training[j][0]=="0" and testing[i][k+1]==training[j][k+1]:
                    list_each_0[k]=list_each_0[k]+1

        for q in range(len(list_each_1)):
            list_each_1[q]=(list_each_1[q])/count_1
            list_each_0[q]=(list_each_0[q])/count_0
        P_Final_1=P_1
        P_Final_0=P_0
        for z in range(len(list_each_1)):
            P_Final_1=P_Final_1*list_each_1[z]
            P_Final_0=P_Final_0*list_each_0[z]
        if testing[i][0]=="1" and P_Final_1>P_Final_0:
            count_desirable=count_desirable+1
        elif testing[i][0]=="0" and P_Final_0>P_Final_1:
            count_desirable=count_desirable+1

    OUTPUT5=(count_desirable/len(testing))
f.close()
g.close()
# "________________________________________________________________________________________"


with open("monks-2.train.txt") as f, open("monks-2.test.txt") as g:
    
    content1 = f.read().splitlines()
    training=[]
    testing=[]
    for i in range(len(content1)):
        training.append(content1[i].split(' '))

    content2 = g.read().splitlines()
    for i in range(len(content2)):
        testing.append(content2[i].split(' '))
    
    for i in range(len(training)):
        training[i]=training[i][1:-1]
    
    for i in range(len(testing)):
        testing[i]=testing[i][1:-1]

    count_1=0
    count_0=0
    count_total=0
    for i in range(len(training)):
        if training[i][0]=='1':
            count_1=count_1+1
        elif training[i][0]=='0': 
            count_0=count_0+1
        count_total=count_total+1
    
    P_1=count_1/count_total
    P_0=count_0/count_total
    count_desirable=0
   
    for i in range(len(testing)):
        a=[0]
        list_each_1=a*6
        list_each_0=a*6
           
        for j in range(len(training)):
            for k in range(6):
                if training[j][0]=="1" and testing[i][k+1]==training[j][k+1]:
                    list_each_1[k]=list_each_1[k]+1
                elif training[j][0]=="0" and testing[i][k+1]==training[j][k+1]:
                    list_each_0[k]=list_each_0[k]+1

        for q in range(len(list_each_1)):
            list_each_1[q]=(list_each_1[q])/count_1
            list_each_0[q]=(list_each_0[q])/count_0
        P_Final_1=P_1
        P_Final_0=P_0

        for z in range(len(list_each_1)):
            P_Final_1=P_Final_1*list_each_1[z]
            P_Final_0=P_Final_0*list_each_0[z]
        if testing[i][0]=="1" and P_Final_1>P_Final_0:
            count_desirable=count_desirable+1
        elif testing[i][0]=="0" and P_Final_0>P_Final_1:
            count_desirable=count_desirable+1
    OUTPUT6=(count_desirable/len(testing))
f.close()
g.close()
# "________________________________________________________________________________________"


with open("monks-3.train.txt") as f, open("monks-3.test.txt") as g:
    
    content1 = f.read().splitlines()
    training=[]
    testing=[]
    for i in range(len(content1)):
        training.append(content1[i].split(' '))

    content2 = g.read().splitlines()
    for i in range(len(content2)):
        testing.append(content2[i].split(' '))
    
    for i in range(len(training)):
        training[i]=training[i][1:-1]
    
    for i in range(len(testing)):
        testing[i]=testing[i][1:-1]

    count_1=0
    count_0=0
    count_total=0
    for i in range(len(training)):
        if training[i][0]=='1':
            count_1=count_1+1
        elif training[i][0]=='0': 
            count_0=count_0+1
        count_total=count_total+1
    P_1=count_1/count_total
    P_0=count_0/count_total
    count_desirable=0
   
    for i in range(len(testing)):
        a=[0]
        list_each_1=a*6
        list_each_0=a*6
                           
        for j in range(len(training)):
            for k in range(6):
                if training[j][0]=="1" and testing[i][k+1]==training[j][k+1]:
                    list_each_1[k]=list_each_1[k]+1
                elif training[j][0]=="0" and testing[i][k+1]==training[j][k+1]:
                    list_each_0[k]=list_each_0[k]+1
        for q in range(len(list_each_1)):
            list_each_1[q]=(list_each_1[q])/count_1
            list_each_0[q]=(list_each_0[q])/count_0
        P_Final_1=P_1
        P_Final_0=P_0

        for z in range(len(list_each_1)):
            P_Final_1=P_Final_1*list_each_1[z]
            P_Final_0=P_Final_0*list_each_0[z]
        if testing[i][0]=="1" and P_Final_1>P_Final_0:
            count_desirable=count_desirable+1
        elif testing[i][0]=="0" and P_Final_0>P_Final_1:
            count_desirable=count_desirable+1
    OUTPUT7=(count_desirable/len(testing))
f.close()
g.close()
# "________________________________________________________________________________________"

print("Tic Tac Toe- ",OUTPUT1)
print("SPECT- ",OUTPUT2)
print("Soybean- ",OUTPUT3)
print("Shuttle-landing- ",OUTPUT4)
print("Monks 1- ",OUTPUT5)
print("Monks 2- ",OUTPUT6)
print("Monks 3- ",OUTPUT7)