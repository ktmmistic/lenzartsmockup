const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = 3000;

// Route mapping
const routes = {
  '/': 'index.html',
  '/buyers_guide': 'buyers_guide.html',
  '/buyers_guide.html': 'buyers_guide.html',
  '/art-materials': 'art-materials.html',
  '/framing': 'framing.html',
  '/demos': 'demos.html',
  '/gift-cards': 'gift-cards.html',
  '/history': 'history.html',
  '/contact': 'contact.html',
  '/legal': 'legal.html',
  '/privacy': 'privacy.html'
};

// Serve static files
app.use(express.static('.'));

// Handle routes
Object.entries(routes).forEach(([route, file]) => {
  app.get(route, (req, res) => {
    const filePath = path.join(__dirname, file);
    console.log(`Route ${route} -> ${file}`);
    if (fs.existsSync(filePath)) {
      res.sendFile(filePath);
    } else {
      res.status(404).send(`Page not found: ${file}`);
    }
  });
});

// Start server
app.listen(PORT, '0.0.0.0', () => {
  console.log(`Lenz Arts server running at http://0.0.0.0:${PORT}`);
  console.log('Server is ready for connections');
});