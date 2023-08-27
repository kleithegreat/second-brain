# Lecture 3
---
## Position, Velocity, and Acceleration
- ### In one dimension:
    - position is a function of t
    - velocity is the derivative of the position function with respect to time
        - position is the integral of velocity with respect to time
    - acceleration is the derivative of velocity with respect to time
        - velocity is the integral of acceleration with respect to time
- Sometimes no position equation is given but only a set of x-t data
    - this is where finite differences comes in

## Finite differences
- the standard way to estimate derivaties numerically is with finite differences
- example: estimate of velocity is literally just delta x / delta t
- ### Taylor series finite differences
    - infinite series expansion of a function in terms of its derivatives
    - the upshot: f'(x) = ( f(x + dx) - f(x) )/dx
        - this is the first order forward finite difference
        - forward because it uses the next term
        - first order because first derivative
    - backward first orderfinite difference: 
        - f'(x) = ( f(x) - f(x - dx) )/dx
    - a more accurate finite difference uses more terms of the taylor series
        - the previous two examples truncated all terms past first order
        - using both the forward and backward finite difference results in a more accurate estimate
        - second order center finite difference
            - forward second order - backwards second order
            - prerequisite: even spacing between data
### In Two Dimensions (Cartesian)
- position, velocity, and acceleration are represented with vectors with x and y components
- each vector component is treated like a 1 dimensional function

## Dealing with Noisy Data
- Finite differences work nicely for perfect measurments but not so much for noisy measurments
- error between true and noisy data gets propagated in finite difference calculations
    - amplified by a lot
- using a **moving average** helps smooth the data
    - average the current, last, and next data point and replace the current data point with the moving average