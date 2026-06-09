# Email Action Agent (FastAPI + LLM)
A lightweight backend service that analyzes email text and generates three outputs:

- Summary of the email
- Extracted actionable tasks
- Step‑by‑step action plan

This project is a simple, modular foundation for building more advanced AI workflows.
It uses FastAPI and a pluggable LLM backend (DeepSeek).

## Features
- Summarizes long or complex emails

- Extracts tasks, deadlines, and priorities

- Generates a structured action plan

- Modular tool design (summarize_email, extract_tasks, generate_action_plan)

- Clean FastAPI endpoint (POST /analyze)

- Environment‑based API key loading

## Project Structure 
``` bash
email_action_agent/
│
├── api/
│   └── main.py
│
├── agent/
│   └── agent.py
│
├── tools/
│   ├── summarize_email.py
│   ├── extract_tasks.py
│   └── generate_action_plan.py
│
├── requirements.txt
└── .env  
```
## SetUp
1. Install dependencies
``` bash
pip install -r requirements.txt
```
2. Add your API key
``` bash
DEEPSEEK_API_KEY=your_key_here
````
3. Run the server
```bash
uvicorn api.main:app --reload
```
4. Test the Api
``` bash
http://127.0.0.1:8000/docs
````
## Notes
This is a simple starter project.
A more advanced multi‑agent LangGraph + Docker system is planned as the next version.
