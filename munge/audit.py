import re

def returnAuditText(filePath, page, branch):
    ## ../forks/inspec-azure/docs/resources/azure_sentinel_incidents_resource.md
    ## to
    ## https://github.com/inspec/inspec-aws/blob/main/docs/resources/azure_sentinel_incidents_resource.md
    ## and
    ## ../forks/inspec-azure/docs/resources/azure_sentinel_incidents_resource.md
    ## to
    ## https://github.com/IanMadd/inspec-aws/blob/im/hugo/docs-chef-io/content/inspec/resources/aws_alb.md

    gitHubInspecEditedBaseUrl = "https://github.com/inspec/"
    gitHubIanMaddEditedBaseUrl = "https://github.com/ianmadd/"
    inspecAwsUrl = "inspec-aws/blob/"
    inspecAzureUrl = "inspec-azure/blob/"
    editedPageHugoDir = "docs-chef-io/content/inspec/resources/"
    sourcePageDir = "docs/resources/"

    if 'forks' in str(filePath):
        editedBaseUrl = gitHubIanMaddEditedBaseUrl
    else:
        editedBaseUrl = gitHubInspecEditedBaseUrl

    if 'inspec-azure' in str(filePath):
        githubEditedPageURL = editedBaseUrl + inspecAzureUrl + branch + "/" + editedPageHugoDir + page
        githubSourcePageUrl = gitHubInspecEditedBaseUrl + inspecAzureUrl + "main/" + sourcePageDir + page
    elif 'inspec-aws' in str(filePath):
        githubEditedPageURL = editedBaseUrl + inspecAwsUrl + branch + "/" + editedPageHugoDir + page
        githubSourcePageUrl = gitHubInspecEditedBaseUrl + inspecAwsUrl + "main/" + sourcePageDir + page


    auditTextStart = '\n\n<div class="admonition-note">\n<p class="admonition-note-title">Migration Links for Review</p>\n<div class="admonition-note-text">\n'
    auditTextEnd = '</div>\n</div>\n'

    sourcePageLinkText = '<p>Source page: <a href="' + githubSourcePageUrl + '">' + githubSourcePageUrl + '</a></p>\n'
    generatedPageLinkText = '<p>Edited page: <a href="' + githubEditedPageURL + '">' + githubEditedPageURL + '</a></p>\n'

    auditText = auditTextStart + sourcePageLinkText + generatedPageLinkText + auditTextEnd

    return auditText
