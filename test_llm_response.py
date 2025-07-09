from llm_api import get_llm_response

question = "Explain reinforcement learning in simple terms"
response = get_llm_response(question)
print ("Model says:",response)