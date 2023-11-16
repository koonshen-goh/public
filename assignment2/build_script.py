# Python 3.10
import os
import re
import stat
import pathlib
import argparse

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
    # Get variables from command line or env vars
    parser = argparse.ArgumentParser(description='build script that updates build numbers for project')
    parser.add_argument('-s', '--source', default=os.environ.get('SourcePath', None), help='root path for the source code')
    parser.add_argument('-b','--build', default=os.environ.get('BuildNum', None), help='build number')
    args = parser.parse_args()
    if args.source == None:
        # Use current file path if path is not given
        args.source = pathlib.Path(__file__).parent
    if args.build == None:
        # Throw exception if build number is not specified
        raise Exception("BuildNum is not defined")
    
    SConstructPath = pathlib.Path(args.source, "develop", "global", "src", "SConstruct")
    VersionPath = pathlib.Path(args.source, "develop", "global", "src", "VERSION")
    # mode = 0755, rwx r-x r-x
    fileMode = stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH
    os.chmod(SConstructPath, fileMode)
    updateSconstruct(SConstructPath, args.build)
    os.chmod(VersionPath, fileMode)
    updateVersion(VersionPath, args.build)
