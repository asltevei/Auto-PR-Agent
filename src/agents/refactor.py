import json
import os
from src.utils.mimo_client import MiMoClient

class RefactorAgent:
    def __init__(self):
        self.client = MiMoClient()
        prompts_path = os.path.join(os.path.dirname(__file__), '../../config/prompts.json')
        with open(prompts_path, 'r') as f:
            self.prompts = json.load(f)

    def execute_refactor(self, source_code: str, review_notes: str) -> str:
        system_prompt = self.prompts.get("refactor_prompt")
        print("[Refactor Agent] Consuming review reports. Generating updated code modules...")
        user_content = f"Original Code:\n{source_code}\n\nReview Recommendations:\n{review_notes}"
        refactored_code = self.client.call_agent(system_prompt, user_content)
        return refactored_code
