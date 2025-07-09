// Client-side router that handles navigation without page reloads
class LenzArtsRouter {
  constructor() {
    this.routes = {
      '/': 'index.html',
      '/art-materials': 'art-materials.html',
      '/framing': 'framing.html',
      '/demos': 'demos.html',
      '/gift-cards': 'gift-cards.html',
      '/history': 'history.html',
      '/contact': 'contact.html',
      '/legal': 'legal.html',
      '/privacy': 'privacy.html',
      '/buyersguide': 'buyersguide.html'
    };
    this.init();
  }

  init() {
    // Handle initial page load
    this.handleRoute(window.location.pathname);
    
    // Handle browser back/forward buttons
    window.addEventListener('popstate', (e) => {
      this.handleRoute(window.location.pathname);
    });

    // Handle all navigation clicks
    document.addEventListener('click', (e) => {
      const link = e.target.closest('a');
      if (link && link.hostname === window.location.hostname) {
        const path = link.pathname;
        if (this.routes[path]) {
          e.preventDefault();
          this.navigate(path);
        }
      }
    });
  }

  async navigate(path) {
    try {
      // Update URL without reload
      history.pushState(null, '', path);
      
      // Load and display the content
      await this.handleRoute(path);
    } catch (error) {
      console.error('Navigation error:', error);
    }
  }

  async handleRoute(path) {
    const filename = this.routes[path];
    if (!filename) {
      console.error('Route not found:', path);
      return;
    }

    try {
      // Fetch the HTML content
      const response = await fetch(filename);
      const html = await response.text();
      
      // Parse the HTML
      const parser = new DOMParser();
      const doc = parser.parseFromString(html, 'text/html');
      
      // Update page title
      document.title = doc.title;
      
      // Update main content
      const newBody = doc.body;
      document.body.innerHTML = newBody.innerHTML;
      
      // Re-initialize any JavaScript that needs to run
      this.reinitializeScripts();
      
      console.log(`✅ Loaded ${filename} for ${path}`);
    } catch (error) {
      console.error('Error loading route:', error);
    }
  }

  reinitializeScripts() {
    // Re-run theme toggle functionality
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
      themeToggle.addEventListener('click', () => {
        const currentTheme = document.body.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        document.body.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
      });
    }

    // Re-run mobile menu functionality
    const hamburger = document.getElementById('hamburger');
    const mobileMenu = document.getElementById('mobile-menu');
    
    if (hamburger && mobileMenu) {
      hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        mobileMenu.classList.toggle('active');
      });
    }

    // Re-run back to top button
    const backToTop = document.getElementById('backToTop');
    if (backToTop) {
      window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
          backToTop.classList.add('show');
        } else {
          backToTop.classList.remove('show');
        }
      });

      backToTop.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    }
  }
}

// Initialize router when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => new LenzArtsRouter());
} else {
  new LenzArtsRouter();
}