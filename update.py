#!/usr/bin/env python

import os
from urllib import parse

HEADER="""# 
# 백준 문제 풀이 목록

---
"""

def main():
    content = ""
    content += HEADER
    
    directories = [];

    for root, dirs, files in os.walk("."):
        dirs.sort()
        if root == '.':
            for dir in ('.git', '.github'):
                try:
                    dirs.remove(dir)
                except ValueError:
                    pass
            continue

        category = os.path.basename(root)
        
        if category == 'images':
            continue
        
        directory = os.path.basename(os.path.dirname(root))
        
        if directory == '.':
            if len(files) == 1:
                content += "## [{}]({})첫번째\n".format(category, parse.quote(os.path.join(root, files[0])))
                directories.append(category)
            continue
            
        if directory not in directories:
            content += "## {}두번째\n".format(directory)
            directories.append(directory)

        for file in files:
            content += "- [{}]({})세번째\n".format(category, parse.quote(os.path.join(root, file)))
        content += "\n"

    with open("README.md", "w") as fd:
        fd.write(content)


if __name__ == "__main__":
    main()
