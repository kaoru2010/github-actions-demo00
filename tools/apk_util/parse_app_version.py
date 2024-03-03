import re
import sys

re_version_code = re.compile(r'android:versionCode="([0-9]+)"')
re_version_name = re.compile(r'android:versionName="([0-9.]+)"')

def parse_version_code(line):
    ma = re_version_code.search(line)
    return ma.group(1) if ma else None

def parse_version_name(line):
    ma = re_version_name.search(line)
    return ma.group(1) if ma else None

def parse_version_code_and_name(lines):
    version_code = None
    version_name = None
    for line in lines:
        if version_code is None:
            version_code = parse_version_code(line)

        if version_name is None:
            version_name = parse_version_name(line)

        if version_code and version_name:
            break

    return version_code, version_name

def main():
    version_code, version_name = parse_version_code_and_name(sys.stdin)
    print("version_code={}".format(version_code))
    print("version_name={}".format(version_name))
    return 0

if __name__ == '__main__':
    sys.exit(main())
