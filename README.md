# Newton-Raphson Method Calculator

## What it is
I made a calculator to numerically solve nonlinear systems of algebraic equations using the Newton-Raphson method. The gist is that it generalizes the single variable formulation by using vectors and the Jacobian matrix, solving for the step size, and then adding the step value to the input, then iterating the crap out of it.

The calculator only works with systems of 2, 3, and 4 variables. This includes $\lambda$ if you are using Lagrange multipliers (what I designed this calculator for).

## How it works
Included below is the formula: $$J(\mathbf{x}_k)\delta\mathbf{x}=-\mathbf{F}(\mathbf{x}_k)$$

Each iteration's process finds the following
$$
\mathrm{rref}\begin{bmatrix}
    \frac{\partial f_1}{\partial x_1} & \dots & \frac{\partial f_1}{\partial x_n} & f_1(\mathbf{x})\\
    \vdots & \ddots & \vdots & \vdots\\
    \frac{\partial f_n}{\partial x_1} & \dots & \frac{\partial f_n}{\partial x_n} & f_n(\mathbf{x})\\
\end{bmatrix}
$$

Then defines $\delta\mathbf{x}$ as the right-most column of the new matrix, and calculates $\mathbf{x}_{k+1}$ as 
$$
\mathbf{x}_{k+1}=\delta\mathbf{x}+\mathbf{x}_k
$$
and re-iterates until the desired accuracy is reached (reccomended: 0.000001)

## How to use it
First, input the number of variables. Any input other than 2, 3, or 4 will yield an error message. Then, input your equations; note that they must take the form
$$
f_n(\mathbf{x})=0
$$
and that you should only input the LHS. Call your variables x1, x2, etc. or the calculator will not work. Then, input your starting guess for each component of $\mathbf{x}$ (i.e. for each variable). Then, input the stop condition (i.e. the calculator will stop iterating and will output the answer when each component of $\delta\mathbf{x}$ is less than your stop condition). Just type in a number, or the calculator will not work. If you have followed these instructions, the calculator should work. If it doesn't, go use Wolfram Alpha (I don't know why you were using this over WA in the first place). If you didn't follow my instructions, follow them and try again.

3var.py is also the last stable version of the calculator before I screwed with it to add functionality for 2 and 4 variables. If main.py fucks up and you don't want to go use WA instead, try running it on 3var.py (if you have a system of 3 variables). Also, note that the calculator can only handle a system with the same number of variables as equations.