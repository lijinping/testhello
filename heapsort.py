# -*- coding: cp936 -*-
#单独针对i进行处理，在一个已经是堆的结构上
def HeapAdjust(listx,i,length): 
    while True:
        if 2*i+1<length:
            bigchild = i*2+1
        else:
            break

        
        if bigchild+1 < length and listx[bigchild+1] > listx[bigchild]:
            bigchild=bigchild+1  #right child is biger

        if listx[i] < listx[bigchild]:
            tmp=listx[i]
            listx[i]=listx[bigchild]
            listx[bigchild]=tmp
            i=bigchild
        else:
            break

    print '**',listx

def createheap(listx,length):
    i=length/2
    while(i>=0):
        HeapAdjust(listx,i,length)
        i=i-1
    print listx
    
def heapsort():
    a=[0,16,20,3,11,17,8,99,188,275]
    size=10
    createheap(a,10)

    i=size-1
    while(i>=0):
        xx=a[i]
        a[i]=a[0]
        a[0]=xx
        HeapAdjust(a,0,i)
        i-=1

    print a


heapsort()        
