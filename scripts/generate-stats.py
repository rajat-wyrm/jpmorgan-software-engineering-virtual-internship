#!/usr/bin/env python3
import subprocess
import json
from datetime import datetime

def get_commit_stats():
    result = subprocess.run(['git', 'log', '--pretty=format:%h|%an|%ad|%s'], 
                          capture_output=True, text=True)
    commits = []
    for line in result.stdout.split('\n'):
        if line:
            parts = line.split('|')
            if len(parts) >= 4:
                commits.append({
                    'hash': parts[0],
                    'author': parts[1],
                    'date': parts[2],
                    'message': parts[3]
                })
    return commits

def get_file_stats():
    result = subprocess.run(['git', 'ls-files'], capture_output=True, text=True)
    files = result.stdout.split('\n')
    extensions = {}
    for file in files:
        if '.' in file:
            ext = file.split('.')[-1]
            extensions[ext] = extensions.get(ext, 0) + 1
    return extensions

if __name__ == '__main__':
    commits = get_commit_stats()
    files = get_file_stats()
    
    stats = {
        'total_commits': len(commits),
        'total_files': len([f for f in files if f]),
        'file_types': files,
        'last_updated': datetime.now().isoformat()
    }
    
    with open('stats.json', 'w') as f:
        json.dump(stats, f, indent=2)
    
    print(f'Stats generated: {len(commits)} commits, {stats["total_files"]} files')
