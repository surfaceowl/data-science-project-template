"""
utility to sort requirements.txt for easier maintenance
"""

# read current content
requirements_file = "../requirements.txt"
requirements = open(requirements_file, 'r')
content = requirements.read().splitlines()
requirements.close()

# write sorted content to requirements.txt
requirements = open(requirements_file, 'w')  # write mode overwrites contents
content = list(set(content))
for item in content:  # remove empty lines
    if item == "":
        content.remove(item)

content.sort(key=lambda y: y.lower())
content = '\n'.join(content)

requirements.write(content)
requirements.write("\n")
requirements.close()
