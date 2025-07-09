const express = require('express');
const app = express();
const port = 3000;

// Serve static files
app.use(express.static('.'));

// Simple fallback - serve index.html for all routes
app.get('*', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

app.listen(port, '0.0.0.0', () => {
  console.log(`🎨 Lenz Arts website running on http://0.0.0.0:${port}`);
});