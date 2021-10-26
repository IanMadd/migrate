import re

from migrate.munge.misc import mergeTextCorrectEmptyLines

topString1 = '''sometext'''

middleString1 = '''


middle text


'''

bottomString1 = '''
bottom text'''

output1 = '''sometext

middle text

bottom text'''

def test_mergeTextCorrectEmptyLines1():
  assert mergeTextCorrectEmptyLines(topString1, middleString1, bottomString1) == output1