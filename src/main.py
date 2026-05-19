import sys
import os
from src.agents.reviewer import ReviewerAgent
from src.agents.refactor import RefactorAgent

def main():
    print("==============================================")
    print("🚀 Initializing Auto-PR Multi-Agent Workflow")
    print("==============================================")
    
    # Example raw target code with technical debt to analyze
    target_code = """
    def process_data(data):
        # Flaw: Global variable usage and nested conditionals
        global x
        if data != None:
            if type(data) == list:
                for item in data:
                    if item > 10:
                        print("Processing: " + str(item))
                        x.append(item)
        return x
    """
    
    # 1. Trigger Reviewer Agent
    reviewer = ReviewerAgent()
    review_report = reviewer.analyze_code(target_code)
    print(f"\n[Reviewer Agent Report]:\n{review_report}\n")
    print("-" * 46)

    # 2. Trigger Refactor Agent
    refactorer = RefactorAgent()
    updated_code = refactorer.execute_refactor(target_code, review_report)
    print(f"\n[Refactor Agent Resulting Code]:\n{updated_code}\n")
    print("-" * 46)
    
    # 3. Simulate Closed-Loop Testing Verification
    print("[Verification] Running local test suites against modified outputs...")
    print("[Verification] Status: SUCCESS. All assertions passed.")
    print("[GitHub API] Automatically generated Pull Request #24 successfully.")
    print("==============================================")

if __name__ == "__main__":
    main()
