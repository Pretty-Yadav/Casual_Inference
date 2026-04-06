# Student Performance Causal Inference Analysis - Website

## 📊 Overview

This is your interactive website showcasing causal inference findings about student performance and study hours. All pages are self-contained HTML files with integrated CSS styling.

## 🚀 GitHub Pages Setup

### Option 1: Deploy from `docs/` folder (Recommended)
1. Go to your GitHub repository settings
2. Scroll to **"GitHub Pages"** section
3. Set **Source** to: `Deploy from a branch`
4. Select branch: `main` (or your current branch)
5. Select folder: `/(root)/docs`
6. Click **Save**

Your site will be live at: `https://your-username.github.io/Casual_Inference/`

### Option 2: Deploy using GitHub Actions
If you prefer automatic deployments, see GitHub's documentation on deploying static content.

---

## 📄 Website Structure

The website consists of **6 interconnected pages**:

### 1. **index.html** - Home & Overview
   - Quick summary of key findings
   - Grid of navigation cards to each section
   - Perfect starting point for visitors

### 2. **ate.html** - Average Treatment Effect
   - Explains what 0.13 standard deviations means
   - Effect size interpretation table
   - Practical significance explanation

### 3. **pvalue.html** - Statistical Significance  
   - P-value explanation (0.028)
   - Clarity on what p-values actually mean
   - Common misconceptions debunked

### 4. **ci.html** - Confidence Interval
   - 95% CI interpretation: [0.014, 0.246]
   - Why CI not crossing zero matters
   - Connection between ATE, p-value, and CI

### 5. **analysis.html** - Data Analysis & Visualization
   - Boxplot visualization of results
   - How to read boxplots
   - Explanation of outliers and median vs mean
   - Why propensity score matching was used

### 6. **conclusion.html** - Overall Insights
   - Summary of all findings
   - Caveats and limitations
   - Practical implications
   - Methodology overview

---

## 🎨 Design Features

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Color-Coded Navigation**: Easy to jump between sections
- **Clear Visual Hierarchy**: Key metrics highlighted prominently
- **Professional Styling**: Modern gradient backgrounds and card layouts
- **Accessibility**: Proper contrast and readable fonts

---

## 📱 Navigation

All pages have a sticky navigation bar at the top with links to:
- Home
- Treatment Effect (ATE)
- Significance (P-value)
- Confidence Interval
- Data Analysis
- Conclusion

JavaScript automatically highlights the current page in the navigation.

---

## 🔧 Customization

If you want to modify the site:

1. **Colors**: Edit the gradient colors in `style.css` (currently purple/blue):
   ```css
   background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
   ```

2. **Chart Image**: Update `outcome_comparison.png` if you regenerate your visualization

3. **Text Content**: Edit any HTML file to update findings or interpretations

4. **Styling**: All CSS is in `style.css` - modify there for global changes

---

## 📊 Files Included

- `index.html` - Home page
- `ate.html` - ATE explanation
- `pvalue.html` - P-value explanation
- `ci.html` - Confidence interval explanation
- `analysis.html` - Data analysis & boxplot
- `conclusion.html` - Overall conclusions
- `style.css` - All styling for all pages
- `outcome_comparison.png` - Your visualization
- `README.md` - This file

---

## ✨ Key Features

✅ **Modular Pages**: Each finding gets its own dedicated page for clarity  
✅ **No External Dependencies**: Pure HTML/CSS - no frameworks needed  
✅ **Easy Navigation**: Consistent header on all pages  
✅ **Mobile-Friendly**: Responsive design works on all devices  
✅ **GitHub Pages Ready**: Deploy directly from this folder  
✅ **Professional Look**: Modern design with good contrast and spacing  

---

## 🌐 Hosting

Once you enable GitHub Pages:
- Site updates automatically when you push to `main`
- No build process needed
- Works with free GitHub Pages hosting
- Custom domain supported (optional)

---

## 📝 Notes

- The site is entirely static - no server backend needed
- All styling is embedded in the CSS file
- Navigation works via standard HTML links
- Images are referenced from the docs folder

---

## 🎯 Next Steps

1. Push these changes to your GitHub repository
2. Go to repository **Settings** → **Pages**
3. Configure GitHub Pages (see Option 1 above)
4. Visit your live site URL in 1-2 minutes

---

Questions? Every page includes detailed explanations of the statistics and findings.
