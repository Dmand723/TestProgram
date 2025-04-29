def openFileSafe(filename,perm):
    import datetime as dt
    openedTime = dt.datetime.now()
    try:
        file = open(filename,perm)
    except FileNotFoundError as e:
        print("you had the following error")
        print(e)
        answer = input("would you like to create this file" + filename + "(y/n)")
        f = open("Assets\ErrorLog\errorlog.txt", "a+")
        f.write(str(openedTime)+ "\n")
        f.write(str(e)+"\n")
        if answer == "y":
            f.write("user created a new file\n")
            file = open(filename,"w")
            f.close
        else:
            f.write("user didnt create a new file\n")
            f.close
            quit()
    except OSError as e:
        f = open("Assets\ErrorLog\errorlog.txt","a+")
        f.write(str(openedTime)+"\n")
        f.write(str(e))
        f.close()
        print("you had the following error")
        print(e)
        input("Press enter to exit")
        quit()
    except Exception as e:
        f = open("Assets/errorLogs/errorLog.txt","a+")
        f.write(str(openedTime),+'\n')
        f.write(str(e))
        f.close
        print("You have the following error \n", e)
        input("Press enter to exit")
        quit()
    return file

def nextLine(openFile):
        line = openFile.readline()
        line = line.strip('\n')
        line = line.replace("~","\n")
        return line