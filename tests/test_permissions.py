import pytest
from migrate.munge.permissions import openAwsPermissions, openAzurePermissions, awsPermissions, azurePermissions

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
    startEnd = openAwsPermissions(awsStringInput1)
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

{{% azure_permissions_service_principal_contributor %}}

'''

def testAzurePermissions1():
    permissionsReplace = False
    startEnd = openAzurePermissions(azureStringInput1)
    permissionsText = azureStringInput1[startEnd['start']: startEnd['end']]
    permissionsOutput, permissionsReplace = azurePermissions(permissionsText)
    azureStringResult1 = azureStringInput1[:startEnd['start']] + permissionsOutput + azureStringInput1[startEnd['end']:]
    assert permissionsReplace == True
    assert azureStringResult1 == azureStringOutput1
