DocsDPUploader
==============

An uploader for scanned file to Dropbox.

Requirements
------------
* phpSane
* Dropbox uploader (by Andrea Fabrizi, https://github.com/andreafabrizi/Dropbox-Uploader)

HOW TO
------

This simple python script upload all scanned file in /var/www/phpsane/ouput/ folder to your Dropbox Home Folder using the dropboxUploader.
You can use crontab to automatically upload all file each hour. <br />
The script also move the scanned file to another dir (/home/pi/scansioni/) to avoid to re-upload the same file each time.
