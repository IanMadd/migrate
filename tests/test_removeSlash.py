import pytest
from migrate.munge.misc import removeSlash

inputString = '''# aws\_alb

Use the `aws_alb` InSpec audit resource to test properties of a single AWS Application Load Balancer (ALB).

## Syntax

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

## Properties

|Property                    | Description|
| ---                        | --- |
|load\_balancer\_name        | The name of the load balancer. |
|load\_balancer\_addresses   | A collectionm of the load balancer addresses. |
|canonical\_hosted\_zone\_id | The ID of the Amazon Route 53 hosted zone for the load balancer. |
|dns\_name                   | The DNS name of the load balancer. |
|availability\_zones         | The Availability Zones for the load balancer. |
|security\_groups            | The security groups for the load balancer. Valid only for load balancers in a VPC. |
|scheme                      | The type of load balancer. Valid only for load balancers in a VPC. |
|state                       | The state of the load balancer. |
|subnets                     | A collection of the subnet ids. |
|type                        | The type of the load balancer. |
|vpc\_id                     | The ID of the VPC for the load balancer. |
|zone\_names                 | A collection of the names of the availability zones. |
|listeners                   | A collection of the listeners for the load balancer. |
|ssl_policies                | A list of the SSL Policies configured for the listeners of the load balancer. |
|external_ports              | A list of the ports configured for the listeners of the load balancer. |
|protocols                   | A list of the protocols configured for the listeners of the load balancer. |
'''

outputString = '''# aws_alb

Use the `aws_alb` InSpec audit resource to test properties of a single AWS Application Load Balancer (ALB).

## Syntax

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

## Properties

|Property                    | Description|
| ---                        | --- |
|load_balancer_name        | The name of the load balancer. |
|load_balancer_addresses   | A collectionm of the load balancer addresses. |
|canonical_hosted_zone_id | The ID of the Amazon Route 53 hosted zone for the load balancer. |
|dns_name                   | The DNS name of the load balancer. |
|availability_zones         | The Availability Zones for the load balancer. |
|security_groups            | The security groups for the load balancer. Valid only for load balancers in a VPC. |
|scheme                      | The type of load balancer. Valid only for load balancers in a VPC. |
|state                       | The state of the load balancer. |
|subnets                     | A collection of the subnet ids. |
|type                        | The type of the load balancer. |
|vpc_id                     | The ID of the VPC for the load balancer. |
|zone_names                 | A collection of the names of the availability zones. |
|listeners                   | A collection of the listeners for the load balancer. |
|ssl_policies                | A list of the SSL Policies configured for the listeners of the load balancer. |
|external_ports              | A list of the ports configured for the listeners of the load balancer. |
|protocols                   | A list of the protocols configured for the listeners of the load balancer. |
'''

def testRemoveSlash():
  output = removeSlash(inputString)
  print(output)
  assert output == outputString
