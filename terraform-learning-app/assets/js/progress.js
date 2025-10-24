// Progress Tracking System

// Initialize progress structure
function initializeProgress() {
    if (!localStorage.getItem('terraformProgress')) {
        const initialProgress = {
            beginner: {
                total: 8,
                completed: 0,
                lessons: {}
            },
            intermediate: {
                total: 10,
                completed: 0,
                lessons: {}
            },
            advanced: {
                total: 12,
                completed: 0,
                lessons: {}
            },
            expert: {
                total: 6,
                completed: 0,
                lessons: {}
            }
        };
        localStorage.setItem('terraformProgress', JSON.stringify(initialProgress));
    }

    if (!localStorage.getItem('activityLog')) {
        localStorage.setItem('activityLog', JSON.stringify([]));
    }
}

// Get current progress
function getProgress() {
    const progress = localStorage.getItem('terraformProgress');
    return progress ? JSON.parse(progress) : null;
}

// Save progress
function saveProgress(progress) {
    localStorage.setItem('terraformProgress', JSON.stringify(progress));
}

// Mark lesson as complete
function markLessonComplete(lessonId) {
    const progress = getProgress();
    const [level, ...lessonParts] = lessonId.split('-');
    const lessonKey = lessonParts.join('-');

    if (progress[level]) {
        if (!progress[level].lessons[lessonKey]) {
            progress[level].lessons[lessonKey] = {
                completed: true,
                completedAt: Date.now()
            };
            progress[level].completed++;
        }
        saveProgress(progress);
    }
}

// Mark lesson as incomplete
function markLessonIncomplete(lessonId) {
    const progress = getProgress();
    const [level, ...lessonParts] = lessonId.split('-');
    const lessonKey = lessonParts.join('-');

    if (progress[level] && progress[level].lessons[lessonKey]) {
        delete progress[level].lessons[lessonKey];
        progress[level].completed = Math.max(0, progress[level].completed - 1);
        saveProgress(progress);
    }
}

// Check if lesson is complete
function isLessonComplete(lessonId) {
    const progress = getProgress();
    const [level, ...lessonParts] = lessonId.split('-');
    const lessonKey = lessonParts.join('-');

    return progress[level] && progress[level].lessons[lessonKey]?.completed === true;
}

// Get activity log
function getActivityLog() {
    const log = localStorage.getItem('activityLog');
    return log ? JSON.parse(log) : [];
}

// Log activity
function logActivity(lessonId, type, title) {
    const activity = getActivityLog();
    activity.unshift({
        lessonId,
        type,
        title,
        timestamp: Date.now()
    });

    // Keep only last 50 activities
    if (activity.length > 50) {
        activity.splice(50);
    }

    localStorage.setItem('activityLog', JSON.stringify(activity));
}

// Get lesson statistics
function getLessonStats() {
    const progress = getProgress();
    const stats = {
        totalLessons: 0,
        completedLessons: 0,
        byLevel: {}
    };

    for (const level in progress) {
        stats.totalLessons += progress[level].total;
        stats.completedLessons += progress[level].completed;
        stats.byLevel[level] = {
            total: progress[level].total,
            completed: progress[level].completed,
            percentage: Math.round((progress[level].completed / progress[level].total) * 100)
        };
    }

    stats.overallPercentage = Math.round((stats.completedLessons / stats.totalLessons) * 100);
    return stats;
}

// Get completion certificate data
function getCertificateData() {
    const progress = getProgress();
    const stats = getLessonStats();

    return {
        name: prompt('Enter your name for the certificate:'),
        date: new Date().toLocaleDateString(),
        completionRate: stats.overallPercentage,
        lessonsCompleted: stats.completedLessons,
        totalLessons: stats.totalLessons
    };
}

// Check if user can get certificate
function canGetCertificate() {
    const stats = getLessonStats();
    return stats.overallPercentage >= 80; // 80% completion required
}

// Generate certificate
function generateCertificate() {
    if (!canGetCertificate()) {
        alert('Complete at least 80% of the course to earn your certificate!');
        return;
    }

    const data = getCertificateData();
    if (!data.name) return;

    const certificate = `
        ╔══════════════════════════════════════════════════════════════╗
        ║                                                              ║
        ║               CERTIFICATE OF COMPLETION                      ║
        ║                                                              ║
        ║                  This certifies that                         ║
        ║                                                              ║
        ║                     ${data.name.toUpperCase()}              ║
        ║                                                              ║
        ║         has successfully completed the course                ║
        ║                                                              ║
        ║          "Terraform with AWS - From Basics to Expert"       ║
        ║                                                              ║
        ║              Completion Rate: ${data.completionRate}%       ║
        ║       Lessons Completed: ${data.lessonsCompleted}/${data.totalLessons}           ║
        ║                                                              ║
        ║                Date: ${data.date}                           ║
        ║                                                              ║
        ╚══════════════════════════════════════════════════════════════╝
    `;

    // Create modal with certificate
    const modal = document.createElement('div');
    modal.className = 'modal active';
    modal.innerHTML = `
        <div class="modal-content">
            <div class="modal-header">
                <h2>🎓 Your Certificate</h2>
                <button class="modal-close" onclick="this.remove()">✕</button>
            </div>
            <pre style="text-align: center; font-size: 0.8rem;">${certificate}</pre>
            <button class="btn btn-primary" onclick="downloadCertificate(\`${certificate}\`)">
                Download Certificate
            </button>
        </div>
    `;

    document.body.appendChild(modal);
}

// Download certificate
function downloadCertificate(content) {
    const blob = new Blob([content], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'terraform-certificate.txt';
    link.click();
    URL.revokeObjectURL(url);
}

// Get learning insights
function getLearningInsights() {
    const stats = getLessonStats();
    const activity = getActivityLog();

    const insights = {
        streak: calculateStreak(),
        totalTime: estimateTotalTime(),
        strongestArea: getStrongestArea(stats),
        weakestArea: getWeakestArea(stats),
        recentActivity: activity.slice(0, 10),
        suggestions: generateSuggestions(stats)
    };

    return insights;
}

// Estimate total learning time
function estimateTotalTime() {
    const stats = getLessonStats();
    // Assuming 30 minutes per lesson average
    return stats.completedLessons * 30;
}

// Get strongest learning area
function getStrongestArea(stats) {
    let strongest = null;
    let maxPercentage = 0;

    for (const level in stats.byLevel) {
        if (stats.byLevel[level].percentage > maxPercentage) {
            maxPercentage = stats.byLevel[level].percentage;
            strongest = level;
        }
    }

    return {
        level: strongest,
        percentage: maxPercentage
    };
}

// Get weakest learning area
function getWeakestArea(stats) {
    let weakest = null;
    let minPercentage = 100;

    for (const level in stats.byLevel) {
        if (stats.byLevel[level].percentage < minPercentage) {
            minPercentage = stats.byLevel[level].percentage;
            weakest = level;
        }
    }

    return {
        level: weakest,
        percentage: minPercentage
    };
}

// Generate learning suggestions
function generateSuggestions(stats) {
    const suggestions = [];

    if (stats.overallPercentage < 25) {
        suggestions.push('Start with the beginner lessons to build a strong foundation');
    } else if (stats.overallPercentage < 50) {
        suggestions.push('Great start! Continue with intermediate lessons');
    } else if (stats.overallPercentage < 75) {
        suggestions.push('You\'re doing well! Move on to advanced topics');
    } else {
        suggestions.push('Excellent progress! Complete the expert challenges');
    }

    const weakest = getWeakestArea(stats);
    if (weakest.percentage < 50) {
        suggestions.push(`Focus more on ${weakest.level} level topics`);
    }

    return suggestions;
}

// Set learning goal
function setLearningGoal(lessonsPerWeek) {
    localStorage.setItem('learningGoal', JSON.stringify({
        lessonsPerWeek,
        startDate: Date.now()
    }));
}

// Check learning goal progress
function checkGoalProgress() {
    const goal = localStorage.getItem('learningGoal');
    if (!goal) return null;

    const { lessonsPerWeek, startDate } = JSON.parse(goal);
    const weeksSinceStart = Math.floor((Date.now() - startDate) / (7 * 24 * 60 * 60 * 1000));
    const expectedLessons = lessonsPerWeek * weeksSinceStart;
    const stats = getLessonStats();

    return {
        expectedLessons,
        actualLessons: stats.completedLessons,
        onTrack: stats.completedLessons >= expectedLessons
    };
}
