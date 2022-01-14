#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import sys

beta = int(sys.argv[1])

# ----- orbit simulation -----

# Relative orbital elements (equation 6)
s_0 = 39.9 # separation during observation
d_a = 0 # semimajor axis
d_l = s_0 * np.cos(np.deg2rad(beta)) # mean longitude ???
d_e = d_l # eccentricity
d_i = s_0 * np.sin(np.deg2rad(beta)) # inclination

# not sure what these are
ue = 0
ui = 0

# FIXME - randomization of ue, d_a, d_e, d_i here
# recompute beta, range

orbit_duration = 96 * 60 # (seconds)
ns = orbit_duration

time = np.arange(orbit_duration)
s = time
mean_anomaly = 2 * np.pi * time / orbit_duration
u = mean_anomaly

# RTN calculations (equation 5)
# FIXME - these don't match up with eq 5
r = d_a - d_e * np.cos(u - ue)
t = d_l - 1.5 * d_a * u + 2 * d_e * np.sin(u - ue)
n = d_i * np.sin(u - ui)

rng = np.sqrt(r**2 + t**2 + n**2) # separation over observation

# ----- observation window -----

duration_obs = 10 # (seconds)
t_0 = int(orbit_duration * 3 / 4)  # middle of observation window

beta = np.arctan(d_i / (2 * d_e - d_l))
nt = 5
idx = np.arange(2 * nt + 1) - nt
crot = np.cos(u[t_0 + idx] - u[t_0])
srot = np.sin(u[t_0 + idx] - u[t_0])

ti = crot * t[t_0 + idx] + srot * r[t_0 + idx]
ri = crot * r[t_0 + idx] - srot * t[t_0 + idx]

yum = (ti * np.sin(beta) - n[t_0 + idx] * np.cos(beta)) * 1e6
xum = ri * 1e6

y0 = yum[nt]
x0 = xum[nt]


# ----- plot -----

def plot(t, y, *, title, xlabel, ylabel):
    plt.plot(t, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True, 'major')
    plt.grid(True, 'minor')
    plt.minorticks_on()

plt.subplot(3, 2, 1)
plot(time / 60, r, title='R', xlabel='time (min)', ylabel='distance (m)')

plt.subplot(3, 2, 3)
plot(time / 60, t, title='T', xlabel='time (min)', ylabel='distance (m)')

plt.subplot(3, 2, 5)
plot(time / 60, n, title='N', xlabel='time (min)', ylabel='distance (m)')

plt.subplot(3, 2, 2)
plot(time / 60, s, title='Separation', xlabel='time (min)', ylabel='distance (m)')
print('t_0:', t_0)
print('r:', r[t_0])
print('t:', t[t_0])
print('n:', n[t_0])
print('separation:', s[t_0])


plt.subplot(3, 2, 4)
plot(idx, xum - x0, title='X', xlabel='time (sec)', ylabel='distance (μm)')

plt.subplot(3, 2, 6)
plot(idx, yum - y0, title='Y', xlabel='time (sec)', ylabel='distance (μm)')

plt.show()
plt.tight_layout()

