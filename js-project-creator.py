import sublime, sublime_plugin
import threading
import os
from shutil import copy2

class CreateJsProjectCommand(sublime_plugin.WindowCommand):
  def run(self):
    folders = self.window.folders()
    if len(folders):
      folder = folders[0]
      thread = CopyFileThread(folder)
      thread.start()


class CopyFileThread(threading.Thread):
  def __init__(self, folder):
    self.folder = folder
    threading.Thread.__init__(self)

  def run(self):
    pathname = os.path.join(os.path.dirname(__file__), 'resource')
    files = os.listdir(pathname)
    try:
      for file in files:
        srcname = os.path.join(pathname, file)
        distname = os.path.join(self.folder, file)
        copy2(srcname, distname)
    except Exception as e:
      print('copy file error when copy ', e)

