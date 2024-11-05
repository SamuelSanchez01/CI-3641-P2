def sortIterator(array):
    """
    Iterator that sorts an array
    """
    if len(array) < 2:
        yield array[0]
    else:
        #Lets fin the index of the minimun element on the array
        index = min(range(len(array)), key=array.__getitem__)
        yield array[index]
        #now iters without the element
        array.pop(index)
        yield from sortIterator(array)


array = [10,45,12,1,354,23]

for x in sortIterator(array):
    print(x)

