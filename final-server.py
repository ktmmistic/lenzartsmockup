#!/usr/bin/env python3
import http.server
import socketserver
import os
from urllib.parse import urlparse

class LenzArtsHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL path
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        # Add CORS headers
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        
        # For clean URLs, always serve index.html
        # The client-side router will handle the rest
        if path.endswith('.html') or path.endswith('.css') or path.endswith('.js') or path.endswith('.png') or path.endswith('.jpg') or path.endswith('.svg'):
            # Serve actual files
            return super().do_GET()
        else:
            # Serve index.html for all clean URLs
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            with open('index.html', 'rb') as f:
                self.wfile.write(f.read())

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    PORT = 3000
    with socketserver.TCPServer(("0.0.0.0", PORT), LenzArtsHandler) as httpd:
        print(f"🎨 Lenz Arts server running on http://0.0.0.0:{PORT}")
        httpd.serve_forever()