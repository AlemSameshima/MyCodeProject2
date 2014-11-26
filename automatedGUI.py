import wx 
import sys
import os
import datetime as dt
import time
import shutil
import sqlite3


conn = sqlite3.connect("fileCheck.db")
c = conn.cursor()

def tableCreate():
    c.execute("CREATE TABLE TimeLog (TimeOfExecution INT)")



def listFile(sourcepath, destinationpath):
    folder = os.listdir(sourcepath)
    for path in folder:
        bk = sourcepath +'\\' +  path
        mt = dt.datetime.fromtimestamp(os.path.getmtime(bk))
        ct = dt.datetime.now()
        tdelta = ct - mt        
        if tdelta < (dt.timedelta(hours = 24)):
            shutil.copy2(bk, destinationpath)
            print (tdelta)
            print('Files Got Modifed')



class windowClass(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)

        self.basicGUI()


    def directory(self,event):
        global sourcepath
        dialog = wx.DirDialog(None, "Choose Source Folder:",style=wx.DD_DEFAULT_STYLE)
        if dialog.ShowModal() == wx.ID_OK:
           sourcepath = dialog.GetPath()
           print(sourcepath)
        dialog.Destroy()
        

    def destinationdirectory(self, event):
        global sourcepath
        global destinationpath
        dialog = wx.DirDialog(None, "Choose Destination Folder",style=wx.DD_DEFAULT_STYLE)
        if dialog.ShowModal() == wx.ID_OK:
           destinationpath = dialog.GetPath()
           print(destinationpath)
           

    def runit (self, event):
        global sourcepath
        global destinationpath
        ct = dt.datetime.now()
        c.execute("INSERT INTO TimeLog(TimeOfExecution) VALUES(?)",
                  ((ct,)))
        listFile(sourcepath, destinationpath)

    def fileCheck(self, event):
        c.execute("SELECT MAX(TimeOfExecution) FROM TimeLog")
        print((c.fetchall()))
            
        
    
            

    def basicGUI(self):
        panel = wx.Panel(self)
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()
        editButton = wx.Menu()

        exitItem = wx.MenuItem(fileButton, wx.ID_EXIT, '\tCtrl+Q')
        exitItem.SetBitmap(wx.Bitmap('Folder/iamout.jpg'))
        fileButton.AppendItem(exitItem)

        self.button1 = wx.Button(self, id=-1, label='Run it', pos=(8, 100), size=(175, 28))
        self.button1.Bind(wx.EVT_BUTTON, self.runit)
                                           
        self.button1 = wx.Button(self, id=-1, label='Choose Source Folder', pos=(8, 20), size=(175, 28))
        self.button1.Bind(wx.EVT_BUTTON, self.directory)

        self.button1 = wx.Button(self, id=-1, label='Choose Destination Folder', pos=(8, 60), size=(175, 28))
        self.button1.Bind(wx.EVT_BUTTON, self.destinationdirectory)

        self.button1 = wx.Button(self, id=-1, label='Retrieve Lastest fileCheck', pos=(200, 20), size=(175, 28))
        self.button1.Bind(wx.EVT_BUTTON, self.fileCheck)

        
                            
        menuBar.Append(fileButton,'File')
        menuBar.Append(editButton, 'Edit')
        
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)
        
        self.SetTitle('Automated File Transfer')
        self.Show(True)



    def Quit(self,e):
        self.Close()
        
              
def main():
    app = wx.App()
    windowClass(None)
    app.MainLoop()

main()

conn.commit()





