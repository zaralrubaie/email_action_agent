from tools.summarize_email import summarize_email
from tools.extract_tasks import extract_tasks
from tools.generate_action_plan import generate_action_plan
from agent.schemas import EmailAnalysis, Task, ActionPlan

def analyze_email(email_text: str) -> EmailAnalysis:
    summary = summarize_email(email_text)
    tasks_raw = extract_tasks(email_text)
    action_plan_raw = generate_action_plan(tasks_raw)

    tasks = [Task(**t) for t in tasks_raw]
    action_plan = ActionPlan(**action_plan_raw)

    return EmailAnalysis(
        summary=summary,
        tasks=tasks,
        action_plan=action_plan
    )
