def getElement(element, site_action):
    if 'id' in [*element]:
        #print(site_action.get_element_by_id(element['id']))
        return site_action.get_element_by_id(element['id'])

    elif 'class' in [*element]:
        #print(site_action.get_element_by_class(element['class']))
        return site_action.get_element_by_class(element['class'])

    elif 'name' in [*element]:
        return site_action.get_element_by_name(element['name'])

    elif 'css' in [*element]:
        return site_action.get_element_by_css(element['css'])

    else:
        temp_var = [*element]
        if "parameter" in temp_var:
            temp_var.remove('parameter')
        xpath_type = temp_var[0]
        xpath_value = element[xpath_type]
        return site_action.get_element_by_xpath(xpath_type, xpath_value)