import sublime
import sublime_plugin

import os


PACKAGE_NAME = "Gams"


class GamsCommand(sublime_plugin.TextCommand):

	def run(self, edit):	

		input_file_path = os.path.split(self.view.file_name())[0]
		input_file_name = os.path.split(self.view.file_name())[1]

		file_name_noSuff = input_file_name.rsplit( ".",1)[0]

		output_file_name = file_name_noSuff + ".lst"
		output_file_path = input_file_path

		if input_file_name.endswith("gms"):

			gams_lib_path = "export PATH=$PATH:\"/Applications/GAMS24.9/GAMS Terminal.app/../sysdir\"; "
			cd_dir = "cd " + input_file_path + "; "
			gams_execute = "gams " + input_file_name + " LogOption=2"
			cmd = gams_lib_path + cd_dir + gams_execute

			os.system(cmd)

			sublime.active_window().open_file(output_file_path + "/" + output_file_name)

		else:

			sublime.error_message("Wrong file format!\nPlease select a \".gms\" file.")
