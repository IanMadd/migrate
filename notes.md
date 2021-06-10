# Notes about migrating resource docs

## Existing Sections:

### AWS

- Title
- Intro text after title
- Syntax
- Parameters
- Each individual parameter
- Properties
- Examples
- Each example
- Matchers
- exists
- bunch of different headings
- AWS Permissions

### Azure

- Title
- Intro text after title
- Azure REST API version, endpoint and http client parameters
- Availability
- Installation
- Syntax
- Parameters
- Properties
- Examples
- Each example
- Matchers
- exists
- Azure Permissions

## Things to deal with:

- common content: we need a section of common properties, parameters, matchers, etc.. that's available to all resources.
  All azure resources have a set of common properties. That's a block of text that we could add
  to each page's text similar to: https://docs.chef.io/resources/apt_repository/#functionality

- Read up on Principal, `Effect` `Allow`/`Deny` https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html 
- https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_effect.html

   - Maybe:
     - Set the permissions for the [Principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) by specifying that the `ec2:VpcEndpointConnectionNotifications` action has the `Effect` element set to `Allow`.

### **AWS**

1. Fix the frontmatter
1. Title
   - delete the title
1. Add install section like in Azure resource docs.
1. Syntax
   1. Parameters
      1. Fix parameter items
      1. Remove "Parameters" heading and replace with "where:"
      1. Each parameter becomes a definition list item
      1. Process parameter required or optional values
1. Properties
   1. Properties should be in a definition list, not a table
   1. Plural resources have a Field, which is just the singular key of the property.
      1. This may be defined in a third table column called Fields, Field, Field Name, or just included in the text (The field name is `whatever`.).
      1. Make this a separate line in the parameter definition: **Field**: `whatever`

1. Examples
   1. Each example is a heading, but should be a bolded sentence.
1. Matchers
   1. Each matcher should be a definition list item
   1. Add Universal Matchers Section
1. Add AWS Principal Permissions shortcode.



### **Azure**

1. Fix the frontmatter
1. Title
   - delete the title
1. Azure REST API version, endpoint and http client parameters
   1. capitalize http in title, and api and http in the paragraph body.
1. Availability
   1. Azure has an availability section followed by Installation
   1. There's never anything in the availability section EXCEPT Installation, so just make this "Installation".
1. Syntax
   1. The parameters in the Syntax section look like a mess and should be edited by hand.
1. Properties
   1. It's a table, convert it to a definition list.
   1. There's a third column, Filter Criteria in plural resources. Add this as part of the definition. **Filter Criteria**: `whatever`.
1. Examples
   1. Each example should be bolded text and not a heading
1. Matchers
   1. Add Universal Matchers Section
1. Azure Permissions
   1. Shortcode for this section cause it's identical everywhere.
      1. Your [Service Principal](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal) must have the `contributor` role for the subscription you wish to test.
