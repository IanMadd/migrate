import re
from . import misc

def azureCommonParameters(text):
  regexHeading = r"^## Azure REST API version, endpoint and ((http)|(HTTP)) client parameters\n"
  substHeading = "## Azure REST API Version, Endpoint, and HTTP Client Parameters\\n"

  if re.search(regexHeading, text, re.M):
    text = re.sub(regexHeading, substHeading, text, 1, re.M)

    parametersHeading = misc.thisH2Match(text, "Azure REST API Version, Endpoint, and HTTP Client Parameters")
    nextHeading = misc.findNextH2(text, parametersHeading.end())

    text = text[:parametersHeading.end()] + "\n\n{{% inspec_azure_common_parameters %}}\n\n" + text[nextHeading['matchStart']:]

  return text
