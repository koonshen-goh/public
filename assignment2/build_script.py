# Python 3.10
import os
import re
import stat
import pathlib

def updateSconstruct(SConstructPath: pathlib.Path, BuildNum: str):
    # "Update the build number in the SConstruct file"
    # Assumes file size is small, read entire file into memory
    buffer = open(SConstructPath, 'r').read()
    # Replace build number
    regexPattern = "(config\.version\s*=\s*Version\(.*point\s*=\s*)(\d+)(.*\))"
    regexSubsitution = f'\g<1>{BuildNum}\g<3>'
    buffer = re.sub(regexPattern, regexSubsitution, buffer, 1, flags=re.DOTALL)
    # Overwrite file
    with open(SConstructPath, 'w') as fout:
        fout.write(buffer)

def updateVersion(VersionPath: pathlib.Path, BuildNum: str):
    # "Update the build number in the VERSION file"
    # Assumes file size is small, read entire file into memory
    buffer = open(VersionPath, 'r').read()
    # Replace build number
    regexPattern = "(ADLMSDK_VERSION_POINT\s*=\s*)(\d+)"
    regexSubsitution = f'\g<1>{BuildNum}'
    buffer = re.sub(regexPattern, regexSubsitution, buffer, 1, flags=re.DOTALL)
    # Overwrite file
    with open(VersionPath, 'w') as fout:
        fout.write(buffer)

if __name__ == "__main__":
    SourcePath = os.environ["SourcePath"]
    BuildNum = os.environ["BuildNum"]
    
    SConstructPath = pathlib.Path(SourcePath, "develop", "global", "src", "SConstruct")
    VersionPath = pathlib.Path(SourcePath, "develop", "global", "src", "VERSION")
    # mode = 0755, rwx r-x r-x
    fileMode = stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH
    os.chmod(SConstructPath, fileMode)
    updateSconstruct(SConstructPath, BuildNum)
    os.chmod(VersionPath, fileMode)
    updateVersion(VersionPath, BuildNum)
