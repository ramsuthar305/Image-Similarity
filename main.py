from index_images import tree
from search import search

if __name__ == "__main__":
    treeObj = tree()
    treeObj.run()
    searchObj = search()
    searchObj.run()
    print("\n{}{}Please check output_data directory for your output\n".format('\033[1m', '\033[94m'))
