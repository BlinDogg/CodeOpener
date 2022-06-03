def returnError(parameters, context):
    print(parameters[0]['text'])
    return True, context


def finish(parameters, context):
    print(parameters[0]['text'])
    return True, context