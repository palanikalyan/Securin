def init_p(d):
    t_comb = sum(1 for row in d for num in row)
    p = {}
    for i in range(2, 13):
        count = sum(1 for row in d for num in row if num == i)
        p[i] = count / t_comb
    return p

def adjust_A(Die_A, Die_B):
    d = [[i + j for j in Die_B] for i in Die_A]
    init_p = init_p(d)
    min_s = [max(2 - max(Die_B), 2 - max(Die_A)) for _ in range(6)]
    new_A = [min(max(num, min_s[i]), 4) for i, num in enumerate(Die_A)]
    return new_A, Die_B

Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]
New_Die_A, New_Die_B = adjust_A(Die_A, Die_B)
print("New Die A:", New_Die_A)
print("New Die B:", New_Die_B)
