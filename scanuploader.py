import subprocess
import os
from subprocess import Popen
from os import environ
from os import listdir
from os.path import isfile, join


def is_movie(path):
    name, ext = os.path.splitext(path)
    print path
    if not ext in EXTENSIONS:
        return False
    return True

def list_folder(path):
    movies = []
    for path, subdirs, files in os.walk(path):
        for name in files:
                if(is_movie(os.path.join(path, name))):
                        movies.append(os.path.join(path, name))

    return movies

EXTENSIONS = [".jpeg", ".tiff", ".pdf", ".jpg", ".tif"]

mypath = "/var/www/phpsane/output/"
#print os.listdir(mypath)
print mypath
files = list_folder(mypath)
print files
for m in files:
  print "File: {0}".format(os.path.basename(m))
#  subprocess.Popen("/home/pi/dropboxuploader/dropbox_uploader.sh UPLOAD ")
  bashCommand = "mv  "
  bashCommand += m
  bashCommand += " /home/pi/scansioni/"
  bashCommand += format(os.path.basename(m))
  print bashCommand
  process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
  output = process.communicate()[0]

  bashCommand = "/home/pi/dropboxuploader/dropbox_uploader.sh upload "
  bashCommand += " /home/pi/scansioni/"
  bashCommand += format(os.path.basename(m))
  print bashCommand
  process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
  output = process.communicate()[0]
