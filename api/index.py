import sys
import os
import warnings
warnings.filterwarnings('ignore')

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

try:
    from backend.app import app
    print("✅ Flask app imported successfully")
except Exception as e:
    print(f"❌ Error importing app: {e}")
    # Create a basic Flask app as fallback
    from flask import Flask, jsonify
    app = Flask(__name__)
    
    @app.route('/')
    def error():
        return jsonify({"error": "Failed to load main app", "details": str(e)})

# For Vercel serverless deployment
def handler(request):
    return app

# Initialize app for Vercel
app.config['ENV'] = 'production'
