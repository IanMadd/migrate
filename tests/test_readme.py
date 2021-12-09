import re
import pytest
from migrate.munge.readme import readmeLinks


inputString1 = '''
|  |  |  | [aws_ssm_resource_compliance_summary](docs/resources/aws_ssm_resource_compliance_summary.md) | [aws_ssm_resource_compliance_summaries](docs/resources/aws_ssm_resource_compliance_summaries.md) |
| Amazon Timestream | Migration & Transfer | [AWS::Transfer::User](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html) | [aws_transfer_user](docs/resources/aws_transfer_user.md) | [aws_transfer_users](docs/resources/aws_transfer_users.md) |

- [azure_active_directory_domain_service](docs/resources/azure_active_directory_domain_service.md)
- [azure_active_directory_domain_services](docs/resources/azure_active_directory_domain_services.md)
- [azure_aks_cluster](docs/resources/azure_aks_cluster.md)
'''

outputString1 = '''
|  |  |  | [aws_ssm_resource_compliance_summary](https://docs.chef.io/inspec/resources/aws_ssm_resource_compliance_summary/) | [aws_ssm_resource_compliance_summaries](https://docs.chef.io/inspec/resources/aws_ssm_resource_compliance_summaries/) |
| Amazon Timestream | Migration & Transfer | [AWS::Transfer::User](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html) | [aws_transfer_user](https://docs.chef.io/inspec/resources/aws_transfer_user/) | [aws_transfer_users](https://docs.chef.io/inspec/resources/aws_transfer_users/) |

- [azure_active_directory_domain_service](https://docs.chef.io/inspec/resources/azure_active_directory_domain_service/)
- [azure_active_directory_domain_services](https://docs.chef.io/inspec/resources/azure_active_directory_domain_services/)
- [azure_aks_cluster](https://docs.chef.io/inspec/resources/azure_aks_cluster/)
'''

def testReadmeLinks():
    assert readmeLinks(inputString1) == outputString1
