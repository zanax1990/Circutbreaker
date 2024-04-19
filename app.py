from flask import Flask, jsonify
import pybreaker
import random

app = Flask(__name__)

# Custom listener class that extends CircuitBreakerListener
class CircuitListener(pybreaker.CircuitBreakerListener):
    def state_change(self, cb, old_state, new_state):
        print(f"Circuit state changed from {old_state} to {new_state}")

# Create the CircuitBreaker instance
breaker = pybreaker.CircuitBreaker(
    fail_max=3,                      # Open the circuit after 3 failures
    reset_timeout=10,                # Close the circuit after 10 seconds
    listeners=[CircuitListener()]    # Attach the custom listener
)

@app.route('/')
def home():
    return "Welcome to the microservice!"

@app.route('/unstable')
def unstable():
    try:
        with breaker:
            if random.random() > 0.5:
                raise Exception("Simulated failure")
            return "Success!"
    except pybreaker.CircuitBreakerError as e:
        return jsonify({"error": "Circuit breaker is open!"}), 503

@app.route('/circuitbreaker')
def circuitbreaker_state():
    return jsonify({
        "state": str(breaker.current_state),
        "failure_count": breaker.fail_counter
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
