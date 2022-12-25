import instaloader

ig = instaloader.Instaloader()
dp = input("Enter Insta username : ")

ig.download_profile(dp , profile_pic_only=True)

import os

# Set the directory you want to rename files in
directory = dp

# Get a list of all the files in the directory
files = os.listdir(directory)

# Iterate through the files, renaming them one by one
for file in files:
    # Split the file name into a list of parts
    parts = file.split('.')

    # Get the file extension
    extension = parts[-1]

    # Join all the parts except the extension back together, and add a new prefix to the file name
    new_name = dp +'.' + extension

    # Use the os.rename() function to rename the file
    os.rename(os.path.join(directory, file), os.path.join(directory, new_name))

from io import BytesIO
import win32clipboard
from PIL import Image

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

filepath = dp+'/'+dp+'.jpg'
image = Image.open(filepath)

output = BytesIO()
image.convert("RGB").save(output, "BMP")
data = output.getvalue()[14:]
output.close()

send_to_clipboard(win32clipboard.CF_DIB, data)
