from index_images import tree
from search import search
import os
if __name__ == "__main__":
    os.mkdir("pickle")
    os.mkdir("output")
    treeObj = tree()
    treeObj.run()
    searchObj = search()
    searchObj.run()
    print("\n{}{}Please check output_data directory for your output\n".format('\033[1m', '\033[94m'))
