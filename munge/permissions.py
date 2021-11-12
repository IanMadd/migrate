import re
from . import misc


def openAzurePermissions(text):
    blockHeadingText = "Azure Permissions"
    propertiesHeadingMatch = misc.thisH2Match(text, blockHeadingText)
    if propertiesHeadingMatch:
        propertiesBlockStart = propertiesHeadingMatch.end(0)
        nextH2Dict = misc.findNextH2(text, propertiesBlockStart)
        propertiesBlockEnd = nextH2Dict["matchStart"]
    else:
        propertiesBlockStart = None
        propertiesBlockEnd = None

    return {'start': propertiesBlockStart, 'end': propertiesBlockEnd}

def openAwsPermissions(text):
    blockHeadingText = "AWS Permissions"
    propertiesHeadingMatch = misc.thisH2Match(text, blockHeadingText)
    if propertiesHeadingMatch:
        propertiesBlockStart = propertiesHeadingMatch.end(0)
        nextH2Dict = misc.findNextH2(text, propertiesBlockStart)
        propertiesBlockEnd = nextH2Dict["matchStart"]
    else:
        propertiesBlockStart = None
        propertiesBlockEnd = None

    return {'start': propertiesBlockStart, 'end': propertiesBlockEnd}

def azurePermissions(text):

    servicePrincipalString = 'Your [Service Principal](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal) must be setup with a `contributor` role on the subscription you wish to test.'

    permissionsTextList = text.splitlines(keepends=True)
    replaced = False

    for index,line in enumerate(permissionsTextList):
        if line.strip() == servicePrincipalString:
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
