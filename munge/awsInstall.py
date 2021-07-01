import re
from . import misc

def addAwsInstallText(text):
  awsInstallText = "## Installation\n\n{{% inspec_aws_install %}}\n\n"""
  syntaxHeading = misc.thisH2Match(text, "Syntax")

  text = text[:syntaxHeading.start()] + awsInstallText + text[syntaxHeading.start():]

  return text
