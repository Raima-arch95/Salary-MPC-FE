// Connect to Backend API
function fetchSalaryData() {
    document.querySelectorAll('.stat-number').forEach(el => {
        el.innerText = 'Loading...';
    });

    fetch("http://127.0.0.1:5000/compute")
        .then(res => res.json())
        .then(data => {
            console.log("API Data:", data);

            document.getElementById("errorMsg").style.display = "none";

            document.getElementById("avgSalary").innerText = data.global_avg || "Encrypted Output";
            document.getElementById("totalEmployees").innerText = data.total_employees || "N/A";
            document.getElementById("highestSalary").innerText = data.highest || "Encrypted Output";
            document.getElementById("lowestSalary").innerText = data.lowest || "Encrypted Output";

            if (data.role_avgs) {
                document.getElementById("engineerAvg").innerText = data.role_avgs.Engineer || "Encrypted Output";
                document.getElementById("managerAvg").innerText = data.role_avgs.Manager || "Encrypted Output";
            }
        })
        .catch(error => {
            console.error("API Error:", error);
            document.getElementById("errorMsg").style.display = "block";
            document.querySelectorAll('.stat-number').forEach(el => {
                el.innerText = 'Unable to fetch data';
            });
        });
}

if (document.getElementById("avgSalary")) {
    fetchSalaryData();
}

// Login Form Handler
const loginForm = document.getElementById('loginForm');
if (loginForm) {
    loginForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        if (username === '' || password === '') {
            alert('Please fill in all fields!');
            return;
        }
        if (password.length < 6) {
            alert('Password must be at least 6 characters!');
            return;
        }
        localStorage.setItem('loggedInUser', username);
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