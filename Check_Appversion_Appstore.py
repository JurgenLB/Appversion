#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Code for retrieving App Version in Appstore
#
# Dependencies;
#
# sudo pip3 install colorama  # For color in commandline output
# sudo pip3 install bs4
# sudo pip3 install lxml
#
#
# 56: GuessedAtParserWarning: No parser was explicitly specified,
# so I'm using the best available HTML parser for this system ("html.parser").
# This usually isn't a problem, but if you run this code on another system,
# or in a different virtual environment, it may use a different parser and behave differently.
# "lxml" is best for fastest result
#
#import urllib
import traceback
#
from urllib import request
from bs4 import BeautifulSoup
from time import sleep
#
app = "online Panasonic Comfort Cloud"
url_app = "https://apps.apple.com/de/app/panasonic-comfort-cloud/id1348640525"
url_api = "https://api.appstoreconnect.apple.com/v1/apps/id1348640525/appStoreVersions"
# https://api.appstoreconnect.apple.com/v1/apps/{id}/appStoreVersions
#
V = ()
#
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#
try:
    print (". ") 
    info = "check Version {}".format(app)
    print (info)
    print ("... ")
    # https://apps.apple.com/de/app/panasonic-comfort-cloud/id1348640525
    #
    app_online = urllib.request.urlopen(url_app).read()
    soup = BeautifulSoup(app_online, 'html.parser')
#    soup = BeautifulSoup(app_online, 'lxml')
#    soup = BeautifulSoup(app_online)
    l = soup.find_all('p')
    print ("..... ")
#    print (soup.prettify())
#      <div class="l-row whats-new__content">
#       <div class="l-column small-12 medium-3 large-4 small-valign-top whats-new__latest">
#        <div class="l-row">
#         <time aria-label="28. September 2022" class="" data-test-we-datetime="" datetime="2022-09-28T00:00:00.000Z">
#          28. Sept. 2022
#         </time>
#         <p class="l-column small-6 medium-12 whats-new__latest__version">
#          Version 1.16.0
#         </p> 
#        </div>
#       </div>
    for tag in l:
#        print (tag)
# <p class="l-column small-6 medium-12 whats-new__latest__version">Version 1.16.0</p>
#        link = tag.get('class',None)
        link = str(tag.string)
        if "Version" in link :
            print (link)
#            Version 1.16.0
            V = link
        else :
            pass
#            print (bcolors.OKCYAN + "Version Not Found in string" + bcolors.ENDC)
            #
        #
    print (" ")
    app_info = "{} = {} ".format(app, V)
    print (app_info)
    print (" ")
#    return V
    #
except Exception as e:
    print (" ")
#    print (bcolors.FAIL + "Oops!  Try again..." + bcolors.ENDC)
    print ("Oops!  Try again...")
    print (" ")
    print (traceback.format_exc())
#    return V
except KeyboardInterrupt:
#    print (bcolors.WARNING + "ctrl + C Pressed" + bcolors.ENDC)
    print ("ctrl + C Pressed")

#    return V
# 
