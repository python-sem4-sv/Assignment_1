import os
import urllib.request as req
from urllib.parse import urlparse

def download(url, to=None):
    for link in url:
        fileName = link.split("/")
        fileName = fileName[-1]
        if to == None:
            directory = "./" + fileName
        else:
            directory = to
        if os.path.isfile(directory):
            print("File", directory, "already exists")
        else:
            print("Downloading...", link)
            urlInfo = req.urlretrieve(link, directory)
            print("File saved to:", urlInfo[0])


