import os
import json
from collections import defaultdict
from itertools import takewhile, count
from pprint import pprint


with open('all_packages.json') as data_all_file:
    data_all = json.load(data_all_file)





with open('dependencies.json') as data_dep_file:
    data_dep = json.load(data_dep_file)



def sort_topologically(graph):
    levels_by_name = {}
    names_by_level = defaultdict(set)

    def walk_depth_first(name):
        if name in levels_by_name:
            return levels_by_name[name]
        children = graph.get(name, None)
        level = 0 if not children else (1 + max(walk_depth_first(lname) for lname in children))
        levels_by_name[name] = level
        names_by_level[level].add(name)
        return level

    for name in graph:
        walk_depth_first(name)

    return list(takewhile(lambda x: x is not None, (names_by_level.get(i, None) for i in count())))

sorted_list = sort_topologically(data_all)




user_input = input("Please input the name of the project you want to install:")

if data_dep["projectName"] == user_input:
    print("Installing %s" % data_dep["projectName"])
    d = data_dep['dependencies']


else:
    print("I'm sorry, but there isn't any project with that name.")

for row in sorted_list:

    for column in row:
        if not os.path.exists('./installed_modules/' + column):
                os.makedirs('./installed_modules/' + column)
        else:
            print("Packages already exist")

if not os.path.exists('./installed_modules/' + user_input):
                os.makedirs('./installed_modules/' + user_input)
else:
    print("Packages already exist")

