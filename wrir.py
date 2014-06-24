import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'audio')

url = 'http://wrir.serverroom.us:7722/wrir'
li = xbmcgui.ListItem('Listen Live', iconImage='http://wrir.org/assets/img/logo.gif')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)
