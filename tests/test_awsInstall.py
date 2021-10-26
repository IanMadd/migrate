import pytest
from migrate.munge.awsInstall import *

inputText = """
# aws\_cloudformation\_stack

Use the `aws_cloudformation_stack ` InSpec audit resource to test properties of a single AWS Cloud Formation Stack.

## Syntax

Ensure that an `aws_cloudformation_stack` exists

    describe aws_cloudformation_stack('stack-name') do
      it { should exist }
    end

    describe aws_cloudformation_stack(stack_name: 'stack-name') do
      it { should exist }
    end
    

"""

outputText = """
# aws\_cloudformation\_stack

Use the `aws_cloudformation_stack ` InSpec audit resource to test properties of a single AWS Cloud Formation Stack.

## Installation

{{% inspec_aws_install %}}

## Syntax

Ensure that an `aws_cloudformation_stack` exists

    describe aws_cloudformation_stack('stack-name') do
      it { should exist }
    end

    describe aws_cloudformation_stack(stack_name: 'stack-name') do
      it { should exist }
    end
    

"""

def testAwsInstallText():
  assert addAwsInstallText(inputText) == outputText