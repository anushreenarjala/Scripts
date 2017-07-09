#!/usr/bin/env python

try:
    import ConfigParser as cfg
except:
    import configparser as cfg

import os
import json
import sys
import youtube_dl
import re

home = os.environ.get('HOME')

firefoxDir = os.path.join(home, ".mozilla/firefox")
if not os.path.isdir(firefoxDir):
    # Try for Mac
    print("Trying mac")
    firefoxDir = os.path.join(home, "Library/Application\ Support/Firefox")

profileFile = os.path.join(firefoxDir, "profiles.ini")
profileParser = cfg.ConfigParser()
profileParser.read(profileFile)
profileDir = profileParser.get('Profile0', 'Path')

# Now get the list of tabs
sessionFile = os.path.join(firefoxDir, profileDir, "sessionstore.js")
if not os.path.exists( sessionFile ):
    sessionFile = os.path.join(firefoxDir, profileDir
            , 'sessionstore-backups', 'recovery.js'
            )

with open(sessionFile, "r") as sf:
    data = json.loads(sf.read())

def main(args):
    tabsURL = set()
    for win in data.get("windows"):
        for tab in win.get("tabs"):
            i = tab.get("index") - 1
            tabsURL.add(tab.get("entries")[i].get("url"))

    # get the you tube tab
    for url in tabsURL:
        if "youtube.com/watch?" in url:
            print("I can download audio from: {}".format(url))
            downloadUrl(url, args)

def downloadUrl(url, args, outputDir=os.path.join(home, "Music/Downloads")):
    ''' Fragment from here
    http://stackoverflow.com/questions/18054500/how-to-use-youtube-dl-from-a-python-programm
    '''
    if not os.path.isdir(outputDir):
        os.makedirs(outputDir)
    outputFile = os.path.join(outputDir, '%(title)s.%(ext)s')

    print("[INFO] Trying url: %s" % url)
    if "--playlist" not in args:
        opts = ["-k", "-x", "-v", "-o", "{0}".format(outputFile)
                , "--audio-format", "best", "--no-playlist" ] + [ url ]
    else:
        print("[INFO] Downloading playlist from youtube.")
        opts = ["-k", "-v", "-x" "-o", "{0}".format(outputFile)
                , "--audio-format", "best" ] + [ url ]

    youtube_dl.main(opts)

if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)
