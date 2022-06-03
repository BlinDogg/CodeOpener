import time
def openLink(parameters, context, site_action):
    url = parameters[0]['url']
    site_action.go_to_URL(url)
    #print('System opens link ' + url)
    time.sleep(3)
    return True, context