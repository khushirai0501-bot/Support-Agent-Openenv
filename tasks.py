from env import SupportTicketEnv
from models import Action

class TaskGrader:
    def __init__(self):
        self.env = SupportTicketEnv()

    # TASK 1: EASY - Sirf Order ID pehchanna
    def task_easy(self, agent_output_id: str):
        obs = self.env.reset()
        # Hum check kar rahe hain kya agent ne wahi ID di jo email mein hai?
        if agent_output_id in obs.email_text and len(agent_output_id) > 4:
            return 1.0  # Perfect Score
        return 0.0

    # TASK 2: MEDIUM - Priority set karna (Logic Based)
    def task_medium(self, email_text: str, priority_selected: str):
        # Agar email mein "Urgent" ya "Broken" hai toh Priority "High" honi chahiye
        score = 0.0
        if "Urgent" in email_text or "broken" in email_text.lower():
            if priority_selected == "High":
                score = 1.0
        else:
            if priority_selected == "Medium" or priority_selected == "Low":
                score = 1.0
        return score

    # TASK 3: HARD - Pura Workflow (ID + Priority + Submit)
    def task_hard(self, steps_taken: list):
        # Steps_taken ek list hogi actions ki
        # Hum check karenge ki kya saare actions sahi sequence mein hain
        score = 0.0
        has_id = False
        has_priority = False
        
        for action in steps_taken:
            if action.action_type == "extract_id": has_id = True
            if action.action_type == "set_priority": has_priority = True
            
        if has_id: score += 0.3
        if has_priority: score += 0.3
        if any(a.action_type == "submit" for a in steps_taken):
            if has_id and has_priority:
                score += 0.4 # Bonus for full completion
                
        return min(score, 1.0)
