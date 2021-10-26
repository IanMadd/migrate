import pytest
from migrate.munge.examples import openExamples, mungeExamples
from migrate.munge.misc import processCodeBlocks, removeEmptySpaces, removeSlash

inputString = """## Properties

|Property             | Description|
| ---                 | --- |
|tags                 | The list of tags that the EFS file system has. |
|names                | The value of the `Name` (case sensitive) tag if it is defined. |
|file\_system\_ids    | The ID of the EFS file system. |
|creation\_tokens     | The creation token that the EFS file system is associated. |
|owner\_ids           | The owner id of the EFS file system. |
|entries              | Provides access to the raw results of the query, which can be treated as an array of hashes. |
|creation\_times      | The creation time of the EFS file system|
|performance\_modes   | The performance mode of the EFS file system, e.g. 'maxIO'.|
|encryption\_status   | This indicates whether the EFS file system is encrypted or not.|
|throughput\_modes    | The throughput mode of the EFS file system.|
|kms\_key\_ids        | The ID of an AWS Key Management Service (AWS KMS) customer master key (CMK) that was used to protect the encrypted EFS file system. |
|size\_in\_bytes      | The latest known metered size (in bytes) of data stored in the file system, in its `value` field. |
|life\_cycle\_states  | The life cycle phase of the EFS file system, e.g. 'deleting'. |

## Examples

##### Ensure you have exactly 3 file systems
    describe aws_efs_file_systems do
      its("entries.count") { should cmp 3 }
    end

##### Use this InSpec resource to request the IDs of all EFS file systems, then test in-depth using `aws_efs_file_system`.
    aws_efs_file_systems.file_system_ids.each do |file_system_id|
      describe aws_efs_file_system(file_system_id) do
        its("tags") { should include("companyName" => "My Company Name") }
        it { should be_encrypted }
        its("throughput_mode") { should eq "bursting" }
        its("performance_mode") { should eq "generalPurpose" }
      end
    end

## Matchers

For a full list of available matchers, please visit our [Universal Matchers page](https://www.inspec.io/docs/reference/matchers/). 

#### exist
"""

outputString = """## Properties

|Property             | Description|
| ---                 | --- |
|tags                 | The list of tags that the EFS file system has. |
|names                | The value of the `Name` (case sensitive) tag if it is defined. |
|file_system_ids    | The ID of the EFS file system. |
|creation_tokens     | The creation token that the EFS file system is associated. |
|owner_ids           | The owner id of the EFS file system. |
|entries              | Provides access to the raw results of the query, which can be treated as an array of hashes. |
|creation_times      | The creation time of the EFS file system|
|performance_modes   | The performance mode of the EFS file system, e.g. 'maxIO'.|
|encryption_status   | This indicates whether the EFS file system is encrypted or not.|
|throughput_modes    | The throughput mode of the EFS file system.|
|kms_key_ids        | The ID of an AWS Key Management Service (AWS KMS) customer master key (CMK) that was used to protect the encrypted EFS file system. |
|size_in_bytes      | The latest known metered size (in bytes) of data stored in the file system, in its `value` field. |
|life_cycle_states  | The life cycle phase of the EFS file system, e.g. 'deleting'. |

## Examples

**Ensure you have exactly 3 file systems.**

```ruby
describe aws_efs_file_systems do
  its("entries.count") { should cmp 3 }
end
```

**Use this InSpec resource to request the IDs of all EFS file systems, then test in-depth using `aws_efs_file_system`.**

```ruby
aws_efs_file_systems.file_system_ids.each do |file_system_id|
  describe aws_efs_file_system(file_system_id) do
    its("tags") { should include("companyName" => "My Company Name") }
    it { should be_encrypted }
    its("throughput_mode") { should eq "bursting" }
    its("performance_mode") { should eq "generalPurpose" }
  end
end
```

## Matchers

For a full list of available matchers, please visit our [Universal Matchers page](https://www.inspec.io/docs/reference/matchers/). 

#### exist
"""

def testExamples():
  output = removeEmptySpaces(inputString)
  output = processCodeBlocks(output)
  output = removeSlash(output)
  startEnd = openExamples(output)
  output = mungeExamples(output, startEnd["start"], startEnd["end"])
  assert output == outputString

inputString2 = '''## Properties

|Property                     | Description|
| ---                         | --- |
|db\_instance\_identifiers    | The unique IDs of the RDS Instances returned. |
|entries                      | Provides access to the raw results of the query, which can be treated as an array of hashes. |
   
## Examples

##### Ensure a specific instance exists
    describe aws_rds_instances do
      its('db_instance_identifiers') { should include 'rds-12345678' }
    end

##### Use the InSpec resource to request the IDs of all RDS instances, then test in-depth using `aws_rds_instance` to ensure all instances are encrypted and have a sensible size.
    aws_rds_instances.db_instance_identifiers.each do |db_instance_identifier|
      describe aws_rds_instance(db_instance_identifier) do
        it { should be_encrypted }
      end
    end

## Matchers

For a full list of available matchers, please visit our [Universal Matchers page](https://www.inspec.io/docs/reference/matchers/). 

#### exist
'''

outputString2 = '''## Properties

|Property                     | Description|
| ---                         | --- |
|db_instance_identifiers    | The unique IDs of the RDS Instances returned. |
|entries                      | Provides access to the raw results of the query, which can be treated as an array of hashes. |

## Examples

**Ensure a specific instance exists.**

```ruby
describe aws_rds_instances do
  its('db_instance_identifiers') { should include 'rds-12345678' }
end
```

**Use the InSpec resource to request the IDs of all RDS instances, then test in-depth using `aws_rds_instance` to ensure all instances are encrypted and have a sensible size.**

```ruby
aws_rds_instances.db_instance_identifiers.each do |db_instance_identifier|
  describe aws_rds_instance(db_instance_identifier) do
    it { should be_encrypted }
  end
end
```

## Matchers

For a full list of available matchers, please visit our [Universal Matchers page](https://www.inspec.io/docs/reference/matchers/). 

#### exist
'''



def testExamples2():
  output = removeEmptySpaces(inputString2)
  output = processCodeBlocks(output)
  output = removeSlash(output)
  startEnd = openExamples(output)
  output = mungeExamples(output, startEnd["start"], startEnd["end"])
  assert output == outputString2


inputString3 = '''## Properties
|Property                                       | Description|                                                       Field                                      |
| ---                                           | --- |                                                               ---                                         | 
|option_group_names                             | The name RDS option group. |                                       option_group_name                           | 
|option_group_description                       | The name of the database associated with each RDS cluster. |       option_group_description                     | 
|engine_names                                   | The name of the engine associated with each RDS cluster. |         engine_name                                 | 
|major_engine_versions                          | The major engine version of a option group. |                      major_engine_version                        | 
|option_group_arns                              | The arn of a option group.|                                        option_group_arn                            | 
|vpc_ids                                        | The vpc id of  option group. |                                     vpc_id                                      | 
|allows_vpc_and_non_vpc_instance_memberships    | The storage allocated to each cluster. |                           allows_vpc_and_non_vpc_instance_memberships  | 
                                                                                                                                                                    
ee also the [AWS documentation on RDS cluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-optiongroup.html).


For a comprehensive list of properties available to test on an RDS cluster see the [AWS Response Object](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/RDS/DBCluster.html).

## Examples

##### Test the engine used with an aws_rds_group_option

    describe aws_rds_group_options do
      its('engine_name')         { should include 'mysql' }
      its('major_engine_version') { should include '5.6.37' }
    end

##### Ensure a specific cluster exists
    describe aws_rds_group_options do
      its('option_group_name') { should include 'option_group_name8-test }
    end

##### Use the InSpec resource to request the IDs of all RDS clusters, then test in-depth using `aws_rds_cluster` to ensure all clusters are encrypted and have a sensible size.
    aws_rds_group_options.option_group_name.each do |option_group_name|
        describe  aws_rds_group_option(option_group_name) do
          it { should exist }
      end
    end



## Matchers

This InSpec audit resource has the following special matchers. For a full list of available matchers, please visit our [matchers page](https://www.inspec.io/docs/reference/matchers/).

#### exist
'''

outputString3 = '''## Properties
|Property                                       | Description|                                                       Field                                      |
| ---                                           | --- |                                                               ---                                         | 
|option_group_names                             | The name RDS option group. |                                       option_group_name                           | 
|option_group_description                       | The name of the database associated with each RDS cluster. |       option_group_description                     | 
|engine_names                                   | The name of the engine associated with each RDS cluster. |         engine_name                                 | 
|major_engine_versions                          | The major engine version of a option group. |                      major_engine_version                        | 
|option_group_arns                              | The arn of a option group.|                                        option_group_arn                            | 
|vpc_ids                                        | The vpc id of  option group. |                                     vpc_id                                      | 
|allows_vpc_and_non_vpc_instance_memberships    | The storage allocated to each cluster. |                           allows_vpc_and_non_vpc_instance_memberships  | 

ee also the [AWS documentation on RDS cluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-optiongroup.html).


For a comprehensive list of properties available to test on an RDS cluster see the [AWS Response Object](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/RDS/DBCluster.html).

## Examples

**Test the engine used with an aws_rds_group_option.**

```ruby
describe aws_rds_group_options do
  its('engine_name')         { should include 'mysql' }
  its('major_engine_version') { should include '5.6.37' }
end
```

**Ensure a specific cluster exists.**

```ruby
describe aws_rds_group_options do
  its('option_group_name') { should include 'option_group_name8-test }
end
```

**Use the InSpec resource to request the IDs of all RDS clusters, then test in-depth using `aws_rds_cluster` to ensure all clusters are encrypted and have a sensible size.**

```ruby
aws_rds_group_options.option_group_name.each do |option_group_name|
    describe  aws_rds_group_option(option_group_name) do
      it { should exist }
  end
end
```



## Matchers

This InSpec audit resource has the following special matchers. For a full list of available matchers, please visit our [matchers page](https://www.inspec.io/docs/reference/matchers/).

#### exist
'''


def testExamples3():
  output = removeEmptySpaces(inputString3)
  output = removeSlash(output)
  output = processCodeBlocks(output)
  startEnd = openExamples(output)
  output = mungeExamples(output, startEnd["start"], startEnd["end"])
  assert output == outputString3