function [A, B] = arms_reduce_system(A, B)
% function [A, B] = arms_reduce_system(A, B)
%
% Returns the reduced state and input matrix for the arm model by correctly
% accounting for the dependent coordinates.
%
% Parameters
% ----------
% A : double, size(19, 19)
%   The state matrix. The states are [q1, q2, q3, q4, q5, q6, q7, q8, q9,
%   q10, q11, q12, q13, q14, q15, q16, u4, u6, u7]'
% B : double, size(19, 4)
%   The input matrix. The inputs are [T4, T6, T7, Fcl]'
%
% Returns
% -------
% A : double, size(4, 4)
%   The state matrix. The states are [q4, q7, u4, u7]'
% B : double, size(4, 3)
%   The input matrix. The inputs are [T4, T7, Fcl]'

% remove the rows and columns that can be removed
A([1:3, 5:6, 8, 18], :) = [];
A(:, [1:3, 5:6, 8, 18]) = [];
% this is a 12 x 12
Ar = A([1:2, 11:12], [1:2, 11:12]);
Ar(3, 2) = Ar(3, 2) + dot(A(11, 3:10)', A(3:10, 12));
Ar(4, 2) = Ar(4, 2) + dot(A(12, 3:10)', A(3:10, 12));
A = Ar;

B([1:3, 5:6, 8:16, 18], :) = [];
B(:, 2) = [];
