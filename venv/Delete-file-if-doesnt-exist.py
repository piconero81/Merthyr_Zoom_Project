import os
def main():
    filePath = 'C:\Users\wanka\AppData\Local\Google\Chrome\UserData\Profile 8\Network\Cookies';
    # Remove a file
    os.remove(['"C:\Users\wanka\AppData\Local\Google\Chrome\UserData\Profile 8\Network\Cookies"'])
    FileNotFoundError
    # As file at filePath is deleted now, so we should check if file exists or not not before deleting them
    if os.path.exists(filePath):
        os.remove(filePath)
    else:
        print("Can not delete the file as it doesn't exists")
    # Handle errors while calling os.remove()
    try:
        os.remove(filePath)
    except:
        print("Error while deleting file ", filePath)
    # Handle errors while calling os.ulink()
    try:
        os.ulink(filePath)
    except:
        print("Error while deleting file ", filePath)
if __name__ == '__main__':
    main()