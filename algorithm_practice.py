array = ["we", "all", "float", "Hello Georgy", 5]

#Largest Element

def largest_element(array):
    print("-Largest Element")
    largest = array[0]
    for element in array:
        element = str(element)
        if (len(element) > len(largest)):
            largest = element
    
    print(largest)

largest_element(array)

#Smallest Element

def smallest_element(array):
    print("-Smallest Element")
    smallest = array[0]
    for element in array:
        element = str(element)
        if (len(element) < len(smallest)):
            smallest = element

    print(smallest)

smallest_element(array)

#Display Pyramid


def display_pyramid(symbol, rows):
    print("-Display Pyramid")
    distance = " "
    rows = int(rows)
    i = 1
    while rows > 0:
        print(distance * rows + symbol * i)
        rows -= 1
        i += 2
    

display_pyramid("k", 9)

