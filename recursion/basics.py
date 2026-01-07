#  print given input N number of times using recursion

def print_number_n_times(num, n, count=0):
    if (count == n):
        return
    # count += 1
    print_number_n_times(num, n, count)
    print(num, end=" ")
    

# print_number_n_times(2, 10)

def print_one_to_n(num):
    if (num == 0):
        return
    print_one_to_n(num-1)
    print(num, end=" ")

# print_one_to_n(10)

def print_n_to_one(num):
    if (num == 0):
        return
    print(num, end=" ")
    print_n_to_one(num-1)

# print_n_to_one(10)

def sum_of_first_n_numbers(num, sum=0):
    if (num < 1):
        return sum
    sum += num
    return sum_of_first_n_numbers(num-1, sum)

# print(sum_of_first_n_numbers(2000))

# def factorial_of_n(n):

def factorial_of_n(num):
    if (num <= 1):
        return num 
    return (num * factorial_of_n(num-1))

# print(factorial_of_n(10)) 

def revese_an_array(arr, reversed_arr=[]):
    if (len(arr) == 0):
        return reversed_arr
    reversed_arr.append(arr.pop())
    return revese_an_array(arr, reversed_arr)

print(revese_an_array([3,4,5,6,7,8]))

# Optimized approch for reversing an array

def reverse_array_using_recursion(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left >= right:
        return arr
    arr[left], arr[right] = arr[right], arr[left]
    return reverse_array_using_recursion(arr, left+1, right-1)

# print(reverse_array_using_recursion([3,4,5,6,7,8]))

def check_polindrome(str, left=0, right=None):
    if right is None:
        right = len(str) - 1
    if left >= right:
        return True
    if str[left] != str[right]:
        return False
    return check_polindrome(str, left+1, right-1)

print(check_polindrome("noona"))
    
