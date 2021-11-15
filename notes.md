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

1. Fix the frontmatter - DONE
2. Add blank lines after headings
3. Add blank lines around all codeblocks
4. Unindent code blocks and add fencing - DONE
5. Title
   - delete the title - DONE
6. Add install section like in Azure resource docs.
7. Syntax
   1. Parameters
      1. Fix parameter items
      2. Remove "Parameters" heading and replace with "where:" - UNDO THIS ONE. PARAMETERS IS BETTER
      3. Each parameter becomes a definition list item
      4. Process parameter required or optional values
      5. Move "For additional information" link text to intro section of documentation.
         1. Change to "For additional information, including details on parameters and properties, see the [ElasticLoadBalancingV2 LoadBalancer documentation](link URL)."
8. Properties
   1. Properties should be in a definition list, not a table
   2. Plural resources have a Field, which is just the singular key of the property.
      1. This may be defined in a third table column called Fields, Field, Field Name, or just included in the text (The field name is `whatever`.).
      2. Make this a separate line in the parameter definition: **Field**: `whatever`

9. Examples
   1. Each example is a heading, but should be a bolded sentence.
10. Matchers
   2. Each matcher should be a definition list item
   3. Add Universal Matchers Section
11. Add AWS Principal Permissions shortcode.



### **Azure**

1. Fix the frontmatter - DONE
2. Add blank lines after headings
3. Add blank lines around all codeblocks
4. Convert indented code blocks to fenced code blocks - DONE
5. Title
   - delete the title - DONE
6. Azure REST API version, endpoint and http client parameters
   1. capitalize http in title, and api and http in the paragraph body. - DONE
   2. convert text to shortcode. - DONE
7. Availability
   1. Azure has an availability section followed by Installation. There's never anything in the availability section EXCEPT Installation, so just make this "Installation". - DONE
8. Syntax
   1. The parameters in the Syntax section look like a mess and should be edited by hand.
9. Properties - DONE
   2. It's a table, convert it to a definition list.
   3. There's a third column, Filter Criteria in plural resources. Add this as part of the definition. **Filter Criteria**: `whatever`.
10. Examples
    1. Each example should be bolded text and not a heading
11. Matchers
    1. Add Universal Matchers Section
12. Azure Permissions
    1. Shortcode for this section cause it's identical almost everywhere. - DONE

