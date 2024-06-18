#Searching a element
def search(array,n,x):
    for i in range (0 , n):
        if (array[i]==x):
            return -1
array = [2,4,0,1,9]
x = 1
n = len (array)
result = search(array,n,x)
if (result == 1):
    print("elemnet not found ")
else:
    print("element found at index:",result)


