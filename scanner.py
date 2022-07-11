import cv2
from pyzbar.pyzbar import decode
import keyboard
import time

# Make one method to decode the barcode

def BarcodeReader():

    # read the image in numpy array using cv2
    # img = cv2.imread(image)
    global vid
    ret, frame = vid.read()
    if not ret:
        return 0
    cv2.imshow(frame)
    time.sleep(2)
    # Decode the barcode image
    detectedBarcodes = decode(frame)

    # If not detected then print the message
    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:

        # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes:

            # Locate the barcode position in image
            (x, y, w, h) = barcode.rect

            # Put the rectangle in image using
            # cv2 to heighlight the barcode
            cv2.rectangle(frame, (x-10, y-10),
                          (x + w+10, y + h+10),
                          (255, 0, 0), 2)

            if barcode.data != "":

                # Print the barcode data
                print(barcode.data)
                print(barcode.type)

    #Display the image
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
      # Take the image from user
    global vid
    vid = cv2.VideoCapture(0)
    while not keyboard.is_pressed("esc"):
        BarcodeReader()
    vid.release()
