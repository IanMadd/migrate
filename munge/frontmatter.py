import re
import toml
import yaml

def fixFrontmatter(text):
  errorLogText = ''
  yamlRegex = r"^---\n"
  yamlSpaceRegex = r"^ {1,}--- {0,}\n"
  titleRegex = r"(\w+)\sResource$"
  identifierBaseString = "inspec/resources/"

  #Find and log bad yaml frontmatter lines

  if re.search(yamlSpaceRegex, text, re.M):
    errorLogText += "Bad YAML frontmatter:\n\n" + text + "\n\n"
    text = re.sub(yamlSpaceRegex, "---\n", text, 2, re.M)
    print(text)

  #get location of preceding and trailing frontmatter yaml markers: ---
  yamlDashesList = [m.start() for m in re.finditer(yamlRegex, text, re.M)]

  #get yaml frontmatter and convert to Python dict
  frontmatter = yaml.load(text[yamlDashesList[0]: yamlDashesList[1]], Loader=yaml.FullLoader)

  if not "platform" in frontmatter:
    if 'aws' in frontmatter['title']:
      frontmatter["platform"] = 'aws'
    if 'azure' in frontmatter['title']:
      frontmatter["platform"] = 'azure'
    if 'habitat' in frontmatter['title']:
      frontmatter["platform"] = 'habitat'
    if 'alicloud' in frontmatter['title']:
      frontmatter["platform"] = 'alicloud'

  if not "title" in frontmatter or not "platform" in frontmatter:
    raise Exception("Missing frontmatter, platform or title: " + str(frontmatter))

  #generate frontmatter values
  title = re.search(titleRegex, frontmatter["title"], re.IGNORECASE)
  if title == None:
    errorLogText += "Missing proper title: " + str(frontmatter) + "\n"

  else:
    menuParent = identifierBaseString + frontmatter["platform"]
    menuIdentifier = menuParent + "/" + title.group(0)

    #make menu frontmatter
    menuDict = {"title": title.group(1), "identifier": menuIdentifier, "parent": menuParent}

    #update frontmatter dict
    frontmatter["title"] = title.group(0)
    frontmatter["draft"] = False
    frontmatter["gh_repo"] = "inspec-" + frontmatter["platform"]

    frontmatter["menu"] = {"inspec": menuDict}
    tomlFrontmatter = toml.dumps(frontmatter)
    # print(tomlFrontmatter)

    text = re.sub(r"^---", "+++", text, 2, re.M)
    text = text[0 : yamlDashesList[0] + 3] + "\n" + tomlFrontmatter + text[yamlDashesList[1]:]
    # print(text)

  return text, errorLogText


