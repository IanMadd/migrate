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

def testAzureInstall():
  assert replaceInstallHeadings(inputText) == outputText

def testReplaceAzureText():
  text = replaceInstallHeadings(inputText)
  assert replaceInstallText(text) == finalOutputText