import pytest
from migrate.munge.headings import spacesAroundHeadings, correctHeadingOrder


heading1 = '''
    its('s3_key_prefix')  { should eq 'logs/' }
    end

## Matchers
#### exist

The control will pass if the describe returns at least one result.

Use `should_not` to test the entity should not exist.

    describe aws_config_delivery_channel('my_channel') do
      it { should exist }
    end

    describe aws_config_delivery_channel('my-nonexistent-channel') do
      it { should_not exist }
    end
## AWS Permissions

Your [Principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html#intro-structure-principal) will need the `ConfigService:Client:DescribeDeliveryChannelsResponse` action with Effect set to Allow.

'''

output1 = '''
    its('s3_key_prefix')  { should eq 'logs/' }
    end

## Matchers

#### exist

The control will pass if the describe returns at least one result.

Use `should_not` to test the entity should not exist.

    describe aws_config_delivery_channel('my_channel') do
      it { should exist }
    end

    describe aws_config_delivery_channel('my-nonexistent-channel') do
      it { should_not exist }
    end

## AWS Permissions

Your [Principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html#intro-structure-principal) will need the `ConfigService:Client:DescribeDeliveryChannelsResponse` action with Effect set to Allow.

'''

def testHeading1():
    assert spacesAroundHeadings(heading1) == output1


heading2 = '''
    its('s3_key_prefix')  { should eq 'logs/' }
    end

## Matchers

##### exist

The control will pass if the describe returns at least one result.

Use `should_not` to test the entity should not exist.

    describe aws_config_delivery_channel('my_channel') do
      it { should exist }
    end

    describe aws_config_delivery_channel('my-nonexistent-channel') do
      it { should_not exist }
    end

### AWS Permissions

Pariatur ex esse et laborum laboris exercitation cillum enim nostrud reprehenderit. 
Minim in aliqua et id veniam tempor mollit ut id id. Dolor aliquip aliqua et nulla irure pariatur magna incididunt anim id. 
Elit labore cillum occaecat veniam aliqua nulla nisi incididunt exercitation magna nisi anim nisi quis.

### Some heading

Your [Principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html#intro-structure-principal) will need the `ConfigService:Client:DescribeDeliveryChannelsResponse` action with Effect set to Allow.

## new Heading

Pariatur ex esse et laborum laboris exercitation cillum enim nostrud reprehenderit. 
Minim in aliqua et id veniam tempor mollit ut id id. Dolor aliquip aliqua et nulla irure pariatur magna incididunt anim id. 
###### Another Heading

Pariatur ex esse et laborum laboris exercitation cillum enim nostrud reprehenderit. 
Minim in aliqua et id veniam tempor mollit ut id id. Dolor aliquip aliqua et nulla irure pariatur magna incididunt anim id. 

'''

output2 = '''
    its('s3_key_prefix')  { should eq 'logs/' }
    end

## Matchers

### exist

The control will pass if the describe returns at least one result.

Use `should_not` to test the entity should not exist.

    describe aws_config_delivery_channel('my_channel') do
      it { should exist }
    end

    describe aws_config_delivery_channel('my-nonexistent-channel') do
      it { should_not exist }
    end

## AWS Permissions

Pariatur ex esse et laborum laboris exercitation cillum enim nostrud reprehenderit. 
Minim in aliqua et id veniam tempor mollit ut id id. Dolor aliquip aliqua et nulla irure pariatur magna incididunt anim id. 
Elit labore cillum occaecat veniam aliqua nulla nisi incididunt exercitation magna nisi anim nisi quis.

### Some heading

Your [Principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html#intro-structure-principal) will need the `ConfigService:Client:DescribeDeliveryChannelsResponse` action with Effect set to Allow.

### new Heading

Pariatur ex esse et laborum laboris exercitation cillum enim nostrud reprehenderit. 
Minim in aliqua et id veniam tempor mollit ut id id. Dolor aliquip aliqua et nulla irure pariatur magna incididunt anim id. 
### Another Heading

Pariatur ex esse et laborum laboris exercitation cillum enim nostrud reprehenderit. 
Minim in aliqua et id veniam tempor mollit ut id id. Dolor aliquip aliqua et nulla irure pariatur magna incididunt anim id. 

'''


def testHeading2():
    assert correctHeadingOrder(heading2) == (output2, '')

heading3 = '''
Your [Principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html#intro-structure-principal) will need the `ConfigService:Client:DescribeDeliveryChannelsResponse` action with Effect set to Allow.

## Syntax

Pariatur ex esse et laborum laboris exercitation cillum enim nostrud reprehenderit. 
Minim in aliqua et id veniam tempor mollit ut id id. Dolor aliquip aliqua et nulla irure pariatur magna incididunt anim id. 

# Another Heading

Pariatur ex esse et laborum laboris exercitation cillum enim nostrud reprehenderit. 
Minim in aliqua et id veniam tempor mollit ut id id. Dolor aliquip aliqua et nulla irure pariatur magna incididunt anim id. 

'''

output3 = '''
Your [Principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html#intro-structure-principal) will need the `ConfigService:Client:DescribeDeliveryChannelsResponse` action with Effect set to Allow.

## Syntax

Pariatur ex esse et laborum laboris exercitation cillum enim nostrud reprehenderit. 
Minim in aliqua et id veniam tempor mollit ut id id. Dolor aliquip aliqua et nulla irure pariatur magna incididunt anim id. 

# Another Heading

Pariatur ex esse et laborum laboris exercitation cillum enim nostrud reprehenderit. 
Minim in aliqua et id veniam tempor mollit ut id id. Dolor aliquip aliqua et nulla irure pariatur magna incididunt anim id. 

'''


def testHeading3():
    assert correctHeadingOrder(heading3) == (output3, 'H1 heading found in wrong place on line 8')

heading4 = '''
Your [Principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html#intro-structure-principal) will need the `ConfigService:Client:DescribeDeliveryChannelsResponse` action with Effect set to Allow.

## Matchers

Pariatur ex esse et laborum laboris exercitation cillum enim nostrud reprehenderit. 
Minim in aliqua et id veniam tempor mollit ut id id. Dolor aliquip aliqua et nulla irure pariatur magna incididunt anim id. 

#### exists

```ruby
# If a virtual network is found it will exist
describe azure_virtual_network(resource_group: 'MyResourceGroup', name: 'MyVnetName') do
  it { should exist }
end
```

## Another Heading

Pariatur ex esse et laborum laboris exercitation cillum enim nostrud reprehenderit. 
Minim in aliqua et id veniam tempor mollit ut id id. Dolor aliquip aliqua et nulla irure pariatur magna incididunt anim id. 

'''

output4 = '''
Your [Principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html#intro-structure-principal) will need the `ConfigService:Client:DescribeDeliveryChannelsResponse` action with Effect set to Allow.

## Matchers

Pariatur ex esse et laborum laboris exercitation cillum enim nostrud reprehenderit. 
Minim in aliqua et id veniam tempor mollit ut id id. Dolor aliquip aliqua et nulla irure pariatur magna incididunt anim id. 

### exists

```ruby
# If a virtual network is found it will exist
describe azure_virtual_network(resource_group: 'MyResourceGroup', name: 'MyVnetName') do
  it { should exist }
end
```

### Another Heading

Pariatur ex esse et laborum laboris exercitation cillum enim nostrud reprehenderit. 
Minim in aliqua et id veniam tempor mollit ut id id. Dolor aliquip aliqua et nulla irure pariatur magna incididunt anim id. 

'''


def testHeading4():
    assert correctHeadingOrder(heading4) == (output4, '')

heading5 = '''

# aws_dynamodb_table

Use the `aws_dynamodb_table` InSpec audit resource to test properties of a single DynamoDb Table.

## Syntax

##### Ensure an DynamoDb Table exists.
    describe aws_dynamodb_table(table_name: 'table-name') do
      it { should exist }
    end
      
#### Parameters
##### table_name _(required)_

The table name used by this DynamoDb Table. This must be passed as a `table_name: 'value'` key-value entry in a hash.

## Parameters

##### table_name _(required)_

The table name used by this DynamoDb Table


## Syntax

##### Ensure an DynamoDb Table exists.
```ruby
describe aws_dynamodb_table(table_name: 'table-name') do
  it { should exist }
end
```

## Properties

|Property                     | Description|
'''

output5 = '''

# aws_dynamodb_table

Use the `aws_dynamodb_table` InSpec audit resource to test properties of a single DynamoDb Table.

## Syntax

### Ensure an DynamoDb Table exists.
    describe aws_dynamodb_table(table_name: 'table-name') do
      it { should exist }
    end
      
## Parameters
### table_name _(required)_

The table name used by this DynamoDb Table. This must be passed as a `table_name: 'value'` key-value entry in a hash.

## Parameters

### table_name _(required)_

The table name used by this DynamoDb Table


## Syntax

### Ensure an DynamoDb Table exists.
```ruby
describe aws_dynamodb_table(table_name: 'table-name') do
  it { should exist }
end
```

## Properties

|Property                     | Description|
'''


def testHeading5():
    assert correctHeadingOrder(heading5) == (output5, '')


heading6 = '''

# aws_dynamodb_table

Use the `aws_dynamodb_table` InSpec audit resource to test properties of a single DynamoDb Table.

## Syntax

##### Ensure an DynamoDb Table exists.
    describe aws_dynamodb_table(table_name: 'table-name') do
      it { should exist }
    end

#### Parameters
##### table_name _(required)_

The table name used by this DynamoDb Table. This must be passed as a `table_name: 'value'` key-value entry in a hash.

## Properties

|Property                     | Description|
| ---                         | --- |
'''
