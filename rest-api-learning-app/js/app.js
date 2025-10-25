// ===================================
// REST API Learning App - Main JS
// ===================================

// Navigation functionality
document.addEventListener('DOMContentLoaded', function() {
    console.log('REST API Learning App Initialized!');

    // Get all navigation links
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('.section');

    // Add click event to navigation links
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();

            // Get target section
            const targetSection = this.getAttribute('data-section');

            // Update active states
            navLinks.forEach(l => l.classList.remove('active'));
            this.classList.add('active');

            // Show target section
            sections.forEach(s => s.classList.remove('active'));
            document.getElementById(targetSection).classList.add('active');

            // Scroll to top of content
            document.querySelector('.content').scrollTop = 0;

            // Update URL hash
            window.location.hash = targetSection;
        });
    });

    // Handle direct URL hash navigation
    function navigateToHash() {
        const hash = window.location.hash.substring(1);
        if (hash) {
            const targetLink = document.querySelector(`[data-section="${hash}"]`);
            if (targetLink) {
                targetLink.click();
            }
        }
    }

    // Navigate on page load if hash exists
    navigateToHash();

    // Handle browser back/forward buttons
    window.addEventListener('hashchange', navigateToHash);
});

// Function to navigate to a specific section (called from buttons)
function goToSection(sectionId) {
    const targetLink = document.querySelector(`[data-section="${sectionId}"]`);
    if (targetLink) {
        targetLink.click();
    }
}

// Quiz functionality for HTTP methods section
function checkAnswer(button, isCorrect) {
    // Reset all buttons in this question
    const question = button.parentElement;
    const buttons = question.querySelectorAll('.quiz-btn');
    buttons.forEach(btn => {
        btn.classList.remove('correct', 'incorrect');
        btn.disabled = false;
    });

    // Mark the clicked button
    if (isCorrect) {
        button.classList.add('correct');
        showFeedback(question, 'Correct! Well done!', 'success');
    } else {
        button.classList.add('incorrect');
        showFeedback(question, 'Not quite. Try again!', 'error');
    }

    // Disable all buttons after answer
    setTimeout(() => {
        buttons.forEach(btn => btn.disabled = true);
    }, 100);
}

// Show feedback message
function showFeedback(element, message, type) {
    // Remove existing feedback
    const existingFeedback = element.querySelector('.feedback');
    if (existingFeedback) {
        existingFeedback.remove();
    }

    // Create new feedback
    const feedback = document.createElement('div');
    feedback.className = 'feedback';
    feedback.textContent = message;
    feedback.style.cssText = `
        margin-top: 10px;
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
        ${type === 'success' ? 'background: #d4edda; color: #155724;' : 'background: #f8d7da; color: #721c24;'}
    `;

    element.appendChild(feedback);

    // Auto-remove feedback after 3 seconds if incorrect
    if (type === 'error') {
        setTimeout(() => {
            feedback.remove();
            const buttons = element.querySelectorAll('.quiz-btn');
            buttons.forEach(btn => {
                btn.disabled = false;
                btn.classList.remove('incorrect');
            });
        }, 2000);
    }
}

// Toggle solution visibility
function toggleSolution(solutionId) {
    const solution = document.getElementById(solutionId);
    const button = event.target;

    if (solution.style.display === 'none' || solution.style.display === '') {
        solution.style.display = 'block';
        button.textContent = 'Hide Solution';
        button.style.background = '#dc3545';
    } else {
        solution.style.display = 'none';
        button.textContent = 'Show Solution';
        button.style.background = '#28a745';
    }
}

// Interactive API demo (optional enhancement)
function tryAPICall(apiUrl, method, displayElementId) {
    const displayElement = document.getElementById(displayElementId);
    displayElement.innerHTML = '<p>Loading...</p>';

    fetch(apiUrl, {
        method: method,
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
        return response.json();
    })
    .then(data => {
        displayElement.innerHTML = `
            <div style="background: #d4edda; padding: 15px; border-radius: 8px;">
                <h4 style="color: #155724; margin-top: 0;">Success! Response:</h4>
                <pre style="background: white; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>${JSON.stringify(data, null, 2)}</code></pre>
            </div>
        `;
    })
    .catch(error => {
        displayElement.innerHTML = `
            <div style="background: #f8d7da; padding: 15px; border-radius: 8px;">
                <h4 style="color: #721c24; margin-top: 0;">Error:</h4>
                <p style="color: #721c24;">${error.message}</p>
            </div>
        `;
    });
}

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Alt + N: Next section
    if (e.altKey && e.key === 'n') {
        e.preventDefault();
        const activeLink = document.querySelector('.nav-link.active');
        const nextLink = activeLink.parentElement.nextElementSibling;
        if (nextLink && nextLink.querySelector('.nav-link')) {
            nextLink.querySelector('.nav-link').click();
        }
    }

    // Alt + P: Previous section
    if (e.altKey && e.key === 'p') {
        e.preventDefault();
        const activeLink = document.querySelector('.nav-link.active');
        const prevLink = activeLink.parentElement.previousElementSibling;
        if (prevLink && prevLink.querySelector('.nav-link')) {
            prevLink.querySelector('.nav-link').click();
        }
    }

    // Alt + H: Go to home/intro
    if (e.altKey && e.key === 'h') {
        e.preventDefault();
        goToSection('intro');
    }
});

// Progress tracking (optional feature)
function initProgressTracking() {
    const completedSections = JSON.parse(localStorage.getItem('completedSections') || '[]');

    // Mark completed sections in navigation
    completedSections.forEach(sectionId => {
        const link = document.querySelector(`[data-section="${sectionId}"]`);
        if (link && !link.querySelector('.checkmark')) {
            const checkmark = document.createElement('span');
            checkmark.className = 'checkmark';
            checkmark.textContent = ' ✓';
            checkmark.style.color = '#28a745';
            link.appendChild(checkmark);
        }
    });
}

function markSectionComplete(sectionId) {
    const completedSections = JSON.parse(localStorage.getItem('completedSections') || '[]');
    if (!completedSections.includes(sectionId)) {
        completedSections.push(sectionId);
        localStorage.setItem('completedSections', JSON.stringify(completedSections));
        initProgressTracking();
    }
}

// Initialize progress tracking on load
document.addEventListener('DOMContentLoaded', initProgressTracking);

// Print helpful tips to console
console.log('%c🚀 REST API Learning App', 'font-size: 20px; color: #667eea; font-weight: bold;');
console.log('%cKeyboard Shortcuts:', 'font-size: 14px; color: #764ba2; font-weight: bold;');
console.log('Alt + N: Next section');
console.log('Alt + P: Previous section');
console.log('Alt + H: Go to home');
console.log('\n%cHappy Learning! 🎓', 'font-size: 16px; color: #28a745;');
