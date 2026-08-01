from random import *
def task2_1(filename,quantity,maximum):
    with open(filename,'w') as file :#file closes automatically
        for i in range(quantity):
            randnum=randint(0,maximum)
            file.write("{}\n".format(randnum))


def task2_2(list_of_integers):
    return mergesort(0,len(list_of_integers)-1,list_of_integers)

def mergesort(low,high,ar):
    if low==high:
        return [ar[low]]
    mid=low+(high-low)//2
    left=mergesort(low,mid,ar)
    right=mergesort(mid+1,high,ar)
    return merge(left,right)

def merge(left,right):
    i,j,k=0,0,0
    result=[None]*(len(left)+len(right))
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result[k]=left[i]
            i+=1
        else:
            result[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        result[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        result[k]=right[j]
        j+=1
        k+=1

    return result


def task2_3(filename_in,filename_out):
    with open(filename_in,'r') as file:#file closes automatically 
        data=[]
        for line in file:
            line=line.strip()
            data.append(int(line))

    data=task2_2(data)
    with open(filename_out,'w') as file:#file closes automatically 
        for line in data:
            file.write('{}\n'.format(data))


    

            
        
            






task2_1("randomnumbers_jimson.txt",1000,5000)
task2_2([56,25,4,98,0,18,4,5,7,0])==[0,0,4,4,5,7,18,25,56,98]
task2_3("randomnumbers_jimson.txt",'sortednumbers_jimson.txt')




