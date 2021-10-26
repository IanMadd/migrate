import pytest
from migrate.munge.misc import formatLinks

inputLinkText = """## Azure Permissions

Your [Service Principal](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal) must be setup with a `contributor` role on the subscription you wish to test.

more text
"""

outputLinkText = """## Azure Permissions

Your [Service Principal](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal) must be setup with a `contributor` role on the subscription you wish to test.

more text
"""


inputLinkText2 = """
For properties applicable to all resources, such as `type`, `name`, `id`, `properties`, refer to [`azure_generic_resource`](azure_generic_resource.md#properties).

Also, refer to [Azure documentation](https://docs.microsoft.com/en-us/rest/api/streamanalytics/) for other properties available.
Any attribute in the response may be accessed with the key names separated by dots (`.`), eg. `properties.<attribute>`.

"""


outputLinkText2 = """
For properties applicable to all resources, such as `type`, `name`, `id`, `properties`, refer to [`azure_generic_resource`]({{< relref "azure_generic_resource.md#properties" >}}).

Also, refer to [Azure documentation](https://docs.microsoft.com/en-us/rest/api/streamanalytics/) for other properties available.
Any attribute in the response may be accessed with the key names separated by dots (`.`), eg. `properties.<attribute>`.

"""

inputLinkText3 = """For more information, refer to [`azure_generic_resource`](azure_generic_resource.md).

Unless defined, `azure_cloud` global endpoint, and default values for the http client will be used.
For more information, refer to the resource pack [README](../../README.md). 

## Availability
"""

outputLinkText3 = """For more information, refer to [`azure_generic_resource`]({{< relref "azure_generic_resource.md" >}}).

Unless defined, `azure_cloud` global endpoint, and default values for the http client will be used.
For more information, refer to the resource pack [README](https://github.com/inspec/inspec-azure/blob/master/README.md). 

## Availability
"""

inputLinkText4 = '''### Installation

This resource is available in the [InSpec Azure resource pack](https://github.com/inspec/inspec-azure). 
For an example `inspec.yml` file and how to set up your Azure credentials, refer to resource pack [README](../../README.md#Service-Principal).

## Syntax
'''

outputLinkText4 = '''### Installation

This resource is available in the [InSpec Azure resource pack](https://github.com/inspec/inspec-azure). 
For an example `inspec.yml` file and how to set up your Azure credentials, refer to resource pack [README](https://github.com/inspec/inspec-azure/blob/master/README.md#Service-Principal).

## Syntax
'''



def testLink():
  repo = '../../inspec-azure'
  assert formatLinks(inputLinkText, repo) == outputLinkText

def testLinkTwo():
  repo = '../../inspec-azure'
  assert formatLinks(inputLinkText2, repo) == outputLinkText2

def testLinkThree():
  repo = '../../inspec-azure'
  assert formatLinks(inputLinkText3, repo) == outputLinkText3

def testLinkFour():
  repo = '../../inspec-azure'
  assert formatLinks(inputLinkText4, repo) == outputLinkText4

