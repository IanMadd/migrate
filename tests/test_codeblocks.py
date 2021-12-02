import pytest
from migrate.munge.misc import processCodeBlocks


codeblockOne = """This is a codeblock:

    describe aws_shield_subscription do

"""

codeblockOneOutput = """This is a codeblock:

```ruby
describe aws_shield_subscription do
```

"""

def test_codeBlocks():
  assert processCodeBlocks(codeblockOne) == codeblockOneOutput

codeblockTwo = """This is a codeblock:

    describe aws_ec2_dhcp_option(name: 'dopt-vpc-1') do
        it { should exist }
    end

"""

codeblockTwoOutput = """This is a codeblock:

```ruby
describe aws_ec2_dhcp_option(name: 'dopt-vpc-1') do
    it { should exist }
end
```

"""

def test_codeBlocksTwo():
  assert processCodeBlocks(codeblockTwo) == codeblockTwoOutput

codeBlockThree="""## Syntax

Ensure that an `aws_ec2_dhcp_option` exists

    describe aws_ec2_dhcp_option('dopt-0123456789abcdefg') do
      it { should exist }
    end

    describe aws_ec2_dhcp_option(dhcp_options_id: 'dopt-0123456789abcdefg') do
      it { should exist }
    end

    describe aws_ec2_dhcp_option(name: 'dopt-vpc-1') do
        it { should exist }
    end

#### Parameters
This resource accepts a one of the below mentioned parameters

"""

codeBlockThreeOutput = """## Syntax

Ensure that an `aws_ec2_dhcp_option` exists

```ruby
describe aws_ec2_dhcp_option('dopt-0123456789abcdefg') do
  it { should exist }
end
```

```ruby
describe aws_ec2_dhcp_option(dhcp_options_id: 'dopt-0123456789abcdefg') do
  it { should exist }
end
```

```ruby
describe aws_ec2_dhcp_option(name: 'dopt-vpc-1') do
    it { should exist }
end
```

#### Parameters
This resource accepts a one of the below mentioned parameters

"""

def test_codeBlocksThree():
  assert processCodeBlocks(codeBlockThree) == codeBlockThreeOutput

codeBlock4 = '''
some text

```ruby
  azure_active_directory_objects.values.each do |value|
    describe azure_active_directory_object(id: value)  do
      it { should exist }
      its('visibility') { should_not be_empty }
    end
  end

```

more text

'''

def test_codeBlocks4():
  assert processCodeBlocks(codeBlock4) == codeBlock4


codeBlock5="""

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

You can find detailed documentation at [Actions, Resources, and Condition Keys for AWS Config](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awsconfig.html).

"""

codeBlock5Output = """

#### exist

The control will pass if the describe returns at least one result.

Use `should_not` to test the entity should not exist.

```ruby
describe aws_config_delivery_channel('my_channel') do
  it { should exist }
end
```

```ruby
describe aws_config_delivery_channel('my-nonexistent-channel') do
  it { should_not exist }
end
```
## AWS Permissions

Your [Principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html#intro-structure-principal) will need the `ConfigService:Client:DescribeDeliveryChannelsResponse` action with Effect set to Allow.

You can find detailed documentation at [Actions, Resources, and Condition Keys for AWS Config](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awsconfig.html).

"""

def test_codeBlocks5():
  assert processCodeBlocks(codeBlock5) == codeBlock5Output


codeBlock6 = '''
### exist

The control will pass if the describe returns at least one result.

      it { should exist }

'''

codeBlock6Output = '''
### exist

The control will pass if the describe returns at least one result.

```ruby
it { should exist }
```

'''

def test_codeBlocks6():
  assert processCodeBlocks(codeBlock6) == codeBlock6Output

