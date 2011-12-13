p = load('armspar.mat');
q = load('armsinit.mat');

% we are looking at the nominal configuration
q4 = 0;
q7 = 0;

% solve for the pitch angle
qi = [q4, q7];
pitch = @(qd)pitch_constraint(qd, qi, p);
q5 = fsolve(pitch, q.q5)

q9g = -0.0257;
q10g = -0.2245;
q11g = 0.2572;
q12g = 1.288;
holoGuess = [q9g, q10g, q11g, q12g, -q9g, q10g, -q11g, q12g];
% plot the initial guess
points = arms_points([0, 0, 0, q4, q5, 0, q7, 0, holoGuess], p);
plot_arms(points)

% solve for the exact solution
qi = [q4, q5, q7];
constraint = @(qd)arms_holonomic(qd, qi, p);
holoInit = fsolve(constraint, holoGuess);
% plot the solution
points = arms_points([0, 0, 0, q4, q5, 0, q7, 0, holoInit], p);
plot_arms(points)

qi = [q5, q7];
right = @(qd)right_arm_constraint(qd, qi, p);
[qRight, rightVal] = fsolve(right, [q9g, q10g, q11g, q12g]);

left = @(qd)left_arm_constraint(qd, qi, p);
[qLeft, leftVal] = fsolve(left, [-q9g, q10g, -q11g, q12g]);

points = arms_points([0, 0, 0, q4, q5, 0, q7, 0, qRight, qLeft], p);
plot_arms(points)

x0 = [0, 0, 0, q4, q5, q7, 0, 0, qRight, qLeft, 0.5, -7.0 / p.rr, 0];

odefunc = @(t, x)arms_ode(t, x, p);

[time, states] = ode45(odefunc, [0 2], x0);
