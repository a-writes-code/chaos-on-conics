# src/video.py

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def make_video(positions, boundary_xy, fps, dpi, cmap, background, output_path):
    N, T, _ = positions.shape

    fig, ax = plt.subplots(figsize=(6, 6), dpi=dpi)
    ax.set_facecolor(background)

    colors = plt.get_cmap(cmap)(np.linspace(0, 1, N))
    scat = ax.scatter(positions[:, 0, 0], positions[:, 0, 1], s=10, c=colors)

    bx, by = boundary_xy
    ax.plot(bx, by, color="black", linewidth=2)

    ax.set_xlim(bx.min() - 1, bx.max() + 1)
    ax.set_ylim(by.min() - 1, positions[:, :, 1].max() + 1)

    def update(frame):
        scat.set_offsets(positions[:, frame, :])
        return scat,

    ani = animation.FuncAnimation(
        fig, update, frames=T, interval=1000 / fps
    )

    ani.save(output_path, fps=fps)
    plt.close(fig)
