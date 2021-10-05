import re

def tableExists(text):
  tableStartRegex = r'^ {0,}\|'
  return re.search(tableStartRegex, text, re.M)

def findTableInText(text):
  tableStartRegex = r'^ {0,}\|'
  tableEndRegex = r"\|\n$ {0,}\n"
  tableEndRegex2 = r"\| {0,}$"
  tableEndRegex3 = r"\n {0,}\n"
  tableStartMatch = re.search(tableStartRegex, text, re.M)
  tableEndMatch = re.search(tableEndRegex, text[tableStartMatch.end():], re.M)
  if tableEndMatch is None:
    for tableEndMatch in re.finditer(tableEndRegex2, text[tableStartMatch.end():]):
      pass

  if tableEndMatch is None:
    tableEndMatch = re.search(tableEndRegex3, text[tableStartMatch.end():], re.M)

  tableEnd = tableStartMatch.end() + tableEndMatch.start() + 1

  return {"start": tableStartMatch.start(), "end": tableEnd}

def goodTable(table):
  tableIsGood = True
  tableLines = table.splitlines()
  columnsNumber = len(re.findall(r"\|", tableLines[0]))

  for line in tableLines:
    if len(re.findall(r"\|", line)) != columnsNumber:
      tableIsGood = False

  return tableIsGood


def convertTableToDict(text):
  errorText = ''
  field = ''
  dictList = []
  tableColumnsLineRegex = r"^ {0,}\| {0,1}-{0,} {0,}\| {0,1}-{0,} {0,}\|"
  fieldNameIsRegex = r"The field name is (`\w+`)\.{0,1}"
  lines = text.splitlines()

  ## First convert the headings to a list of keys
  ## and remove empty list items
  keys = lines[0].split('|')
  keys = [key.replace(' ', '').lower() for key in keys]
  while('' in keys):
    keys.remove('')

  # The field column gets called different things, so standardize it to just "field"
  possibleFieldValues = ['Filter Criteria', 'field']
  if len(keys) == 3:
    if possibleFieldValues[0] or possibleFieldValues[1] in keys[2]:
      keys[2] = 'field'

  if keys[0] == 'properties' or keys[0] == 'name':
    keys[0] = 'property'

  if keys[0] != 'property' or keys[1] != 'description':
    errorText = 'Error. Incorrectly formatted table. Wrong headings: ' + text

  if not re.search(tableColumnsLineRegex, lines[1]):
    errorText = 'Error. Incorrectly formatted table: ' + text

  dictList = []
  if errorText == '':

    for line in lines[2:]:

      if line.count('|') > len(keys) + 1:
        errorText = 'Error. Incorrectly formatted table: ' + text
      elif line.count('|') == len(keys):
        errorText = 'Error. Incorrectly formatted table: ' + text

      else:
        lineList = line.split('|')
        lineList = [line.strip() for line in lineList]
        while('' in lineList):
          lineList.remove('')

        dict = {}
        for index,key in enumerate(keys):
          if key == "description" and 'The field name is' in lineList[index]:
            field = ''
            fieldNameMatch = re.search(fieldNameIsRegex, lineList[index])
            lineList[index] = re.sub(fieldNameIsRegex, '', lineList[index])
            lineList[index].strip()
            field = fieldNameMatch.group(1)

          if key == 'field':
            notApplicable = ['Not Applicable', 'NA', 'N/A', '']
            if not lineList[index].startswith('`') and lineList[index] not in notApplicable:
              lineList[index] = '`' + lineList[index]
            if not lineList[index].endswith('`') and lineList[index] not in notApplicable:
              lineList[index] = lineList[index] + '`'

          dict[key] = lineList[index].strip()


        if field != '':
          dict['field'] = field

        dictList.append(dict)

  if errorText != '':
    dictList = ''

  return dictList, errorText
