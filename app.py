from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import math

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:  # This covers negative numbers and 0,1
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    """Check if a number is perfect (sum of proper divisors equals the number)."""
    if n < 1:  # Perfect numbers are only defined for positive integers
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

def is_armstrong(n: int) -> bool:
    """Check if a number is an Armstrong number."""
    # Handle negative numbers - Armstrong numbers are typically defined only for positive integers
    if n < 0:
        return False
    num_str = str(abs(n))
    power = len(num_str)
    return sum(int(digit) ** power for digit in num_str) == n

def get_digit_sum(n: int) -> int:
    """Calculate the sum of digits."""
    # For negative numbers, we'll sum the absolute value's digits
    return sum(int(digit) for digit in str(abs(n)))

def get_properties(n: int) -> list:
    """Get list of properties (armstrong, odd/even)."""
    properties = []
    if is_armstrong(n):
        properties.append("armstrong")
    # Negative numbers can still be odd or even
    properties.append("odd" if abs(n) % 2 else "even")
    return properties

def get_fun_fact(n: int) -> str:
    """Get a fun fact about the number from numbersapi.com."""
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math")
        return response.text if response.status_code == 200 else f"{n} is a number"
    except requests.RequestException:
        return f"{n} is a number"

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    """Endpoint to classify a number and return its properties."""
    number = request.args.get('number')
    
    if not number:
        return jsonify({
            "number": "missing",
            "error": True,
            "message": "Number parameter is required"
        }), 400
    
    try:
        num = int(number)
        
        # Return the response with appropriate handling of negative numbers
        response = {
            "number": num,
            "is_prime": is_prime(num),
            "is_perfect": is_perfect(num),
            "properties": get_properties(num),
            "digit_sum": get_digit_sum(num),
            "fun_fact": get_fun_fact(num)
        }
        return jsonify(response)
        
    except ValueError:
        return jsonify({
            "number": number,
            "error": True,
            "message": "Input must be an integer"
        }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
