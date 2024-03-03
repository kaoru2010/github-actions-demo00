import unittest
from parse_app_version import parse_version_code_and_name

class ParseAppVersionTest(unittest.TestCase):

    def test_parse_version_code_and_name(self):
        lines = """
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.en_japan.ambi"
    android:versionCode="15"
    android:versionName="3.1" >
</manifest>
        """

        version_code, version_name = parse_version_code_and_name(lines.splitlines())

        self.assertEqual(version_code, '15')
        self.assertEqual(version_name, '3.1')

if __name__ == '__main__':
    unittest.main()
