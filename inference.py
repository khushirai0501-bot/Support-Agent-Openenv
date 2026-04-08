import requests

# Ye function check karega ki aapka OpenEnv sahi se reset ho raha hai ya nahi
def test_submission():
    # Local testing ke liye localhost, deployment ke liye Hugging Face URL
    url = "http://0.0.0.0:7860/reset" 
    try:
        response = requests.post(url)
        if response.status_code == 200:
            print("Environment Reset Successful:", response.json())
        else:
            print("Failed to reset environment")
    except Exception as e:
        print(f"Error connecting to environment: {e}")

if __name__ == "__main__":
    test_submission()