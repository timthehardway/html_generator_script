# html_generator_script
A 'quick fix' for building a html image gallery suited to the specific needs of an art school. Not at all flexible or bug-free yet, so I am working on an improved object oriented version including unit tests.

This script was written to automate the writing of html image galleries for kunst & co (art school). Using a seperate folder containing the images and a split up html template, the script handles the following actions:

* filtering out images (.jpg, .jpeg, .png) from a given folder.
* renaming the image files (no spaces, all lowercase).
* adding user-specified titles to each image.
* building the html for all the images in rows of three.
* writing a complete html file which can then be uploaded.
