from math import exp

t = [[5, exp(-3)], [15, exp(-3) * ((3)**1)], [21, exp(-3)*((3)**2) / 2], [25, exp(-3)*((3)**3) / 6], [19,exp(-3)*((3)**4) / 24], [9,exp(-3)*((3)**5) / 120], [5,exp(-3)*((3)**6) / 720], [1,exp(-3)*((3)**7) / 5040]]
print(t)
sm = 0
for (i, j) in t:
    sm += (i - 100 * j)**2 / (100*j)
print(sm)