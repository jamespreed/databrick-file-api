from bottle import request, route, run
import os
import json

@route('/list')
def list_files():
    path = request.query.get('path')
    if path=='favicon.ico':
        return '{}'
    contents = []
    for f in os.listdir(os.path.abspath(path)):
        fpath = os.path.join(os.path.abspath(path), f).replace('\\','/')
        try:
            contents.append(
                {
                    'path': fpath, 
                    'is_dir': os.path.isdir(fpath), 
                    'file_size': 0 if os.path.isdir(fpath) else os.path.getsize(fpath)
                }
            )
        except:
            print('Error - Path not added:', f)
    return json.dumps(contents)
    
run(host='localhost', port=8001)