import re

def tableExists(text):
  tableStartRegex = r'^ {0,}\|'
  return re.search(tableStartRegex, text, re.M)

def findTableInText(text):
  tableStartRegex = r'^ {0,}\|'
  tableEndRegex = r"\|\n$ {0,}\n"
  tableStartMatch = re.search(tableStartRegex, text, re.M)
  tableEndMatch = re.search(tableEndRegex, text[tableStartMatch.end():], re.M)
  tableEnd = tableStartMatch.end() + tableEndMatch.start() + 1

  return tableStartMatch.start(), tableEnd

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
  dictList = []
  tableColumnsLineRegex = r"^ {0,}\| {0,1}-{0,} {0,}\| {0,1}-{0,} {0,}\|"
  lines = text.splitlines()

  ## First convert the headings to a list of keys
  ## and remove empty list items
  keys = lines[0].split('|')
  keys = [key.replace(' ', '').lower() for key in keys]
  while('' in keys):
    keys.remove('')

  # The field column gets called different things, so standardize it to just "field"
  if len(keys) == 3 and "field" in keys[2]:
    keys[2] = 'field'

  if keys[0] == 'properties':
    keys[0] = 'property'

  if keys[0] != 'property' or keys[1] != 'description':
    errorText = 'Error. Incorrectly formatted table: ' + text

  # for key in keys:
  #   print(key)

  if not re.search(tableColumnsLineRegex, lines[1]):
    errorText = 'Error. Incorrectly formatted table: ' + text

  dictList = []
  if errorText == '':

    for line in lines[2:]:
      # print(line)
      # print(len(keys))
      # print(line.count('|'))

      if line.count('|') > len(keys) + 1:
        errorText = 'Error. Incorrectly formatted table: ' + text
      elif line.count('|') == len(keys):
        errorText = 'Error. Incorrectly formatted table: ' + text

      else:
        lineList = line.split('|')
        lineList = [line.strip() for line in lineList]
        while('' in lineList):
          lineList.remove('')
        # print(lineList)

        dict = {}
        for index,key in enumerate(keys):
          dict[key] = lineList[index]

        dictList.append(dict)

  # print(dictList)
  if errorText != '':
    dictList = ''

  return dictList, errorText

if __name__ == "__main__":

  inputTable1='''|Property                                    | Description                                       |   Field           |
| ----------------------------               | ---------------------------------                 |   ---             |
| route_table_ids                          | The route table IDs                               | |
| vpc_ids                                   | The VPC IDs                                        `vpc_id`          |
| entries                                    | Provides access to the raw results of the query, which can be treated as an array of hashes. | Not Applicable | '''

  print(goodTable(inputTable1))
