import pytest
from inspec.support.misc import removeHeadingTitle


inputText = '''---
title: About the aws_rds_clusters Resource
platform: aws
---

# aws\_rds\_clusters

Use the `aws_rds_clusters` InSpec audit resource to test properties of a collection of AWS RDS clusters.

RDS gives you access to the capabilities of a MySQL, MariaDB, PostgreSQL, Microsoft SQL Server, Oracle, or Amazon Aurora database server.

## Syntax

 Ensure you have exactly 3 clusters

    describe aws_rds_clusters do
      its('db_cluster_identifiers.count') { should cmp 3 }
    end
    
#### Parameters

more text
'''

outputText = '''---
title: About the aws_rds_clusters Resource
platform: aws
---

Use the `aws_rds_clusters` InSpec audit resource to test properties of a collection of AWS RDS clusters.

RDS gives you access to the capabilities of a MySQL, MariaDB, PostgreSQL, Microsoft SQL Server, Oracle, or Amazon Aurora database server.

## Syntax

 Ensure you have exactly 3 clusters

    describe aws_rds_clusters do
      its('db_cluster_identifiers.count') { should cmp 3 }
    end
    
#### Parameters

more text
'''

def testRemoveTitle():
  assert removeHeadingTitle(inputText) == outputText

inputText2 = '''---
title: About the aws_sns_topics Resource
---

# aws\_sns\_topics
Use the `aws_sns_topics` InSpec audit resource to test all or a group of the SNS Topic ARNs in an account.

User the 'aws\_sns\_topic' InSpec audit resource to test a single SNS Topic in an account.

'''

outputText2 = '''---
title: About the aws_sns_topics Resource
---

Use the `aws_sns_topics` InSpec audit resource to test all or a group of the SNS Topic ARNs in an account.

User the 'aws\_sns\_topic' InSpec audit resource to test a single SNS Topic in an account.

'''

def testRemoveTitle2():
  assert removeHeadingTitle(inputText2) == outputText2