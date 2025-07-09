#!/usr/bin/env python3
import http.server
import socketserver
import os
import signal
import sys

class LenzArtsHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve index.html for clean URLs to enable client-side routing
        clean_urls = ['/', '/art-materials', '/framing', '/demos', '/gift-cards', '/history', '/contact', '/legal', '/privacy', '/buyersguide']
        
        if self.path in clean_urls:
            self.path = '/index.html'
        
        return super().do_GET()
    
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def signal_handler(sig, frame):
    print('\nShutting down server...')
    sys.exit(0)

if __name__ == "__main__":
    PORT = 8080
    os.chdir('/home/runner/workspace')
    
    signal.signal(signal.SIGINT, signal_handler)
    
    with socketserver.TCPServer(("0.0.0.0", PORT), LenzArtsHandler) as httpd:
        print(f"🎨 Lenz Arts server running on http://0.0.0.0:{PORT}")
        print(f"✅ Client-side routing enabled for clean URLs")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")