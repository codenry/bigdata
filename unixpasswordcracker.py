#!/usr/bin/python

import crypt

def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word,salt)
        if (cyptWord == cryptPass):
            print ("[+] Found Password: "+word+"\n")
            return

    print ("[-] Password Not Found.\n")
    return
#!Yo yo yo! 
def main():
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print ("[*] Cracking Password For:; " + user)
            testPass(CryptPass)

    if __main__ == "__main__":
        main()
