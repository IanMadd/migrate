import pytest
from inspec.munge.properties import *
from inspec.munge.misc import mergeTextCorrectEmptyLines

inputText1 = '''
## Parameters

| Name           | Description                                                                      |
|----------------|----------------------------------------------------------------------------------|
| name           | Name of the Azure Migrate Project Database to test.                                   |
| resource_group | Azure resource group that the targeted resource resides in. `MyResourceGroup`    |
| project_name   | Azure Migrate Assessment Project.                                                |

The parameter set should be provided for a valid query:

- `resource_group` and `project_name` and `name`

## Properties

| Property                      | Description                                                      |
|-------------------------------|------------------------------------------------------------------|
| id                            | Path reference to the Migrate Project Database.                  |
| name                          | Unique name of a Migrate Project Database.                      |
| type                          | Type of the object. `Microsoft.Migrate/MigrateProjects/Databases`|
| properties                    | Properties of the assessment.                                    |
| properties.assessmentData     | Assessment details of the database published by various sources. |
| assessmentIds                 | The database assessment scope/Ids.                               |
| migrationBlockersCounts       | The number of blocking changes found.                            |
| breakingChangesCounts         | The number of breaking changes found.                            |
| assessmentTargetTypes         | The assessed target database types.                              |
| solutionNames                 | The names of the solutions that sent the data.                   |
| instanceIds                   | The database servers' instance Ids.                              |
| databaseNames                 | The name of the databases.                                       |

For properties applicable to all resources, such as `type`, `name`, `id`, and `properties`, refer to [`azure_generic_resource`](azure_generic_resource.md#properties).

Also, refer to [Azure documentation](https://docs.microsoft.com/en-us/rest/api/migrate/projects/databases/get-database) for other properties available. Any attribute in the response nested within properties is accessed with the key names separated by dots (`.`) and attributes nested in the assessmentData are pluralized and listed as a collection.

## Examples

### Test that Migrate Project Database has a SQL assessmentTargetType

```ruby
describe azure_migrate_project_database(resource_group: 'MIGRATED_VMS', project_name: 'ZONEA_MIGRATE_ASSESSMENT_PROJECT', name: 'SQL_DB') do
  its('assessmentTargetTypes') { should include 'SQL' }
end
'''

outputText1 = '''
## Parameters

| Name           | Description                                                                      |
|----------------|----------------------------------------------------------------------------------|
| name           | Name of the Azure Migrate Project Database to test.                                   |
| resource_group | Azure resource group that the targeted resource resides in. `MyResourceGroup`    |
| project_name   | Azure Migrate Assessment Project.                                                |

The parameter set should be provided for a valid query:

- `resource_group` and `project_name` and `name`

## Properties

`id`
: Path reference to the Migrate Project Database.

`name`
: Unique name of a Migrate Project Database.

`type`
: Type of the object. `Microsoft.Migrate/MigrateProjects/Databases`.

`properties`
: Properties of the assessment.

`properties.assessmentData`
: Assessment details of the database published by various sources.

`assessmentIds`
: The database assessment scope/Ids.

`migrationBlockersCounts`
: The number of blocking changes found.

`breakingChangesCounts`
: The number of breaking changes found.

`assessmentTargetTypes`
: The assessed target database types.

`solutionNames`
: The names of the solutions that sent the data.

`instanceIds`
: The database servers' instance Ids.

`databaseNames`
: The name of the databases.

For properties applicable to all resources, such as `type`, `name`, `id`, and `properties`, refer to [`azure_generic_resource`](azure_generic_resource.md#properties).

Also, refer to [Azure documentation](https://docs.microsoft.com/en-us/rest/api/migrate/projects/databases/get-database) for other properties available. Any attribute in the response nested within properties is accessed with the key names separated by dots (`.`) and attributes nested in the assessmentData are pluralized and listed as a collection.

## Examples

### Test that Migrate Project Database has a SQL assessmentTargetType

```ruby
describe azure_migrate_project_database(resource_group: 'MIGRATED_VMS', project_name: 'ZONEA_MIGRATE_ASSESSMENT_PROJECT', name: 'SQL_DB') do
  its('assessmentTargetTypes') { should include 'SQL' }
end
'''

def testProperties1():
  startEnd = openProperties(inputText1)
  output = mungeProperties(inputText1, startEnd['start'], startEnd['end'])
  definitionsText = mergeTextCorrectEmptyLines(inputText1[:startEnd['start']], output[0], inputText1[startEnd['end']:])
  assert definitionsText == outputText1


inputText2 = '''## Parameters

- `resource_group` (Optional)

## Properties

|Property       | Description                                                                          | Filter Criteria<superscript>*</superscript> |
|---------------|--------------------------------------------------------------------------------------|-----------------|
| ids           | A list of the unique resource ids.                                                   | `id`            |
| locations     | A list of locations for all the resources being interrogated.                        | `location`      |
| names         | A list of names of all the resources being interrogated.                             | `name`          |
| tags          | A list of `tag:value` pairs defined on the resources being interrogated.             | `tags`          |
| properties    | A list of properties for all the resources being interrogated.                       | `properties`    |

<superscript>*</superscript> For information on how to use filter criteria on plural resources refer to [FilterTable usage](https://github.com/inspec/inspec/blob/master/dev-docs/filtertable-usage.md).

## Examples

### Test that an Example Resource Group has the Named AKS Cluster
```ruby
describe azure_aks_clusters(resource_group: 'ExampleGroup') do
  its('names') { should include('ClusterName') }
end
```
'''

outputText2 = '''## Parameters

- `resource_group` (Optional)

## Properties

`ids`
: A list of the unique resource ids.

: **Field**: `id`

`locations`
: A list of locations for all the resources being interrogated.

: **Field**: `location`

`names`
: A list of names of all the resources being interrogated.

: **Field**: `name`

`tags`
: A list of `tag:value` pairs defined on the resources being interrogated.

: **Field**: `tags`

`properties`
: A list of properties for all the resources being interrogated.

: **Field**: `properties`

<superscript>*</superscript> For information on how to use filter criteria on plural resources refer to [FilterTable usage](https://github.com/inspec/inspec/blob/master/dev-docs/filtertable-usage.md).

## Examples

### Test that an Example Resource Group has the Named AKS Cluster
```ruby
describe azure_aks_clusters(resource_group: 'ExampleGroup') do
  its('names') { should include('ClusterName') }
end
```
'''

def testProperties2():
  startEnd = openProperties(inputText2)
  output = mungeProperties(inputText2, startEnd['start'], startEnd['end'])
  definitionsText = mergeTextCorrectEmptyLines(inputText2[:startEnd['start']], output[0], inputText2[startEnd['end']:])
  assert definitionsText == outputText2


inputText3 = '''Both the parameter sets needs be provided for a valid query:
- `resource_group` and `name`
## Properties

| Name                           | Description                                                                      |
|--------------------------------|----------------------------------------------------------------------------------|
| resource_group                 | Azure resource group that the targeted resource resides in. `MyResourceGroup`    |
| name                           | Name of the Azure resource to test. `MyDf`                                       |
| type                           | The resource type.                                                             |
| provisioning_state             | The Data Factory provisioning state.                                                   |
| repo_configuration_type        | The Git or VSTS repository configuration type. |

## Examples

### Test that a Data Factory exists

'''

outputText3 = '''Both the parameter sets needs be provided for a valid query:
- `resource_group` and `name`
## Properties

`resource_group`
: Azure resource group that the targeted resource resides in. `MyResourceGroup`.

`name`
: Name of the Azure resource to test. `MyDf`.

`type`
: The resource type.

`provisioning_state`
: The Data Factory provisioning state.

`repo_configuration_type`
: The Git or VSTS repository configuration type.

## Examples

### Test that a Data Factory exists

'''

def testProperties3():
  startEnd = openProperties(inputText3)
  output = mungeProperties(inputText3, startEnd['start'], startEnd['end'])
  print('Output: ' + output[0])
  print('Output: ' + '\n\n' + output[1])
  definitionsText = mergeTextCorrectEmptyLines(inputText3[:startEnd['start']], output[0], inputText3[startEnd['end']:])
  assert definitionsText == outputText3
