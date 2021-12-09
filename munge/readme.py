import re

## format links in readme.md files
def readmeLinks(pageText):
    regex = r"(\[\w+\])\(docs\/resources\/(\w+).md\)"
    subst = subst = "\\g<1>(https://docs.chef.io/inspec/resources/\\g<2>/)"
    pageText = re.sub(regex, subst, pageText, 0, re.MULTILINE)

    return pageText
