import cv2
from ultralytics import YOLO
import imutils

# Load the YOLOv8 model
model = YOLO('runs/detect/yolov8n_se2/weights/best.pt')

# Open the video file
# video_path = "path/to/your/video/file.mp4"

cap = cv2.VideoCapture(0)


# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()
    frame = frame[0:480, 0:480]

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame, conf=0.8)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        # resized_frame = imutils.resize(frame, height=480)
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()