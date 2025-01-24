# Flask Rate Limiter

This is a simple Flask application that demonstrates how to implement a rate-limiting decorator to restrict the number of requests a user can make to specific endpoints within a given time window.

---

## 📖 Overview

### Features:
- Implements a custom **rate-limiting decorator**.
- Tracks users based on their IP address.
- Returns an error response if the user exceeds the allowed number of requests.
- Fully customizable rate limit (requests per window) and time window.

---

## 🔧 Getting Started

### Prerequisites
- Python 3.x
- Flask

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/PriyankaTaug/RateLimiting.git

2. Install requirements.txt file
   ```bash
    pip freeze > requirements.txt


📂 Project Structure
.
├── decorator.py        # Main Flask application
├── README.md       # Project documentation
└── requirements.txt # Python dependencies
└── venv  # Virtual environment


🧪 Testing the Rate Limiter

Use a tool like Postman or curl to make multiple requests to the /limited endpoint:

curl http://127.0.0.1:5000/limited

Observe the response:

### For requests within the limit:
   {
        "message": "You are within the rate limit."
   }


After exceeding the limit:
   {
        "error": "Rate limit exceeded"
   }
 


🔄 Customization

Adjusting the Rate Limit
Modify the @rate_limit decorator in your endpoint:

  @rate_limit(limit=10, window=120)  # Allow 10 requests every 2 minutes


🤝 Contributing
Contributions are welcome! If you want to improve this project or add new features:


Fork the repository.
Create a feature branch.
Submit a pull request.


💬 Contact
For questions or feedback:

Email: priyankataug98@gmail.com
