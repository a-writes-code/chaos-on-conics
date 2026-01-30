#!/bin/bash

# List of curve types to generate videos for
CURVE_TYPES=("circle" "ellipse" "parabola" "hyperbola")


# File parameters #
OUTPUT_DIR="outputs/"


# Simulation (physics) parameters #
x0=1.0
y0=1.5
vx0=0
vy0=0
del_x=0.001
del_t=0.001
g=98.1 # Imagine different units #

# Video parameters #
fps=60
dpi=120
T=5000

# Loop over each curve type
for CURVE in "${CURVE_TYPES[@]}"; do
    echo "Generating video for curve type: $CURVE"

    python scripts/generate_video.py \
        --curve_type "$CURVE" \
        --output_path "$OUTPUT_DIR" \
        --T $T \
        --fps $fps \
        --dpi $dpi \
        --x0 $x0 \
        --y0 $y0 \
        --del_x $del_x \
        --vx0 $vx0 \
        --vy0 $vy0 \
        --del_t $del_t \
        --g $g 
done

echo "All videos generated!"