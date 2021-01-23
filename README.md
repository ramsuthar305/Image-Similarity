# Image-Similarity
This repo is to find duplicate or identical pictures and decode QR code from pictures if present

## Instructions to run the program
1. Place all your Images in `data` directory
1. Open terminal in the folder
1. Run `pip3 install virtualenv`
1. `virtualenv gigindia`
1. `source gigindia/source/bin/activate`
1. `pip3 install -r requirements.txt`
1. `python3 main.py`
1. Wait for program to execute
1. Once done check output files in `output` directory

## Time complexity of similarity algorithm is `nlog(n)`

## References 
1. [PyImageSearch](https://www.pyimagesearch.com/2017/11/27/image-hashing-opencv-python/)
1. [Vp Tree](https://pypi.org/project/vptree/)

### Program first creates hashes and VP tree of images
### Than in order to find similarity it calculate hamming differences between images
