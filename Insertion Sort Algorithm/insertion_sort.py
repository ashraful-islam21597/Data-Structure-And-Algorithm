num=[5,4,2,3,1]
def InsertionSort(num):
    i=1
    while i<len(num):
        j=i-1
        while j>=0 and num[j]>num[j+1]:
            num[j+1],num[j]=num[j],num[j+1]
            j=j-1
        i+=1
    return num
print(InsertionSort(num))