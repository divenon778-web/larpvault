import http.server, socketserver, json, os, random, urllib.parse

CLIPS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'larpclips')

def get_clip_files():
    if not os.path.isdir(CLIPS_DIR):
        return []
    exts = {'.mp4', '.mov', '.avi', '.mkv', '.webm'}
    return [f for f in os.listdir(CLIPS_DIR) if os.path.splitext(f)[1].lower() in exts]

class H(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Strip RSC query for static - serve HTML instead of 404 for any dashboard RSC
        if '?_rsc=' in self.path:
            raw = self.path.split('?')[0]
            check = '.' + raw
            if not os.path.exists(check) and not os.path.exists(check + '/index.html'):
                if raw.startswith('/dashboard'):
                    self.path = '/dashboard/'
                else:
                    self.path = raw
            else:
                self.path = raw
        
        # Handle dashboard routes - serve main dashboard for all /dashboard/* paths
        if self.path.startswith('/dashboard/') and self.path != '/dashboard/':
            # Check if file exists
            check = '.' + self.path
            if not os.path.exists(check) and not os.path.exists(check + '/index.html'):
                self.path = '/dashboard/'
        
        if self.path.startswith('/api/auth/session'):
            self.send_response(200)
            self.send_header('Content-Type','application/json')
            self.send_header('Cache-Control','no-store')
            self.end_headers()
            # Check larp_auth is set via query? Just return fake user larp
            data={"user":{"id":"1","username":"larp","email":"larp@larpvault.co","vendorBalanceCents":0,"customerBalanceCents":0,"avatar":None},"expires":"2099-01-01T00:00:00.000Z"}
            self.wfile.write(json.dumps(data).encode())
            return
        if self.path.startswith('/api/safety-check'):
            self.send_response(200)
            self.send_header('Content-Type','application/json')
            self.send_header('Cache-Control','no-store')
            self.end_headers()
            self.wfile.write(json.dumps({"safe":True}).encode())
            return
        if self.path.startswith('/api/clips/stock'):
            self.send_response(200)
            self.send_header('Content-Type','application/json')
            self.send_header('Cache-Control','no-store')
            self.end_headers()
            files = get_clip_files()
            self.wfile.write(json.dumps({"count": len(files), "files": files}).encode())
            return
        if self.path.startswith('/api/clips/purchase'):
            parsed = urllib.parse.urlparse(self.path)
            params = urllib.parse.parse_qs(parsed.query)
            qty = int(params.get('qty', ['1'])[0])
            files = get_clip_files()
            if not files:
                self.send_response(200)
                self.send_header('Content-Type','application/json')
                self.send_header('Cache-Control','no-store')
                self.end_headers()
                self.wfile.write(json.dumps({"error":"no stock","clips":[]}).encode())
                return
            picked = random.choices(files, k=min(qty, len(files)))
            unique = list(dict.fromkeys(picked))
            clips_out = [{"name": n, "url": "/larpclips/" + urllib.parse.quote(n)} for n in unique]
            self.send_response(200)
            self.send_header('Content-Type','application/json')
            self.send_header('Cache-Control','no-store')
            self.end_headers()
            self.wfile.write(json.dumps({"clips": clips_out, "stock": len(files)}).encode())
            return
        if self.path.startswith('/api/market/stats'):
            self.send_response(200)
            self.send_header('Content-Type','application/json')
            self.send_header('Cache-Control','no-store')
            self.end_headers()
            files = get_clip_files()
            stock = len(files)
            self.wfile.write(json.dumps({"totalClips":stock,"totalRobux":stock,"rate":"$0.25/clip","inStock": stock > 0}).encode())
            return
        if self.path.startswith('/api/user/balance'):
            self.send_response(200)
            self.send_header('Content-Type','application/json')
            self.send_header('Cache-Control','no-store')
            self.end_headers()
            self.wfile.write(json.dumps({"vendorBalanceCents":0,"customerBalanceCents":0}).encode())
            return
        if self.path.startswith('/api/user/clips-orders') or self.path.startswith('/api/user/purchase-stats') or self.path.startswith('/api/user/vendor-stats'):
            self.send_response(200)
            self.send_header('Content-Type','application/json')
            self.send_header('Cache-Control','no-store')
            self.end_headers()
            self.wfile.write(json.dumps([]).encode())
            return
        if self.path.startswith('/api/user/sales') or self.path.startswith('/api/vendor/listings'):
            self.send_response(200)
            self.send_header('Content-Type','application/json')
            self.send_header('Cache-Control','no-store')
            self.end_headers()
            self.wfile.write(json.dumps([]).encode())
            return
        if self.path.startswith('/api/user/switch-mode'):
            self.send_response(200)
            self.send_header('Content-Type','application/json')
            self.send_header('Cache-Control','no-store')
            self.end_headers()
            self.wfile.write(json.dumps({"ok":True}).encode())
            return
        return super().do_GET()
    def end_headers(self):
        self.send_header('Cache-Control','no-store, no-cache, must-revalidate')
        self.send_header('Pragma','no-cache')
        self.send_header('Expires','0')
        super().end_headers()
port = int(os.environ.get("PORT", 8787))
with socketserver.TCPServer(("",port),H) as httpd:
    print(f"serving at http://localhost:{port} - no-cache + api mock")
    httpd.serve_forever()
