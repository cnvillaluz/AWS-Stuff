// ===================================
// REST API Learning App - Exercises
// ===================================

// Exercise 1: Random Quote Fetcher - Interactive Demo
function createQuoteDemo() {
    // This function can be used to add a live demo to the exercises section
    // Students can test the quote API directly in the browser
    console.log('Exercise demos available!');
}

// Exercise Helper: Test API Connection
function testAPIConnection(apiUrl, callback) {
    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            callback(null, data);
        })
        .catch(error => {
            callback(error, null);
        });
}

// Code Validator: Check if student code has required elements
function validateCode(code, requirements) {
    const results = {
        passed: true,
        feedback: []
    };

    requirements.forEach(req => {
        if (typeof req === 'string') {
            // Simple string check
            if (!code.includes(req)) {
                results.passed = false;
                results.feedback.push(`Missing required element: ${req}`);
            } else {
                results.feedback.push(`✓ Found: ${req}`);
            }
        } else if (typeof req === 'object' && req.regex) {
            // Regex check
            if (!req.regex.test(code)) {
                results.passed = false;
                results.feedback.push(`Missing: ${req.description}`);
            } else {
                results.feedback.push(`✓ Found: ${req.description}`);
            }
        }
    });

    return results;
}

// Exercise Templates
const exerciseTemplates = {
    basicGET: `// ==UserScript==
// @name         My API Script
// @match        https://*/*
// @grant        GM_xmlhttpRequest
// @connect      api.example.com
// ==/UserScript==

(function() {
    'use strict';

    GM_xmlhttpRequest({
        method: "GET",
        url: "YOUR_API_URL_HERE",
        onload: function(response) {
            const data = JSON.parse(response.responseText);
            console.log(data);
            // TODO: Display the data on the page
        },
        onerror: function(error) {
            console.error("Error:", error);
        }
    });
})();`,

    basicPOST: `// ==UserScript==
// @name         POST Request Script
// @match        https://*/*
// @grant        GM_xmlhttpRequest
// @connect      api.example.com
// ==/UserScript==

(function() {
    'use strict';

    const dataToSend = {
        // Add your data here
    };

    GM_xmlhttpRequest({
        method: "POST",
        url: "YOUR_API_URL_HERE",
        headers: {
            "Content-Type": "application/json"
        },
        data: JSON.stringify(dataToSend),
        onload: function(response) {
            console.log("Response:", response.responseText);
        },
        onerror: function(error) {
            console.error("Error:", error);
        }
    });
})();`,

    withUI: `// ==UserScript==
// @name         Script with UI
// @match        https://*/*
// @grant        GM_xmlhttpRequest
// @connect      api.example.com
// ==/UserScript==

(function() {
    'use strict';

    // Create UI container
    const container = document.createElement('div');
    container.style.cssText = 'position:fixed; top:20px; right:20px; background:white; padding:20px; border-radius:10px; box-shadow:0 4px 6px rgba(0,0,0,0.1); z-index:9999;';

    // Add button
    const button = document.createElement('button');
    button.textContent = 'Fetch Data';
    button.style.cssText = 'padding:10px 20px; background:#007bff; color:white; border:none; border-radius:5px; cursor:pointer;';

    // Add result display
    const resultDiv = document.createElement('div');
    resultDiv.style.cssText = 'margin-top:15px;';

    container.appendChild(button);
    container.appendChild(resultDiv);
    document.body.appendChild(container);

    // Button click handler
    button.addEventListener('click', function() {
        resultDiv.innerHTML = 'Loading...';

        GM_xmlhttpRequest({
            method: "GET",
            url: "YOUR_API_URL_HERE",
            onload: function(response) {
                const data = JSON.parse(response.responseText);
                // Display the data
                resultDiv.innerHTML = \`<pre>\${JSON.stringify(data, null, 2)}</pre>\`;
            },
            onerror: function(error) {
                resultDiv.innerHTML = 'Error loading data';
            }
        });
    });
})();`
};

// Exercise Challenges
const exerciseChallenges = [
    {
        id: 1,
        title: "Random Quote Fetcher",
        difficulty: "Beginner",
        api: "https://api.quotable.io/random",
        requirements: [
            "GM_xmlhttpRequest",
            "@connect api.quotable.io",
            "onload",
            "JSON.parse"
        ],
        hints: [
            "Use GET method to fetch the quote",
            "Parse the response with JSON.parse()",
            "Access quote with data.content and author with data.author",
            "Create a div to display the quote on the page"
        ]
    },
    {
        id: 2,
        title: "GitHub User Info",
        difficulty: "Beginner",
        api: "https://api.github.com/users/{username}",
        requirements: [
            "GM_xmlhttpRequest",
            "@connect api.github.com",
            "createElement",
            "appendChild"
        ],
        hints: [
            "Create an input field for username",
            "Add a button to trigger the search",
            "Use template literals to build the URL",
            "Display avatar using img tag with user.avatar_url"
        ]
    },
    {
        id: 3,
        title: "Weather Dashboard",
        difficulty: "Intermediate",
        api: "https://api.openweathermap.org/data/2.5/weather",
        requirements: [
            "GM_xmlhttpRequest",
            "API key handling",
            "Error handling",
            "Temperature conversion"
        ],
        hints: [
            "Sign up for free API key at openweathermap.org",
            "Pass city name and API key as URL parameters",
            "Handle errors for invalid city names",
            "Display temperature, conditions, and icon"
        ]
    },
    {
        id: 4,
        title: "Cryptocurrency Tracker",
        difficulty: "Intermediate",
        api: "https://api.coingecko.com/api/v3/simple/price",
        requirements: [
            "Multiple API parameters",
            "Auto-refresh functionality",
            "Price change indicators",
            "Styling"
        ],
        hints: [
            "Use setInterval for auto-refresh",
            "Track previous price to show increase/decrease",
            "Use colors: green for up, red for down",
            "Format currency with toFixed(2)"
        ]
    },
    {
        id: 5,
        title: "Multi-API Dashboard",
        difficulty: "Advanced",
        api: "Multiple APIs",
        requirements: [
            "Multiple GM_xmlhttpRequest calls",
            "Promise handling",
            "Data aggregation",
            "Responsive UI"
        ],
        hints: [
            "Fetch from weather, quote, and GitHub APIs",
            "Use counters to track completed requests",
            "Combine all data into single dashboard",
            "Use grid layout for organized display"
        ]
    }
];

// Function to show exercise hints progressively
let hintIndex = 0;
function showNextHint(exerciseId) {
    const exercise = exerciseChallenges.find(ex => ex.id === exerciseId);
    if (exercise && hintIndex < exercise.hints.length) {
        console.log(`💡 Hint ${hintIndex + 1}: ${exercise.hints[hintIndex]}`);
        hintIndex++;
    } else {
        console.log('No more hints available!');
    }
}

// Function to reset hints
function resetHints() {
    hintIndex = 0;
}

// Exercise progress tracker
const exerciseProgress = {
    completed: JSON.parse(localStorage.getItem('exercisesCompleted') || '[]'),

    markComplete(exerciseId) {
        if (!this.completed.includes(exerciseId)) {
            this.completed.push(exerciseId);
            localStorage.setItem('exercisesCompleted', JSON.stringify(this.completed));
            console.log(`✓ Exercise ${exerciseId} completed!`);
            this.showProgress();
        }
    },

    isComplete(exerciseId) {
        return this.completed.includes(exerciseId);
    },

    showProgress() {
        const total = exerciseChallenges.length;
        const completed = this.completed.length;
        const percentage = Math.round((completed / total) * 100);
        console.log(`📊 Progress: ${completed}/${total} exercises completed (${percentage}%)`);
    },

    reset() {
        this.completed = [];
        localStorage.removeItem('exercisesCompleted');
        console.log('Progress reset!');
    }
};

// Common API endpoints for practice (no auth required)
const practiceAPIs = {
    quotes: {
        name: "Quotable - Random Quotes",
        url: "https://api.quotable.io/random",
        method: "GET",
        auth: false,
        description: "Get random inspirational quotes"
    },
    jokes: {
        name: "JokeAPI - Random Jokes",
        url: "https://v2.jokeapi.dev/joke/Any?safe-mode",
        method: "GET",
        auth: false,
        description: "Get random jokes"
    },
    github: {
        name: "GitHub API - User Info",
        url: "https://api.github.com/users/{username}",
        method: "GET",
        auth: false,
        description: "Get GitHub user information"
    },
    catFacts: {
        name: "Cat Facts",
        url: "https://catfact.ninja/fact",
        method: "GET",
        auth: false,
        description: "Get random cat facts"
    },
    dogImages: {
        name: "Dog CEO - Random Dog Images",
        url: "https://dog.ceo/api/breeds/image/random",
        method: "GET",
        auth: false,
        description: "Get random dog images"
    },
    publicAPIs: {
        name: "Public APIs List",
        url: "https://api.publicapis.org/random?auth=null",
        method: "GET",
        auth: false,
        description: "Discover random public APIs"
    },
    advice: {
        name: "Advice Slip",
        url: "https://api.adviceslip.com/advice",
        method: "GET",
        auth: false,
        description: "Get random advice"
    },
    ipInfo: {
        name: "IP Geolocation",
        url: "https://ipapi.co/json/",
        method: "GET",
        auth: false,
        description: "Get your IP information and location"
    }
};

// Function to list all practice APIs
function listPracticeAPIs() {
    console.log('%c📚 Practice APIs (No Auth Required)', 'font-size: 16px; font-weight: bold; color: #667eea;');
    Object.entries(practiceAPIs).forEach(([key, api]) => {
        console.log(`\n%c${api.name}`, 'font-weight: bold; color: #764ba2;');
        console.log(`URL: ${api.url}`);
        console.log(`Method: ${api.method}`);
        console.log(`Description: ${api.description}`);
    });
}

// Code snippets library
const codeSnippets = {
    simpleGET: `GM_xmlhttpRequest({
    method: "GET",
    url: "https://api.example.com/data",
    onload: (response) => console.log(response.responseText)
});`,

    withHeaders: `GM_xmlhttpRequest({
    method: "GET",
    url: "https://api.example.com/data",
    headers: {
        "Authorization": "Bearer YOUR_TOKEN",
        "Content-Type": "application/json"
    },
    onload: (response) => console.log(response.responseText)
});`,

    postRequest: `GM_xmlhttpRequest({
    method: "POST",
    url: "https://api.example.com/data",
    headers: { "Content-Type": "application/json" },
    data: JSON.stringify({ key: "value" }),
    onload: (response) => console.log(response.responseText)
});`,

    errorHandling: `GM_xmlhttpRequest({
    method: "GET",
    url: "https://api.example.com/data",
    onload: function(response) {
        if (response.status === 200) {
            const data = JSON.parse(response.responseText);
            console.log("Success:", data);
        } else {
            console.error("Error:", response.status);
        }
    },
    onerror: (error) => console.error("Request failed:", error)
});`,

    createUI: `const div = document.createElement('div');
div.textContent = 'Hello!';
div.style.cssText = 'position:fixed; top:10px; right:10px; background:white; padding:10px; z-index:9999;';
document.body.appendChild(div);`
};

// Helper function to copy code snippet
function copySnippet(snippetName) {
    const snippet = codeSnippets[snippetName];
    if (snippet) {
        navigator.clipboard.writeText(snippet).then(() => {
            console.log(`✓ Copied ${snippetName} to clipboard!`);
        });
    } else {
        console.log('Snippet not found');
    }
}

// Initialize exercises on page load
document.addEventListener('DOMContentLoaded', function() {
    console.log('%c📝 Exercise System Ready!', 'font-size: 14px; color: #28a745; font-weight: bold;');
    console.log('Available commands:');
    console.log('- listPracticeAPIs() - Show all practice APIs');
    console.log('- exerciseProgress.showProgress() - Check your progress');
    console.log('- showNextHint(exerciseId) - Get hints for exercises');
    console.log('- copySnippet(snippetName) - Copy code snippets');
});

// Export functions to global scope for console access
window.listPracticeAPIs = listPracticeAPIs;
window.showNextHint = showNextHint;
window.resetHints = resetHints;
window.exerciseProgress = exerciseProgress;
window.copySnippet = copySnippet;
window.exerciseTemplates = exerciseTemplates;
window.practiceAPIs = practiceAPIs;
window.codeSnippets = codeSnippets;
