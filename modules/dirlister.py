import os

def run(**args):

    print "[*] In dirlister modeule."
    files = os.listdir(".")

    return str(files)


