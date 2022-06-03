from Modules.subsidiary import getElement
def setFields(parameters, context, user, site_action):
    #print(parameters)
    for element in parameters:
        parameter_value = user[user['parameter'] == element['parameter']]['value'].values
        print('Set value ' + str(parameter_value))
        site_action.set_data(parameter_value, getElement(element, site_action))
    return True, context