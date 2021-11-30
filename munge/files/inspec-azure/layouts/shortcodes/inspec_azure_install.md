
This resource is available in the [Chef InSpec Azure resource pack](https://github.com/inspec/inspec-azure).

### Setting up Azure credentials for Chef InSpec

To use Chef InSpec Azure resources, you will need to create a Service Principal
Name (SPN) for auditing an Azure subscription.

This can be done on the command line or from the Azure Portal:

- [Azure CLI](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-authenticate-service-principal-cli)
- [PowerShell](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-authenticate-service-principal)
- [Azure Portal](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal)

The information from the SPN can be specified either in the file
`~/.azure/credentials`, as environment variables, or by using Chef InSpec target URIs.

#### Setting up the Azure Credentials File

By default, Chef InSpec is configured to look at `~/.azure/credentials`, and it
should contain:

```powershell
[<SUBSCRIPTION_ID>]
client_id = CLIENT_ID_VALUE
client_secret = CLIENT_SECRET_VALUE
tenant_id = TENANT_ID_VALUE
```

<div class="admonition-note">
<p class="admonition-note-title">Note</p>
<div class="admonition-note-text">

In the Azure web portal, these values are labeled differently:
- The `client_id` is referred to as the 'Application ID'
- The `client_secret` is referred to as the 'Key (Password Type)'
- The `tenant_id` is referred to as the 'Directory ID'

</div>
</div>

With the credentials are in place, you may now execute Chef InSpec:

```bash
inspec exec my-inspec-profile -t azure://
```

#### Using Environment variables to provide credentials

You may also set the Azure credentials via environment variables:

- `AZURE_SUBSCRIPTION_ID`
- `AZURE_CLIENT_ID`
- `AZURE_CLIENT_SECRET`
- `AZURE_TENANT_ID`

For example:

```bash
AZURE_SUBSCRIPTION_ID="2fbdbb02-df2e-11e6-bf01-fe55135034f3" \
AZURE_CLIENT_ID="58dc4f6c-df2e-11e6-bf01-fe55135034f3" \
AZURE_CLIENT_SECRET="Jibr4iwwaaZwBb6W" \
AZURE_TENANT_ID="6ad89b58-df2e-11e6-bf01-fe55135034f3" inspec exec my-profile -t azure://
```

#### Using the Chef InSpec target option to provide credentials on Azure

If you have created a `~/.azure/credentials` file as above, you may also use the Chef InSpec command line `--target` / `-t` option to select a subscription ID.  For example:

```bash
inspec exec my-profile -t azure://2fbdbb02-df2e-11e6-bf01-fe55135034f3
```
