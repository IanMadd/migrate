import pytest
from inspec.munge.misc import removeEmptySpaces

inputString = '''Use the `aws_iam_user` InSpec audit resource to test properties of a single AWS IAM User.
    
## Syntax

An `aws_iam_user` resource block declares the tests for a single AWS IAM User by user name.

    describe aws_iam_user(user_name: 'psmith') do
      it { should exist }
    end

  
One of either the EC2 instance's ID or name must be be provided.
    
'''

outputString = '''Use the `aws_iam_user` InSpec audit resource to test properties of a single AWS IAM User.

## Syntax

An `aws_iam_user` resource block declares the tests for a single AWS IAM User by user name.

    describe aws_iam_user(user_name: 'psmith') do
      it { should exist }
    end


One of either the EC2 instance's ID or name must be be provided.

'''

def testRemoveSpaces():
  assert removeEmptySpaces(inputString) == outputString