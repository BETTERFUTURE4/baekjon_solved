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
    solveds = [];

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
                solved = "## [{}]({})\n".format(category, parse.quote(os.path.join(root, files[0])))
                if solved not in solveds:
                    content += solved
                    solveds.add(solved)
                directories.append(category)
            continue
            
        if directory not in directories:
            content += "### ✨ {}\n".format(directory)
            content += "|                 문제번호              |                     링크                     |\n"
            content += "| ----- | ----- |\n"
            directories.append(directory)

        for file in set(files):
            content += "|{}|[링크]({})|\n".format(category, parse.quote(os.path.join(root, file)))

    with open("README.md", "w") as fd:
        fd.write(content)
        
if __name__ == "__main__":
    main()
