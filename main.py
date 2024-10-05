import os
import shutil #shell utilities

# Specify the source directory and dest directory
source_dir = '/Users/pouyarad/Downloads'
dest_dir = '/Users/pouyarad/Downloads/Co-op Resume/CV'

# If file does not exist in the directory create the respective folder
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)