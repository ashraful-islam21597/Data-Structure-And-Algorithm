q=[]
head=0
tail=0
q_size=5
# implementaion of enque and deque for circular que
# to enque operation
def enque(q,tail,item):
    if (tail+1)%(q_size+1) == head:
        print("que is full")
        return
    return (tail+1)%(q_size+1)

#to deque operation
def deque(q,head,item):
    if tail==head:
        print("que is empty")
        return -1
    return (head+1)%(q_size+1)



# applications of enque and deque
for i in range(1,50,3):

    tail = enque(q, tail, i)
    print(tail)
    # enque element untill que get full
    if tail != None:
        q.insert(tail,i)
        print(q)
    else:
        # deque an element whwn from que when the que que get full
        tail=len(q)
        q.pop(head)
        head = deque(q, head, 101)

        print(head,q)

