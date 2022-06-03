from Modules.subsidiary import getElement
def clickAndSetFields(parameters, context, user, site_action):
    #print(parameters)
    for element in parameters:
        js_element = getElement(element, site_action)
        site_action.click_buttom(js_element)
        parameter_value = user[user['parameter'] == element['parameter']]['value'].values
        print('Set value ' + str(parameter_value))
        site_action.set_data(parameter_value, js_element)
    return True, context