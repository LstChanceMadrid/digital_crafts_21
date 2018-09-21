names = ["Alex", "John", "Mary", "Steve", "John", "Steve", "Steve"]
numbers = [5, 3, 6, 5, 7, 8, 5, 7]

def remove_duplicate(array):
    new_array = []
    for item in array:
        if item not in new_array:

            new_array.append(item)
    print(new_array)








remove_duplicate(names)
remove_duplicate(numbers)
