const express = require('express');
const path = require('path');

const app = express();
const PORT = 3000;

// Serve static files
app.use(express.static(__dirname));

// Handle all routes by serving index.html (for client-side routing)
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`🎨 Lenz Arts server running on http://0.0.0.0:${PORT}`);
  console.log(`📍 Local: http://localhost:${PORT}`);
  console.log(`🌐 Network: http://172.31.128.91:${PORT}`);
});

// Handle graceful shutdown
process.on('SIGINT', () => {
  console.log('\nServer shutting down gracefully...');
  process.exit(0);
});

process.on('SIGTERM', () => {
  console.log('\nServer shutting down gracefully...');
  process.exit(0);
});