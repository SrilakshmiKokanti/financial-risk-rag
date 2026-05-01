from app.config import get_llm

PROMPT = (
    'Score if the answer contains hallucinated info not in the context. '
    '0.0 = heavy hallucination, 1.0 = none. Only output the float.'
)

def evaluate_hallucination(context, answer):
    llm = get_llm()
    msg = f'Context: {context}\nAnswer: {answer}'
    resp = llm.invoke([{'role': 'system', 'content': PROMPT}, {'role': 'user', 'content': msg}])
    try:
        return float(resp.content.strip())
    except ValueError:
        return 0.0

if __name__ == '__main__':
    score = evaluate_hallucination(
        'Market risk includes equity, interest rate, and FX risk.',
        'Market risk includes equity, interest rate, FX, and crypto volatility.',
    )
    print(f'Hallucination: {score:.2f}')
    assert score >= 0.6
    print('PASSED')