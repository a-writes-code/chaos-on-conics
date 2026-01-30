# src/utils.py
import argparse
import numpy as np

from .curves import *

def generate_boundary_points(P, d, seed=0):
    """
    Generate x values uniformly in [-d, d].
    The actual y-values come from src/curves.py.
    """
    rng = np.random.default_rng(seed)
    x = rng.uniform(-d, d, size=P)
    x = np.sort(x)
    return x


def get_argparser():
    parser = argparse.ArgumentParser(
        description="Butterfly-effect simulation for particles interacting with a curve boundary"
    )

    # ---------------------------------------------------------
    # (1) Boundary / curve sampling parameters
    # ---------------------------------------------------------
    parser.add_argument(
        "--curve_type",
        type=str, default="circle",
        choices=["circle", "parabola", "ellipse", "hyperbola"],
        help="Type of boundary curve",
    )

    parser.add_argument(
        "--P",
        type=int,default=2000,
        help="Number of (x, y) points used to represent the boundary curve"
    )

    parser.add_argument(
        "--d",
        type=float,
        default=2.0,
        help="Range parameter: x ~ Uniform(-d, d) when sampling the curve"
    )

    # ---------------------------------------------------------
    # (2) Initial particle configuration
    # ---------------------------------------------------------
    parser.add_argument(
        "--x0",
        type=float,
        default=1.0,
        help="Initial x-location of the first particle"
    )

    parser.add_argument(
        "--y0",
        type=float,
        default=1.5,
        help="Initial y-location of all particles"
    )

    parser.add_argument(
        "--vx0",
        type=float,
        default=0.0,
        help="Initial x-velocity (shared by all particles)"
    )

    parser.add_argument(
        "--vy0",
        type=float,
        default=0.0,
        help="Initial y-velocity (must be non-positive)"
    )

    parser.add_argument(
        "--N",
        type=int,
        default=100,
        help="Number of particles"
    )

    parser.add_argument(
        "--del_x",
        type=float,
        default=1e-3,
        help="Horizontal separation between adjacent particles"
    )    

    # ---------------------------------------------------------
    # (3) Physics parameters
    # ---------------------------------------------------------
    parser.add_argument(
        "--g",
        type=float,
        default=98.1,
        help="Gravitational acceleration"
    )

    parser.add_argument(
        "--del_t",
        type=float,
        default=1e-3,
        help="Time step size"
    )

    # ---------------------------------------------------------
    # (5) Simulation control
    # ---------------------------------------------------------
    parser.add_argument(
        "--T",
        type=int,
        default=10_000,
        help="Number of simulation steps"
    )

    parser.add_argument(
        "--reflection_eps",
        type=float,
        default=1e-8,
        help="Numerical tolerance when detecting wall collisions"
    )

    # ---------------------------------------------------------
    # (6) Video / rendering parameters
    # ---------------------------------------------------------
    parser.add_argument(
        "--fps",
        type=int,
        default=60,
        help="Frames per second for the output video"
    )

    parser.add_argument(
        "--dpi",
        type=int,
        default=120,
        help="DPI for matplotlib rendering"
    )

    parser.add_argument(
        "--cmap",
        type=str,
        default="viridis",
        help="Colormap used to color particles"
    )

    parser.add_argument(
        "--background",
        type=str,
        default="white",
        choices=["white", "black"],
        help="Background color for the video"
    )

    parser.add_argument(
        "--output_path",
        type=str,
        default="outputs/",
        help="Path to save the generated video"
    )

    # ---------------------------------------------------------
    # Reproducibility / misc
    # ---------------------------------------------------------
    parser.add_argument(
        "--seed",
        type=int,
        default=0,
        help="Random seed (used for curve sampling, if applicable)"
    )

    return parser
