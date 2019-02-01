def nth_min(lst, n):
    new_lst = []
    if (n==1):
        return min(lst)
    else:
        ans = min(lst)
        for num in lst:
            if num!=ans:
                new_lst.append(num)
        return nth_min(new_lst, n - 1)

print(nth_min([5, 6, 2, 0], 1))
print(nth_min([1, 4, 3, 2], 3))
print(nth_min([3, 5, 1, 8], 4))
