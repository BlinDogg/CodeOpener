import json
import pandas as pd
import SelPath
from Modules.Module_openLink import openLink
from Modules.Module_setFields import setFields
from Modules.Module_pressButton import pressButton
from Modules.Module_errorAndFinish import returnError, finish
from Modules.Module_agreeToTerms import agreeToTerms
from Modules.Module_clickAndSet import clickAndSetFields

with open('JSONS/dropbox_workflow.json', encoding='utf-8') as json_file:
    workflow = json.load(json_file)
user = pd.DataFrame(columns=['parameter', 'value'])
user.loc[0] = ['first name', 'Konstantin']
user.loc[1] = ['email', 'hui@mail.ru']
user.loc[2] = ['password', 'gfjJryT41f65']
user.loc[3] = ['news-checkbox', False]
user.loc[4] = ['age', '21']
user.loc[5] = ['employed', True]
user.loc[6] = ['sex', 'Male']
user.loc[7] = ['position', 'System Analyst']
user.loc[8] = ['hobby', 'piano']
user.loc[9] = ['married', False]
user.loc[10] = ['last name', 'Nikitin']
user.loc[11] = ['full_name', 'Konstantin Nikitin']
user.loc[12] = ['phone', '89035529619']
user.loc[13] = ['university', 'IRU']
user.loc[14] = ['patronymic', 'Eugenevich']

site_action = SelPath.Sel_Mod(workflow, user)


def findIndexByNumber(workflow, number):
    l = len(workflow['tasks'])
    for i in range(l):
        if (workflow['tasks'][i]['number'] == number):
            return i
    print('Absent task number')
    return 0


def runWorkflow(workflow):
    task_number = 1
    context = 0
    while (task_number != 0):
        task_index = findIndexByNumber(workflow, task_number)
        ifSuccess, context = runTask(workflow['tasks'][task_index], context)
        if (ifSuccess == True):
            task_number = workflow['tasks'][task_index]['on-success']
        else:
            task_number = workflow['tasks'][task_index]['on-error']
    return 0



def runTask(task, context):
    print('Running Task: ' + task['name'] + ' (' + str(task['number']) + ')')

    if (task['name'] == 'Open Link'):
        ifSuccess, context = openLink(task['parameters'], context, site_action)
    elif (task['name'] == 'Set Fields'):
        ifSuccess, context = setFields(task['parameters'], context, user, site_action)
    elif (task['name'] == 'Press Button'):
        ifSuccess, context = pressButton(task['parameters'], context, site_action)
    elif (task['name'] == 'Return Error'):
        ifSuccess, context = returnError(task['parameters'], context)
    elif (task['name'] == 'Finish'):
        ifSuccess, context = finish(task['parameters'], context)
    elif (task['name'] == "Agree to Terms"):
        ifSuccess, context = agreeToTerms(task['parameters'], context, site_action)
    elif (task['name'] == "Click and Set"):
        ifSuccess, context = clickAndSetFields(task['parameters'], context,user, site_action)
    else:
        print('WTF?')

    print()
    return ifSuccess, context




runWorkflow(workflow)