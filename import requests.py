import ctypes
import requests

# Replace this with the URL of the API that returns the photo
api_url = 'https://api.waifu.pics/sfw/hug'

# Fetch the photo from the API
response = requests.get(api_url)

# Save the photo to a file
with open('photo.jpg', 'wb') as f:
    f.write(response.content)

# Use the ctypes module to set the photo as the desktop wallpaper
ctypes.windll.user32.SystemParametersInfoW(20, 0, 'C:\\path\\to\\photo.jpg', 0)

print('Desktop wallpaper changed!')
