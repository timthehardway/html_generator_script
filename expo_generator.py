# (NL) januari 2022
#
# Kunst en Co Uden virtuele expositie HTML generator
#
# Op basis van een map met afbeeldingen en informatie 
# van de gebruiker bouwt dit script een HTML galerij. 
#
# Het script maakt gebruik van de volgende bestanden:
# - expo_template_top.html
# - expo_template_bottom.html
# - aparte map met afbeeldingen.

import os

# PROMPT USER FOR IMAGE FOLDER, OUTPUT FILENAME, EXPO DATA.
#
source_directory = input("Naam map met foto's: ")
output_filename = input("Naam output bestand (zonder .html): ") + ".html"
expo_name = input("Naam expositie: ")
expo_info = input("Korte beschrijving van de expositie: ")

# CLEAN UP FILENAMES: REMOVE ALL SPACES AND SET TO LOWERCASE.
#
path =  os.getcwd() + "\\" + source_directory
filenames = os.listdir(path)

for filename in filenames:
    os.rename((source_directory + "\\" + filename), (source_directory + "\\" + filename.replace(" ", "-").lower()))

# SCAN IMAGE FOLDER, FILTER OUT AND COUNT IMAGES.
#
all_filenames = os.listdir(path)
image_filenames = []
for file in all_filenames:
    if file.endswith((".jpg", ".jpeg", ".png")):
        image_filenames.append(file)

num_of_images = len(image_filenames)

# PROMPT USER FOR IMAGE TITLES.
image_titles = []
print("\nVoer voor elke afbeelding een titel in: ")
for name in image_filenames:
    image_titles.append(input(f"* {name}: "))

# FETCH HTML TEMPLATE DATA.
#
html_template_top = ""
html_template_bottom = ""

with open("expo_template_top.html", 'r') as file:
    html_template_top = file.read()

with open("expo_template_bottom.html", 'r') as file:
    html_template_bottom = file.read()

# GENERATE TITLE AND DESCRIPTION HTML CODE.
#
html_template_middle = f"""

        <div class="container pb-2 textblock">
          <h2>{expo_name}</h2>
          <p>{expo_info}</p>
        </div>

        <div class="container pt-3">
        """

# GENERATE IMAGE GALLERY HTML CODE: IMAGE BLOCKS.
#
html_blocks_per_image = []

for i in range(0, num_of_images):
    html_code = f"""
        <div class="col-sm-4 text-center">
            <figure><a href=\"{source_directory}\\{image_filenames[i]}">
            <img src=\"{source_directory}\\{image_filenames[i]}" class="w-50 hover-shadow img-thumbnail sm-4" alt=\"{image_filenames[i]}\">
            <figcaption class="figure-caption imgtext">{image_titles[i]}</figcaption></a></figure>
        </div>
        """
    html_blocks_per_image.insert(i, html_code)

# GENERATE IMAGE GALLERY HTML CODE: IMPLEMENT ROWS.
#
row_top_code = """
    <div class="row">
    """

row_bottom_code = """
    </div>
    """

num_of_complete_rows = num_of_images // 3
num_of_remaining_images = num_of_images % 3

html_blocks_per_row = []

images_per_row = 3
iterator_images = 0

for row in range(0, num_of_complete_rows):
    print(f">>>> building complete row {row}.")

    html_code_row = row_top_code

    for image in range(0, images_per_row):
        html_code_row += html_blocks_per_image[iterator_images]
        print(f">>>> iterator images = {iterator_images}")
        iterator_images += 1

    html_code_row += row_bottom_code
    html_blocks_per_row.append(html_code_row)

if num_of_remaining_images > 0:
    print(f">>>> adding extra row for {num_of_remaining_images} remaining images.")

    html_code_row = row_top_code

    for image in range(0, num_of_remaining_images):
        html_code_row += html_blocks_per_image[iterator_images]
        print(f">>>> iterator images = {iterator_images}")
        iterator_images += 1

    html_code_row += row_bottom_code
    html_blocks_per_row.append(html_code_row)

# BUILD OUTPUT HTML FILE.
#
out_file = open(output_filename, "x")
out_file.write(html_template_top)
out_file.write(html_template_middle)
for block in html_blocks_per_row:
    out_file.writelines(block)
out_file.write(html_template_bottom)
out_file.close()
