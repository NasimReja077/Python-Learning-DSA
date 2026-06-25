def Divide(arr, l, r):
    if (l < r):
        m = (l + r) // 2
        Divide(arr, l, m)
        Divide(arr, m + 1, r)
        merge(arr, l, m, r)

def merge(arr, l, m, r):  # Merge two sorted parts.
    s1 = m - l + 1 # end - srart + 1 Find left array size. end - start + 1
    s2 = r - m # r-(m+1)+1

    # Create temporary arrays.
    L_list = [0] * s1
    R_list = [0] * s2

    for i in range(s1): #(L , m l start and m end) Copy left elements.
        L_list[i] = arr[l + i] # ue og array l is start from left and + 1 use for go to next eliment
    
    for j in range(s2):
        R_list[j] = arr[m + 1 + j] # m+1 is use for Sart in m+1 end j 

    i = j = 0
    k = l # original array position

    while (i < s1 and j < s2): # Loop until one array finishes.
        if (L_list[i] < R_list[j]): # 21 < 24
            arr[k] = L_list[i] # Put 21 into original array.
            i = i + 1 # Move pointers.
            k = k + 1
        else:
            arr[k] = R_list[j]
            j = j + 1
            k = k + 1

    while (i < s1): # If left array still has elements.
        arr[k] = L_list[i]
        i = i + 1
        k = k + 1

    while (j < s2):
        arr[k] = R_list[j]
        j = j + 1
        k = k + 1

# Driver code
arr = [21, 45, 24, 89, 7, 5, 10]
Divide(arr, 0, len(arr) - 1)
print(arr)