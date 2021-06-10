import pytest
from inspec.munge.misc import findNextH2

inputString = """
some text

## Heading

more text

### Sub Heading

more text

## Other Heading

more text

### others sub heading
"""



def testfirstH2():
  result = findNextH2(inputString)
  assert result["matchStart"] == 12
  assert result["matchEnd"] == 23
  assert str(result["matchObject"]) == "<re.Match object; span=(12, 23), match='## Heading\\n'>"

def testNextH2():
  result = findNextH2(inputString, 22)
  assert result["matchStart"] == 63
  assert result["matchEnd"] == 80
  assert str(result["matchObject"]) == "<re.Match object; span=(41, 58), match='## Other Heading\\n'>"

def testFindEnd():
  result = findNextH2(inputString, 80)
  assert result["matchStart"] == len(inputString)
  assert result["matchEnd"] == len(inputString)
  assert result["matchObject"] == None
