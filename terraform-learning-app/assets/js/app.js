// Main Application JavaScript

// Tab Navigation
function showTab(tabName) {
    // Hide all tab contents
    const contents = document.querySelectorAll('.tab-content');
    contents.forEach(content => content.classList.remove('active'));

    // Remove active class from all buttons
    const buttons = document.querySelectorAll('.tab-button');
    buttons.forEach(button => button.classList.remove('active'));

    // Show selected tab
    document.getElementById(tabName).classList.add('active');

    // Add active class to clicked button
    event.target.classList.add('active');

    // Load content based on tab
    if (tabName === 'lessons') {
        loadLessons();
    } else if (tabName === 'practice') {
        loadPracticeExercises();
    } else if (tabName === 'labs') {
        loadLabs();
    }
}

// Initialize app on page load
document.addEventListener('DOMContentLoaded', function() {
    initializeProgress();
    updateDashboard();
    loadLessons();
    loadPracticeExercises();
    loadLabs();
});

// Update dashboard statistics
function updateDashboard() {
    const progress = getProgress();

    // Calculate totals
    const totalLessons = progress.beginner.total + progress.intermediate.total +
                         progress.advanced.total + progress.expert.total;
    const totalCompleted = progress.beginner.completed + progress.intermediate.completed +
                           progress.advanced.completed + progress.expert.completed;
    const overallProgress = Math.round((totalCompleted / totalLessons) * 100);

    // Update summary stats
    document.getElementById('totalCompleted').textContent = totalCompleted + '/' + totalLessons;
    document.getElementById('totalProgress').textContent = overallProgress + '%';
    document.getElementById('currentStreak').textContent = calculateStreak();

    // Update progress cards
    updateProgressCard('beginner', progress.beginner);
    updateProgressCard('intermediate', progress.intermediate);
    updateProgressCard('advanced', progress.advanced);
    updateProgressCard('expert', progress.expert);

    // Update recent activity
    displayRecentActivity();
}

// Update individual progress card
function updateProgressCard(level, data) {
    const badge = document.getElementById(level + 'Progress');
    const bar = document.getElementById(level + 'Bar');

    if (badge && bar) {
        badge.textContent = data.completed + '/' + data.total;
        const percentage = (data.completed / data.total) * 100;
        bar.style.width = percentage + '%';
    }
}

// Calculate learning streak
function calculateStreak() {
    const activity = getActivityLog();
    if (activity.length === 0) return 0;

    let streak = 0;
    const today = new Date().toDateString();
    const yesterday = new Date(Date.now() - 86400000).toDateString();

    // Check if there's activity today or yesterday
    const hasRecentActivity = activity.some(item => {
        const activityDate = new Date(item.timestamp).toDateString();
        return activityDate === today || activityDate === yesterday;
    });

    if (hasRecentActivity) {
        // Calculate consecutive days
        const sortedActivity = activity.sort((a, b) => b.timestamp - a.timestamp);
        const uniqueDays = [...new Set(sortedActivity.map(a => new Date(a.timestamp).toDateString()))];

        for (let i = 0; i < uniqueDays.length; i++) {
            const dayDate = new Date(uniqueDays[i]);
            const expectedDate = new Date(Date.now() - (i * 86400000)).toDateString();

            if (dayDate.toDateString() === expectedDate) {
                streak++;
            } else {
                break;
            }
        }
    }

    return streak;
}

// Display recent activity
function displayRecentActivity() {
    const activityList = document.getElementById('activityList');
    const activity = getActivityLog().slice(0, 5); // Get last 5 activities

    if (activity.length === 0) {
        activityList.innerHTML = '<p class="empty-state">Complete your first lesson to see activity here!</p>';
        return;
    }

    activityList.innerHTML = activity.map(item => `
        <div class="activity-item">
            <div>
                <div class="activity-title">${item.title}</div>
                <div class="activity-time">${formatTimeAgo(item.timestamp)}</div>
            </div>
            <div>${item.type === 'complete' ? '✅' : '📖'}</div>
        </div>
    `).join('');
}

// Format timestamp as "time ago"
function formatTimeAgo(timestamp) {
    const now = Date.now();
    const diff = now - timestamp;

    const minutes = Math.floor(diff / 60000);
    const hours = Math.floor(diff / 3600000);
    const days = Math.floor(diff / 86400000);

    if (minutes < 1) return 'Just now';
    if (minutes < 60) return minutes + ' minute' + (minutes > 1 ? 's' : '') + ' ago';
    if (hours < 24) return hours + ' hour' + (hours > 1 ? 's' : '') + ' ago';
    return days + ' day' + (days > 1 ? 's' : '') + ' ago';
}

// Navigate to specific section
function goToSection(section) {
    showTab('lessons');
    // Scroll to section
    setTimeout(() => {
        const element = document.querySelector(`[data-level="${section}"]`);
        if (element) {
            element.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    }, 100);
}

// Reset progress
function resetProgress() {
    if (confirm('Are you sure you want to reset all your progress? This cannot be undone.')) {
        localStorage.clear();
        initializeProgress();
        updateDashboard();
        alert('Progress has been reset!');
        location.reload();
    }
}

// Mark lesson as complete
function toggleLessonComplete(lessonId) {
    const progress = getProgress();
    const checkbox = document.querySelector(`[data-lesson="${lessonId}"]`);

    if (checkbox.checked) {
        markLessonComplete(lessonId);
        logActivity(lessonId, 'complete', 'Completed: ' + lessonId);

        // Show success animation
        showSuccessNotification('Lesson completed! 🎉');
    } else {
        markLessonIncomplete(lessonId);
    }

    updateDashboard();
}

// Show success notification
function showSuccessNotification(message) {
    const notification = document.createElement('div');
    notification.className = 'alert alert-success';
    notification.style.position = 'fixed';
    notification.style.top = '20px';
    notification.style.right = '20px';
    notification.style.zIndex = '10000';
    notification.style.animation = 'slideInRight 0.3s ease';
    notification.textContent = message;

    document.body.appendChild(notification);

    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Start lesson/lab
function startLesson(lessonId, type = 'lesson') {
    logActivity(lessonId, 'start', 'Started: ' + lessonId);
    updateDashboard();

    if (type === 'lesson') {
        openLessonModal(lessonId);
    } else if (type === 'lab') {
        openLabModal(lessonId);
    } else if (type === 'practice') {
        openPracticeModal(lessonId);
    }
}

// Open lesson in modal
function openLessonModal(lessonId) {
    const lesson = getLessonContent(lessonId);
    if (!lesson) return;

    const modal = createModal(lesson.title, lesson.content);
    document.body.appendChild(modal);
}

// Create modal
function createModal(title, content) {
    const modal = document.createElement('div');
    modal.className = 'modal active';
    modal.innerHTML = `
        <div class="modal-content">
            <div class="modal-header">
                <h2>${title}</h2>
                <button class="modal-close" onclick="this.closest('.modal').remove()">✕</button>
            </div>
            <div class="modal-body">
                ${content}
            </div>
        </div>
    `;

    // Close on background click
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            modal.remove();
        }
    });

    return modal;
}

// Export progress as JSON
function exportProgress() {
    const progress = {
        progress: getProgress(),
        activity: getActivityLog(),
        exportDate: new Date().toISOString()
    };

    const dataStr = JSON.stringify(progress, null, 2);
    const dataBlob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(dataBlob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'terraform-learning-progress.json';
    link.click();
    URL.revokeObjectURL(url);
}

// Import progress from JSON
function importProgress(event) {
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function(e) {
        try {
            const data = JSON.parse(e.target.result);
            localStorage.setItem('terraformProgress', JSON.stringify(data.progress));
            localStorage.setItem('activityLog', JSON.stringify(data.activity));
            alert('Progress imported successfully!');
            location.reload();
        } catch (error) {
            alert('Error importing progress: Invalid file format');
        }
    };
    reader.readAsText(file);
}
