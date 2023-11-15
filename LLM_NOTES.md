# Huggingface's LLMs

## Generate

```python
gen_output = model.generate(
    input_ids,
    max_length=50,
    num_beams=5,
    no_repeat_ngram_size=2,
    early_stopping=True,
    temperature=0.7,
    top_k=50,
    top_p=0.95,
    do_sample=True,
    num_return_sequences=3,
    bos_token_id=tokenizer.bos_token_id,
    eos_token_id=tokenizer.eos_token_id,
    pad_token_id=tokenizer.pad_token_id,
    decoder_start_token_id=tokenizer.bos_token_id,
    decoder_end_token_id=tokenizer.eos_token_id,
    output_scores=True,
    output_attentions=True,
    output_hidden_states=True,
    return_dict_in_generate=True,
)
```

> What is num_beams? - the number of beams for beam search. Must be between 1 and infinity. 1 means no beam search. Default to 1. 2 -> 2 beams are kept. A beam is a candidate sequence of tokens that the model considers at each step. The model generates a beam of tokens at each time step, and then selects the most probable beam to continue to the next time step. The beam search algorithm keeps track of the top k scoring sequences at each time step, and generates the next token for each of them.

> What does do_sample? - the model will use sampling instead of greedy decoding. Difference between greedy decoding and sampling is that greedy decoding always picks the most probable next token while sampling picks a token from the probability distribution of the next token.

> What is top_k? - the number of highest probability vocabulary tokens to keep for top-k-filtering. Between 1 and infinity. Default to 50. E.g. 1 -> only 1 token is kept, which is the most probable token (argmax). 2 -> keep the top 2 tokens, ...

> What is top_p? - the cumulative probability of the most likely tokens to sample from. Must be between 0 and 1. E.g. 0.95 -> 95% of the probability mass is in the top 50% of the vocabulary, 0.99 -> 99% of the probability mass is in the top 1% of the vocabulary

> What is no_repeat_ngram_size? - the size of n-grams to ban repetition, E.g. 2 -> bigrams cannot be repeated 

> What does early_stopping? - stop when eos_token_id is generated. By default the EOS token id is eos_token_id

> What is the difference between max_length and max_new_tokens? - max_length is the maximum length of the sequence to be generated. max_new_tokens is the maximum number of tokens to generate. If max_new_tokens is not None, then max_length is ignored. If max_new_tokens is None, then max_length is used.

> What happens if the input sequence is longer than max_length? - The output sequence will be truncated to max_length starting from the end of the input sequence. 