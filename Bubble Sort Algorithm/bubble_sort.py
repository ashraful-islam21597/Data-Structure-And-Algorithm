num=[7,4,3,6,5]
def bubbleSortAlgorithm(num):
    i=0
    while i<len(num):
        j=0
        while j<len(num)-i-1:
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]
            j+=1
        i+=1
    return num
print(bubbleSortAlgorithm(num))