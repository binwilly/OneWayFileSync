# Written by Guillermo Schwindt Tzoneff (binwilly@gmail.com)

# Helper functions for building file paths.

import sublime
import os

settings = sublime.load_settings('OneWayFileSync.sublime-settings')

def check_folder_to_sync(file_path):
    #Check if the folder is in the file path
    # if not, return false, so don't take action this plugin
    sync_folder_name = settings.get("sync_folder_name")

    if (file_path.find(sync_folder_name) == -1):
        return False
    return True

def create_target_path(file_path):
    src_path = settings.get("src_path")
    target_path = settings.get("target_path")
    filename = os.path.split(file_path)[1]
    
    #Delete the source path from the file path
    file_to_copy = file_path.replace(src_path, '');
    file_to_copy = file_to_copy.replace(filename, '');
    #Add the target path with before the filename
    path_to_copy = os.path.join(target_path, file_to_copy)
    return path_to_copy
