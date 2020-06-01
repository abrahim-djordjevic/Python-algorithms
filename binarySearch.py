def binarySearch(array, desired, low, high):
    mid = (low + high)//2
    while(low < high):
        if(desired > array[mid]):
            low = mid+1
            mid = (low + high)//2
        elif(desired < array[mid]):
            high = mid-1
            mid = (low + high)//2
        else:
            return array[mid]

if(__name__) == ("__main__"):
    array = [1,2,3,4,5,6,7,8,9,10]
    print(binarySearch(array,10, 0, len(array)))
