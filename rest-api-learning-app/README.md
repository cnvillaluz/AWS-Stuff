# REST API & Greasemonkey Script Learning Application

A comprehensive, interactive learning application designed to teach you REST API fundamentals and how to create powerful Greasemonkey/Tampermonkey scripts.

## What You'll Learn

- **REST API Fundamentals**: Understand what REST APIs are, how they work, and how to use them
- **HTTP Methods**: Master GET, POST, PUT, PATCH, and DELETE requests
- **Request/Response Structure**: Learn about headers, status codes, and data formats
- **Greasemonkey Scripting**: Create browser automation scripts that interact with APIs
- **Practical Applications**: Build real-world projects with hands-on exercises

## Features

- **Interactive Learning**: Navigate through lessons at your own pace
- **Code Examples**: Real, working code examples you can copy and modify
- **Hands-on Exercises**: Practice with exercises ranging from beginner to advanced
- **Project Ideas**: 6+ real-world projects to build your portfolio
- **No Installation Hassles**: Simple, open-and-run setup

---

## Installation Guide (Stress-Free!)

### Option 1: Simple - Open Directly in Browser (Recommended)

This is the easiest method - no server required!

1. **Download or Clone the Repository**
   ```bash
   # If you have git installed
   git clone https://github.com/cnvillaluz/AWS-Stuff.git
   cd AWS-Stuff/rest-api-learning-app
   ```

   Or simply download the ZIP file and extract it.

2. **Open the Application**
   - Navigate to the `rest-api-learning-app` folder
   - Double-click on `index.html`
   - The app will open in your default browser!

   **That's it! You're ready to start learning!**

---

### Option 2: Using a Local Web Server (Optional)

While not required, using a web server provides a more authentic development experience.

#### Using Python (if installed)

```bash
# Navigate to the app folder
cd rest-api-learning-app

# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```

Then open your browser and go to: `http://localhost:8000`

#### Using Node.js (if installed)

```bash
# Install http-server globally (one-time only)
npm install -g http-server

# Navigate to the app folder
cd rest-api-learning-app

# Start the server
http-server -p 8000
```

Then open your browser and go to: `http://localhost:8000`

#### Using VS Code Live Server Extension

1. Install the "Live Server" extension in VS Code
2. Open the `rest-api-learning-app` folder in VS Code
3. Right-click on `index.html`
4. Select "Open with Live Server"

---

## Setting Up Greasemonkey/Tampermonkey

To actually run the scripts you create during the exercises, you'll need a userscript manager:

### For Chrome/Edge/Brave

1. Install **Tampermonkey** extension:
   - Visit: https://www.tampermonkey.net/
   - Click "Download" and select your browser
   - Or search "Tampermonkey" in Chrome Web Store

2. Click "Add to Chrome/Edge/Brave"

3. You're done! The Tampermonkey icon will appear in your browser toolbar

### For Firefox

1. Install **Greasemonkey** or **Tampermonkey**:
   - Greasemonkey: https://addons.mozilla.org/en-US/firefox/addon/greasemonkey/
   - Tampermonkey: https://addons.mozilla.org/en-US/firefox/addon/tampermonkey/

2. Click "Add to Firefox"

3. You're done! The extension icon will appear in your toolbar

### For Safari

1. Install **Tampermonkey**:
   - Visit: https://www.tampermonkey.net/
   - Download the Safari version
   - Follow the installation prompts

---

## How to Use the Application

### Getting Started

1. **Open the App**: Launch `index.html` in your browser
2. **Navigate**: Use the sidebar menu to explore different sections
3. **Learn**: Read through each section's content
4. **Practice**: Try the interactive quizzes and exercises
5. **Build**: Apply your knowledge to the project ideas

### Navigation

- **Click** on any topic in the left sidebar to jump to that section
- Use the **"Next"** buttons at the bottom of each section
- Use **keyboard shortcuts**:
  - `Alt + N`: Next section
  - `Alt + P`: Previous section
  - `Alt + H`: Go to home

### Interactive Features

- **Quizzes**: Test your knowledge with interactive multiple-choice questions
- **Code Examples**: Copy and paste working code examples
- **Exercises**: View solutions by clicking "Show Solution" buttons
- **Console Commands**: Open browser console (F12) for bonus features

---

## Testing Your Greasemonkey Scripts

### Step 1: Create Your First Script

1. Click the **Tampermonkey/Greasemonkey icon** in your browser
2. Select **"Create a new script"**
3. Copy one of the examples from the learning app
4. Paste it into the editor
5. Click **File > Save** (or Ctrl+S)

### Step 2: Test the Script

1. Navigate to a website that matches your `@match` pattern
   - Example: If `@match` is `https://*/*`, it runs on all HTTPS sites
2. The script will run automatically!
3. Check the browser console (F12) to see output

### Step 3: Debug and Improve

1. Open browser console (F12)
2. Look for errors in the Console tab
3. Edit your script in Tampermonkey
4. Refresh the page to see changes

---

## Practice Exercises

The app includes hands-on exercises:

### Beginner Exercises
1. **Random Quote Fetcher** - Display inspirational quotes on any webpage
2. **GitHub User Info** - Search and display GitHub user profiles

### Intermediate Exercises
3. **Currency Converter** - Convert between currencies in real-time
4. **Weather Dashboard** - Show current weather on any site
5. **Cryptocurrency Tracker** - Monitor crypto prices

### Advanced Projects
6. **Price Tracker** - Track e-commerce prices over time
7. **Multi-API Dashboard** - Aggregate data from multiple sources
8. **Form Auto-Filler** - Automatically fill forms with saved data

---

## No-Auth Practice APIs

The app teaches you using real APIs that don't require authentication:

- **Quotable API**: Random quotes - `https://api.quotable.io/random`
- **JokeAPI**: Random jokes - `https://v2.jokeapi.dev/joke/Any`
- **GitHub API**: User info - `https://api.github.com/users/{username}`
- **Cat Facts**: Random cat facts - `https://catfact.ninja/fact`
- **Dog CEO**: Random dog images - `https://dog.ceo/api/breeds/image/random`
- **Advice Slip**: Random advice - `https://api.adviceslip.com/advice`

All ready to use in your scripts!

---

## Troubleshooting

### App won't load in browser
- **Solution**: Make sure you're opening `index.html`, not another file
- Try a different browser (Chrome, Firefox, Edge all work)
- Check if JavaScript is enabled in your browser

### Styles look broken
- **Solution**: Make sure the folder structure is intact:
  ```
  rest-api-learning-app/
    ├── index.html
    ├── css/
    │   └── styles.css
    └── js/
        ├── app.js
        └── exercises.js
  ```

### Script won't run in Tampermonkey
- Check that the `@match` pattern includes the website you're on
- Make sure you saved the script (Ctrl+S)
- Try refreshing the webpage
- Check browser console (F12) for errors

### API calls not working
- Ensure you have `@grant GM_xmlhttpRequest` in the metadata
- Add `@connect` directive for the API domain
  - Example: `@connect api.quotable.io`
- Check if the API is actually working by visiting it in browser

### CORS errors
- Don't use regular `fetch()` - use `GM_xmlhttpRequest` instead
- `GM_xmlhttpRequest` bypasses CORS restrictions

---

## Browser Compatibility

This app works in all modern browsers:

- ✅ Google Chrome (recommended)
- ✅ Mozilla Firefox
- ✅ Microsoft Edge
- ✅ Brave Browser
- ✅ Safari
- ✅ Opera

**Minimum Requirements**: Any browser released after 2018

---

## Learning Path Recommendation

### Week 1: Foundations
1. Complete **Introduction** and **REST API Basics**
2. Learn **HTTP Methods** and **Requests & Responses**
3. Understand **Status Codes**

### Week 2: Advanced Concepts
4. Study **Headers & Authentication**
5. Master **Data Formats** (JSON/XML)
6. Complete the interactive quizzes

### Week 3: Greasemonkey
7. Learn **Greasemonkey Basics**
8. Master **API Calls in Scripts**
9. Complete beginner exercises (1-2)

### Week 4: Practice
10. Complete intermediate exercises (3-5)
11. Start an advanced project (6-8)
12. Build your own custom script!

---

## Tips for Success

1. **Go at Your Own Pace**: There's no rush - take time to understand each concept
2. **Practice Regularly**: Code every day, even if just for 15 minutes
3. **Experiment**: Modify the examples and see what happens
4. **Use the Console**: `console.log()` is your best debugging friend
5. **Read API Docs**: Always check the API documentation
6. **Start Small**: Begin with simple scripts, then add features
7. **Ask Questions**: Search online if you're stuck - the community is helpful!

---

## Additional Resources

- **Tampermonkey Documentation**: https://www.tampermonkey.net/documentation.php
- **Public APIs List**: https://github.com/public-apis/public-apis
- **Greasy Fork (Script Repository)**: https://greasyfork.org/
- **MDN JavaScript Docs**: https://developer.mozilla.org/en-US/docs/Web/JavaScript
- **REST API Tutorial**: https://restfulapi.net/

---

## What's Next?

After completing this course, you can:

1. **Build Personal Tools**: Create scripts to enhance your favorite websites
2. **Automate Tasks**: Save time with automation scripts
3. **Join the Community**: Share your scripts on Greasy Fork
4. **Learn More**: Explore advanced topics like OAuth, GraphQL, and WebSockets
5. **Contribute**: Help others by creating tutorials and sharing knowledge

---

## FAQ

**Q: Do I need programming experience?**
A: Basic JavaScript knowledge is helpful, but the app explains everything from scratch.

**Q: Is this free?**
A: Yes! Completely free and open source.

**Q: Can I use this offline?**
A: Yes! Once downloaded, it works completely offline.

**Q: Will my scripts work on any website?**
A: Scripts work on websites that match your `@match` pattern. Some sites may have protections against userscripts.

**Q: Are there any risks?**
A: Userscripts run in your browser and can't harm your computer. Only install scripts from trusted sources.

**Q: Can I share the scripts I create?**
A: Absolutely! Share them on Greasy Fork or GitHub.

---

## Credits

Created for learners who want to master REST APIs and browser automation.

### Technologies Used
- HTML5
- CSS3
- Vanilla JavaScript (no frameworks!)
- REST APIs for examples

---

## Support

If you encounter any issues:

1. Check the **Troubleshooting** section above
2. Review the **Browser Console** (F12) for errors
3. Consult the **Additional Resources** for more help

---

## License

This educational application is open source and free to use.

---

## Get Started Now!

Don't wait - start your journey to becoming a REST API and Greasemonkey expert!

1. Open `index.html` in your browser
2. Click on "Introduction" in the sidebar
3. Begin learning!

**Happy Coding!** 🚀

---

*Last Updated: October 2024*
