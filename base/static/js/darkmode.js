document.addEventListener('DOMContentLoaded', function () {
    // Select the dark mode toggle button
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    const bodyElement = document.body;

    // Check if dark mode is enabled in localStorage
    if (localStorage.getItem('darkMode') === 'enabled') {
        bodyElement.classList.add('dark-mode');
        darkModeToggle.textContent = 'DARK MODE: ON';
    }

    // Toggle dark mode on button click
    darkModeToggle.addEventListener('click', () => {
        bodyElement.classList.toggle('dark-mode');

        // Update button text and save mode to localStorage
        if (bodyElement.classList.contains('dark-mode')) {
            darkModeToggle.textContent = 'DARK MODE: ON';
            localStorage.setItem('darkMode', 'enabled');
        } else {
            darkModeToggle.textContent = 'DARK MODE: OFF';
            localStorage.setItem('darkMode', 'disabled');
        }
    });
});
