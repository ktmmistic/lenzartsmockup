# Lenz Arts - Business Website

## Overview

Lenz Arts is a responsive business website showcasing a family-owned art supply store and custom framing business in Santa Cruz, California. The website features three main pages with comprehensive company information, contact details, and rich historical content. Built with pure HTML, CSS, and JavaScript, it includes modern design elements and dual theme support.

## System Architecture

### Frontend Architecture
- **Pure HTML/CSS/JS**: Static website built with vanilla HTML5, CSS3, and JavaScript
- **Responsive Design**: Mobile-first approach with viewport meta tags and flexible layouts
- **Theme System**: Dual light/dark theme support using CSS custom properties and data attributes
- **Navigation System**: Fixed navigation with active states and smooth transitions
- **Component-Based Styling**: Consistent design system across all pages using shared CSS patterns

### Design System
- **Color Palette**: Warm earth tones (browns/oranges) reflecting art supplies branding
- **Color Theming**: CSS variables for seamless light/dark mode switching with persistent localStorage
- **Typography**: Modern system font stack with responsive scaling
- **Layout**: Centered content with maximum width constraints and grid-based features
- **Transitions**: Smooth 0.3-0.4s transitions for theme switching and interactions

## Key Components

### Pages
1. **Home Page** (`index.html`): Hero section, features showcase, company statistics, and call-to-action
2. **Contact Page** (`contact.html`): Phone numbers, email addresses, hours, address, and interactive map
3. **History Page** (`history.html`): Complete company history and news archives dating back to 1968

### Styling Architecture
- **CSS Variables**: Centralized theme management using custom properties with light/dark variants
- **Theme Toggle**: JavaScript-based dark/light mode switching with localStorage persistence
- **Fixed Navigation**: Sticky header with backdrop blur and active page highlighting
- **Responsive Grid**: CSS Grid and Flexbox layouts that adapt to different screen sizes
- **Typography Scale**: Consistent heading hierarchy and responsive text sizing
- **Interactive Elements**: Hover effects, transforms, and smooth transitions throughout

### Theme System
- **Light Theme**: Warm cream background (#f9f7f1) with earth-tone accents
- **Dark Theme**: Dark backgrounds (#121212) with brighter accent colors for contrast
- **Persistent Storage**: Theme preference saved in localStorage across sessions
- **Smooth Transitions**: 0.3-0.4s ease transitions between theme states and interactions

## Data Flow

### Static Content Flow
1. HTML files serve static content directly to browsers
2. CSS provides styling and theme variables
3. JavaScript handles theme switching and local storage persistence
4. No server-side processing or database interactions

### Theme Management
1. User clicks theme toggle
2. JavaScript updates body class or data attributes
3. CSS variables automatically adjust colors
4. Theme preference stored in localStorage for persistence

## External Dependencies

### None Required
- **No Framework Dependencies**: Pure HTML/CSS/JavaScript implementation
- **No CDN Requirements**: All assets self-hosted
- **No API Integrations**: Static content only
- **No Database**: File-based content storage

### Browser Compatibility
- Modern browsers supporting CSS custom properties
- ES6+ JavaScript features for theme management
- Responsive design using CSS Grid and Flexbox

## Deployment Strategy

### Static Hosting Options
- **GitHub Pages**: Direct deployment from repository
- **Netlify**: Drag-and-drop or Git-based deployment
- **Vercel**: Static site hosting with zero configuration
- **Traditional Web Hosting**: Simple file upload to web server

### Build Process
- **No Build Step Required**: Direct HTML/CSS/JS files
- **Optional Optimization**: Minification and asset compression
- **CDN Distribution**: Asset delivery through content delivery networks

### File Structure
```
/
├── index.html          # Home page with hero section and features
├── art-materials.html  # Art supplies and materials catalog
├── framing.html        # Custom framing services information
├── demos.html          # Art demonstrations and workshops
├── gift-cards.html     # Gift card information and purchase
├── buyersguide.html    # Art supply buyer's guide and recommendations
├── history.html        # Company history and news archives (Our Story)
├── contact.html        # Contact information and Google Maps integration
├── legal.html          # Legal notices and terms
├── privacy.html        # Privacy policy and data protection information
├── 2002Sentinel-March17-fire.html  # News article template example
├── replit.md          # Project documentation
└── attached_assets/   # Original HTML files and images provided by user
```

### News Article Template
The `2002Sentinel-March17-fire.html` file serves as the standard template for individual news articles with:
- **Hero Section**: Publication name, article title (centered), date, and author
- **Article Content**: Full newspaper content with proper formatting
- **Photo Sections**: Highlighted image areas with captions and descriptions
- **Quote Styling**: Italicized quotes with left border highlighting
- **Footer Notes**: Editor corrections or additional context
- **Navigation**: Back button to return to history page
- **Responsive Design**: Mobile-first approach with proper image scaling
- **Consistent Styling**: Matches site's color scheme and typography system

## User Preferences

Preferred communication style: Simple, everyday language.

## Changelog

## Recent Changes

✓ Enhanced homepage carousel with robust class-based implementation
✓ Added smooth fade transitions, auto-play with hover pause, and keyboard navigation
✓ Fixed carousel transition protection to prevent rapid clicking issues
✓ Created comprehensive buyers_guide.html using contact.html template structure
✓ Integrated authentic July Buyer's Guide cover image with anniversary art event
✓ Added dual image display showing current issue and 2024 archive collection
✓ Implemented PDF download section with Adobe Reader help
✓ Added publication schedule details for Santa Cruz Sentinel distribution
✓ Ensured full mobile responsiveness and dark theme compatibility
✓ Maintained consistent navigation and footer standardization across all pages
✓ Updated favicon from doodle boy to official Lenz Arts logo across all 10 website pages for professional branding
✓ Enhanced hero CTA button hover effects with proper purple/cyan color scheme
✓ Standardized mobile menu styling using index.html template across pages
✓ Fixed hamburger menu lavender background styling per user preference
✓ Completed standardization of all 7 news article pages with consistent features
✓ Fixed JavaScript errors across all news articles with proper DOM loading
✓ Added dark/light mode toggles to all news article pages with theme persistence
✓ Implemented back-to-top buttons on all articles with purple styling
✓ Standardized cyan footer styling (#01a0c6) across all news article pages
✓ Added company description intro text section below hero with elegant styling and gradient accents
✓ Optimized hero section for mobile with responsive image scaling and improved touch-friendly buttons
✓ Enhanced CTA buttons to hero-style prominence with larger padding, shadows, and mobile optimization
✓ Reduced intro text section size for better page balance while maintaining visual appeal
✓ Deleted duplicate buyersguide.html file to maintain single buyer's guide page
✓ Updated homepage CTA button to link to /buyers_guide instead of /buyersguide
✓ Added routing support for both /buyers_guide and /buyers_guide.html in working_server.py
✓ Changed server port from 8000 to 3000 for proper Replit integration

## Changelog

- July 04, 2025: Updated favicon from doodle boy to official Lenz Arts logo across all website pages for professional branding
- July 04, 2025: Added company description intro text section below hero with elegant gradient styling and decorative accents
- July 04, 2025: Optimized hero section and CTA buttons for mobile responsiveness with improved touch targets
- July 04, 2025: Enhanced CTA buttons to hero-style prominence with larger sizing and enhanced visual appeal
- July 04, 2025: Confirmed security assessment - router.js innerHTML usage is safe (false positive XSS alert)
- July 04, 2025: Verified working_server.py as recommended production server with clean URL routing
- July 04, 2025: Cleaned up buyer's guide routing - deleted duplicate buyersguide.html and updated server to port 3000
- July 04, 2025: Fixed homepage CTA button to properly link to /buyers_guide with complete PDF functionality
- July 04, 2025: Fixed JavaScript errors in all 7 news article pages by implementing proper DOM loading sequences
- July 04, 2025: Added missing dark/light mode toggle buttons to 2002Sentinel-March17-fire.html and 2002Sentinel-March20-fire.html
- July 04, 2025: Completed standardization of all news article pages with back-to-top buttons, theme toggles, and cyan footers
- July 04, 2025: Implemented error-free JavaScript with DOMContentLoaded event listeners and null checks across all articles
- July 03, 2025: Completely rebuilt art-materials.html using index.html template to fix hamburger menu visibility
- July 03, 2025: Fixed art materials page JavaScript errors and added homepage navigation links to art materials and framing pages
- July 03, 2025: Standardized hamburger menu appearance using index.html template across all 10 pages with responsive design improvements
- July 03, 2025: Fixed all navigation linking issues across 10 pages - home links now use "/" and mobile menus corrected
- July 03, 2025: Resolved infinite redirect loop by replacing index.html redirect with complete home page content
- July 02, 2025: Added back to top buttons to all pages with smooth scroll and dark theme support
- July 02, 2025: Fixed all navigation linking issues and file reference inconsistencies
- July 02, 2025: Completed mobile responsive design improvements across all 7 pages
- July 02, 2025: Fixed hamburger navigation and resolved CSS conflicts
- July 02, 2025: Applied consistent mobile typography and layout improvements
- July 02, 2025: Website completed with home, contact, and history pages
- July 02, 2025: Initial setup and project documentation