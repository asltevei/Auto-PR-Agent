import json
import os
from src.utils.mimo_client import MiMoClient

class ReviewerAgent:
    def __init__(self):
        self.client = MiMoClient()
        prompts_path = os.path.join(os.path.dirname(__file__), '../../config/prompts.json')
        with open(prompts_path, 'r') as f:
            self.prompts = json.load(f)

    def analyze_code(self, source_code: str) -> str:
        system_prompt = self.prompts.get("reviewer_prompt")
        # Simulating complex reasoning tracking
        print("[Reviewer Agent] Initiating long-chain reasoning on file dependencies...")
        analysis_result = self.client.call_agent(system_prompt, f"Analyze this code:\n\n{source_code}")
        return analysis_result
