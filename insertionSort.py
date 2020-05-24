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
    for i in range(1,n):
        key = array[i]
        j = i-1
        while(j>=0 and key < array[j]):
            array[j+1] = array[j]
            j= j-1
        array[j+1] = key
    print(array)

if __name__ == "__main__":
    main()
