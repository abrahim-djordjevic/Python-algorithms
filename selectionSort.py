from numpy import ndarray

def main():
    print("How many elements do you want in the array?")
    numElement = int(input())
    a = ndarray((numElement),int)
    for i in range(0, numElement):
        print("what integer do you want at position " + str(i))
        a[i] = int(input())
    selectionSort(a)

def selectionSort(array):
    n = len(array)
    #first loop goes over n-1 items to be sorted
    for i in range(n):
        k = i;
        #second loop is for finding the smallest item
        #in the rest of the array
        for j in range(i+1,n):
            if(array[j] < array[k]):
                k = j
        array[i], array[k] = array[k], array[i]
    print(array)

if __name__ == "__main__":
    main()
