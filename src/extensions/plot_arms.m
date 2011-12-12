function plot_arms(points)
figure()
lines = plot3(points(1, :), points(2, :), -points(3, :));
set(lines, 'Marker', 'o', ...
    'MarkerSize', 4, ...
    'Linewidth', 2)
hold on
circle_xz(points(:, 3), norm(points(:, 3) - points(:, 1)))
circle_xz(points(:, 6), norm(points(:, 6) - points(:, 8)))
axis equal

function circle_xz(loc, r)
% function circle_xz(loc, r)

theta = [0 : 0.2 : 2 * pi, 0];
xp = r * cos(theta);
yp = zeros(length(xp));
zp = r * sin(theta);

plot3(loc(1) + xp , loc(2) + yp, -(loc(3) + zp));
