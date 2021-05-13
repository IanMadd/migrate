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