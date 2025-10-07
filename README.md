Flask Circuit Breaker Microservice

A simple Flask-based microservice demonstrating how to implement the Circuit Breaker pattern using pybreaker
.
This project shows how microservices can handle failures gracefully, prevent cascading errors, and recover automatically.

🚀 Features

🔌 Built with Flask – lightweight Python web framework

🧠 Uses pybreaker for circuit breaker logic

📉 Simulates unreliable services with random failures

📊 Provides real-time breaker state info via API

🛠️ Includes custom listener to log state changes

Installation & Setup

Clone the repository:

git clone https://github.com/your-username/flask-circuit-breaker.git
cd flask-circuit-breaker


Create a virtual environment (recommended):

python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate


Install dependencies:

pip install flask pybreaker


Run the microservice:

python app.py


By default, the service runs at:
👉 http://0.0.0.0:5001

📡 API Endpoints
GET /

Returns a welcome message (health check).

Example:

curl http://localhost:5001/


Response:

Welcome to the microservice!

GET /unstable

Simulates an unreliable service. Randomly fails 50% of the time.
After 3 consecutive failures, the circuit opens and blocks further requests for 10 seconds.

Example:

curl http://localhost:5001/unstable


✅ Possible response:

Success!


❌ If circuit is open:

{"error": "Circuit breaker is open!"}

GET /circuitbreaker

Shows the current state of the circuit breaker and number of failures.

Example:

curl http://localhost:5001/circuitbreaker


Response:

{
  "state": "closed",
  "failure_count": 0
}

🔁 Circuit Breaker Behavior
State	Description
Closed	All requests are allowed. Circuit monitors failures.
Open	Circuit blocks all requests after fail_max failures.
Half-Open	After reset_timeout, allows 1 request to test recovery.

Config (default):

fail_max = 3 – Open after 3 consecutive failures

reset_timeout = 10 – Attempt recovery after 10 seconds

🧪 Testing Tips

Repeatedly call /unstable to trigger failures and see state transitions.

Watch the terminal to see state changes logged by the custom CircuitListener.

🛠️ Tech Stack

Python 3.8+

Flask – REST API framework

pybreaker – Circuit breaker implementation

📜 License

This project is open-source and available under the MIT License.
