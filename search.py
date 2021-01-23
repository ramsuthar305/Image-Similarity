from pyimagesearch.hashing import convert_hash
from pyimagesearch.hashing import dhash
import pickle
import time
import cv2
from imutils import paths
import os


class search:
	def __init__(self):
		self.imagePaths = list(paths.list_images("data"))
		self.treePickle = pickle.loads(open("pickle/vptree.pickle", "rb").read())
		self.hashPickle = pickle.loads(open("pickle/hashes.pickle", "rb").read())
		self.similarImageFile = "output/similarImageData.txt"
		self.uniqueImageFile = "output/uniqueImageData.txt"
		self.qrImageFile = "output/qrImageData.txt"
		self.qrData = []

	def findSimilarImages(self):
		self.allResults = []
		qrCodeDetector = cv2.QRCodeDetector()
		similarFile = open(self.similarImageFile, "w")
		uniqueFile = open(self.uniqueImageFile, "w")

		print("Finding similar images and decoding QR codes if any.... ")
		for (i, imagePath) in enumerate(self.imagePaths):
			# load the image
			image = cv2.imread(imagePath)
			arr = []
			# convert image to hash
			queryHash = dhash(image)
			queryHash = convert_hash(queryHash)
			results = self.treePickle.get_all_in_range(queryHash, 21)

			for (count, (d, h)) in enumerate(results):
				resultPaths = self.hashPickle.get(h, "")
				arr.append(resultPaths[0])

			if len(arr) > 1:
				similarFile.write(", ".join(arr) + os.linesep)

			elif len(arr) == 1:
				uniqueFile.write(arr[0] + os.linesep)

		similarFile.close()
		uniqueFile.close()


	def getAllQrcodes(self):
		image = cv2.imread("qrcode.png")
		queryHash = dhash(image)
		results = self.treePickle.get_all_in_range(queryHash, 30)
		for (count, (d, h)) in enumerate(results):
			resultPaths = self.hashPickle.get(h, "")
			for i in resultPaths:
				self.qrData.append(i)


	def getQrImagesText(self):
		self.getAllQrcodes()
		qrCodeDetector = cv2.QRCodeDetector()
		qrFile = open(self.qrImageFile, "w")
		for qrImage in self.qrData:
			image = cv2.imread(qrImage)
			decodedData = qrCodeDetector.detectAndDecode(image)
			if len(decodedData[0])>0:
				qrFile.write("QR Code Path:{}\tDecoded Text: {} {}".format(
					qrImage, decodedData[0], os.linesep))
		qrFile.close()

	def run(self):
		self.findSimilarImages()
		self.getQrImagesText()


if __name__ == "__main__":
	obj = search()
	obj.run()
