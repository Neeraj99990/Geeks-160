##  create a  new python program for  reverce an array in java .

def reverse_array(arr):
    return arr[::-1]


array = list(map(int, input("Enter the elements of the array separated by space: ").split()))

print("Reversed array ", array)