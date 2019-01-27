from bottle import route, run
from dbfsapi import DatabricksFileAPI
import json
from jinja2 import Template

dbfapi = DatabricksFileAPI(
    host='http://localhost:8001',
    token='',
    api_route='/'
)

template = Template(
"""<html><body>
<table style="border: 10px solid white; width: 100%;" rules="groups">
<thead style="border-bottom: 1px solid black; text-align: left;">
  <tr>
    <th>Path</th><th>Directory</th><th>Size</th>
  </tr>
</thead>
<tbody>
{% for row in directories %}
  <tr>
    <td><a href=/{{ row.path }}>{{ row.path.split('/')[-1] }}</a></td>
    <td>{{ row.is_dir }}</td>
    <td>{{ row.file_size }}</td>
  </tr>
{% endfor %}
{% for row in files %}
  <tr>
    <td>{{ row.path.split('/')[-1] }}</td>
    <td>{{ row.is_dir }}</td>
    <td>{{ row.file_size }}</td>
  </tr>
{% endfor %}
</tbody>
</table>
</body></html>
"""
)

def table(j):
    d = sorted(
            filter(lambda x: x.get('is_dir'), j),
            key=lambda x: (not x.get('is_dir'), x.get('path').lower())
        )
    f = sorted(
            filter(lambda x: not x.get('is_dir'), j),
            key=lambda x: (not x.get('is_dir'), x.get('path').lower())
        )
    return template.render(directories=d, files=f)
    
    
@route('<apiurl:path>')
def test(apiurl):
    apiurl = apiurl.lstrip('/')
    print('SHOWING:', apiurl)
    
    ret = dbfapi.List(apiurl)
    
    return table(ret)
    
run(host='localhost', port=8002)


