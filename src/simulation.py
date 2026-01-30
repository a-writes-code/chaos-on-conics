# src/simulation.py
import numpy as np


def reflect_velocity(vx, vy, dydx):
    """
    Reflect velocity across surface normal.
    """
    # tangent vector ~ (1, dydx)
    tx, ty = 1.0, dydx
    norm = np.sqrt(tx**2 + ty**2)
    tx, ty = tx / norm, ty / norm

    # normal vector
    nx, ny = -ty, tx

    v_dot_n = vx * nx + vy * ny
    vx_new = vx - 2 * v_dot_n * nx
    vy_new = vy - 2 * v_dot_n * ny

    return vx_new, vy_new


def simulate(
    x_init,y_init,
    vx0,vy0,
    curve_fn,
    curve_params,
    del_t,g,T,
):
    """
    Returns positions of shape (N, T, 2)
    """
    assert vy0 <= 0.0, "Initial vy must be non-positive"

    N = len(x_init)
    positions = np.zeros((N, T, 2))

    x = x_init.copy()
    y = y_init.copy()
    vx = np.full(N, vx0)
    vy = np.full(N, vy0)

    for t in range(T):
        # store
        positions[:, t, 0] = x
        positions[:, t, 1] = y

        # advance
        x_new = x + vx * del_t
        y_new = y + vy * del_t - 0.5 * g * del_t**2
        vy_new = vy - g * del_t
        vx_new = vx.copy()

        # collision check
        _, y_curve, dydx_curve = curve_fn(x_new, **curve_params)

        below = y_new < y_curve

        if np.any(below):
            vx_ref, vy_ref = reflect_velocity(
                    vx_new[below],
                    vy_new[below],
                    dydx_curve[below],
                )

            vx_new[below] = vx_ref
            vy_new[below] = vy_ref

        # project particle back onto the boundary
        y_new[below] = y_curve[below]

        # commit step
        x = x_new
        y = y_new
        vx = vx_new
        vy = vy_new

    return positions
