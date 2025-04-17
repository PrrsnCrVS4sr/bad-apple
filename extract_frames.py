import cv2
import os

def extract_frames(video_path, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break  # End of video

        # Save the frame as an image file
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.png")
        cv2.imwrite(frame_filename, frame)

        frame_count += 1

    cap.release()
    print(f"Extracted {frame_count} frames to '{output_folder}'.")

# Example usage
video_path = "bad_apple.mp4"
output_folder = "frames"
extract_frames(video_path, output_folder)
