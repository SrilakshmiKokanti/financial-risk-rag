from app.config import get_llm

PROMPT = (
    'You are an evaluator. Score how faithful the answer is to the context '
    'on a scale of 0.0 to 1.0. Only output the float.'
)

def evaluate_faithfulness(question, context, answer):
    llm = get_llm()
    msg = f'Question: {question}\nContext: {context}\nAnswer: {answer}'
    resp = llm.invoke([{'role': 'system', 'content': PROMPT}, {'role': 'user', 'content': msg}])
    try:
        return float(resp.content.strip())
    except ValueError:
        return 0.0

if __name__ == '__main__':
    score = evaluate_faithfulness(
        'What is credit risk?',
        'Credit risk is managed through diversification.',
        'The policy manages credit risk via diversification.',
    )
    print(f'Faithfulness: {score:.2f}')
    assert score >= 0.7
    print('PASSED')