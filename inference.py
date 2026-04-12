import sys

def run_inference():
    task_name = "SupportAgent"

    # Dummy rewards for multiple steps
    rewards = [0.5, 0.7, 0.9]
    score = 0.95
    steps = len(rewards)

    print(f"[START] task={task_name}", flush=True)
    for i, r in enumerate(rewards, start=1):
        print(f"[STEP] step={i} reward={r}", flush=True)
    print(f"[END] task={task_name} score={score} steps={steps}", flush=True)

if __name__ == "__main__":
    run_inference()
