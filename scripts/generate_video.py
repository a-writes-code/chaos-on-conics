# scripts/generate_video.py
import numpy as np
import sys
import os

# Add parent directory (project root) to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.utils import *
from src.curves import *
from src.simulation import *
from src.video import *


def main():
    parser = get_argparser()
    args = parser.parse_args()

    # Boundary
    x_curve = generate_boundary_points(args.P, args.d, args.seed)
    curve_fn = CURVE_REGISTER[args.curve_type]
    bx, by, _ = curve_fn(x_curve)

    # Initial particles
    x_init = args.x0 + np.arange(args.N) * args.del_x
    y_init = np.full(args.N, args.y0)

    positions = simulate(
        x_init=x_init,
        y_init=y_init,
        vx0=args.vx0,
        vy0=args.vy0,
        curve_fn=curve_fn,
        curve_params={},  # defaults only for now
        del_t=args.del_t,
        g=args.g,
        T=args.T,
    )

    os.makedirs(args.output_path, exist_ok=True)
    args.file_name = os.path.join(args.output_path, f"{args.curve_type}.mp4")

    make_video(
        positions=positions,
        boundary_xy=(bx, by),
        fps=args.fps,
        dpi=args.dpi,
        cmap=args.cmap,
        background=args.background,
        output_path=args.file_name,
    )


if __name__ == "__main__":
    main()
