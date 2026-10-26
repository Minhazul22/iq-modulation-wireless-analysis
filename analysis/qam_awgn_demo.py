#!/usr/bin/env python3
"""Generate an illustrative square-QAM constellation comparison with additive noise.

This is a teaching simulation, not a reconstruction of the laboratory measurements.
The noise standard deviation is specified in normalized constellation-coordinate
units; it is not a calibrated SNR or a measured channel model.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def square_qam_points(order: int) -> np.ndarray:
    """Return a unit-square-normalized ideal square-QAM constellation."""
    side = int(np.sqrt(order))
    if side * side != order or side < 2:
        raise ValueError("Modulation order must be a square integer (4, 16, 64, 256, ...).")
    levels = np.arange(-(side - 1), side, 2, dtype=float)
    points = np.array([(i, q) for q in levels for i in levels], dtype=float)
    return points / np.max(np.abs(points))


def plot_comparison(
    orders: list[int], noise_std: float, samples: int, seed: int, output: Path
) -> None:
    rng = np.random.default_rng(seed)
    cols = 2
    rows = int(np.ceil(len(orders) / cols))
    fig, axes = plt.subplots(rows, cols, figsize=(11, 4.8 * rows), squeeze=False)
    axes_flat = axes.ravel()

    for ax, order in zip(axes_flat, orders):
        ideal = square_qam_points(order)
        indexes = rng.integers(0, len(ideal), size=samples)
        transmitted = ideal[indexes]
        noise = rng.normal(0.0, noise_std, size=transmitted.shape)
        received = transmitted + noise

        ax.scatter(ideal[:, 0], ideal[:, 1], s=20, marker="x",
                   linewidths=0.8, label="Ideal symbols")
        ax.scatter(received[:, 0], received[:, 1], s=7, alpha=0.4,
                   label="Noisy samples")
        ax.set_title(f"{order}-QAM")
        ax.set_xlabel("In-phase (I), normalized")
        ax.set_ylabel("Quadrature (Q), normalized")
        ax.set_xlim(-1.25, 1.25)
        ax.set_ylim(-1.25, 1.25)
        ax.set_aspect("equal", adjustable="box")
        ax.grid(True, alpha=0.25)
        ax.legend(loc="upper left", fontsize=8)

    for ax in axes_flat[len(orders):]:
        ax.set_visible(False)

    fig.suptitle(
        "Illustrative square-QAM constellations under additive noise\n"
        f"noise std = {noise_std:g} normalized units; simulation only",
        fontsize=13,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=180, bbox_inches="tight")
    print(f"Saved illustrative simulation to: {output}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--orders", nargs="+", type=int, default=[4, 16, 64, 256],
        help="Square modulation orders to plot (default: 4 16 64 256)",
    )
    parser.add_argument(
        "--noise-std", type=float, default=0.06,
        help="Noise standard deviation in normalized I/Q coordinates (default: 0.06)",
    )
    parser.add_argument(
        "--samples", type=int, default=1500,
        help="Number of noisy received symbols per modulation order (default: 1500)",
    )
    parser.add_argument("--seed", type=int, default=7, help="Random seed (default: 7)")
    parser.add_argument(
        "--output", type=Path, default=Path("images/qam-awgn-simulation.png"),
        help="Output image path",
    )
    args = parser.parse_args()

    if not args.orders or any(order < 4 for order in args.orders):
        parser.error("Provide one or more square-QAM orders of at least 4.")
    if args.noise_std < 0:
        parser.error("--noise-std must be non-negative.")
    if args.samples < 1:
        parser.error("--samples must be at least 1.")
    for order in args.orders:
        side = int(np.sqrt(order))
        if side * side != order:
            parser.error(f"{order} is not a square-QAM order.")

    plot_comparison(args.orders, args.noise_std, args.samples, args.seed, args.output)


if __name__ == "__main__":
    main()
