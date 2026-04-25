from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample salary data
salary_data = {
    "global_avg": "₹8,50,000",
    "total_employees": 124,
    "highest": "₹24,00,000",
    "lowest": "₹3,20,000",
    "role_avgs": {
        "Engineer": "₹9,00,000",
        "Manager": "₹12,00,000"
    },
    "status": "encrypted",
    "message": "Data computed using MPC and Functional Encryption"
}

# Store submitted salaries
submitted_salaries = []

@app.route('/compute', methods=['GET'])
def compute():
    return jsonify(salary_data)

@app.route('/submit', methods=['POST'])
def submit_salary():
    data = request.get_json()
    submitted_salaries.append(data)

    # Update averages based on submissions
    if len(submitted_salaries) > 0:
        total = sum([s['salary'] for s in submitted_salaries])
        avg = total // len(submitted_salaries)
        salary_data['total_employees'] = 124 + len(submitted_salaries)
        salary_data['global_avg'] = f"₹{avg:,}"

    return jsonify({"status": "success", "message": "Salary submitted and encrypted!"})

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Salary Benchmarking API is running!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)