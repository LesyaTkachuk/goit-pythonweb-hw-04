# goit-pythonweb-hw-04

Script for asynchronous recursive copying of files and placing them into subfolder with file extension names.

To run the script provide -s <absolute_path_to_source_folder>:

```
python main.py -s <absolute_path_to_source_folder>
```

All files from source directory will be copied to the dist directory in the root of the project and sorted to the folders with file extension names.

To specify another destination folder add optional argument -d <absolute_path_to_destination_folder>:

```
python main.py -s <absolute_path_to_source_folder> -d <absolute_path_to_destination_folder>
```
