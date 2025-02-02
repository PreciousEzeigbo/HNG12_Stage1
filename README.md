# HNG12_Stage1
A RESTful API built with Flask that provides mathematical properties and fun facts about numbers.

## Features  
- Determines if a number is **prime**  
- Determines if a number is **perfect**  
- Identifies **Armstrong numbers**, **even**, and **odd** numbers  
- Calculates **digit sum**  
- Fetches fun mathematical facts from [Numbers API](http://numbersapi.com/)  
- **CORS enabled**  
- Input validation and error handling  

## Dependencies  
- Python **3.8+**  
- Flask  
- Flask-CORS  
- Requests library  
- Gunicorn (for production deployment)  
# Installation
Clone the repository:
```
git clone https://github.com/PreciousEzeigbo/HNG12_Stage1.git
cd flask-number-classifier
```

Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:
```
pip install -r requirements.txt
```
Run the development server:
```
python app.py
```

# API Documentation
Endpoint: GET /api/classify-number
Parameters:
number (required): Integer to analyze
Success Response (200 OK):
json
```
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number..."
}
```
Error Response (400 Bad Request):
json
```
{
    "number": "invalid_input",
    "error": true
}
```

# Deployment
https://hng12-stage1-ocoi.onrender.com

# Useful links
https://hng.tech/hire/python-developers
