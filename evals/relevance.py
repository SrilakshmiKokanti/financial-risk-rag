from app.config import get_llm

PROMPT = (
    'Score how relevant the context is to answering the question '
    'on a scale of 0.0 to 1.0. Only output the float.'
)

def evaluate_relevance(question, context):
    llm = get_llm()
    msg = f'Question: {question}\nContext: {context}'
    resp = llm.invoke([{'role': 'system', 'content': PROMPT}, {'role': 'user', 'content': msg}])
    try:
        return float(resp.content.strip())
    except ValueError:
        return 0.0

if __name__ == '__main__':
    score = evaluate_relevance(
        'What are operational risk controls?',
        'Operational risk controls include process audits and staff training.',
    )
    print(f'Relevance: {score:.2f}')
    assert score >= 0.7
    print('PASSED')