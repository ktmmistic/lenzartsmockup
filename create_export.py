import json
import os
import base64
from datetime import datetime

def read_file_content(filepath):
    try:
        # Try reading as text first
        with open(filepath, 'r', encoding='utf-8') as f:
            return {'type': 'text', 'content': f.read()}
    except UnicodeDecodeError:
        # If binary, encode as base64
        with open(filepath, 'rb') as f:
            return {'type': 'binary', 'content': base64.b64encode(f.read()).decode('utf-8')}
    except Exception as e:
        return {'type': 'error', 'content': f'Error reading file: {str(e)}'}

def get_file_tree(root_path, exclude_dirs=None):
    if exclude_dirs is None:
        exclude_dirs = {'node_modules', '__pycache__', '.git', '.replit_cache'}
    
    file_tree = {}
    
    for root, dirs, files in os.walk(root_path):
        # Remove excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        rel_root = os.path.relpath(root, root_path)
        if rel_root == '.':
            rel_root = ''
        
        for file in files:
            file_path = os.path.join(root, file)
            rel_file_path = os.path.join(rel_root, file) if rel_root else file
            
            # Skip hidden files except .replit
            if file.startswith('.') and file not in ['.replit']:
                continue
                
            file_tree[rel_file_path] = read_file_content(file_path)
    
    return file_tree

# Create the project export
project_export = {
    'metadata': {
        'project_name': 'Lenz Arts Website',
        'export_date': datetime.now().isoformat(),
        'description': 'Complete static website for Lenz Arts - art supply and framing business in Santa Cruz, California',
        'version': '1.0.0',
        'technology_stack': ['HTML5', 'CSS3', 'JavaScript', 'Node.js', 'Express.js'],
        'features': [
            'Responsive design with mobile-first approach',
            'Dark/light theme support with localStorage persistence',
            'Clean URL routing',
            'Historical news article archive',
            'Contact information and Google Maps integration',
            'Art materials catalog and framing services',
            'Gift card information and buyer\'s guide'
        ],
        'pages': [
            'index.html - Homepage with hero section and company info',
            'art-materials.html - Art supplies and materials catalog',
            'framing.html - Custom framing services',
            'demos.html - Art demonstrations and workshops',
            'gift-cards.html - Gift card information',
            'buyers_guide.html - Art supply buyer\'s guide with PDF',
            'history.html - Company history and news archives',
            'contact.html - Contact info, hours, and location',
            'legal.html - Legal notices and terms',
            'privacy.html - Privacy policy'
        ],
        'news_articles': [
            '2002Sentinel-March17-fire.html - Fire damage coverage',
            '2002Sentinel-March20-fire.html - Fire recovery story',
            '2007Sentinel-April8-fire.html - Fire anniversary article',
            '2009Sentinel-May14-Killion.html - Award recognition',
            '2013Sentinel-July26-45Anniversary.html - 45th anniversary',
            '2013Sentinel-July29-EditorialLenz.html - Editorial piece',
            '2016Sentinel-March18-LifetimeAward.html - Lifetime achievement'
        ],
        'server_configurations': [
            'express_server.js - Node.js Express server (recommended)',
            'working_server.py - Python HTTP server with routing',
            'server_node.js - Alternative Node.js server'
        ]
    },
    'project_structure': get_file_tree('.'),
    'deployment_info': {
        'recommended_server': 'express_server.js',
        'port': 3000,
        'hosting_options': [
            'Replit Deploy - One-click deployment',
            'Netlify - Static site hosting',
            'Vercel - Static site hosting',
            'GitHub Pages - Static hosting',
            'Traditional web hosting - File upload'
        ],
        'requirements': {
            'runtime': 'Node.js 18+ for Express server, or static hosting for basic functionality',
            'dependencies': '@paypal/paypal-server-sdk, express, serve',
            'environment': 'PORT=3000 recommended for Replit'
        },
        'setup_instructions': [
            '1. Extract files to web server directory',
            '2. For Node.js: npm install && node express_server.js',
            '3. For static hosting: Upload HTML/CSS/JS files directly',
            '4. Ensure proper routing for clean URLs (/history vs /history.html)'
        ]
    },
    'technical_notes': {
        'routing': 'Clean URL routing implemented in both Express and Python servers',
        'themes': 'CSS custom properties with JavaScript toggle and localStorage persistence',
        'responsive': 'Mobile-first design with CSS Grid and Flexbox',
        'assets': 'All images and files included in attached_assets directory',
        'browser_support': 'Modern browsers supporting CSS custom properties and ES6+'
    }
}

# Write to JSON file
with open('lenz_arts_project_export.json', 'w', encoding='utf-8') as f:
    json.dump(project_export, f, indent=2, ensure_ascii=False)

print(f'✓ Project exported to lenz_arts_project_export.json')
print(f'✓ Exported {len(project_export["project_structure"])} files')
print('✓ Includes all HTML pages, CSS, JavaScript, assets, and server configurations')
print('✓ Ready for deployment on any web hosting platform')