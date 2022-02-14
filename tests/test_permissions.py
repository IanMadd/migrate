import pytest
from migrate.munge.permissions import awsPermissions, azurePermissions
from migrate.munge.misc import openBlock

awsStringInput1 = '''
Use `should` to check if the entity is available.

    describe aws_sns_subscriptions do
      it { should be_available }
    end

## AWS Permissions

Your [Principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html#intro-structure-principal) will need the `SNS:Client:ListSubscriptionsResponse` action with `Effect` set to `Allow`.
'''

awsStringOutput1 = '''
Use `should` to check if the entity is available.

    describe aws_sns_subscriptions do
      it { should be_available }
    end

## AWS Permissions

{{% aws_permissions_principal action="SNS:Client:ListSubscriptionsResponse" %}}
'''

def testAwsPermissions1():
    permissionsReplace = False
    startEnd = openBlock(awsStringInput1, "AWS Permissions")
    permissionsText = awsStringInput1[startEnd['start']: startEnd['end']]
    permissionsOutput, permissionsReplace = awsPermissions(permissionsText)
    awsStringResult1 = awsStringInput1[:startEnd['start']] + permissionsOutput + awsStringInput1[startEnd['end']:]
    assert permissionsReplace == True
    assert awsStringResult1 == awsStringOutput1

azureStringInput1 = '''
# If we expect 'ClusterName' to never exist
describe azure_aks_cluster(resource_group: 'example', name: 'ClusterName') do
  it { should_not exist }
end
```
## Azure Permissions

Your [Service Principal](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal) must be setup with a `contributor` role on the subscription you wish to test.

'''

azureStringOutput1 = '''
# If we expect 'ClusterName' to never exist
describe azure_aks_cluster(resource_group: 'example', name: 'ClusterName') do
  it { should_not exist }
end
```
## Azure Permissions

{{% azure_permissions_service_principal role="contributor" %}}

'''

def testAzurePermissions1():
    permissionsReplace = False
    startEnd = openBlock(azureStringInput1, "Azure Permissions")
    permissionsText = azureStringInput1[startEnd['start']: startEnd['end']]
    permissionsOutput, permissionsReplace = azurePermissions(permissionsText)
    azureStringResult1 = azureStringInput1[:startEnd['start']] + permissionsOutput + azureStringInput1[startEnd['end']:]
    assert permissionsReplace == True
    assert azureStringResult1 == azureStringOutput1


azureStringInput2 = '''# If we expect 'EmptyExampleGroup' Resource Group to not have Network Security Groups
describe azure_network_security_groups(resource_group: 'EmptyExampleGroup') do
  it { should_not exist }
end
```
## Azure Permissions

Your [Service Principal](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal) must be setup with a minimum of `reader` role on the subscription you wish to test.
'''

azureStringOutput2 = '''# If we expect 'EmptyExampleGroup' Resource Group to not have Network Security Groups
describe azure_network_security_groups(resource_group: 'EmptyExampleGroup') do
  it { should_not exist }
end
```
## Azure Permissions

{{% azure_permissions_service_principal role="reader" %}}
'''

def testAzurePermissions2():
    permissionsReplace = False
    startEnd = openBlock(azureStringInput2, "Azure Permissions")
    permissionsText = azureStringInput2[startEnd['start']: startEnd['end']]
    permissionsOutput, permissionsReplace = azurePermissions(permissionsText)
    print(permissionsOutput)
    azureStringResult2 = azureStringInput2[:startEnd['start']] + permissionsOutput + azureStringInput2[startEnd['end']:]
    assert permissionsReplace == True
    assert azureStringResult2 == azureStringOutput2


azureStringInput3 = '''### exists

```ruby
# If the Azure Power BI gateway is found, it will exist
describe azure_power_bi_gateway(gateway_id: 'GATEWAY_ID')  do
  it { should exist }
end
# if the Azure Power BI gateway is not found, it will not exist
describe azure_power_bi_gateway(gateway_id: 'GATEWAY_ID')  do
  it { should_not exist }
end
```

## Azure Permissions

Your [Service Principal](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal) must be set up with a `Dataset.Read.All` role on the Azure Power BI Workspace you wish to test.
'''


def testAzurePermissions3():
    permissionsReplace = False
    startEnd = openBlock(azureStringInput3, "Azure Permissions")
    permissionsText = azureStringInput3[startEnd['start']: startEnd['end']]
    permissionsOutput, permissionsReplace = azurePermissions(permissionsText)
    azureStringResult3 = azureStringInput3[:startEnd['start']] + permissionsOutput + azureStringInput3[startEnd['end']:]
    assert permissionsReplace == False
    assert azureStringResult3 == azureStringInput3
