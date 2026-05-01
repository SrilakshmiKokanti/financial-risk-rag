import pytest
from unittest.mock import patch, MagicMock

def test_load_documents_returns_list():
    with patch('rag.loader.os.listdir', return_value=['credit_risk_policy.txt']):
        with patch('rag.loader.TextLoader') as ml:
            ml.return_value.load.return_value = [MagicMock(page_content='test', metadata={})]
            from rag.loader import load_documents
            assert isinstance(load_documents(), list)

def test_risk_score_critical():
    from agent.tools import calculate_risk_score
    assert 'CRITICAL' in calculate_risk_score.invoke({'probability': 0.9, 'impact': 9.5})

def test_risk_score_low():
    from agent.tools import calculate_risk_score
    assert 'LOW' in calculate_risk_score.invoke({'probability': 0.1, 'impact': 1.0})