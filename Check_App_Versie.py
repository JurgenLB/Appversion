#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Code for retrieving App Version in Appstore
#
# Dependencies;
#
# sudo pip3 install bs4
# sudo pip3 install lxml
#
# 47: GuessedAtParserWarning: No parser was explicitly specified,
# so I'm using the best available HTML parser for this system ("lxml").
# This usually isn't a problem, but if you run this code on another system,
# or in a different virtual environment, it may use a different parser and behave differently.
#
#import urllib
import traceback
#
from subprocess import Popen, PIPE, STDOUT
from time import sleep
from urllib import request
#
try:
    from bs4 import BeautifulSoup
except:
    Popen("sudo pip3 install bs4", shell=True, stdout=PIPE, stderr=PIPE)
    sleep (1)
    from bs4 import BeautifulSoup
#
#
app = "online Panasonic Comfort Cloud"
url_app = "https://apps.apple.com/de/app/panasonic-comfort-cloud/id1348640525"
url_api = "https://api.appstoreconnect.apple.com/v1/apps/id1348640525/appStoreVersions"
# https://api.appstoreconnect.apple.com/v1/apps/{id}/appStoreVersions
#
V = ()
#
def app_check(app, url_, v):
    try:
        info = "check Version {}".format(app)
        print (info)
        print ("... ")
        # https://apps.apple.com/de/app/panasonic-comfort-cloud/id1348640525
        #
#        app_online = urllib.request.urlopen(url_).read()
        app_online = request.urlopen(url_).read()
#        soup = BeautifulSoup(app_online)
#        soup = BeautifulSoup(pcc_online, 'html.parser')
        soup = BeautifulSoup(app_online, 'lxml')
        l = soup.find_all('p')
        print ("...... ")
        for tag in l:
            if "Version" in link :
                print (link)
#            Version 1.16.0
                v = link
            else :
                pass
    except Exception as e:
        print (" ")
        print ("Oops!  Try again...")
        print (" ")
        print (traceback.format_exc())
        #
    except KeyboardInterrupt:
        print ("ctrl + C Pressed")
        #
    finally:
        print (" ")
        app_info = "{} = {} ".format(app, v)
        print (app_info)
        print (" ")
        return v
