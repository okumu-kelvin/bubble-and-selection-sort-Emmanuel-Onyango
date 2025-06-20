myarray=[13,34,66,33,12,9]
def bubble_sort(myarray):
    a=len(myarray)
    for i in range(a-1):
        for j in range(a-i-1):
            if myarray[j]>myarray[j+1]:
                temp=myarray[j]
                myarray[j]=myarray[j+1]
                myarray[j+1]=temp
    # TODO: Implement bubble sort
    return myarray
print("Sorted array is: ",bubble_sort(myarray))
