import pytest
from migrate.munge.properties import *
from migrate.munge.misc import mergeTextCorrectEmptyLines

inputText1 = '''
See also the [AWS documentation on Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference).

## Properties

|Property                    | Description|
| ---                        | --- |
|load_balancer_name        | The name of the load balancer. |
|load_balancer_addresses   | A collectionm of the load balancer addresses. |
|canonical_hosted_zone_id | The ID of the Amazon Route 53 hosted zone for the load balancer. |
|protocols                   | A list of the protocols configured for the listeners of the load balancer. |

## Examples

##### Test that an ALB has its availability zones configured correctly
    describe aws_alb('arn::alb') do
      its('zone_names.count')  { should be > 1 }
      its('zone_names')        { should include 'us-east-2a' }
      its('zone_names')        { should include 'us-east-2b' }
    end
'''

outputText1 = '''
See also the [AWS documentation on Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference).

## Properties

`load_balancer_name`
: The name of the load balancer.

`load_balancer_addresses`
: A collectionm of the load balancer addresses.

`canonical_hosted_zone_id`
: The ID of the Amazon Route 53 hosted zone for the load balancer.

`protocols`
: A list of the protocols configured for the listeners of the load balancer.

## Examples

##### Test that an ALB has its availability zones configured correctly
    describe aws_alb('arn::alb') do
      its('zone_names.count')  { should be > 1 }
      its('zone_names')        { should include 'us-east-2a' }
      its('zone_names')        { should include 'us-east-2b' }
    end
'''

def testProperties1():
  startEnd = openProperties(inputText1)
  output = mungeProperties(inputText1, startEnd['start'], startEnd['end'])
  # print(inputText1[startEnd['start']:startEnd['end']])
  definitionsText = mergeTextCorrectEmptyLines(inputText1[:startEnd['start']], output[0], inputText1[startEnd['end']:])
  # print("definitionText: " + definitionsText)
  # print("Errors: " + output[1])
  assert definitionsText == outputText1


inputText2 = '''See also the [AWS documentation on Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference).

## Properties

|Property            | Description |
| ---                | --- |
|ids                 | The ID of the internet gateway. The field name is `id`.|
|names               | The value of the `Name` tag. It is `nil` if not defined. The field name is `name`.|
|vpc\_ids            | The ID of the attached VPC. It is `nil` if the resource is in a `detached` state. The field name is `vpc_id`.|


## Examples

More text
'''

outputText2 = '''See also the [AWS documentation on Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference).

## Properties

`ids`
: The ID of the internet gateway.

: **Field**: `id`

`names`
: The value of the `Name` tag. It is `nil` if not defined.

: **Field**: `name`

`vpc\_ids`
: The ID of the attached VPC. It is `nil` if the resource is in a `detached` state.

: **Field**: `vpc_id`

## Examples

More text
'''

def testProperties2():
  startEnd = openProperties(inputText2)
  output = mungeProperties(inputText2, startEnd['start'], startEnd['end'])
  definitionsText = mergeTextCorrectEmptyLines(inputText2[:startEnd['start']], output[0], inputText2[startEnd['end']:])
  assert definitionsText == outputText2


inputText3 = '''#### Parameters

This resource does not expect any parameters.

## Properties
|Property                                       | Description|                                                       Field                                      |
| ---                                           | --- |                                                               ---                                         |
|option_group_names                             | The name RDS option group. |                                       option_group_name                           |
|option_group_description                       | The name of the database associated with each RDS cluster. |       option_group_description                     |

See also the [AWS documentation on RDS cluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-optiongroup.html).


For a comprehensive list of properties available to test on an RDS cluster see the [AWS Response Object](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/RDS/DBCluster.html).

## Examples

##### Test the engine used with an aws_rds_group_option
'''

outputText3 = '''#### Parameters

This resource does not expect any parameters.

## Properties

`option_group_names`
: The name RDS option group.

: **Field**: `option_group_name`

`option_group_description`
: The name of the database associated with each RDS cluster.

: **Field**: `option_group_description`

See also the [AWS documentation on RDS cluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-optiongroup.html).


For a comprehensive list of properties available to test on an RDS cluster see the [AWS Response Object](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/RDS/DBCluster.html).

## Examples

##### Test the engine used with an aws_rds_group_option
'''

def testProperties3():
  startEnd = openProperties(inputText3)
  output = mungeProperties(inputText3, startEnd['start'], startEnd['end'])
  definitionsText = mergeTextCorrectEmptyLines(inputText3[:startEnd['start']], output[0], inputText3[startEnd['end']:])
  assert definitionsText == outputText3