import pytest
from inspec.munge.misc import fixFrontmatter

aws_frontmatter_input = """---
title: About the aws_ec2_dhcp_option Resource
platform: aws
---
"""

aws_frontmatter_output = """+++
title = "aws_ec2_dhcp_option Resource"
platform = "aws"
draft = false
gh_repo = "inspec-aws"

[menu.inspec]
title = "aws_ec2_dhcp_option"
identifier = "inspec/resources/aws/aws_ec2_dhcp_option Resource"
parent = "inspec/resources/aws"
+++
"""

def test_fixFrontmatter():
  assert fixFrontmatter(aws_frontmatter_input) == aws_frontmatter_output