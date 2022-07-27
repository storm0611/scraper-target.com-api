video = 'docs/untitled.mp4'
# instagram
# import instapy_cli 

# username = 'mesaliquidation'
# password = 'Temp1234'
# text = 'This will be the caption of your video.' + '\r\n' + 'You can also use hashtags! #hash #tag #now'

# with instapy_cli.client(username, password) as cli:
#     print("upload results=", cli.upload(video, text))

# tiktok
from TiktokAutoUploader import TiktokBot
tiktok_bot = TiktokBot()

# Use a video from your directory.
tiktok_bot.upload.uploadVideo(video, "This is text \n overlay on \n the video", 1, 45)
