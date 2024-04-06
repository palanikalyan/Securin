def tot_comb():
    return 6 * 6

def dist():
    d = [[0]*6 for _ in range(6)]
    for i in range(1, 7):
        for j in range(1, 7):
            d[i-1][j-1] = i + j
    return d

def probs(d):
    t_comb = sum(1 for row in d for num in row)
    p = {}
    for i in range(2, 13):
        count = sum(1 for row in d for num in row if num == i)
        p[i] = count / t_comb
    return p

t_comb = tot_comb()
print("Total combinations:", t_comb)

d = dist()
print("Distribution of combinations:")
for row in d:
    print(row)

p = probs(d)
print("Probabilities of sums:")
for key, value in p.items():
    print(f"P(Sum = {key}) = {value:.2f}")
