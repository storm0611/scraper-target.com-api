import cv2
import argparse
import os
import urllib.request   
import numpy as np
import random

img_url = 'https://target.scene7.com/is/image/Target/GUEST_622fe0b9-af6d-4897-b200-14b609fcd669'
img_name = 'Vivitar 3ct Rope Lights'
img_original_price = '12.75'
img_our_price = '12.75'

start_time = 6
stop_time = 10

req = urllib.request.urlopen(img_url)
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
img = cv2.imdecode(arr, -1) # 'Load it as it is'
# cv2.imshow("src", img)

img = cv2.putText(img, img_name, (10, 40), cv2.FONT_HERSHEY_SIMPLEX,
                  0.7, (120, 14, 156), 2, cv2.LINE_AA)
img = cv2.putText(img, "Original: $" + img_original_price, (30, 70), cv2.FONT_HERSHEY_SIMPLEX,
                  0.5, (199, 26, 26), 2, cv2.LINE_AA)
img = cv2.putText(img, "Our: $" + img_our_price, (30, 100), cv2.FONT_HERSHEY_SIMPLEX,
                  0.5, (199, 26, 26), 2, cv2.LINE_AA)

cv2.imshow("dst", img)

if cv2.waitKey() & 0xff == 27: quit()

cap = cv2.VideoCapture('my_baby_dog.mp4')

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")

# Read until video is completed
while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count / fps

        print('fps = ' + str(fps))
        print('number of frames = ' + str(frame_count))
        print('duration (S) = ' + str(duration))
        minutes = int(duration / 60)
        seconds = duration % 60
        print('duration (M:S) = ' + str(minutes) + ':' + str(seconds))
        # Display the resulting frame
        frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # ADD OVERLAY TEXT
        if start_time < duration < stop_time:
            cv2.putText(img=frame, text='EKO', org=(int(frameWidth / 2 - 20), int(frameHeight / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=3,
                        color=(0, 255, 0))
        # cv2.putText(img=frame, text='EKO', org=(int(frameWidth / 2 - 20), int(frameHeight / 2)),
        #             fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=3,
        #             color=(0, 255, 0))
        cv2.imshow('Frame', frame)
        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break


# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
