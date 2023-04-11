# auto_label_images

- This repo contains 2 scripts that I use to add a textbox to a batch of images.
- The textbox is located in the bottom-left corner.
- There are 2 scripts:
  - `add_btmleft_image_text.py`: a generic script for adding the textbox to a single image.
  - `auto_label_by_filename.bash`: a NOT generic script for labeling a batch of images in a directory based on their filename.

I created these scripts to add information to photos of dishes from restaurants.
Specifically, I am exploring the world of Asian cuisine and created this system for a photo album where each
dish is labeled with its (1) name, (2) restauarant, and (3) city. 

**Photo Album:** [2023 Spring - Houston Chinatown Food Adventures](https://photos.app.goo.gl/VHv1u7wzcgtSVLkp6)

### Before:

![Unlabeled image](taiwan-style_egg_custard__Six_Ping_Bakery__Houston,_TX.jpg)

### After:

![Labeled image](taiwan-style_egg_custard__Six_Ping_Bakery__Houston,_TX--labeled.jpg)

## Howto

**Install `add_btmleft_image_text.py`**

Since this Python script is generic (any number of lines, etc), I place this in my local executable's directory. 

    cp add_btmleft_image_text.py $HOME/.local/bin/
    
**Install font or select another**

I use the font [_Comfortaa_](https://fonts.google.com/specimen/Comfortaa) to create the labels. You can use any TrueType (.ttf) font, but must supply the path.

Either way, you **must** edit the `file_font` within `auto_label_by_filename.bash` to the path of a TrueType font on your system.

**Option A: label a single image**

- You can use `add_btmleft_image_text.py` to label a single image with arbitrary text.
- The text is of the form: `this in a line@@this is a second line below it@@and so on`.
- The longest line is used to set the font size of all other lines so that the text forms a rectangle.

Run it with `--help` to see all options:

    add_btmleft_image_text.py --help
    
**Option B: label all `.jpg` images in a directory**

- I should make the filetype an option, shouldn't I?
- But, again, this script was made for a very specific, personal application.
- You have to set a specific filename structure.

Add files with this format:

  - words are separated by a single `_`.
  - lines are separated by a double `__`.
  - the filetype is always `.jpg`.
  - If you need to duplicate the text, you can add `-NUMBER` before `.jpg` (e.g. `-2.jpg`)

Example, the file: `taiwan-style_egg_custard__Six_Ping_Bakery__Houston,_TX.jpg`

Will create the following textbox:

    taiwan-style egg custard
    Six Ping Bakery
    Houston, TX
    
And if it is a duplicate text, then the filename could be: `taiwan-style_egg_custard__Six_Ping_Bakery__Houston,_TX-2.jpg`
    
Run the batch bash script (in same directory as the images)

    auto_label_by_filename.bash

What will happen:

[<img src="https://img.youtube.com/vi/ofXlMjnEmdQ/maxresdefault.jpg" width="50%">](https://youtu.be/ofXlMjnEmdQ)
