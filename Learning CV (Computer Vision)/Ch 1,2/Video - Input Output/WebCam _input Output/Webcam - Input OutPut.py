import cv2

# Read webcam
webcam = cv2.VideoCapture(0)

# Visualize webcam
while True:
    ret, frame = webcam.read()

    cv2.imshow('frame', frame)

    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
