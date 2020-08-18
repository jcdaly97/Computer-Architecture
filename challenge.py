def reverse(arr):
    for i in range(len(arr) -1, -1,  -1):
        print(arr[i])
    


test = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
reverse(test)
print(test[::-1])