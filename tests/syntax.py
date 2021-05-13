import pytest
from inspec.support.misc import mungeSyntaxBlock

inputSyntaxBlock = """
Ensure that an `aws_alb` exists

    describe aws_alb('arn:aws:elasticloadbalancing') do
      it { should exist }
    end

    describe aws_alb(load_balancer_arn: 'arn:aws:elasticloadbalancing') do
      it { should exist }
    end
    
#### Parameters

##### load\_balancer\_arn _(required)_

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

`load\_balancer\_arn` | `REQUIRED`

: This resource accepts a single parameter, the ALB Arn which uniquely identifies the ALB. 
  This can be passed either as a string or as a `load_balancer_arn: 'value'` key-value entry in a hash.

: See also the [AWS documentation on Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference).

"""





def testMungeSyntaxBlock():
  assert mungeSyntaxBlock(inputSyntaxBlock, 0, 619) == {"text": outputSyntaxBlock, "start": 0, "end": 619}

output = mungeSyntaxBlock(inputSyntaxBlock, 0, 619)
print(output["text"])

print(outputSyntaxBlock)