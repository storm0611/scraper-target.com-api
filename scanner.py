import cv2
# from pyzbar.pyzbar import decode
import keyboard
import time
import json
import PIL.Image as image_
from pip import main

# from cvzone.HandTrackingModule import HandDetector
# detector = HandDetector(maxHands=1, detectionCon=0.7)
# Make one method to decode the barcode
# def BarcodeReader():

#     # read the image in numpy array using cv2
#     # img = cv2.imread(image)
#     cap = cv2.VideoCapture(deviceID)
    
#     ret, frame = cap.read()
#     print(ret)
#     if not ret:
#         return 0
#     width = cap.get(3)  # float `width`
#     height = cap.get(4)  # float `height`
#     print("w=", width)
#     print("h=", height)
#     print(frame)
#     print(type(frame))
#     time.sleep(2)
#     # img = detector.findHands(frame)
#     print(cv2.UMat(frame))
#     cv2.imshow("sss", cv2.UMat(frame))
#     # # Decode the barcode image
#     # detectedBarcodes = decode(frame)

#     # # If not detected then print the message
#     # if not detectedBarcodes:
#     #     print("Barcode Not Detected or your barcode is blank/corrupted!")
#     # else:

#     #     # Traverse through all the detected barcodes in image
#     #     for barcode in detectedBarcodes:

#     #         # Locate the barcode position in image
#     #         (x, y, w, h) = barcode.rect

#     #         # Put the rectangle in image using
#     #         # cv2 to heighlight the barcode
#     #         cv2.rectangle(frame, (x-10, y-10),
#     #                       (x + w+10, y + h+10),
#     #                       (255, 0, 0), 2)

#     #         if barcode.data != "":

#     #             # Print the barcode data
#     #             print(barcode.data)
#     #             print(barcode.type)

#     # #Display the image
#     # cv2.waitKey(0)
#     # cv2.destroyAllWindows()
#     cap.release()
#     return deviceID


# if __name__ == "__main__":
#       # Take the image from user
#     global deviceID
#     deviceID = 700
#     while not keyboard.is_pressed("esc"):
#         sss = BarcodeReader()
#         if sss:
#             print(deviceID)
#             jsonString = json.dumps({"deviceID": deviceID})
#             jsonFile = open("deviceID.json", "a")
#             jsonFile.write(jsonString)
#             jsonFile.close()
#         # deviceID += 1
    
# import the opencv library
import cv2


# define a video capture object
vid = cv2.VideoCapture(700)

while(True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
