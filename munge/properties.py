import re
from . import misc
from . import tableToDict
from . import dictToDefinition

def mungeProperties(text, start, end):
    errorText = ''
    propertiesText = text[start: end]
    if tableToDict.tableExists(propertiesText):
        propertiesTableStartEnd = tableToDict.findTableInText(propertiesText)
        propertiesTable = propertiesText[propertiesTableStartEnd['start']: propertiesTableStartEnd['end']]
        if tableToDict.goodTable(propertiesTable):
            dictionaryOutput = tableToDict.convertTableToDict(propertiesTable)
            if dictionaryOutput[1] == '':
                definitions = dictToDefinition.convertDictToDef(dictionaryOutput[0])
                definitionsStartEnd = propertiesTableStartEnd
                propertiesText = propertiesText[:definitionsStartEnd['start']] + definitions + propertiesText[definitionsStartEnd['end']:]
            else:
                errorText += dictionaryOutput[1]
        else:
            errorText = 'Bad table ' + propertiesTable
    else:
        errorText = 'No table found: ' + text

    filterTableRegex = r"^<superscript>\*<\/superscript> For information on how to use filter criteria [\w| |\[|\]|\(|\)|\:|\/|\.|\-]+$"
    filterTableSubst = "{{% inspec_filter_table %}}"
    propertiesText = re.sub(filterTableRegex, filterTableSubst, propertiesText, 1, re.M)

    return propertiesText, errorText

