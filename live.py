import cv2
from ultralytics import YOLO
from stream import stream_url

# Load YOLO model
model = YOLO(r"C:\Users\k.belhadj\Desktop\Repos\Car_detection_model\weights\best.pt")  # Replace with your model

# Stream URL
#stream_url = ""

cap = cv2.VideoCapture(stream_url)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to read from stream. Retrying...")
        continue

    # Perform YOLO detection
    results = model(frame)

    # Annotate each frame
    for result in results:
        annotated_frame = result.plot()  # Use .plot() to draw the detections on the frame

    # Display the annotated frame
    cv2.imshow("YOLO Detection", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
