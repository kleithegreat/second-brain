from sympy import *

x = symbols("x")
fx = ln(x) * sinh(x) / E**x

center = (fx.subs(x, 1.75) - fx.subs(x, 1.25)) / (1.75 - 1.25)
centerError = abs( (0.336925 - center) / 0.336925 ) * 100

step = 0.25

forward = (fx.subs(x, 1.5 + step) - fx.subs(x, 1.5)) / step
backward = (fx.subs(x, 1.5) - fx.subs(x, 1.5 - step)) / step

forwardError = abs( (0.336925 - forward) / 0.336925 )  * 100
backwardError = abs( (0.336925 - backward) / 0.336925 ) * 100

while backwardError > centerError:
    print(step)
    step -= 0.0001
    if step < 0:
        break
    
    forward = (fx.subs(x, 1.5 + step) - fx.subs(x, 1.5)) / step
    backward = (fx.subs(x, 1.5) - fx.subs(x, 1.5 - step)) / step

    forwardError = abs( (0.336925 - forward) / 0.336925 )  * 100
    backwardError = abs( (0.336925 - backward) / 0.336925 ) * 100
    
print(step)
