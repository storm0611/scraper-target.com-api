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


req = urllib.request.urlopen(img_url)
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
img = cv2.imdecode(arr, -1) # 'Load it as it is'
# cv2.imshow("src", img)

img = cv2.putText(img, img_name, (10, 40), cv2.FONT_HERSHEY_SIMPLEX,
                  0.7, (199, 26, 26), 2, cv2.LINE_AA)
img = cv2.putText(img, "Original: $" + img_original_price, (30, 70), cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
                  0.6, (120, 14, 156), 2, cv2.LINE_AA)
img = cv2.putText(img, "Our: $" + img_our_price, (30, 100), cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
                  0.6, (120, 14, 156), 2, cv2.LINE_AA)

cv2.imshow("dst", img)

if cv2.waitKey() & 0xff == 27: quit()

# # Construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-ext", "--extension", required=False,
#                 default='png', help="extension name. default is 'png'.")
# ap.add_argument("-o", "--output", required=False,
#                 default='output.mp4', help="output video file")
# args = vars(ap.parse_args())

# # Arguments
# dir_path = '.'
# ext = args['extension']
# output = args['output']

# images = []
# for f in os.listdir(dir_path):
#     if f.endswith(ext):
#         images.append(f)

# # Determine the width and height from the first image
# image_path = os.path.join(dir_path, images[0])
# frame = cv2.imread(image_path)
# cv2.imshow('video', frame)
# height, width, channels = frame.shape

# # Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Be sure to use lower case
# out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))

# for image in images:

#     image_path = os.path.join(dir_path, image)
#     frame = cv2.imread(image_path)

#     out.write(frame)  # Write out frame to video

#     cv2.imshow('video', frame)
#     if (cv2.waitKey(1) & 0xFF) == ord('q'):  # Hit `q` to exit
#         break

# # Release everything if job is finished
# out.release()
# cv2.destroyAllWindows()

# print("The output video is {}".format(output))
