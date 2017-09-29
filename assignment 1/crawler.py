import urllib
test = urllib.urlopen("http://strathmore.edu/").read()
sane = 0
needlestack = []
while sane == 0:
  curpos = test.find("href")
  if curpos >= 0:
    testlen = len(test)
    test = test[curpos:testlen]
    curpos = test.find('"')
    testlen = len(test)
    test = test[curpos+1:testlen]
    curpos = test.find('"')
    needle = test[0:curpos]
    if needle.startswith("http" or "www"):
        needlestack.append(needle)
  else:
    sane = 1
for item in needlestack:
    print item