import os
import re
import yaml
import toml
from pathlib import Path
from support import syntax



directory = Path("../inspec-aws/docs/resources")
outputDirectory = Path("../inspec-aws/docs-chef-io/content/inspec/resources")



def examplesBlock(text):
  blockHeadingText = "Examples"

def propertiesBlock(text):
  blockHeadingText = "Properties"

def matchersBlock(text):
  blockHeadingText = "Matchers"

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
More text here.

See also the [AWS documentation on Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference).

"""

output = syntax.mungeSyntaxBlock(inputSyntaxBlock, 0, 617)
print(output["text"])