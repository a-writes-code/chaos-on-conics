# src/curves.py

import numpy as np

'''
Quadratic functions return upper and lower branches.
'''

def circle(x, r=2.0, eps = 1.0e-8, off=1.0):
    """
    x^2 + y^2 = r^2
    Returns upper and lower branches.
    """
    
    inside = r**2 - x**2
    inside = np.clip(inside, 0.0, None)

    y = -np.sqrt(inside)
    dydx = -x / (y + eps)

    off = -r
    y-=off

    # x_out = np.concatenate([x, x])
    # y_out = np.concatenate([y, -y])
    # dydx_out = np.concatenate([dydx, -dydx])

    # return x_out, y_out, dydx_out
    return x, y, dydx


def parabola(x, a=0.5, off=0.0):
    """
    y = a x^2
    """
    y = a * x**2
    dydx = 2 * a * x
    y-=off
    return x, y, dydx


def ellipse(x, a=3.0, b=2.0, eps=1.0e-8, off=1.0):
    """
    x^2/a^2 + y^2/b^2 = 1
    """
    inside = 1.0 - (x**2) / (a**2)
    inside = np.clip(inside, 0.0, None)

    y = -b * np.sqrt(inside)
    dydx = -(b * x) / (a**2 * y + eps)

    off=-b
    y-=off

    # x_out = np.concatenate([x, x])
    # y_out = np.concatenate([y, -y])
    # dydx_out = np.concatenate([dydx, -dydx])

    # return x_out, y_out, dydx_out
    return x, y, dydx


def hyperbola(x, a=1.0, b=1.0, eps=1.0e-8, off=1.0):
    """
    y^2/b^2 - x^2/a^2 = 1
    (Horizontal hyperbola)
    """
    inside = (x**2) / (a**2) + 1.0
    inside = np.clip(inside, 0.0, None)

    y = b * np.sqrt(inside)
    dydx = (b * x) / (a**2 * y + eps)

    off=b
    y-=off

    # x_out = np.concatenate([x, x])
    # y_out = np.concatenate([y, -y])
    # dydx_out = np.concatenate([dydx, -dydx])

    # return x_out, y_out, dydx_out
    return x, y, dydx

CURVE_REGISTER = {
    "circle": circle,
    "parabola": parabola,
    "ellipse": ellipse,
    "hyperbola": hyperbola,
}

### Feel free to add more curves here ###