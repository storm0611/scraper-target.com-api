import time
import cv2
import argparse
import os
import urllib.request   
import numpy as np
import random
import sqlite3
from PIL import ImageFont, ImageDraw, Image  
from moviepy.editor import *
    
frameSize = (800, 1280)
fps = 30
dir = os.getcwd() + "\\video\\"


def zoom(img, zoom_factor=2):    
    return cv2.resize(img, None, fx=zoom_factor, fy=zoom_factor)


def create_video(video_name, video_ext, img_url, img_title, original_price, our_price):
    pos_title = (10, 80)
    pos_img = (60, 130)
    pos_original = (110, 650)
    pos_our = (400, 660)

    # Load background image in OpenCV
    image = cv2.imread("product_background.jpg")

    # Load product image
    req = urllib.request.urlopen(img_url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)  # 'Load it as it is'
    # cv2.imshow("src", img)
    img = cv2.resize(img, (500, 480))
    # copied_img = img.copy()

    # Convert the image to RGB (OpenCV uses BGR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Pass the image to PIL
    image = Image.fromarray(image)

    draw = ImageDraw.Draw(image)

    # Draw the text
    font = ImageFont.truetype("arial.ttf", 36)
    draw.text(pos_title, img_title, font=font, fill=(0, 0, 0))
    font = ImageFont.truetype("arial.ttf", 28)
    draw.text(pos_original, "$" + original_price, font=font, fill=(0, 0, 0))
    font = ImageFont.truetype("arial.ttf", 36)
    draw.text(pos_our, "$" + our_price, font=font, fill=(0, 0, 0))

    # Get back the image to OpenCV
    # image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # image = Image.fromarray(image)
    img = Image.fromarray(img)
    copied_img = image.copy()
    copied_img.paste(img, pos_img)
    # copied_img.save('dst image.jpg', quality=95)
    product_img = np.asarray(copied_img)

    # cv2.imshow("dst", product_img)

    image = cv2.imread('background.jpg')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)

    img = Image.fromarray(product_img)
    copied_img = image.copy()
    copied_img.paste(img, (random.randint(0, 800 - 630), random.randint(0, 1280 - 740)))
    # copied_img.save('dst image.jpg', quality=95)
    final_img = np.asarray(copied_img)

    # cv2.imshow("final", final_img)

    # zoom setting
    rate = 1
    src_img = product_img
    cposx = random.randint(0, 800 - 630) + 315
    cposy = random.randint(0, 1280 - 740) + 370

    # video setting
    global frameSize, fps
        
    video_length = 3
    out = cv2.VideoWriter(str(video_name) + video_ext,
                        cv2.VideoWriter_fourcc(*'DIVX'), fps, frameSize)
    
    for cnt_frame in range(0, video_length * fps):
        # zooming
        src_img = zoom(product_img, rate)
        height, width, channel = src_img.shape
        # print(src_img.shape)
        img = Image.fromarray(src_img)
        
        copied_img = image.copy()
        copied_img.paste(img, (cposx - int(width / 2), cposy - int(height / 2)))
        # copied_img.save('dst image.jpg')
        
        final_img = np.asarray(copied_img)
        final_img = cv2.cvtColor(final_img, cv2.COLOR_RGB2BGR)    
        # cv2.imshow("final", final_img)
        rate = rate + 0.001
        
        # write to video file
        out.write(final_img)
        # key = cv2.waitKey()
        # if key == 27:
        #     break

    print(str(video_name) + video_ext + ":quit")
    out.release()
    

def create_video_ads(prefix, ext, count, dst_name):
    padding = 0.5
    video_clips = []
    for cnt in range(0, count):
        video_clips.append(VideoFileClip(prefix + str(cnt) + ext))

    video_fx_list = [video_clips[0]]
    idx = video_clips[0].duration - padding
    for video in video_clips[1:]:
        video_fx_list.append(video.set_start(idx).crossfadein(padding))
        # video_fx_list.append(video.crossfadein(padding))
        idx += video.duration - padding

    global frameSize, fps
    final_video = CompositeVideoClip(video_fx_list, frameSize)

    # slided_clips = [clip.fx(transfx.slide_out, 1, 'bottom')
    #                 for clip in video_clips]
    # print(slided_clips)
    # final_video = concatenate(slided_clips, padding=-1)

    final_video.write_videofile(dst_name, fps=fps)


if __name__ == '__main__':
    start_time = time.time()
    
    prefix = 'out'
    ext = '.mp4'
    
    # img_url = 'https://target.scene7.com/is/image/Target/GUEST_622fe0b9-af6d-4897-b200-14b609fcd669'
    # img_title = 'Vivitar 3ct Rope Lights'
    # original_price = '12.75'
    # our_price = '12.75'
    
    conn = sqlite3.connect('mydb.db')
    cur = conn.cursor()
    
    sql = "SELECT * FROM Shoes_products"
    results = cur.execute(sql).fetchall()
    cnt = 0
    for row in results:
        if cnt >= 10:
            break
        
        img_url = str(row[6])
        img_title = str(row[4])
        original_price = str(row[8])
        if row[16]:
            our_price = str(row[16])
        else:
            our_price = str(float(original_price)  / 2)
        
        print(img_title, original_price, our_price)
        create_video(dir + prefix + str(cnt), ext, img_url, img_title, original_price, our_price)
        
        cnt += 1
    
    end_time = time.time()
    print("created 10 video:", end_time - start_time)
       
    cv2.destroyAllWindows()
    
    create_video_ads(dir + prefix, ext, 10, "final.mp4")
    
    print("created final video", time.time() - end_time)
    
    conn.close()
