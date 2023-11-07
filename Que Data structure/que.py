num=[]
tail=0
head=0
num_size=5
def enque(num,tail,head,value):
    if (tail+1)%(num_size+1) != head:
        num.insert(tail,value)
        tail=(tail+1)%(num_size+1)
        return num,tail

for i in range(5):
    print(enque(num,len(num),head,i))