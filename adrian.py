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

time = np.arange(orbit_duration)
mean_anomaly = 2 * np.pi * time / orbit_duration

# RTN calculations (equation 5)
# FIXME - these don't match up with eq 5
r = d_a - d_e * np.cos(mean_anomaly - ue)
t = d_l - 1.5 * d_a * mean_anomaly + 2 * d_e * np.sin(mean_anomaly - ue)
n = d_i * np.sin(mean_anomaly - ui)

s = np.sqrt(r**2 + t**2 + n**2) # separation over observation

# ----- observation window -----

duration_obs = 10 # (seconds)
t_0 = int(orbit_duration * 3 / 4)  # middle of observation window
t_obs = t_0 + np.arange(-duration_obs // 2, duration_obs // 2)
# rotation matrix during observation
c_rot = np.cos(mean_anomaly[t_obs])
s_rot = np.cos(mean_anomaly[t_obs])

x_obs = r[t_obs] * c_rot - t[t_obs] * s_rot
y_obs = r[t_obs] * s_rot + t[t_obs] * c_rot
# FIXME - what is this?  expected y += n[t_obs] / tan(beta)
y_obs = y_obs * np.sin(beta) - n[t_obs] * np.cos(beta)

# FIXME - is this cheating?  shouldnt we compute this from beta and s?
x_0 = x_obs[duration_obs // 2]
y_0 = y_obs[duration_obs // 2]

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
plot(t_obs, (x_obs - x_0) * 1e6, title='X', xlabel='time (sec)', ylabel='distance (μm)')

plt.subplot(3, 2, 6)
plot(t_obs, (y_obs - y_0) * 1e6, title='Y', xlabel='time (sec)', ylabel='distance (μm)')

plt.show()
plt.tight_layout()

