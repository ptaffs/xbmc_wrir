import sys
import xbmcgui
import xbmcplugin
import urllib2, json

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')

url="http://files.wrir.org/cgi-bin/rightnow"
result=json.load(urllib2.urlopen(url))

print result['title'];
print result['poster'];

livestream = 'http://wrir.serverroom.us:7722/wrir'
li = xbmcgui.ListItem('Stream: ' + result['title'],
 iconImage='http://wrir.org/' + result['poster'])
xbmcplugin.addDirectoryItem(handle=addon_handle, url=livestream, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)
