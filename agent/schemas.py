from pydantic import BaseModel
from typing import List, Optional

class Task(BaseModel):
    task: str
    deadline: Optional[str] = None

class ActionPlan(BaseModel):
    priority: str
    steps: List[str]

class EmailAnalysis(BaseModel):
    summary: str
    tasks: List[Task]
    action_plan: ActionPlan
