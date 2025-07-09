const express = require('express');
const path = require('path');

const app = express();
const port = 3000;

// Serve static files first
app.use(express.static(__dirname));

// Handle all routes by serving index.html (client-side router takes over)
app.get('*', (req, res) => {
  console.log(`📍 Serving index.html for: ${req.path}`);
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(port, '0.0.0.0', () => {
  console.log(`🎨 Lenz Arts server running on http://0.0.0.0:${port}`);
  console.log(`✅ Client-side routing enabled`);
});