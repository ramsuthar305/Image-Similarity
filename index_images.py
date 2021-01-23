from pyimagesearch.hashing import convert_hash
from pyimagesearch.hashing import hamming
from pyimagesearch.hashing import dhash
from imutils import paths
import argparse
import pickle
import vptree
import cv2


class tree:
	def __init__(self):
		self.imagePaths = list(paths.list_images("data"))
		self.hashes = {}
		self.treePickle = "pickle/vptree.pickle"
		self.hashPickle = "pickle/hashes.pickle"

	def formHashes(self):
		for (i, imagePath) in enumerate(self.imagePaths):
			# load the input image
			print("[INFO] processing image {}/{} {}".format(i + 1,
															len(self.imagePaths), imagePath))
			image = cv2.imread(imagePath)

			# compute the hash for the image and convert it
			h = dhash(image)
			h = convert_hash(h)

			# update the hashes dictionary
			tmp = self.hashes.get(h, [])
			tmp.append(imagePath)
			self.hashes[h] = tmp

	def formTreePickle(self):
		print("[INFO] building VP-Tree...")
		points = list(self.hashes.keys())
		tree = vptree.VPTree(points, hamming)
		print("[INFO] serializing VP-Tree...")
		f = open(self.treePickle, "wb")
		f.write(pickle.dumps(tree))
		f.close()

	def formHashPickle(self):
		print("[INFO] serializing hashes...")
		f = open(self.hashPickle, "wb")
		f.write(pickle.dumps(self.hashes))
		f.close()

	def run(self):
		self.formHashes()
		self.formTreePickle()
		self.formHashPickle()


if __name__ == "__main__":
	obj = tree()
	obj.run()
