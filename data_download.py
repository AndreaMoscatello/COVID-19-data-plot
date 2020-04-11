"""
IMPORTANT: the following lines download the full github repository.
you have to do this just once a day in order to update the data.
Once the data are updated you'd better comment this, otherwise the program will download them again
everytime and this will be much slower.
Otherwise you can just manually download them from GitHub, this maybe will take less time.

Also this is working in Ubuntu 18, and it requires svn to work:
sudo apt install subversion
I'm pretty sure this will not work on Windows os iOS.
If you are not able to run thise section just delete it and download manually the directory from github.
You may have to modify the os.chdir() argument then.
"""

import os


print("Downloading the data, may take a while...")
stream = os.popen("svn checkout https://github.com/pcm-dpc/COVID-19/")
output = stream.read()
output
print("Download complete!")
