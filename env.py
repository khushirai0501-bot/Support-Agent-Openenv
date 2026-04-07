import random
from models import Observation, Action, Reward
from typing import Tuple

class SupportTicketEnv:
    def __init__(self):
        # Hamara chhota sa database (Simulating real world)
        self.tickets = [
            "Hi, my order #ORD101 is late. I want a refund!",
            "Order #ORD202 delivered but item is broken. Urgent!",
            "Hello, where is my package #ORD303? It's been a week."
        ]
        self.current_ticket = ""
        self.extracted_id = ""
        self.priority = "None"
        self.is_done = False

    def reset(self) -> Observation:
        # Naya task start karne ke liye sab zero karna
        self.current_ticket = random.choice(self.tickets)
        self.extracted_id = ""
        self.priority = "None"
        self.is_done = False
        
        return Observation(
            email_text=self.current_ticket,
            current_status="Open",
            extracted_order_id="None"
        )

    def step(self, action: Action) -> Tuple[Observation, float, bool, dict]:
        reward_value = 0.0
        
        # Logic 1: Agar agent Order ID nikalta hai
        if action.action_type == "extract_id":
            # Simple check: Kya ID email mein hai?
            if action.value in self.current_ticket:
                self.extracted_id = action.value
                reward_value = 0.4 # Partial reward for finding ID
            else:
                reward_value = -0.1 # Penalty for wrong ID

        # Logic 2: Agar agent priority set karta hai
        elif action.action_type == "set_priority":
            self.priority = action.value
            reward_value = 0.2

        # Logic 3: Final submission
        elif action.action_type == "submit":
            if self.extracted_id != "" and self.priority != "None":
                reward_value = 0.4 # Bonus for completing the task
                self.is_done = True
            else:
                reward_value = -0.5 # Big penalty for incomplete work

        obs = Observation(
            email_text=self.current_ticket,
            current_status="Closed" if self.is_done else "Open",
            extracted_order_id=self.extracted_id
        )

        return obs, reward_value, self.is_done, {}

    def state(self):
        # Current status batane ke liye
        return {"ticket": self.current_ticket, "id": self.extracted_id}