import time
from Modules.subsidiary import getElement
def pressButton(parameters, context, site_action):

    site_action.click_buttom(getElement(parameters[0], site_action))
    time.sleep(3)
    return True, context