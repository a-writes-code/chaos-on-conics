# Simulation of Particles Falling on Conic Curves #

I wanted to test this idea from [this video by Alex Gustafsson]([url](https://www.youtube.com/watch?v=0zmWEzrtvJA#:~:text=Butterfly%20effect%20in%20a%20circle,Visuals%20in%20Python%20&%20FFmpeg)). It describes dynamics of particles when they are dropped on conic sections. There's a [blogpost]([url](https://ffmpeg.org/download.html)) which describes this as well.

---

## Requirements

- Python 3.10+  
- Python packages: see `requirements.txt`  
- FFmpeg (for `.mp4` video output)

On Mac, `brew install ffmpeg`. On Ubuntu/Debian, `sudo apt install ffmpeg`. On Windows, see [here]([url](https://ffmpeg.org/download.html)).

### Installing Python dependencies

```bash
pip install -r requirements.txt
```

## Generating videos ##

Run the `scripts/generate_videos.py` directly or use a shell file (for example, `run.sh`).

Currently, videos are saved with only the curve name, be careful if you're playing around with different parameters.
