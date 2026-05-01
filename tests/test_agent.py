import pytest
from unittest.mock import patch, AsyncMock, MagicMock

@pytest.mark.asyncio
async def test_run_agent_returns_answer():
    mock_msg = MagicMock()
    mock_msg.content = 'Credit risk is managed via diversification.'
    with patch('agent.graph.create_react_agent') as mock_fn:
        mock_agent = AsyncMock()
        mock_agent.ainvoke.return_value = {'messages': [mock_msg]}
        mock_fn.return_value = mock_agent
        with patch('agent.graph.get_llm', return_value=MagicMock()):
            from agent.graph import run_agent
            result = await run_agent('What is credit risk?', 'test')
            assert result['answer']