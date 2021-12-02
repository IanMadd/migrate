import pytest
from migrate.munge.parameters import *
from migrate.munge.misc import openBlock

inputText1= '''

# aws_cloudfront_distribution

Use the `aws_cloudfront_distribution` InSpec audit resource to test the properties of a single AWS CloudFront distribution.

## Syntax

Ensure that an `aws_cloudfront_distribution` exists:

    describe aws_cloudfront_distribution('DISTRIBUTION') do
      it { should exist }
    end

    describe aws_cloudfront_distribution(distribution_id: 'DISTRIBUTION') do
      it { should exist }
    end

## Parameters

### distribution_id _(required)_

The CloudFront distribution ID, which can be passed either as a string or as a `name: 'value'` key-value entry in a hash.

### disallowed_ssl_protocols _(optional)_

If provided, this parameter is expected to be an array of strings identifying SSL/TLS protocols that you wish not to allow.

Included in the array should be the union of disallowed identifiers for:

- custom origin SSL/TLS protocols (currently SSLv3 | TLSv1 | TLSv1.1 | TLSv1.2)
- identifiers for the minimum SSL/TLS protocol in the Viewer Certificate that CloudFront can use to communicate with viewers (currently SSLv3 | TLSv1 | TLSv1_1026 | TLSv1.1_2016 | TLSv1.2_2018 | TLSv1.2_2019 | TLSv1.2_2021).

Newer protocol identification strings (when available) may be provided in the set, as validity is not checked. The default value for disallowed_ssl_protocols is `%w{SSLv3 TLSv1 TLSv1_2016}`.

For additional information, see the [AWS API reference for CloudFront distributions](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_distribution.html) documentation. For available SSL/TLS version identifiers, see [OriginSslProtocols](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_OriginSslProtocols.html) and [AWS::CloudFront::distribution ViewerCertificate](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html) documentation.

### origin_domain_name _(optional)_

The domain name for the origin.

Provide the `origin_domain_name` if you want to validate the `s3_origin_path` property.

## Properties

|Property                             | Description|
'''

outputText1 = '''

# aws_cloudfront_distribution

Use the `aws_cloudfront_distribution` InSpec audit resource to test the properties of a single AWS CloudFront distribution.

For additional information, including details on parameters and properties, see the [AWS API reference for CloudFront distributions](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_distribution.html) documentation. For available SSL/TLS version identifiers, see [OriginSslProtocols](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_OriginSslProtocols.html) and [AWS::CloudFront::distribution ViewerCertificate](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html) documentation.

## Syntax

Ensure that an `aws_cloudfront_distribution` exists:

    describe aws_cloudfront_distribution('DISTRIBUTION') do
      it { should exist }
    end

    describe aws_cloudfront_distribution(distribution_id: 'DISTRIBUTION') do
      it { should exist }
    end

## Parameters

`distribution_id` _(required)_

: The CloudFront distribution ID, which can be passed either as a string or as a `name: 'value'` key-value entry in a hash.

`disallowed_ssl_protocols` _(optional)_

: If provided, this parameter is expected to be an array of strings identifying SSL/TLS protocols that you wish not to allow.

: Included in the array should be the union of disallowed identifiers for:

: - custom origin SSL/TLS protocols (currently SSLv3 | TLSv1 | TLSv1.1 | TLSv1.2)
  - identifiers for the minimum SSL/TLS protocol in the Viewer Certificate that CloudFront can use to communicate with viewers (currently SSLv3 | TLSv1 | TLSv1_1026 | TLSv1.1_2016 | TLSv1.2_2018 | TLSv1.2_2019 | TLSv1.2_2021).

: Newer protocol identification strings (when available) may be provided in the set, as validity is not checked. The default value for disallowed_ssl_protocols is `%w{SSLv3 TLSv1 TLSv1_2016}`.

`origin_domain_name` _(optional)_

: The domain name for the origin.

: Provide the `origin_domain_name` if you want to validate the `s3_origin_path` property.

## Properties

|Property                             | Description|
'''

def testAwsMoveLink1():
    pageText, pageTextMoved = moveAWSLink(inputText1)
    startEnd = openBlock(pageText, 'Parameters')
    outputText, errorText = mungeParametersBlock(pageText, startEnd['start'], startEnd['end'])
    print(outputText)
    print(errorText)
    assert outputText == outputText1
    assert errorText == ''
    assert pageTextMoved == True


inputText2 = '''# aws_alb

Use the `aws_alb` InSpec audit resource to test properties of a single AWS Application Load Balancer (ALB).

## Syntax

Ensure that an `aws_alb` exists

    describe aws_alb('arn:aws:elasticloadbalancing') do
      it { should exist }
    end

    describe aws_alb(load_balancer_arn: 'arn:aws:elasticloadbalancing') do
      it { should exist }
    end

## Parameters

### load_balancer_arn _(required)_

This resource accepts a single parameter, the ALB Arn which uniquely identifies the ALB.
This can be passed either as a string or as a `load_balancer_arn: 'value'` key-value entry in a hash.

See also the [AWS documentation on Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference).

## Properties

|Property                    | Description|
'''

outputText2 = '''# aws_alb

Use the `aws_alb` InSpec audit resource to test properties of a single AWS Application Load Balancer (ALB).

For additional information, including details on parameters and properties, see the [AWS documentation on Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference).

## Syntax

Ensure that an `aws_alb` exists

    describe aws_alb('arn:aws:elasticloadbalancing') do
      it { should exist }
    end

    describe aws_alb(load_balancer_arn: 'arn:aws:elasticloadbalancing') do
      it { should exist }
    end

## Parameters

### load_balancer_arn _(required)_

This resource accepts a single parameter, the ALB Arn which uniquely identifies the ALB.
This can be passed either as a string or as a `load_balancer_arn: 'value'` key-value entry in a hash.

## Properties

|Property                    | Description|
'''

def testAwsMoveLink2():
    assert moveAWSLink(inputText2) == (outputText2, True)


inputText3 = '''# aws_alb

Use the `aws_alb` InSpec audit resource to test properties of a single AWS Application Load Balancer (ALB).

## Syntax

Ensure that an `aws_alb` exists

    describe aws_alb('arn:aws:elasticloadbalancing') do
      it { should exist }
    end

    describe aws_alb(load_balancer_arn: 'arn:aws:elasticloadbalancing') do
      it { should exist }
    end

## Parameters

### load_balancer_arn _(required)_

This resource accepts a single parameter, the ALB Arn which uniquely identifies the ALB.
This can be passed either as a string or as a `load_balancer_arn: 'value'` key-value entry in a hash.

Id consectetur irure quis nisi [AWS documentation on Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference).

## Properties

|Property                    | Description|
'''

def testAwsMoveLink3():
    assert moveAWSLink(inputText3) == (inputText3, False)

inputText4 = '''
# aws_apigateway_account

Use the `aws_apigateway_account` InSpec audit resource to test properties of a single specific AWS API Gateway account.

The `AWS::ApiGateway::Account` resource specifies the IAM role that Amazon API Gateway uses to write API logs to Amazon CloudWatch Logs.

## Syntax

Ensure that the account exists.

    describe aws_apigateway_account do
      it { should exist }
    end

## Parameters

For additional information, see the [AWS documentation on AWS API Gateway accounts.](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-account.html).

## Properties

| Property | Description |
| --- | --- |
'''

outputText4 = '''
# aws_apigateway_account

Use the `aws_apigateway_account` InSpec audit resource to test properties of a single specific AWS API Gateway account.

The `AWS::ApiGateway::Account` resource specifies the IAM role that Amazon API Gateway uses to write API logs to Amazon CloudWatch Logs.

For additional information, including details on parameters and properties, see the [AWS documentation on AWS API Gateway accounts.](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-account.html).

## Syntax

Ensure that the account exists.

    describe aws_apigateway_account do
      it { should exist }
    end

## Parameters

The resource does not require any parameters.

## Properties

| Property | Description |
| --- | --- |
'''

def testAwsMoveLink4():
    assert moveAWSLink(inputText4) == (outputText4, True)

inputText5 = '''

# aws_cloudfront_cache_policies

Use the `aws_cloudfront_cache_policies` InSpec audit resource to test properties of multiple AWS CloudFront cache policies.

The `AWS::CloudFront::CachePolicy` resource describes the CloudFront cache policy.

## Syntax

Ensure that the custom resource exists.

    describe aws_cloudfront_cache_policies do
      it { should exist }
    end

## Parameters

This resource does not require any parameters.

For additional information, see the [AWS documentation on AWS CloudFront cache policy.](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cache-policy.html).

## Properties

| Property | Description | Field |
| --- | --- | --- |
'''

outputText5 = '''

# aws_cloudfront_cache_policies

Use the `aws_cloudfront_cache_policies` InSpec audit resource to test properties of multiple AWS CloudFront cache policies.

The `AWS::CloudFront::CachePolicy` resource describes the CloudFront cache policy.

For additional information, including details on parameters and properties, see the [AWS documentation on AWS CloudFront cache policy.](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cache-policy.html).

## Syntax

Ensure that the custom resource exists.

    describe aws_cloudfront_cache_policies do
      it { should exist }
    end

## Parameters

This resource does not require any parameters.

## Properties

| Property | Description | Field |
| --- | --- | --- |
'''


def testAwsMoveLink5():
    assert moveAWSLink(inputText5) == (outputText5, True)



inputText6 = '''
# azure_container_registries

Use the `azure_container_registries` InSpec audit resource to test properties and configuration of Azure Container Registries.

## Azure REST API version, endpoint and HTTP client parameters

This resource interacts with API versions supported by the resource provider.
The `api_version` can be defined as a resource parameter.
If not provided, the latest version will be used.
For more information, refer to [`azure_generic_resource`](azure_generic_resource.md).

Unless defined, this resource will use the `azure_cloud` global endpoint and default values for the HTTP client.
For more information, refer to the resource pack [README](../../README.md).

## Availability

### Installation
'''

outputText6 = '''
# azure_container_registries

Use the `azure_container_registries` InSpec audit resource to test properties and configuration of Azure Container Registries.

## Azure REST API Version, Endpoint, and HTTP Client Parameters

{{% inspec_azure_common_parameters %}}

## Availability

### Installation
'''

def testAzureParameters():
    assert azureCommonParameters(inputText6) == outputText6


inputText7 = '''
```ruby
describe aws_alb(load_balancer_arn: 'arn:aws:elasticloadbalancing') do
    it { should exist }
end
```

## Parameters

### load_balancer_arn _(required)_

This resource accepts a single parameter, the ALB Arn which uniquely identifies the ALB.
This can be passed either as a string or as a `load_balancer_arn: 'value'` key-value entry in a hash.

## Properties

`load_balancer_name`
: The name of the load balancer.
'''

outputText7 = '''
```ruby
describe aws_alb(load_balancer_arn: 'arn:aws:elasticloadbalancing') do
    it { should exist }
end
```

## Parameters

`load_balancer_arn` _(required)_

: This resource accepts a single parameter, the ALB Arn which uniquely identifies the ALB.
  This can be passed either as a string or as a `load_balancer_arn: 'value'` key-value entry in a hash.

## Properties

`load_balancer_name`
: The name of the load balancer.
'''

def testMungeParametersBlock1():
    startEnd = openBlock(inputText7, 'Parameters')
    outputText, errorText = mungeParametersBlock(inputText7, startEnd['start'], startEnd['end'])
    print(outputText)
    print('error Text -->' + errorText + '<--')
    assert outputText == outputText7
    assert errorText == ''

inputText8 = '''

```ruby
describe azure_container_group(resource_group: 'RESOURCE_GROUP_NAME', name: 'CONTAINER_GROUP_NAME') do
  it  { should exist }
end
```

## Parameters

| Name           | Description                                                                      |
|----------------|----------------------------------------------------------------------------------|
| name           | Name of the Azure container group to test.                                      |
| resource_group | Azure resource group that the targeted resource resides in. `MyResourceGroup`|

The parameter set should be provided for a valid query:
- `resource_group` and `name`

## Properties

`id`
: The resource ID.

`name`
: The container group name.

`type`
: The resource type.

'''

outputText8 = '''

```ruby
describe azure_container_group(resource_group: 'RESOURCE_GROUP_NAME', name: 'CONTAINER_GROUP_NAME') do
  it  { should exist }
end
```

## Parameters

`name`
: Name of the Azure container group to test.

`resource_group`
: Azure resource group that the targeted resource resides in. `MyResourceGroup`.

The parameter set should be provided for a valid query:
- `resource_group` and `name`

## Properties

`id`
: The resource ID.

`name`
: The container group name.

`type`
: The resource type.

'''


def testMungeParametersBlock2():
    startEnd = openBlock(inputText8, 'Parameters')
    print(startEnd['start'], startEnd['end'])
    outputText, errorText = mungeParametersBlock(inputText8, startEnd['start'], startEnd['end'])
    print(outputText)
    print('error Text -->' + errorText + '<--')
    assert outputText == outputText8
    assert errorText == ''

inputText9 = '''

Test that the base path mapping exists.

    describe aws_apigateway_base_path_mapping(domain_name: 'DOMAIN_NAME', base_path: 'BASE_PATH') do
      it { should exist }
    end

## Parameters

`domain_name` _(required)_

The domain name of the base path mapping resource to be described.

`base_path` _(required)_

The base path name that callers of the API must provide as part of the URL after the domain name.

## Properties

| Property | Description |
| --- | --- |
| base_path | The base path name that callers of the API must provide as part of the URL after the domain name. |
| rest_api_id | The string identifier of the associated RestApi.|
| stage | The name of the associated stage. |
'''

outputText9 = '''

Test that the base path mapping exists.

    describe aws_apigateway_base_path_mapping(domain_name: 'DOMAIN_NAME', base_path: 'BASE_PATH') do
      it { should exist }
    end

## Parameters

`domain_name` _(required)_

: The domain name of the base path mapping resource to be described.

`base_path` _(required)_

: The base path name that callers of the API must provide as part of the URL after the domain name.

## Properties

| Property | Description |
| --- | --- |
| base_path | The base path name that callers of the API must provide as part of the URL after the domain name. |
| rest_api_id | The string identifier of the associated RestApi.|
| stage | The name of the associated stage. |
'''


def testMungeParametersBlock3():
    startEnd = openBlock(inputText9, 'Parameters')
    print(startEnd['start'], startEnd['end'])
    outputText, errorText = mungeParametersBlock(inputText9, startEnd['start'], startEnd['end'])
    print(outputText)
    print('error Text -->' + errorText + '<--')
    assert outputText == outputText9
    assert errorText == ''



inputText10 = '''

Test that the base path mapping exists.

    describe aws_apigateway_base_path_mapping(domain_name: 'DOMAIN_NAME', base_path: 'BASE_PATH') do
      it { should exist }
    end

## Parameters

`domain_name` _(required)_

The domain name of the base path mapping resource to be described.

`base_path` _(required)_

The base path name that callers of the API must provide as part of the URL after the domain name.
Nulla commodo consectetur excepteur id incididunt tempor veniam et dolor esse ullamco.

Magna excepteur eu mollit et laboris labore do dolore veniam.

## Properties

| Property | Description |
| --- | --- |
| base_path | The base path name that callers of the API must provide as part of the URL after the domain name. |
| rest_api_id | The string identifier of the associated RestApi.|
| stage | The name of the associated stage. |
'''

outputText10 = '''

Test that the base path mapping exists.

    describe aws_apigateway_base_path_mapping(domain_name: 'DOMAIN_NAME', base_path: 'BASE_PATH') do
      it { should exist }
    end

## Parameters

`domain_name` _(required)_

: The domain name of the base path mapping resource to be described.

`base_path` _(required)_

: The base path name that callers of the API must provide as part of the URL after the domain name.
  Nulla commodo consectetur excepteur id incididunt tempor veniam et dolor esse ullamco.

: Magna excepteur eu mollit et laboris labore do dolore veniam.

## Properties

| Property | Description |
| --- | --- |
| base_path | The base path name that callers of the API must provide as part of the URL after the domain name. |
| rest_api_id | The string identifier of the associated RestApi.|
| stage | The name of the associated stage. |
'''


def testMungeParametersBlock4():
    startEnd = openBlock(inputText10, 'Parameters')
    print(startEnd['start'], startEnd['end'])
    outputText, errorText = mungeParametersBlock(inputText10, startEnd['start'], startEnd['end'])
    print(outputText)
    print('error Text -->' + errorText + '<--')
    assert outputText == outputText10
    assert errorText == ''
