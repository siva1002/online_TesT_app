amount=int(input('enter the numbers'))
notes=[500,200,100]
count=[0,0,0]
notes_in_hand=0
exists=0
minamount=0
for item in notes:
    minamount+=item
if minamount < amount:
    for c in range(len(count)):
        count[c]+=1
    for i in count:
        notes_in_hand+=1
    balance=amount-minamount
    for k  in count:
        notes_in_hand+=k

    for j in range(len(count)):
        if balance !=0 and balance>=notes[j]:
            exist=balance//notes[j]
            balance=balance%notes[j]
            count[j]=exist+1
else:
    n=0
    temp=amount
    for i in range(len(notes)):
        if temp != 0 and temp >= notes[i]:
            count[i]=temp//notes[i]
            temp=temp-(count[i]*notes[i])
    for k in count:
            notes_in_hand+=1
for i in range(3):
     amount=notes[i]
     n=count[i]
     print('{}*{}={}'.format(amount,n,amount*n))
totalnotes=count[0]+count[1]+count[2]
print('total notes:',totalnotes)
