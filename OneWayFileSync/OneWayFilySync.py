# OneWaySyncPath
# Written by Guillermo Schwindt Tzoneff (binwilly@gmail.com)

# Changelog 
# Created basic plugin for sublime text 2 to sync one way folders (30/05/2012)
# Copy files on_post_save event

import sublime
import sublime_plugin
import os
import shutil
import pathManager


settings = sublime.load_settings('OneWayFileSync.sublime-settings')

class OneWayFileSyncCommand(sublime_plugin.EventListener):

	src_path = settings.get("src_path")
	target_path = settings.get("target_path")
	
	def on_post_save(self, view):
		# When a file is saved, put a copy of the file into the
		# target directory.
		# don't save files above configured size

		src_path = settings.get("src_path")
		target_path = settings.get("target_path")
		file_path = view.file_name()
		
		if (pathManager.check_folder_to_sync(file_path) == False):
			print "This must no be copy - End of sync"
			return
		
		if view.size() > settings.get("max_file_size_bytes"):
			print 'File not synced, file too large (%d bytes)' % view.size()
			return

		self.copy_file(src_path, target_path, file_path)

	def copy_file(self, src_path, target_path, file_path, force = False):
		#copy file to target if has changed
		#or you cant force to overwrite anyway
		path_to_copy = pathManager.create_target_path(file_path)
		print 'path to copy', path_to_copy

		# make sure that we have a directory to write into
		if os.access(path_to_copy, os.F_OK) == False:
			os.makedirs(path_to_copy)

		shutil.copy(file_path, path_to_copy)
		