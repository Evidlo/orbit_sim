#!/usr/bin/env python

from math import cos, sin, atan, degrees, pi, sqrt

beta = 37 # target beta (degrees)
s = 39.9 # target separation (m)
u = 2 * pi * 3 / 4 # mean anomaly at observation point

# relative orbital elements (equation 6)
d_a = 0
d_l = s * cos(beta)
d_ex = -s * cos(beta) * sin(u)
d_ey = s * cos(beta) * cos(u)
d_ix = s * sin(beta) * sin(u)
d_iy = -s * sin(beta) * cos(u)

# RTN frame (equation 5)
r = d_a - cos(u) * d_ex - sin(u) * d_ey
t = d_l + 2 * sin(u) * d_ex - 2 * cos(u) * d_ey
n = sin(u) * d_ix - cos(u) * d_iy

# sanity check - compute beta/separation from RTN coordinates
# at observation position
actual_separation = sqrt(r**2 + t**2 + n**2)
actual_beta = degrees(atan(n / t))

print('r:', r)
print('t:', t)
print('n:', n)
print('actual separation:', actual_separation)
print('actual beta:', actual_beta)

# r: 0.0
# t: -30.5400206726192
# n: -25.677171520944277
# actual separation: 39.9
# actual beta: 40.056158015954125
