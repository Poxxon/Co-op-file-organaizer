# PDF File Organizer Script

This Python script automates the process of organizing `.pdf` files based on specific keywords (such as "intern", "coop", or "winter") found in their filenames. It scans a source directory, identifies matching files, and moves them to a designated folder for improved file management.

## Background

During my job search, I ended up downloading a lot of job postings, and it quickly became overwhelming to manage them all. To solve this, I came up with this script to easily organize those files based on certain keywords, such as "intern", "coop", and "winter". It helps to keep my job applications and postings neatly sorted into folders.

## Features

- **Keyword Matching**: The script identifies `.pdf` files that contain keywords like "intern", "coop", "co-op", or "winter".
- **File Organization**: Files matching the criteria are moved to a specified destination folder.
- **Folder Creation**: If the destination folder does not exist, the script automatically creates it.
- **Cross-platform**: Works on any system that supports Python and its standard libraries.

## Requirements

- Python 3.x
- The `os` and `shutil` libraries (included in the Python Standard Library).

## Usage

1. Clone or download this script.
2. Edit the script to set your desired `source_dir` (where your files are stored) and `dest_dir` (where you want the organized files to be moved).
   ```python
   source_dir = '/path/to/your/source/directory'
   dest_dir = '/path/to/your/destination/directory'
3. Run the script:

    ```bash
    python main.py
    ```

4. The script will search for `.pdf` files in the source directory that contain the specified keywords in their filenames. These files will be moved to the destination folder.

## Example

Let's say you have the following files in your source directory:

- `2023_internship.pdf`
- `coop_winter_application.pdf`
- `summer_intern.pdf`

After running the script, files with the keywords "intern", "coop", or "winter" will be moved to the destination folder, while others will remain in the source directory.

## Future Updates

Planned future updates for this script include adding a **Graphical User Interface (GUI)**. This GUI will allow users to easily:

- Specify the source directory.
- Input custom keywords to search for.
- Set the destination directory for the organized files.

This update will make the script more user-friendly, eliminating the need to manually edit the source code to change paths or keywords.

## Customization

If you need to search for different keywords or file types, you can modify the `keywords` list or change the file extension in the script. For example:

```python
keywords = ['intern', 'coop', 'co-op', 'winter']  # Modify or add new keywords
