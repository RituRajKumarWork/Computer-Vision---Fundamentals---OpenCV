import cv2

# Define video path
video_path = '../Video - Input Output/vlc-record-2024-05-04-22h22m39s-SnapSave.io-Hotstar Specials The Legend Of Hanuman _ New Season _ Coming Soon _ DisneyPlus Hotstar.mp4-.mp4'

# Open video file
video = cv2.VideoCapture(video_path)

# Play video
while True:
    ret, frame = video.read()
    if not ret:
        break
    cv2.imshow('Video', frame)
    cv2.waitKey(40)

# Release resources
video.release()
cv2.destroyAllWindows()
