def main():
    array = [3,2,1,5,4]
    mergeSort(array, 0, len(array)-1)
    print(array)

def mergeSort(array, left, right):
    if left >= right:
        return
    #split the array
    middle = (left + right)//2
    mergeSort(array, left, middle)
    mergeSort(array, middle + 1, right)
    #merge the array
    merge(array, left, right, middle)

def merge(array, left, right, middle):
    leftCopy = array[left:middle+1]
    rightCopy = array[middle+1:right+1]
    #variables used to keep track of our position in the arrays
    i = 0
    j = 0
    k = left
    #find smallest value in left or right array and place in sorted array
    while(i < len(leftCopy) and j < len(rightCopy)):
        if(leftCopy[i] <= rightCopy[j]):
            array[k] = leftCopy[i]
            i = i + 1
        else:
            array[k] = rightCopy[j]
            j = j + 1
        k = k + 1
    #go through remaining elements after left or right is empty
    while(i < len(leftCopy)):
        array[k] = leftCopy[i]
        i = i + 1
        k = k + 1
        
    while(j < len(rightCopy)):
        array[k] = rightCopy[j]
        j = j + 1
        k = k + 1

if __name__ == "__main__":
    main()
        
    

