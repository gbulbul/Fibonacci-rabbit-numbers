def fib_num(n, m):
    num_of_rab=[1,1]
    for i in range(n):
        if i < 2:
            initial = 1
            num_of_rab.append(initial)
        elif (i < m) or (m == 0):
            total = num_of_rab[i - 1] + num_of_rab[i - 2]
            num_of_rab.append(total)
        elif i == m:
            total = num_of_rab[i - 1] + num_of_rab[i - 2] - 1
            num_of_rab.append(total)
        else:
            total = num_of_rab[i - 1] + num_of_rab[i - 2]+ num_of_rab[i-(m+1)]
    return total
print(fib_num(6,3))