x = load("RTN_relative_state.mat").RTN_relative_state
r = x(1, :, :)
t = x(2, :, :)
n = x(3, :, :)
beta = rad2deg(atan(n ./ t))
separation = sqrt(r.^2 + t.^2 + n.^2)
design_beta = -28
y = r
x = (t - n .* tan(deg2rad(beta))) .* sin(deg2rad(beta))

subplot(3, 3, 1)
hold on
plot(r)
title('R')
xlabel('time (s)')
ylabel('offset (m)')

subplot(3, 3, 4)
hold on
plot(t)
title('T')
xlabel('time (s)')
ylabel('offset (m)')

subplot(3, 3, 7)
hold on
plot(n)
title('N')
xlabel('time (s)')
ylabel('offset (m)')

subplot(3, 3, 2)
hold on
plot(beta)
title('Beta')
xlabel('time (s)')
ylabel('angle (deg)')

subplot(3, 3, 5)
hold on
plot(separation)
title('Separation')
xlabel('time (s)')
ylabel('offset (m)')

subplot(3, 3, 3)
hold on
plot(x)
title('X')
xlabel('time (s)')
ylabel('offset (m)')

subplot(3, 3, 6)
hold on
plot(y)
title('Y')
xlabel('time (s)')
ylabel('offset (m)')
