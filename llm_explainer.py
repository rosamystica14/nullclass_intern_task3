# llm_explainer.py
from llm_api import get_llm_response

def explain_paper(title, abstract):
    prompt = f"""
    Here's a research paper titled: "{title}"
    Abstract: {abstract}

    Please explain the core idea of this paper in simple terms suitable for a student.
    """
    response = get_llm_response(prompt)
    return response
