import pytest
from inspec.munge.syntax import mungeSyntaxBlock

inputSyntaxBlock = """
Ensure that an `aws_alb` exists

    describe aws_alb('arn:aws:elasticloadbalancing') do
      it { should exist }
    end

    describe aws_alb(load_balancer_arn: 'arn:aws:elasticloadbalancing') do
      it { should exist }
    end
    
#### Parameters

##### load_balancer_arn _(required)_

This resource accepts a single parameter, the ALB Arn which uniquely identifies the ALB. 
This can be passed either as a string or as a `load_balancer_arn: 'value'` key-value entry in a hash.

See also the [AWS documentation on Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference).

"""

outputSyntaxBlock = """
Ensure that an `aws_alb` exists

    describe aws_alb('arn:aws:elasticloadbalancing') do
      it { should exist }
    end

    describe aws_alb(load_balancer_arn: 'arn:aws:elasticloadbalancing') do
      it { should exist }
    end
    
where:

`load_balancer_arn` | `REQUIRED`

: This resource accepts a single parameter, the ALB Arn which uniquely identifies the ALB. 
  This can be passed either as a string or as a `load_balancer_arn: 'value'` key-value entry in a hash.

See also the [AWS documentation on Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference).

"""

def testMungeSyntaxBlock():
  assert mungeSyntaxBlock(inputSyntaxBlock, 0, 619) == outputSyntaxBlock

syntaxBlock2 = '''## Syntax

    describe aws_security_group('sg-12345678') do
      it { should exist }
    end

    # May also use hash syntax
    describe aws_security_group(group_id: 'sg-12345678') do
      it { should exist }
    end

    # Ensure you have a Security Group with a specific name.  Names are
    # unique within a VPC but not across VPCs.
    # Using only Group returns an error if multiple SGs match.
    describe aws_security_group(group_name: 'my-group') do
      it { should exist }
    end

    # Add vpc_id to ensure uniqueness.
    describe aws_security_group(group_name: 'my-group', vpc_id: 'vpc-12345678') do
      it { should exist }
    end

#### Parameters

You must provide at least one parameter; `group_id`, `group_name` or `vpc_id`

##### group_id _(required if no other parameter provided)_

The Security Group ID which uniquely identifies the SG.
This can be passed either as a string or as a `group_id: 'value'` key-value entry in a hash.

##### group_name _(required if no other parameter provided)_

The Security Group name.
This can be passed either as a string or as a `group_name: 'value'` key-value entry in a hash.

##### vpc_id _(required if no other parameter provided)_

The ID of the VPC associated with the SG.
This can be passed either as a string or as a `vpc_id: 'value'` key-value entry in a hash.

See also the [AWS documentation on Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html).
'''


syntaxBlock2Output = '''## Syntax

    describe aws_security_group('sg-12345678') do
      it { should exist }
    end

    # May also use hash syntax
    describe aws_security_group(group_id: 'sg-12345678') do
      it { should exist }
    end

    # Ensure you have a Security Group with a specific name.  Names are
    # unique within a VPC but not across VPCs.
    # Using only Group returns an error if multiple SGs match.
    describe aws_security_group(group_name: 'my-group') do
      it { should exist }
    end

    # Add vpc_id to ensure uniqueness.
    describe aws_security_group(group_name: 'my-group', vpc_id: 'vpc-12345678') do
      it { should exist }
    end

where:

You must provide at least one parameter; `group_id`, `group_name` or `vpc_id`

`group_id` _(required if no other parameter provided)_

: The Security Group ID which uniquely identifies the SG.
  This can be passed either as a string or as a `group_id: 'value'` key-value entry in a hash.

`group_name` _(required if no other parameter provided)_

: The Security Group name.
  This can be passed either as a string or as a `group_name: 'value'` key-value entry in a hash.

`vpc_id` _(required if no other parameter provided)_

: The ID of the VPC associated with the SG.
  This can be passed either as a string or as a `vpc_id: 'value'` key-value entry in a hash.

See also the [AWS documentation on Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html).
'''


def testAnotherSyntaxBlock():
  assert mungeSyntaxBlock(syntaxBlock2, 0, 1463) == syntaxBlock2Output
