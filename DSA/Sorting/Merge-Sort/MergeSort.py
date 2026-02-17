def Divide(arr, l, r):
    if (l < r):
        m = (l + r) // 2
        Divide(arr, l, m)
        Divide(arr, m + 1, r)
        merge(arr, l, m, r)

def merge(arr, l, m, r):
    s1 = m - l + 1
    s2 = r - m

    L_list = [0] * s1
    R_list = [0] * s2

    for i in range(s1):
        L_list[i] = arr[l + i]
    
    for j in range(s2):
        R_list[j] = arr[m + 1 + j]

    i = j = 0
    k = l

    while (i < s1 and j < s2):
        if (L_list[i] < R_list[j]):
            arr[k] = L_list[i]
            i = i + 1
            k = k + 1
        else:
            arr[k] = R_list[j]
            j = j + 1
            k = k + 1

    while (i < s1):
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