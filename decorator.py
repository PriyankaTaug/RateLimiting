from flask import Flask, jsonify, request
from time import time

app = Flask(__name__)


rate_limit_cache = {}

def rate_limit(limit,window):
    def decorator(func):
        def wrapper(*args,**kwargs):
            user = request.remote.addr
            now = time()
            if user not in rate_limit_cache:
                rate_limit_cache[user] = []
            rate_limit_cache[user]  = [t for t in rate_limit_cache[user] if now-t >window]
            if len(rate_limit_cache[user]) >= limit:
                return jsonify({"error":"Rate limit exceeded"}),429
            rate_limit_cache[user].append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@app.route('/limited', methods=['GET'])
@rate_limit(limit=5, window=60)
def limites_endpoints():
    return jsonify({"message": "You are within the rate limit."})

