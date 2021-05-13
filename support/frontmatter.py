


def fixFrontmatter(text):
  yamlRegex = r"^---\n"
  titleRegex = r"(\w+)\sResource$"
  identifierBaseString = "inspec/resources/"

  #get location of preceding and trailing frontmatter yaml markers: ---
  yamlDashesList = [m.start() for m in re.finditer(yamlRegex, text, re.M)]

  #get yaml frontmatter and convert to Python dict
  frontmatter = yaml.load(text[yamlDashesList[0]: yamlDashesList[1]], Loader=yaml.FullLoader)

  #generate frontmatter values
  title = re.search(titleRegex, frontmatter["title"])
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

  return text

