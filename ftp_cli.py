#!/usr/bin/python
#python version: Python 3.5.2
# -*- coding: utf-8 -*-

# FTP CLI interface
import sys
import os
try:
    import ftplib # on importe le module et on la renomme juste pour le script en "ftp"
except ImportError:
    sys.exit("""You need ftplib!
                install it from http://pypi.python.org/pypi/foo
                or run pip install ftplib.""")
 
class ftp_cli:
    
    #logger class need to be created
    def __init__(self, source, login, password, logger):
        self.source = source
        self.login = login
        self.password = password
        self.logger = logger

    #to split a repo URL + sub directoies
    def getRepoInfos(self):
        return (self.source.split("/",1)[0], '/'+self.source.split("/",1)[1])
    
    #to initialise an ftp connection
    def initFTP(self, repo, tree):
        ftp = ftplib.FTP(repo)
        ftp.login(self.login, self.password)
        ftp.cwd(tree)
        return ftp
    
    #to list ftp directory content
    def dirListing(self, ftp):
        data = []
        ftp.dir(data.append)
        #ftp.quit()
 
        for line in data:
            print (line)
    
    #to retrieve a file
    def getFile(self, ftp, filename):
        try:
            ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
        except:
            print ("Error")
    
    #to upload a file
    def uploadFile(self, ftp, file):
        ext = os.path.splitext(file)[1]

        if ext in (".txt", ".htm", ".html"):
            ftp.storlines("STOR " + file, open(file))
        else:
            ftp.storbinary("STOR " + file, open(file, "rb"), 1024)
 
        ftp = ftplib.FTP("127.0.0.1")
        ftp.login("username", "password")

#####main test #####

#to read files
cli_source = ftp_cli("ftp.wipo.int/pub/its4nice/ITSupport_and_download_area/19631114/Documentation/", "", "", "")
(repo, tree) = cli_source.getRepoInfos()
ftp_source = cli_source.initFTP(repo, tree)
cli_source.dirListing(ftp_source)
cli_source.getFile(ftp_source, "NICE_taxonomy_specification_V3-10.doc")
ftp_source.quit()


#to store files
cli_destination = ftp_cli("127.0.0.1/pub/", "", "", "")
ftp_destination = cli_source.initFTP(repo, tree)
cli_destination.uploadFile(ftp_destination, "example.pdf")
