#!/usr/bin/env python
import sys
import urllib.request
import urllib.parse
import urllib.error
import os
import tempfile
import subprocess

def main():
    print("Downloading get-pip.py...")
    url = 'https://bootstrap.pypa.io/get-pip.py'
    
    try:
        response = urllib.request.urlopen(url)
        content = response.read()
        
        with tempfile.NamedTemporaryFile(mode='wb', suffix='.py', delete=False) as f:
            f.write(content)
            temp_file = f.name
        
        print("Installing pip...")
        subprocess.run([sys.executable, temp_file] + sys.argv[1:])
        
        os.unlink(temp_file)
        print("Pip installation complete!")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
