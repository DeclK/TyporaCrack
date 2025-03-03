# this script is to crack the typora software on Ubuntu/Linux
from pathlib import Path
import os
import re

licence_dir = '/usr/share/typora/resources/page-dist/static/js'
licence_dir = Path(licence_dir)

# check if the directory exists
if not licence_dir.exists():
    raise Exception('cannot find the directory')

# change the permission
print(f"Doing sudo chmod 777 -R for {str(licence_dir)}, might need to enter password")
os.system('sudo chmod 777 -R ' + str(licence_dir))

prefix = 'LicenseIndex'

licence_dir = Path(licence_dir).iterdir()

licence_file = None
for file in licence_dir:
    if file.name.startswith(prefix):
        licence_file = file

print(f"Found the licence file: {licence_file.name}")
if licence_file is None:
    raise Exception('cannot find licence file')

print("Overwriting the licence file...")
# read file content
with open(licence_file, 'r') as f:
    content = f.read()

# replace the pattern
target = 'e.hasActivated="true"==e.hasActivated'
replacement = 'e.hasActivated="true"=="true"'
content = re.sub(target, replacement, content)

# write the content to original file
with open(licence_file, 'w') as f:
    f.write(content)

print("Hack done!")