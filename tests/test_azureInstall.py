import pytest
from migrate.munge.azureInstall import *


inputText = '''
For more information, refer to the resource pack [README](../../README.md). 

## Availability

### Installation

This resource is available in the [InSpec Azure resource pack](https://github.com/inspec/inspec-azure). 
For an example `inspec.yml` file and how to set up your Azure credentials, refer to resource pack [README](../../README.md#Service-Principal).

### Version

## NextHeading
'''

outputText = '''
For more information, refer to the resource pack [README](../../README.md). 

## Installation

This resource is available in the [InSpec Azure resource pack](https://github.com/inspec/inspec-azure). 
For an example `inspec.yml` file and how to set up your Azure credentials, refer to resource pack [README](../../README.md#Service-Principal).

### Version

## NextHeading
'''

finalOutputText = '''
For more information, refer to the resource pack [README](../../README.md). 

## Installation

{{% inspec_azure_install %}}

## NextHeading
'''

inputText2 = '''

Unless defined, `azure_cloud` global endpoint, and default values for the HTTP client will be used.
For more information, refer to the resource pack [README](../../README.md).
For api related info : [`Azure pipeline Docs`](https://docs.microsoft.com/en-us/rest/api/datafactory/pipelines/list-by-factory).
## Availability

### Installation

This resource is available in the [InSpec Azure resource pack](https://github.com/inspec/inspec-azure).
For an example `inspec.yml` file and how to set up your Azure credentials, refer to resource pack [README](../../README.md#Service-Principal).

'''

outputText2 = '''

Unless defined, `azure_cloud` global endpoint, and default values for the HTTP client will be used.
For more information, refer to the resource pack [README](../../README.md).
For api related info : [`Azure pipeline Docs`](https://docs.microsoft.com/en-us/rest/api/datafactory/pipelines/list-by-factory).
## Installation

This resource is available in the [InSpec Azure resource pack](https://github.com/inspec/inspec-azure).
For an example `inspec.yml` file and how to set up your Azure credentials, refer to resource pack [README](../../README.md#Service-Principal).

'''

def testAzureInstall():
  assert replaceInstallHeadings(inputText) == outputText

def testReplaceAzureText():
  text = replaceInstallHeadings(inputText)
  assert replaceInstallText(text) == finalOutputText
  
def testAzureInstall2():
  assert replaceInstallHeadings(inputText2) == outputText2