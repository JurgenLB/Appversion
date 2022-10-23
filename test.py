#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import Check_App_Versie
#
app = "online Panasonic Comfort Cloud"
url_app = "https://apps.apple.com/de/app/panasonic-comfort-cloud/id1348640525"
V = ()
#
x = Check_App_Versie.app_check(app, url_app, V)
print (type(x))
print (x)
