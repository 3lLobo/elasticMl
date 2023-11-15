# Experiment on a conversation for code generation with the LLama model.
from pprint import pprint
import time
from transformers import pipeline
from src.tcp_llm import listen_for_prompt, StandbyLLM
import asyncio


model_path = 'openlm-research/open_llama_7b'

def get_llm(model_path: str) -> pipeline:
    """
    Get the LLama model.

    Args:
        model_path (str): The path to the model.

    Returns:
        pipeline: The LLama model.
    """
    llm = pipeline(
        'text-generation',
        model=model_path,
        tokenizer=model_path,
        device=0,
        framework='pt',
    )
    # Test the llm
    test_prompt = 'Navy-seals have this saying before going into battle: "Go get '
    res_test = llm(test_prompt, max_length=20, do_sample=True, top_k=10, num_return_sequences=1)
    pprint(res_test)

    return llm


async def main():
    """
    Init the experiment loop with the StandbyLLM on port 9999.
    """
    port = 9999
    log_msg = "\n[LOG] - {time} - {msg} \n"
    llm = get_llm(model_path)
    llama = StandbyLLM(llm)
    pprint(log_msg.format(time=time.time(), msg="LLama loaded 🦙"))
    prompt_gen = listen_for_prompt(port) 

    while True:
        prompt = await prompt_gen.__anext__()
        llama_res = llama.run(prompt)
        pprint(log_msg.format(time=time.time(), msg=llama_res))

        

if __name__ == "__main__":
    asyncio.run(main())
