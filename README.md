# databrick-file-api
A wrapper for the Databricks DBFS API to allow web-browsing of the databricks files using a bottle app.

### Example
To see an example via browsing your local files:
- Launch `filelistapp.py` and `bottleapp.py`:
```
python filelistapp.py
python bottleapp.py
```
- Browse to http://localhost:8002/C:/ to start exploring.

This will mimic the Databricks API (List only for now) on your local files.  `filelistapp` launches a bottle app that allows enables browsing of the local files using an API very similar to the Databricks API.  `bottleapp` also launches a bottle app that makes API calls to the `filelistapp` server.
