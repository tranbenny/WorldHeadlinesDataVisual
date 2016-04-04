# figure out a regular expression to get rid of html tags
# figure out a regular expression to get rid of string encoded bytes

import re
import pickle

input = '\xe2\x80\x9d Erdogan says of the Diyanet Center of America.<br clear=\'all\'/><br/>hello'
input2 = 'the airport\xe2\x80\x99s chief executive said Saturday.<br clear=\'all\'/><br/><br/><a href="http://rc.feedsportal.com/r/247396742651/u/75/f/636708/c/34656/s/4eacdabd/sc/13/rc/1/rc.htm" rel="nofollow"><img src="http://rc.feedsportal.com/r/247396742651/u/75/f/636708/c/34656/s/4eacdabd/sc/13/rc/1/rc.img" border="0"/></a><br/><br/><a href="http://rc.feedsportal.com/r/247396742651/u/75/f/636708/c/34656/s/4eacdabd/sc/13/rc/2/rc.htm" rel="nofollow"><img src="http://rc.feedsportal.com/r/247396742651/u/75/f/636708/c/34656/s/4eacdabd/sc/13/rc/2/rc.img" border="0"/></a><br/><br/><a href="http://rc.feedsportal.com/r/247396742651/u/75/f/636708/c/34656/s/4eacdabd/sc/13/rc/3/rc.htm" rel="nofollow"><img src="http://rc.feedsportal.com/r/247396742651/u/75/f/636708/c/34656/s/4eacdabd/sc/13/rc/3/rc.img" border="0"/></a><br/><br/><a href="http://da.feedsportal.com/r/247396742651/u/75/f/636708/c/34656/s/4eacdabd/sc/13/a2.htm"><img src="http://da.feedsportal.com/r/247396742651/u/75/f/636708/c/34656/s/4eacdabd/sc/13/a2.img" border="0"/></a><br/><a href="http://adchoice.feedsportal.com/r/247396742651/u/75/f/636708/c/34656/s/4eacdabd/sc/13/ach.htm"><img src="http://adchoice.feedsportal.com/r/247396742651/u/75/f/636708/c/34656/s/4eacdabd/sc/13/ach.img" border="0"/></a><img width="1" height="1" src="http://pi.feedsportal.com/r/247396742651/u/75/f/636708/c/34656/s/4eacdabd/sc/13/a2t.img" border="0"/><img width="1" height="1" src="http://pi2.feedsportal.com/r/247396742651/u/75/f/636708/c/34656/s/4eacdabd/sc/13/a2t2.img" border="0"/><img width=\'1\' height=\'1\' src=\'http://feeds.washingtonpost.com/c/34656/f/636708/s/4eacdabd/sc/13/mf.gif\' border=\'0\'/>'
input3 = 'Tension is the diplomats\xe2\x80\x99 curse, which Russians cure by writing verse'


texts = pickle.load(open('encodedTexts.py', 'rb'))


# specifically, remove a, img, br tags
# if <p> or <ul>, <li> tags are still present, then remove the tags but keep the texts
def replaceInput(input):
    newInput = re.sub('<(br|a|img|p|span|time)([^>]*)>', '', input)
    newInput = re.sub('(</a>|</p>|<ul>|</ul>|<li>|</li>|</span>|</time>|<em>|</em>|<strong>|</strong>)', '', newInput)
    print("OLD")
    print(input)
    print("NEW")
    print(newInput)
    return newInput


results = []
for text in texts:
    results.append(replaceInput(text))



print("\n")
for result in results:
    if result.find('<') != -1:
        print("FAILED TEST")
        print(result)

