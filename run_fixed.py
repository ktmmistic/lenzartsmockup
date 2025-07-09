#!/usr/bin/env python3
import http.server
import socketserver
import os

PORT = 3000

print("🎨 Lenz Arts website starting...")
print(f"✅ Server will be at http://0.0.0.0:{PORT}")

class RoutingHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)
    
    def do_GET(self):
        # Parse the request path
        path = self.path.split('?')[0].strip('/')
        print(f"📍 Request: {self.path} → clean path: '{path}'")
        
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
        
        # Check if this is a routed path
        if path in routes:
            file_to_serve = routes[path]
            print(f"✅ Routing '{path}' → '{file_to_serve}'")
            
            # Check if the file exists
            if os.path.exists(file_to_serve):
                try:
                    # Read the file
                    with open(file_to_serve, 'rb') as f:
                        content = f.read()
                    
                    # Send the response
                    self.send_response(200)
                    self.send_header('Content-Type', 'text/html; charset=utf-8')
                    self.send_header('Content-Length', str(len(content)))
                    self.end_headers()
                    self.wfile.write(content)
                    print(f"✅ Successfully served {file_to_serve}")
                    return
                    
                except Exception as e:
                    print(f"❌ Error reading {file_to_serve}: {e}")
                    self.send_error(500, f"Error reading file: {e}")
                    return
            else:
                print(f"❌ File not found: {file_to_serve}")
                self.send_error(404, f"File not found: {file_to_serve}")
                return
        
        # For all other requests (CSS, images, etc.), use the default handler
        print(f"⚠️ Default handler for: '{path}'")
        return super().do_GET()

    def end_headers(self):
        # Add cache-busting headers
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

if __name__ == "__main__":
    with socketserver.TCPServer(("0.0.0.0", PORT), RoutingHandler) as httpd:
        print(f"🚀 Server running at http://0.0.0.0:{PORT}")
        print("🌐 Available routes:")
        print("   / (homepage)")
        print("   /art-materials")
        print("   /framing")
        print("   /demos")
        print("   /gift-cards")
        print("   /history")
        print("   /contact")
        print("   /legal")
        print("   /privacy")
        print("   /buyersguide")
        print("\nPress Ctrl+C to stop the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped")