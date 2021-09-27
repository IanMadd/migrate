import re

def convertDictToDef(dict):
  definitionsMarkdown = ''

  for term in dict:

    for key, value in term.items():
      if key == "property":
        definitionsMarkdown += '`' + value + '`\n'
      elif key == "description":
        if not value.endswith('.'):
          value += '.'
        definitionsMarkdown += ": " + value + '\n'
      elif key == 'field':
        definitionsMarkdown += "\n: **Field**: " + value + '\n'

    definitionsMarkdown += "\n"

  definitionsMarkdown = "\n" + definitionsMarkdown
  return definitionsMarkdown

if __name__ == '__main__':
  dict1 = [{'property': 'bucket_name', 'description': 'The name of the bucket.'},
  {'property': 'key', 'description': 'The key within the bucket.'},
  {'property': 'content_length', 'description': 'Size of the body in bytes.'},
  ]

  print(convertDictToDef(dict1))