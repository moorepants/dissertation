function [A, B] = arms_state_space(eq, p)
% function [A, B] = arms_state_space(eq, p)
%
% Returns the state and input matrix for the model with respect to the
% supplied equilibrium point and parameters.
%
% Parameters
% ----------
% eq : double, size(19, 1)
%   The desired equilibrium point.
% p : structure
%   The model parameters.
%
% Returns
% -------
% A : double, size(19, 19)
%   The state matrix. The states are [q1, q2, q3, q4, q5, q6, q7, q8, q9,
%   q10, q11, q12, q13, q14, q15, q16, u4, u6, u7]'
% B : double, size(19, 4)
%   The input matrix. The inputs are [T4, T6, T7, Fcl]'
%
% Notes
% -----
% The system is fourth order but you can't just delete the rows and columns
% to reduce the system. Use the reduce_arms function to do this properly.

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
    % perturb the jth variable
    perturb1(j) = perturb1(j) + delta;
    perturb2(j) = perturb2(j) - delta;
    % solve differential equations for perturbed state, making sure the
    % constraints are satisfied
    prime1 = arms_ode(0.0, constraints(perturb1, p), p);
    prime2 = arms_ode(0.0, constraints(perturb2, p), p);
    % compute partial derivative
    A(:, j) = (prime1 - prime2) ./ 2 ./ delta;
end

inputEq = [0; 0; 0; 0];
B = zeros(length(eq), length(inputEq));
for j = 1:length(inputEq)
    % initialize function input
    perturb1 = inputEq;
    perturb2 = inputEq;
    % perturb the jth variable
    perturb1(j) = perturb1(j) + delta;
    perturb2(j) = perturb2(j) - delta;
    % solve differential equations for perturbed state, making sure the
    % constraints are satisfied
    prime1 = arms_ode(0.0, eq, p, perturb1);
    prime2 = arms_ode(0.0, eq, p, perturb2);
    % compute partial derivative
    B(:, j) = (prime1 - prime2) ./ 2 ./ delta;
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
