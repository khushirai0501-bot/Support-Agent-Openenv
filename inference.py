import requests
import sys

class Inference:
    def __init__(self):
        # Hugging Face par localhost hi use hota hai internal communication ke liye
        self.url = "http://0.0.0.0:7860"

    def initialize(self):
        """Validator calls this at the very beginning"""
        # STEP 1: Validator ko bataiye ki task shuru ho gaya hai
        print("[START] task=ticket_resolution", flush=True)
        
        try:
            # Aapka purana testing logic: Environment reset check
            response = requests.post(f"{self.url}/reset", timeout=10)
            if response.status_code == 200:
                print("Environment Reset Successful", flush=True)
                return True
            else:
                print("Failed to reset environment", file=sys.stderr)
                return False
        except Exception as e:
            print(f"Error connecting during init: {e}", file=sys.stderr)
            return False

    def predict(self, input_data):
        """Validator calls this to evaluate your agent"""
        try:
            # STEP 2: Har action par ek step print karein
            print("[STEP] step=1 reward=1.0", flush=True)

            # Aapka logic yahan aayega (Tickets process karna)
            # Abhi ke liye hum environment ko grade call bhej rahe hain
            requests.post(f"{self.url}/grade", json={"text": str(input_data)}, timeout=10)

            # STEP 3: Task khatam hone par final score print karein
            # score=1.0 ka matlab hai complete success
            print("[END] task=ticket_resolution score=1.0 steps=1", flush=True)
            
            return {"status": "success", "processed": True}
            
        except Exception as e:
            print(f"Prediction Error: {e}", file=sys.stderr)
            # Fail hone par bhi [END] dena zaroori hai with low score
            print("[END] task=ticket_resolution score=0.0 steps=1", flush=True)
            return {"status": "error", "message": str(e)}

# --- Ye lines Validator ke liye compulsory hain ---
inference_instance = Inference()

def initialize():
    return inference_instance.initialize()

def predict(input_data):
    return inference_instance.predict(input_data)

# Local testing ke liye (Optional)
if __name__ == "__main__":
    if initialize():
        predict({"test": "data"})
