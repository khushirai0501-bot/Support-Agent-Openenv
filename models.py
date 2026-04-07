from pydantic import BaseModel
from typing import Optional, List

# Agent ko kya dikhega (Observation)
class Observation(BaseModel):
    email_text: str          # Customer ki email
    current_status: str       # Ticket open hai ya closed?
    extracted_order_id: str   # Kya koi order ID mil chuki hai?
    last_action_error: Optional[str] = None

# Agent kya kar sakta hai (Action)
class Action(BaseModel):
    action_type: str         # 'extract_id', 'set_priority', 'submit'
    value: str               # Example: 'ORD-123' ya 'High'

# Reward aur Status
class Reward(BaseModel):
    value: float             # 0.0 se 1.0 ke beech
    comment: str             # Kyun mila reward? (Judges love this!)