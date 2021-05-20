+++
title = "{{ .Name | humanize | title }} resource"
draft = false
gh_repo = "inspec"
platform = "<PLATFORM>"

[menu]
  [menu.automate]
    title = "{{ .Name | humanize | title }}"
    identifier = "inspec/resources/<PLATFORM>/{{ .Name | humanize | title }}"
    parent = "inspec/"
+++


{{% Run `hugo new -k resource resources/RESOURCE_NAME.md` to generate a new resource page. %}}

## Syntax

## Properties

## Examples

## Matchers

For a full list of available matchers, please visit our [Universal Matchers page](https://docs.chef.io/inspec/matchers/).