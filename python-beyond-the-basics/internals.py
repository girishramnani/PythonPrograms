__author__ = 'Girish'
import ctypes as ct
import win32com.client as com
app = com.Dispatch("WMPlayer.OCX")
import win32gui as gui


t = ct.cdll.msvcrt
print(t._getdrives())