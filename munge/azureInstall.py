import re
from . import misc

def replaceInstallHeadings(text):
  regexAvail = r"^## Availability\n\n"
  substAvail = ""

  regexInstall = r"^### Installation\n"
  substInstall = "## Installation\\n"

  text = re.sub(regexAvail, substAvail, text, 1, re.M)
  text = re.sub(regexInstall, substInstall, text, 1, re.M)

  return text

def replaceInstallText(text):
  installStart = misc.thisH2Match(text, "Installation")
  nextHeading = misc.findNextH2(text, installStart.end())

  substText = "\n\n{{% inspec_azure_install %}}\n\n"

  text = text[:installStart.end()] + substText + text[nextHeading['matchStart']:]
  return text