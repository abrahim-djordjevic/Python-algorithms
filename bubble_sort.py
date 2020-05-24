from numpy import ndarray

def main():
    print("How many elements do you want in the array?")
    numElement = int(input())
    a = ndarray((numElement),int)
    for i in range(0, numElement):
        print("what integer do you want at position " + str(i))
        a[i] = int(input())
    bubbleSort(a)
    

def bubbleSort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    print(array)


if __name__ == "__main__":
    main()
