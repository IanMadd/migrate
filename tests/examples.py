import pytest
from inspec.support.examples import openExamples, mungeExamples

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
  startEnd = openExamples(inputString)
  output = mungeExamples(inputString, startEnd["start"], startEnd["end"])
  assert output == outputString
