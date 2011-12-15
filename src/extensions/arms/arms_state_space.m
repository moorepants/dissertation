function A = arms_state_space(eq, p)

delta = 1e-11; % perturbance value

% make sure the constraint equations are properly solved

eq = constraints(eq, p);

% build the stability matrix by numerically calculating the partial
% derivatives of each differential equation with respect to each state
% variable
A = zeros(length(eq));
for j = 1:length(eq);
    perturb1 = eq; %initialize function input
    perturb2 = eq; %initialize function input
    perturb1(j) = perturb1(j) + delta; %perturb the jth variable
    perturb2(j) = perturb2(j) - delta;
    % solve differential equations for perturbed state, making sure the
    % constraints are satisfied
    prime1 = arms_ode(0.0, constraints(perturb1, p), p);
    prime2 = arms_ode(0.0, constraints(perturb2, p), p);
    % compute partial derivative
    A(:, j) = (prime1 - prime2) ./ 2 ./ delta;
end

function eq = constraints(eq, p)

% solve for the pitch angle
qi = [eq(4), eq(7)];
pitch = @(qd)pitch_constraint(qd, qi, p);
eq(5) = fsolve(pitch, eq(5), optimset('Display', 'Off'));

% solve the arm constraints
qi = [eq(5), eq(7)];

right = @(qd)right_arm_constraint(qd, qi, p);
eq(9:12) = fsolve(right, eq(9:12), optimset('Display', 'Off'));

left = @(qd)left_arm_constraint(qd, qi, p);
eq(13:16) = fsolve(left, eq(13:16), optimset('Display', 'Off'));
