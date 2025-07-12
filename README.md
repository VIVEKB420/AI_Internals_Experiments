# AI_Internals_Experiments
Small experiments exploring AI/ML concepts.

Summarizer Using Hugging Face model.

Notes:
1) Inference means process of generating outputs (predictions, tokens, or text) from a trained Large Language Model (LLM) like GPT, LLaMA, or Mistral.
2) It works in stages. First the input is converted into tokens. 
3) These tokens are passed through a embedding layer to get the contexual meaning and relationships betwenn them. These are vectors.
4) These vectors go through the LLM Stack(Self Attention, FeedForward layers, Layer Normalization). Self Attention focuses on important parts of the input. FF layers transforms and learns new representations. Normalization for stability and depth.
5) Output is the logits. These are predicted vector of tokens. Raw scores for each possible next token in vocab.
6) Finally, the decoding happens. The logits are converted into probabilities and model decides the next token using different algos like Greedy decoding(most probable toekn), sampling(pick random from top k), Beam Search(explore multiple token paths and select best one)
