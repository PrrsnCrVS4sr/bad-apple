import numpy as np
import pygame
import time
import sys

def display_frame_ascii(image):
    _, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    frame_output = [' '.join(['-' if pixel == 255 else ' ' for pixel in row]) for row in binary]
    sys.stdout.write("\033[H\033[J")  # Clear screen
    sys.stdout.write("\n".join(frame_output) + "\n")
    sys.stdout.flush()

def play_sound(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

def main(frames_file="preloaded_frames.npz", sound_file="bad_apple.mp3", fps=30):
    data = np.load(frames_file)
    frames = data["frames"]
    frame_duration = 1 / fps

    play_sound(sound_file)
    sys.stdout.write("\033[H\033[J")  # Clear screen

    for frame in frames:
        start_time = time.time()

        display_frame_ascii(frame)

        elapsed = time.time() - start_time
        time_to_sleep = frame_duration - elapsed
        if time_to_sleep > 0:
            time.sleep(time_to_sleep)

    pygame.mixer.music.stop()

if __name__ == "__main__":
    import cv2  # Only imported if script runs, to keep preload script faster
    main()
