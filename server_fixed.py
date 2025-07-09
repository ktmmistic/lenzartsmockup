#!/usr/bin/env python3
import http.server
import socketserver
import os
import mimetypes

PORT = 3000

print("🎨 Lenz Arts website starting...")
print(f"✅ Server will be at http://0.0.0.0:{PORT}")

class FixedHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)
    
    def do_GET(self):
        # Handle specific routes without .html extension
        original_path = self.path
        clean_path = self.path.strip('/').split('?')[0]  # Remove query params too
        
        print(f"📍 Request: {original_path} → clean_path: '{clean_path}'")
        
        # Route mapping
        routes = {
            '': 'index.html',
            'home': 'index.html',
            'art-materials': 'art-materials.html',
            'framing': 'framing.html',
            'demos': 'demos.html',
            'gift-cards': 'gift-cards.html',
            'history': 'history.html',
            'contact': 'contact.html',
            'legal': 'legal.html',
            'privacy': 'privacy.html',
            'buyersguide': 'buyersguide.html'
        }
        
        if clean_path in routes:
            # Serve the file directly
            file_path = routes[clean_path]
            print(f"✅ Serving file: {file_path}")
            
            if os.path.exists(file_path):
                # Set content type
                content_type, _ = mimetypes.guess_type(file_path)
                if content_type is None:
                    content_type = 'text/html'
                
                # Read and serve file
                try:
                    with open(file_path, 'rb') as f:
                        content = f.read()
                    
                    self.send_response(200)
                    self.send_header('Content-Type', content_type)
                    self.send_header('Content-Length', str(len(content)))
                    self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
                    self.send_header('Pragma', 'no-cache')
                    self.send_header('Expires', '0')
                    self.end_headers()
                    self.wfile.write(content)
                    return
                except Exception as e:
                    print(f"❌ Error reading file {file_path}: {e}")
                    self.send_error(500, f"Internal server error reading {file_path}")
                    return
            else:
                print(f"❌ File not found: {file_path}")
                self.send_error(404, f"File not found: {file_path}")
                return
        else:
            print(f"⚠️ No routing rule for: '{clean_path}', using default handler")
            # Use default handler for static files (CSS, images, etc.)
            return super().do_GET()

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

if __name__ == "__main__":
    with socketserver.TCPServer(("0.0.0.0", PORT), FixedHandler) as httpd:
        print(f"🚀 Server running at http://0.0.0.0:{PORT}")
        print("Press Ctrl+C to stop the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped")