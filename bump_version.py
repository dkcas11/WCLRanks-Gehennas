#!/usr/bin/python3

import os
import datetime
from subprocess                         import getoutput

print("Bumping")

version = ""
date_version = datetime.date.today().strftime("%Y%m%d")

os.rename("WCLRanks-Gehennas.toc", "WCLRanks-Gehennas.toc.old")
toc = open("WCLRanks-Gehennas.toc", "w+")

with open("WCLRanks-Gehennas.toc.old") as fp:
    line = fp.readline()
    while line:
        if "## Version: " in line:
            version_list = line.replace("## Version: ", "").split(".")
            version_list.pop()
            version_list.append(date_version)
            version = ".".join(version_list)
            line = "## Version: " + version
        toc.write(line)
        line = fp.readline()
toc.close()

print("Version:", version)

ret = getoutput("git add Data/")
print(ret)
ret = getoutput("git commit -m \"Daily update: %s\"" % date_version)
print(ret)
ret = getoutput("git tag WCLRanks-Gehennas-%s" % version)
print(ret)
ret = getoutput("git push origin main --tags")
print(ret)