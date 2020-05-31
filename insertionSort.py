from numpy import ndarray

def main():
    print("How many elements do you want in the array?")
    numElement = int(input())
    a = ndarray((numElement),int)
    for i in range(0, numElement):
        print("what integer do you want at position " + str(i))
        a[i] = int(input())
    insertionSort(a)

def insertionSort(array):
    n = len(array)
    #first loop goes over the n-1 items to be sorted
    for i in range(1,n):
        key = array[i]
        j = i
        #second loop is for inserting array[i] into the correct position
        while(j>0 and key < array[j-1]):
            array[j] = array[j-1]
            j=j-1
        array[j] = key
    print(array)

if __name__ == "__main__":
    main()
