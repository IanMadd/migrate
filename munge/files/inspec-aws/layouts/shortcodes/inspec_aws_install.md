This resource is available in the [Chef InSpec AWS resource pack](https://github.com/inspec/inspec-aws).

### Setting up AWS credentials for Chef InSpec

Chef InSpec uses the standard AWS authentication mechanisms. Typically, you will
create an IAM user specifically for auditing activities.

1. Create an IAM user in the AWS console, with your choice of username. Check the
   box marked **Programmatic Access**.
1. On the Permissions screen, choose Direct Attach. Select the AWS-managed IAM
   Profile named "ReadOnlyAccess." If you wish to restrict the user further, you
   may do so; see individual Chef InSpec resources to identify which permissions
   are required.
1. After generating the key, record the Access Key ID and Secret Key.

#### Using Environment Variables to provide credentials

You may provide the credentials to Chef InSpec by setting the following environment
variables: `AWS_REGION`, `AWS_ACCESS_KEY_ID`, and `AWS_SECRET_ACCESS_KEY`. You may
also use `AWS_PROFILE`, or if you are using MFA, `AWS_SESSION_TOKEN`. See the
[AWS Command Line Interface Docs](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
for details.

Once you have your environment variables set, you can verify your credentials by running:

```bash
$ inspec detect -t aws://

== Platform Details
Name:      aws
Families:  cloud, api
Release:   aws-sdk-v2.10.125
```

#### Using the Chef InSpec target option to provide credentials on AWS

Look for a file in your home directory named `~/.aws/credentials`. If it does not
exist, create it. Choose a name for your profile; here, we're using the name
'auditing'. Add your credentials as a new profile, in INI format:

```bash
[auditing]
aws_access_key_id = ACCESS_KEY_ID
aws_secret_access_key = ACCESS_KEY_VALUE
```

You may now run Chef InSpec using the `--target` / `-t` option, using the format
`-t aws://region/profile`.  For example, to connect to the Ohio region using a
profile named 'auditing', use `-t aws://us-east-2/auditing`.

To verify your credentials, run:

```bash
$ inspec detect -t aws://

== Platform Details
Name:      aws
Families:  cloud, api
Release:   aws-sdk-v2.10.125
```
