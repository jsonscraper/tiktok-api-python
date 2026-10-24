"""Black-box transport contract tests; no paid requests and no credentials."""
import http.server,threading,subprocess,os,json,sys,pathlib,time,tempfile
ROOT=pathlib.Path(__file__).resolve().parents[1]
os.chdir(ROOT)
requests=[]
class Server(http.server.BaseHTTPRequestHandler):
 def log_message(self,*args):pass
 def do_GET(self):
  from urllib.parse import urlsplit,parse_qs
  url=urlsplit(self.path);requests.append((url.path,parse_qs(url.query),self.command))
  status=200;body=b'{"status":"ok","id":18446744073709551616,"tiktok":{"aweme_detail":{"aweme_id":"7106855913906081070"}}}'
  content='application/json'
  if url.path=='/retry':status=429
  if url.path=='/forbidden':status=403
  if url.path=='/redirect':status=302
  if url.path=='/binary':body=b'binary-content';content='application/octet-stream'
  if url.path=='/malformed':body=b'not-json'
  if url.path=='/application-error':body=b'{"status":"fail","rate_limit_reached":true}'
  if url.path=='/slow':time.sleep(.2)
  self.send_response(status);self.send_header('Content-Type',content);self.send_header('Retry-After','0')
  if status==302:self.send_header('Location','/stolen')
  self.end_headers()
  try:self.wfile.write(body)
  except (BrokenPipeError,ConnectionResetError):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),Server)
threading.Thread(target=server.serve_forever,daemon=True).start()
base='http://127.0.0.1:'+str(server.server_port)
if (ROOT/'pyproject.toml').exists():lang='python';cmd=[sys.executable,'tests/runner.py']
elif (ROOT/'package.json').exists():lang='node';cmd=['node','tests/runner.mjs']
elif (ROOT/'go.mod').exists():
 lang='go';exe=tempfile.mktemp(prefix='jsonscraper-contract-');subprocess.run(['go','build','-o',exe,'./tests/runner.go'],check=True);cmd=[exe]
elif (ROOT/'pom.xml').exists():
 lang='java';dest=tempfile.mkdtemp(prefix='jsonscraper-java-test-');subprocess.run(['javac','-d',dest]+[str(p) for p in (ROOT/'src/main/java').rglob('*.java')]+['tests/Runner.java'],check=True);cmd=['java','-cp',dest,'Runner']
elif (ROOT/'JsonScraper.csproj').exists():
 lang='dotnet';subprocess.run(['dotnet','build','tests/Runner.csproj','--nologo','-o','tests/build'],check=True);cmd=['dotnet','tests/build/Runner.dll']
else:lang='php';cmd=[os.environ.get('PHP_BIN','php'),'tests/runner.php']
def run(path,**env):
 before=len(requests);e=os.environ.copy();e.update(BASE_URL=base,API_PATH=path,RETRIES='0',TIMEOUT='3',PRODUCT='tiktok');e.update(env);e['NO_PROXY']='127.0.0.1,localhost';e['no_proxy']='127.0.0.1,localhost'
 r=subprocess.run(cmd,env=e,capture_output=True,timeout=20)
 assert r.returncode==0,(lang,r.stderr.decode())
 assert b'contract-secret' not in r.stdout+r.stderr,'Credential leaked in output'
 return r.stdout,requests[before:]
raw,req=run('/getVideoByID');d=json.loads(raw)
assert d['status']=='ok' and str(d['id'])=='18446744073709551616',(lang,raw)
assert len(req)==1 and req[0][2]=='GET'
q=req[0][1];assert q['license_key']==['contract-secret'] and q['video_id']==['a&b?x=1+/Ю'] and q['count']==['0'] and q['flag']==['false'],q
raw,req=run('/getUserInfo',PRODUCT='instagram');assert json.loads(raw)['status']=='ok'
raw,req=run('/forbidden');assert json.loads(raw)['error']==403 and len(req)==1
raw,req=run('/retry',RETRIES='1');assert json.loads(raw)['error']==429 and len(req)==2
raw,req=run('/redirect');assert json.loads(raw)['error']==302 and len(req)==1
raw,req=run('//attacker.example/leak');assert json.loads(raw)['error']=='transport' and not req
raw,req=run('/binary');assert raw==b'binary-content'
raw,req=run('/application-error');assert json.loads(raw)['status']=='fail'
raw,req=run('/slow',TIMEOUT='0.05');assert json.loads(raw)['error']=='transport'
raw,req=run('/malformed')
if lang in ['python','node','php']:assert json.loads(raw)['error']=='transport'
else:assert raw==b'not-json'
server.shutdown()
print(lang+': 10 contract checks passed')
