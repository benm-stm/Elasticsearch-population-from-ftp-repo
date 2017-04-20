#!/usr/bin/python
# -*- coding: utf-8 -*-
# FTP CLI interface

import sys
try:
    import ftplib # on importe le module et on la renomme juste pour le script en "ftp"
except ImportError:
    sys.exit("""You need ftplib!
                install it from http://pypi.python.org/pypi/foo
                or run pip install ftplib.""")
 
class ftp_cli:

    def __init__(self, source, login, password, logger):
        self.source = source
        self.login = login
        self.password = password
        self.logger = logger

    def getRepoInfos(self):
        return (self.source.split("/",1)[0], '/'+self.source.split("/",1)[1])

    def initFTP(self, repo, tree):
        ftp = ftplib.FTP(repo)
        ftp.login(self.login, self.password)
        ftp.cwd(tree)
        return ftp

    def dirListing(self, ftp):
        data = []
        ftp.dir(data.append)
        #ftp.quit()
 
        for line in data:
            print (line)
    
    def getFile(self, ftp, filename):
        try:
            ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
        except:
            print ("Error")
        ftp.quit()
 

#####main test #####

cli = ftp_cli("ftp.wipo.int/pub/its4nice/ITSupport_and_download_area/19631114/Documentation/", "", "", "")
(repo, tree) = cli.getRepoInfos()
ftp = cli.initFTP(repo, tree)
cli.dirListing(ftp)
cli.getFile(ftp, "NICE_taxonomy_specification_V3-10.doc")
