import pytest
from migrate.munge.audit import *

filepath1 = "../forks/inspec-azure/docs/resources/azure_sentinel_incidents_resource.md"
page1 = "azure_sentinel_incidents_resource.md"
branch1 = "im/hugo"

output1 = '''

<div class="admonition-note">
<p class="admonition-note-title">Migration Links for Review</p>
<div class="admonition-note-text">
<p>Source page: <a href="https://github.com/inspec/inspec-azure/blob/main/docs/resources/azure_sentinel_incidents_resource.md">https://github.com/inspec/inspec-azure/blob/main/docs/resources/azure_sentinel_incidents_resource.md</a></p>
<p>Edited page: <a href="https://github.com/ianmadd/inspec-azure/blob/im/hugo/docs-chef-io/content/inspec/resources/azure_sentinel_incidents_resource.md">https://github.com/ianmadd/inspec-azure/blob/im/hugo/docs-chef-io/content/inspec/resources/azure_sentinel_incidents_resource.md</a></p>
</div>
</div>
'''

def testAuditText1():
    assert returnAuditText(filepath1, page1, branch1) == output1

filepath2 = "../inspec-azure/docs/resources/azure_sentinel_incidents_resource.md"
page2 = "azure_sentinel_incidents_resource.md"
branch2 = "hugo_migrate"

output2 = '''

<div class="admonition-note">
<p class="admonition-note-title">Migration Links for Review</p>
<div class="admonition-note-text">
<p>Source page: <a href="https://github.com/inspec/inspec-azure/blob/main/docs/resources/azure_sentinel_incidents_resource.md">https://github.com/inspec/inspec-azure/blob/main/docs/resources/azure_sentinel_incidents_resource.md</a></p>
<p>Edited page: <a href="https://github.com/inspec/inspec-azure/blob/hugo_migrate/docs-chef-io/content/inspec/resources/azure_sentinel_incidents_resource.md">https://github.com/inspec/inspec-azure/blob/hugo_migrate/docs-chef-io/content/inspec/resources/azure_sentinel_incidents_resource.md</a></p>
</div>
</div>
'''

def testAuditText2():
    assert returnAuditText(filepath2, page2, branch2) == output2


filepath3 = "../forks/inspec-aws/docs/resources/aws_sentinel_incidents_resource.md"
page3 = "aws_sentinel_incidents_resource.md"
branch3 = "blerg"

output3 = '''

<div class="admonition-note">
<p class="admonition-note-title">Migration Links for Review</p>
<div class="admonition-note-text">
<p>Source page: <a href="https://github.com/inspec/inspec-aws/blob/main/docs/resources/aws_sentinel_incidents_resource.md">https://github.com/inspec/inspec-aws/blob/main/docs/resources/aws_sentinel_incidents_resource.md</a></p>
<p>Edited page: <a href="https://github.com/ianmadd/inspec-aws/blob/blerg/docs-chef-io/content/inspec/resources/aws_sentinel_incidents_resource.md">https://github.com/ianmadd/inspec-aws/blob/blerg/docs-chef-io/content/inspec/resources/aws_sentinel_incidents_resource.md</a></p>
</div>
</div>
'''

def testAuditText3():
    assert returnAuditText(filepath3, page3, branch3) == output3

filepath4 = "../inspec-aws/docs/resources/aws_sentinel_incidents_resource.md"
page4 = "aws_sentinel_incidents_resource.md"
branch4 = "something_else"

output4 = '''

<div class="admonition-note">
<p class="admonition-note-title">Migration Links for Review</p>
<div class="admonition-note-text">
<p>Source page: <a href="https://github.com/inspec/inspec-aws/blob/main/docs/resources/aws_sentinel_incidents_resource.md">https://github.com/inspec/inspec-aws/blob/main/docs/resources/aws_sentinel_incidents_resource.md</a></p>
<p>Edited page: <a href="https://github.com/inspec/inspec-aws/blob/something_else/docs-chef-io/content/inspec/resources/aws_sentinel_incidents_resource.md">https://github.com/inspec/inspec-aws/blob/something_else/docs-chef-io/content/inspec/resources/aws_sentinel_incidents_resource.md</a></p>
</div>
</div>
'''

def testAuditText4():
    assert returnAuditText(filepath4, page4, branch4) == output4

