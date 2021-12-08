import re
from . import misc


def azurePermissions(text):

    servicePrincipalString1 = 'Your [Service Principal](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal) must be setup with a `contributor` role on the subscription you wish to test.'
    servicePrincipalString2 = 'Your [Service Principal](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal) must be set up with a `contributor` role on the subscription you wish to test.'

    permissionsTextList = text.splitlines(keepends=True)
    replaced = False

    for index,line in enumerate(permissionsTextList):
        if line.strip() == servicePrincipalString1 or line.strip() == servicePrincipalString2:
            replaced = True
            permissionsTextList[index] = "{{% azure_permissions_service_principal_contributor %}}\n"

    if replaced:
        text = ''.join(permissionsTextList)

    return text, replaced

def awsPermissions(text):

    awsActionRegex = r"will need the `([\w|:]+)` action"
    principalStartText = 'Your [Principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html#intro-structure-principal)'
    permissionsTextList = text.splitlines(keepends=True)
    replaced = False

    for index,line in enumerate(permissionsTextList):
        if line.strip().startswith(principalStartText):
            if (actionMatch := re.search(awsActionRegex, line)) is not None:
                shortcodeText = '{{% aws_permissions_principal action="' + actionMatch.group(1) + '" %}}\n'
                permissionsTextList[index] = shortcodeText
                replaced = True

    if replaced:
        text = ''.join(permissionsTextList)

    return text, replaced
