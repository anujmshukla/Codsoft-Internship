import cv2

def main():
    # Create a VideoCapture object to access the camera.
    cap = cv2.VideoCapture(1)  # Use 0 for the default camera, or provide the camera index if you have multiple cameras connected.

    # Set the desired resolution.
    width = 20
    height = 20
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    while True:
        # Read a frame from the camera.
        ret, frame = cap.read()

        if not ret:
            break

        # Perform any image processing here if needed.
        # For example, you can resize the frame using cv2.resize function:
        # frame = cv2.resize(frame, (new_width, new_height))

        # Display the resized frame.
        cv2.imshow('Resized Camera', frame)

        # Exit the loop if the 'q' key is pressed.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the VideoCapture and close any open windows.
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
