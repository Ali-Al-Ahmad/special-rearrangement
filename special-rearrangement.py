"this function rearrange a list of numbers, even number to left side/odd number to right side"

numbers_array = [1, 2, 5, 8, 3, 6, 9, 4, 7, 10]
#               [2, 8, 6, 4, 10, 1, 5, 3, 9, 7]

def _special_rearrangement(numbers):
    length_of_array = len(numbers)

    for i in range(length_of_array):
        for j in range(length_of_array-1):

            # check if number is odd move it to the right (index + 1)
            if numbers[j] % 2 == 1:
                temp = numbers[j+1]
                numbers[j+1] = numbers[j]
                numbers[j] = temp
    return numbers

new_array = _special_rearrangement(numbers_array)
print(new_array)
