import os
import shutil #shell utilities

# Specify the source directory and dest directory
source_dir = '/Users/pouyarad/Downloads'
dest_dir = '/Users/pouyarad/Downloads/Co-op Resume/CV'

# If file does not exist in the directory create the respective folder
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

# List all the files in the source directory
files = os.listdir(source_dir)

# Loop through each file in the source directory
for file_name in files:
    # Check if file ends with .pdf and contains 'intern', 'coop' or 'winter'
    if file_name.endswith('.pdf') and any(keyword in file_name.lower() for keyword in 
    ['intern', 'coop', 'co-op', 'winter']):
        