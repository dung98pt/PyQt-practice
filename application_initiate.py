from PyQt5 import QtWidgets, QtCore
import os, glob
import ntpath
def compile_view():
    "compile view file"
    if os.path.exists("views/ui/"):
        for filename in glob.glob('views/ui/*.ui'):
            output_filename = ntpath.splitext(ntpath.basename(filename))[0]+"_ui.py"
            command = "pyuic5 "+filename.replace("\\", "/")+" -o "+"views/"+output_filename
            os.system(command)
            # fix icon folder location
            f = open("views/"+output_filename, "r+", encoding="utf8")
            script = f.read().replace("../../icons/", "icons/")
            f.seek(0)
            f.truncate()
            f.write(script)
            f.close()

compile_view()