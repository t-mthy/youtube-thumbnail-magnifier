# Module: YouTube Video Thumbnail Magnifier
#
# Author: t-mthy
#
# Description: Copy YouTube video URL. Paste URL to console prompt.
# View the magnified image.
# ==============================================================================


import cv2
import urllib.request
import numpy as np


yt_url = input("Enter YouTube video URL: ")

# extract youtube ID from URL
yt_vid_id = yt_url.split("watch?v=")[-1]

# get maxres URL
max_res = "https://i.ytimg.com/vi/" + yt_vid_id + "/maxresdefault.jpg"

# maxres URL --> openCV imread
req = urllib.request.urlopen(max_res)
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
img = cv2.imdecode(arr, -1)

# resize/magnify
img = cv2.resize(img, (0, 0), fx=1.3, fy=1.3)

# display thumbnail
cv2.imshow("Your YouTube Thumbnail:", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
