def linearSearch(array, desired):
    for i in range(0, len(array)):
        if(array[i] == desired):
            return array[i]
    return -1
			
if(__name__) == "__main__":
    array = [1,2,3,4,5]
    print(linearSearch(array, 5))
    
