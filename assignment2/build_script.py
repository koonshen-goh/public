import os
import re

def updateSconstruct():
    # "Update the build number in the SConstruct file"
    os.chmod(os.path.join(os.environ["SourcePath"],"develop","global","src","SConstruct"), 0755)
    fin = open(os.path.join(os.environ["SourcePath"],"develop","global","src","SConstruct"), 'r')
    fout = open(os.path.join(os.environ["SourcePath"],"develop","global","src","SConstruct1"), 'w')
    for line in fin:
        line=re.sub("point\=[\d]+","point="+os.environ["BuildNum"],line)
        fout.write(line)
    fin.close()
    fout.close()
    os.remove(os.path.join(os.environ["SourcePath"],"develop","global","src","SConstruct"))
    os.rename(os.path.join(os.environ["SourcePath"],"develop","global","src","SConstruct1"),
    os.path.join(os.environ["SourcePath"],"develop","global","src","SConstruct"))

def updateVersion():
    # "Update the build number in the VERSION file"
    os.chmod(os.path.join(os.environ["SourcePath"],"develop","global","src","VERSION"), 0755)
    fin = open(os.path.join(os.environ["SourcePath"],"develop","global","src","VERSION"), 'r')

