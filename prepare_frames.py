import cv2
import os
import numpy as np
from tqdm import tqdm

def prepare_frames(frames_folder, output_file="preloaded_frames.npz", size=(48, 48)):
    frame_files = sorted(
        [f for f in os.listdir(frames_folder) if f.endswith((".png", ".jpg"))]
    )
    frames = []
    for filename in tqdm(frame_files):
        path = os.path.join(frames_folder, filename)
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if img is not None:
            resized = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
            frames.append(resized)

    frames_array = np.array(frames)
    np.savez_compressed(output_file, frames=frames_array)
    print(f"Saved {len(frames)} frames to {output_file}")

if __name__ == "__main__":
    prepare_frames("frames", "preloaded_frames.npz")
