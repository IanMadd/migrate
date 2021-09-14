import re
from . import misc

def azureCommonParameters(text):
  regexHeading = r"^## Azure REST API [v|V]ersion, [e|E]ndpoint,{0,1} and ((http)|(HTTP)) [c|C]lient [p|P]arameters\n"
  substHeading = "## Azure REST API Version, Endpoint, and HTTP Client Parameters\\n"

  if re.search(regexHeading, text, re.M):
    text = re.sub(regexHeading, substHeading, text, 1, re.M)

    parametersHeading = misc.thisH2Match(text, "Azure REST API Version, Endpoint, and HTTP Client Parameters")
    nextHeading = misc.findNextH2(text, parametersHeading.end())

    text = text[:parametersHeading.end()] + "\n\n{{% inspec_azure_common_parameters %}}\n\n" + text[nextHeading['matchStart']:]

  return text
