from numpy import ndarray

def main():
    print("How many elements do you want in the array?")
    numElement = int(input())
    a = ndarray((numElement),int)
    for i in range(0, numElement):
        print("what integer do you want at position " + str(i))
        a[i] = int(input())
    quickSort(a, 0, len(a)-1)

def quickSort(array, low, high):
    if(low < high):
        p = partition(array, low, high)
        quickSort(array, low, p-1)
        quickSort(array, p+1, high)
    print(array)

def partition(array, low, high):
    pivot = array[high]
    i = low
    for j in range(low, high):
        if(array[j] < pivot):
            array[i], array[j] = array[j], array[i]
            i = i + 1
    array[i], array[high] = array[high], array[i]
    return i

if __name__ == "__main__":
    main()
