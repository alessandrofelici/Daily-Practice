import numpy as np

k = (8.99 * 10**9)
q1 = 16.7 * 10**-9
q2 = (2 * 10**-3) / 4
L = 2.75 * 10**-2

r_sep1 = np.array([0.5 * L, L, 0])
r_sep2 = np.array([-0.5 * L, L, 0])
r_sep3 = np.array([-1.5 * L, L, 0])
r_sep4 = np.array([-2.5 * L, L, 0])
r_seps = [r_sep1, r_sep2, r_sep3, r_sep4]

F = np.array([0,0,0])
for r in r_seps:
    F = F + np.array(((k * q1 * q2) / np.linalg.norm(r)**3) * r)

print(F)