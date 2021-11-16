import re
from . import misc
from . import tableToDict
from . import dictToDefinition

def openProperties(text):
  blockHeadingText = "Properties"
  propertiesHeadingMatch = misc.thisH2Match(text, blockHeadingText)
  if propertiesHeadingMatch:
    propertiesBlockStart = propertiesHeadingMatch.end(0)
    nextH2Dict = misc.findNextH2(text, propertiesBlockStart)
    propertiesBlockEnd = nextH2Dict["matchStart"]
  else:
    propertiesBlockStart = None
    propertiesBlockEnd = None

  return {'start': propertiesBlockStart, 'end': propertiesBlockEnd}

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
        # print("Definitions in mungeProperties: " + definitions)
      else:
        errorText += dictionaryOutput[1]
    else:
      errorText = 'Bad table ' + propertiesTable
  else:
    errorText = 'No table found: ' + text

  return propertiesText, errorText

