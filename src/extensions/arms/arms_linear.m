p = load('armspar.mat');
q = load('armsinit.mat');

% we are looking at the nominal configuration
q4 = 0;
q7 = 0;

% solve for the pitch angle
qi = [q4, q7];
pitch = @(qd)pitch_constraint(qd, qi, p);
q5 = fsolve(pitch, q.q5, optimset('Display', 'Off'));

% initial guesses for the arm angles
q9g = -0.0257;
q10g = -0.2245;
q11g = 0.2572;
q12g = 1.288;

% solve the arm constraints
qi = [q5, q7];
right = @(qd)right_arm_constraint(qd, qi, p);
qRight = fsolve(right, [q9g, q10g, q11g, q12g], optimset('Display', 'Off'));

left = @(qd)left_arm_constraint(qd, qi, p);
qLeft = fsolve(left, [-q9g, q10g, -q11g, q12g], optimset('Display', 'Off'));

% caluculate eigenvalues for a range of speeds
speed = 0:0.1:10;
w = zeros(19, length(speed));
for k = 1:length(speed)
    eq = [0, 0, 0, q4, q5, 0, q7, 0, qRight, qLeft, 0, -speed(k) / p.rr, 0];
    A = arms_state_space(eq, p);
    w(:, k) = eig(A);
end

plot(speed, w, '.')
