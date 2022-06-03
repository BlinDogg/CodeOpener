from Modules.subsidiary import getElement
def agreeToTerms(parameters, context, site_action):

    site_action.click_buttom(getElement(parameters[0], site_action))
    #print('Click on button ' + parameters[0]['name'] + ' and id = ' + parameters[0]['class'])

    return True, context