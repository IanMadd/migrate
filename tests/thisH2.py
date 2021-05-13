import pytest
from inspec.support.misc import thisH2Match

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

def testMatch():
  result = thisH2Match(inputString, "Heading")
  assert str(result) == "<re.Match object; span=(12, 22), match='## Heading'>"

def testMatch2():
  result = thisH2Match(inputString, "Other Heading")
  assert str(result) == "<re.Match object; span=(63, 79), match='## Other Heading'>"
