import pytest
from migrate.munge.azureParameters import azureCommonParameters


inputText = '''
# azure_container_registries

Use the `azure_container_registries` InSpec audit resource to test properties and configuration of Azure Container Registries.

## Azure REST API version, endpoint and HTTP client parameters

This resource interacts with API versions supported by the resource provider.
The `api_version` can be defined as a resource parameter.
If not provided, the latest version will be used.
For more information, refer to [`azure_generic_resource`](azure_generic_resource.md).

Unless defined, this resource will use the `azure_cloud` global endpoint and default values for the HTTP client.
For more information, refer to the resource pack [README](../../README.md).

## Availability

### Installation
'''

outputText = '''
# azure_container_registries

Use the `azure_container_registries` InSpec audit resource to test properties and configuration of Azure Container Registries.

## Azure REST API Version, Endpoint, and HTTP Client Parameters

{{% inspec_azure_common_parameters %}}

## Availability

### Installation
'''

def testAzureParameters():
  assert azureCommonParameters(inputText) == outputText