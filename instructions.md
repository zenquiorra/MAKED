To load a file from our generated dataset, we need `Python 2.7+` installed in our system

#### Import necessary packages
Within `python` terminal, we need to 
```python
# import the json module and our dedicated Parser

import json
from fileparser import Parse


# enter the path to our json article
path = "path/to/a/json/file"

# define the file_loader function
def file_loader(path_to_file):
    # Loads a json file
    with open(path_to_file, encoding = 'utf-8') as f:
        data = json.load(f)
    return data
    
# execute the file_loader function
file = file_loader(path)

# create an object of our file using the Parse class
article = Parse(file)

# `article` in now an object of Parse class, and it has 10+ defined methods, which can be found in our `fileparser.py` file, the most important ones for reference now are the following three methods:

```

`get_textall()` returns a string with complete text of the article.

`get_summary()` returns the text summary of the article.

`get_keywords()` returns a list of keywords associated with the article.

`get_images(path/to/imagefolder/)` Requires path to image folder for the corresponding language, returns a list of tuples containing name of images and their captions pairs. Image name is of the format "hash of the article" ## "part of the subsection the image belongs to" ## "randomized token". Image name can be extracted from the list  and they can be found in our file directory


> Note : Some articles may lack keywords, since the data is captured from an unordered set from the original data. However, in the complete dataset, all articles have keywords associated with them. 
