#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib
import re

def getLatestBrowserUserAgent(sPlatform, sBrowser):
    sPlatform = sPlatform.lower()
    sBrowser = sBrowser.lower()
    lValidPlatorms = {"windows", "macintosh", "linux", "android", "ios"}
    lValidBrowsers = {"chrome", "firefox", "safari", "internet-explorer", "edge", "opera", "vivaldi", "yandex-browser"}
    
    if sPlatform not in lValidPlatorms or sBrowser not in lValidBrowsers:
        return False

    try:
        link = "https://www.whatismybrowser.com/guides/the-latest-user-agent/" + sBrowser
        f = urllib.urlopen(link)
        lWebContent = f.read()
    except:
        return False

    sRegEx1 = re.escape('<td><span class="code">')
    sRegEx2 = re.escape('</span></td>')
    sRegExTotal = r''+sRegEx1 + '(.*?)' + sRegEx2
    lLatestBrowserUserAgentFound = re.findall(sRegExTotal, lWebContent, re.IGNORECASE)
    for sLatestBrowserUserAgentFound  in lLatestBrowserUserAgentFound:
        if re.search(sPlatform, sLatestBrowserUserAgentFound, re.IGNORECASE):
            return sLatestBrowserUserAgentFound

sLatestBrowserUserAgentContent = getLatestBrowserUserAgent("macintosh", "safari")
print (sLatestBrowserUserAgentContent)