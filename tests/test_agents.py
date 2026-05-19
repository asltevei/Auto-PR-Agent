import pytest
from src.agents.reviewer import ReviewerAgent
from src.agents.refactor import RefactorAgent

def test_agent_workflow_initialization():
    reviewer = ReviewerAgent()
    refactorer = RefactorAgent()
    
    assert reviewer is not None
    assert refactorer is not None

def test_reviewer_workflow_mock():
    reviewer = ReviewerAgent()
    mock_code = "def add(a, b): return a + b"
    result = reviewer.analyze_code(mock_code)
    assert len(result) > 0
