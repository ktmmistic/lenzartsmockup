#!/usr/bin/env python3
import http.server
import socketserver
import os
import sys

PORT = 8000
DIRECTORY = "/home/runner/workspace"

class ReliableHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()
    
    def log_message(self, format, *args):
        sys.stdout.write("%s - - [%s] %s\n" %
                         (self.address_string(),
                          self.log_date_time_string(),
                          format%args))
        sys.stdout.flush()

if __name__ == "__main__":
    os.chdir(DIRECTORY)
    print(f"Starting Lenz Arts server on port {PORT}...")
    print(f"Serving files from: {DIRECTORY}")
    
    try:
        httpd = socketserver.TCPServer(("0.0.0.0", PORT), ReliableHandler)
        httpd.allow_reuse_address = True
        print(f"🎨 Lenz Arts website running at http://0.0.0.0:{PORT}")
        print("✅ Server ready - check your Replit preview")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
        httpd.shutdown()
    except Exception as e:
        print(f"❌ Server error: {e}")
        sys.exit(1)