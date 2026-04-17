// Login Form Handler
const loginForm = document.getElementById('loginForm');

if (loginForm) {
    loginForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        // Simple validation
        if (username === '' || password === '') {
            alert('Please fill in all fields!');
            return;
        }

        if (password.length < 6) {
            alert('Password must be at least 6 characters!');
            return;
        }

        // Store username for dashboard
        localStorage.setItem('loggedInUser', username);

        // Redirect to dashboard
        window.location.href = 'dashboard.html';
    });
}

// Salary Form Handler
const salaryForm = document.getElementById('salaryForm');

if (salaryForm) {
    salaryForm.addEventListener('submit', function(e) {
        e.preventDefault();
        alert('✅ Your salary data has been encrypted and submitted successfully!');
        salaryForm.reset();
    });
}

// Logout handler
const logoutBtn = document.querySelector('.logout-btn');
if (logoutBtn) {
    logoutBtn.addEventListener('click', function() {
        localStorage.removeItem('loggedInUser');
        window.location.href = 'index.html';
    });
}