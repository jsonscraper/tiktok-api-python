import os,json,sys
sys.path.insert(0,'src')
from jsonscraper_tiktok import Client,APIError
try:
 c=Client('contract-secret',base_url=os.environ['BASE_URL'],timeout=float(os.getenv('TIMEOUT','3')),retries=int(os.getenv('RETRIES','0')))
 data=c.request(os.environ['API_PATH'],video_id='a&b?x=1+/Ю',license_key='override',count=0,flag=False)
 if isinstance(data,bytes):sys.stdout.buffer.write(data)
 else:print(json.dumps(data))
except APIError as e:print(json.dumps({'error':e.status}))
except Exception:print(json.dumps({'error':'transport'}))
