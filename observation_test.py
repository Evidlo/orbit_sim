#!/usr/bin/env python
# Evaluate spacecraft relative position and velocity
# at instant of observation

from math import cos, sin, atan, pi, sqrt
from math import degrees as deg
from math import radians as rad

beta = rad(37) # target beta (rad)
s = 39.9 # target separation (m)
u = 2 * pi * 2 / 4 # arg of latitude of observation point (rad)
orbit_duration = 96 * 60 # (s)

# relative orbital elements (equation 6)
d_a =   0
d_l =  -s * cos(beta)
d_ex =  s * cos(beta) * sin(u)
d_ey = -s * cos(beta) * cos(u)
d_ix =  s * sin(beta) * sin(u)
d_iy = -s * sin(beta) * cos(u)

# relative RTN frame (equation 5)
r_r = d_a - cos(u) * d_ex - sin(u) * d_ey
r_t = d_l + 2 * sin(u) * d_ex - 2 * cos(u) * d_ey
r_n = sin(u) * d_ix - cos(u) * d_iy

n = 2 * pi / orbit_duration # mean motion (rad/s)
v_r = n * sin(u) * d_ex - n * cos(u) * d_ey
v_t = -1.5 * n * d_a + 2 * n * cos(u) * d_ex + 2 * n * sin(u) * d_ey
v_n = cos(u) * d_ix + sin(u) * d_iy

# sanity check - compute beta/separation from RTN coordinates
# at observation position
actual_separation = sqrt(r_r**2 + r_t**2 + r_n**2)
actual_beta = deg(atan(r_n / r_t))

print('design separation:', s)
print('design beta:', deg(beta))
print()
print('actual separation:', actual_separation)
print('actual beta:', actual_beta)
print()
print("RTN offset:")
print('r_r:', r_r)
print('r_t:', r_t)
print('r_n:', r_n)
print()
print("RTN velocity:")
print('v_r:', v_r)
print('v_t:', v_t)
print('v_n:', v_n)

# design separation: 39.9
# design beta: 37.0

# actual separation: 39.9
# actual beta: 37.0

# RTN offset:
# r_r: 0.0
# r_t: 31.865556850886982
# r_n: 24.012419423766726

# RTN velocity:
# v_r: 0.03475993031433835
# v_t: 0.0
# v_n: 0.0
