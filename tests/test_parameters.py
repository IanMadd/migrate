import pytest
from migrate.munge.parameters import *

inputText1= '''

# aws\_cloudfront\_distribution

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

### distribution\_id _(required)_

The CloudFront distribution ID, which can be passed either as a string or as a `name: 'value'` key-value entry in a hash.

### disallowed\_ssl\_protocols _(optional)_

If provided, this parameter is expected to be an array of strings identifying SSL/TLS protocols that you wish not to allow.

Included in the array should be the union of disallowed identifiers for:

- custom origin SSL/TLS protocols (currently SSLv3 | TLSv1 | TLSv1.1 | TLSv1.2)
- identifiers for the minimum SSL/TLS protocol in the Viewer Certificate that CloudFront can use to communicate with viewers (currently SSLv3 | TLSv1 | TLSv1_1026 | TLSv1.1_2016 | TLSv1.2_2018 | TLSv1.2_2019 | TLSv1.2_2021).

Newer protocol identification strings (when available) may be provided in the set, as validity is not checked. The default value for disallowed_ssl_protocols is `%w{SSLv3 TLSv1 TLSv1_2016}`.

For additional information, see the [AWS API reference for CloudFront distributions](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_distribution.html) documentation. For available SSL/TLS version identifiers, see [OriginSslProtocols](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_OriginSslProtocols.html) and [AWS::CloudFront::distribution ViewerCertificate](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html) documentation.

### origin\_domain\_name _(optional)_

The domain name for the origin.

Provide the `origin_domain_name` if you want to validate the `s3_origin_path` property.

## Properties

|Property                             | Description|
'''

outputText1 = '''

# aws\_cloudfront\_distribution

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

### distribution\_id _(required)_

The CloudFront distribution ID, which can be passed either as a string or as a `name: 'value'` key-value entry in a hash.

### disallowed\_ssl\_protocols _(optional)_

If provided, this parameter is expected to be an array of strings identifying SSL/TLS protocols that you wish not to allow.

Included in the array should be the union of disallowed identifiers for:

- custom origin SSL/TLS protocols (currently SSLv3 | TLSv1 | TLSv1.1 | TLSv1.2)
- identifiers for the minimum SSL/TLS protocol in the Viewer Certificate that CloudFront can use to communicate with viewers (currently SSLv3 | TLSv1 | TLSv1_1026 | TLSv1.1_2016 | TLSv1.2_2018 | TLSv1.2_2019 | TLSv1.2_2021).

Newer protocol identification strings (when available) may be provided in the set, as validity is not checked. The default value for disallowed_ssl_protocols is `%w{SSLv3 TLSv1 TLSv1_2016}`.

### origin\_domain\_name _(optional)_

The domain name for the origin.

Provide the `origin_domain_name` if you want to validate the `s3_origin_path` property.

## Properties

|Property                             | Description|
'''

def testAwsMoveLink1():
    assert moveAWSLink(inputText1) == (outputText1, True)


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

inputText6 = '''
## Syntax

An `aws_iam_access_keys` resource block returns all IAM Access Keys and allows the testing of that group of Access Keys.

      describe aws_iam_access_keys do
        it                    { should exist }
        its('access_key_ids') { should include 'AKIA1111111111111111' }
      end

#### Parameters

This resources accepts a single optional parameter, a Username for which to retrieve all Access Keys.
If not provided, all Access Keys for all Users will be retrieved.

##### username _(optional)_

The IAM Username for which to retrieve the Access Keys.
This can be passed either as a string or as a `username: 'value'` key-value entry in a hash.

See also the [AWS documentation on IAM Access Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html).

## Properties

| Property               | Description|
'''

outputText6 = '''
## Syntax

An `aws_iam_access_keys` resource block returns all IAM Access Keys and allows the testing of that group of Access Keys.

      describe aws_iam_access_keys do
        it                    { should exist }
        its('access_key_ids') { should include 'AKIA1111111111111111' }
      end

## Parameters

This resources accepts a single optional parameter, a Username for which to retrieve all Access Keys.
If not provided, all Access Keys for all Users will be retrieved.

##### username _(optional)_

The IAM Username for which to retrieve the Access Keys.
This can be passed either as a string or as a `username: 'value'` key-value entry in a hash.

See also the [AWS documentation on IAM Access Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html).

## Properties

| Property               | Description|
'''

def testFixParametersHeading6():
    assert fixParametersHeading(inputText6) == (outputText6, True)
