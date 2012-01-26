function [A, B, C, D, K, X0] = spring_ode(parameters, sampleTime, arg)
% function [A, B, C, D, K, X0] = spring_ode(parameters, sampleTime, arg)
%
% Returns the innovations form of a simple undamped harmonic oscillator.
%
% Parameters
% ----------
% parameters : double
%   The single parameter, spring stiffness, in N/m.
% sampleTime : double
%   Unused for this continous model.
% arg : double
%   The fixed parameters, mass, in kg.
%
% Returns
% -------
% A : double, 2 x 2
%   The state matrix. The states are [distance, velocity].
% B : double, 2 x 0
%   The input matrix. There are no inputs.
% C : double, 1 x 2
%   The output matrix. The output is acceleration.
% D : double, 1 x 0
%   The feedforward matrix. There are no inputs.
% K : double, 2 x 1
%   The Kalman gain matrix.
% X0 : double, 2 x 1
%   The initial states.

k = parameters(1);
m = arg;

A = [0, 1; -k / m, 0];
B = zeros(2, 0);
C = [-k / m, 0];
D = zeros(1, 0);
K = zeros(2, 1);
X0 = zeros(2, 1);
