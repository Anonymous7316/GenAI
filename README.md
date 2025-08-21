# GenAI Learning Repository

This repository contains experiments and learning examples for working with Generative AI models and LangChain integrations across multiple LLM providers.

## What's new

- Organized examples under `Langchain_models/` with separate folders for chat models, embedding models, prompts, and message utilities.
- Added demos showing structured output parsing using Pydantic and TypedDict in `Langchain-structured-output/`.
- Included both cloud API and local model examples (Hugging Face API and local HF/transformers usage).

## Features

- OpenAI, Anthropic and Hugging Face integration examples
- Embedding generation and similarity examples
- Chat model examples (API and local)
- Prompt generation utilities and templates
- Structured output parsing demos (Pydantic & TypedDict)

## Prerequisites

- Python 3.8+
- Git
- API keys for any external providers you plan to use (OpenAI, Hugging Face, Anthropic, Google, etc.)

## Setup

1. Create and activate a virtual environment

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file at the repository root and add your API keys (do not commit this file):

   ```env
   OPENAI_API_KEY=your_openai_api_key
   HUGGINGFACE_API_KEY=your_huggingface_api_key
   ANTHROPIC_API_KEY=your_anthropic_api_key
   GOOGLE_API_KEY=your_google_api_key
   # Any other environment variables used by examples
   ```

## Project structure (highlight)

```
README.md
requirements.txt
Langchain_models/
  ChatModels/
    1_chatmodel_openai.py        # Chat model using OpenAI API
    2_chatmodel_anthropic.py     # Chat model using Anthropic API
    3_chatmodel_hf_api.py        # Chat model using Hugging Face Inference API
    4_chatmodel_hf_local.py      # Example using a local HF model (transformers/accelerate)
  EmbeddingModels/
    1_embedding_openai_query.py  # Query-time embeddings (OpenAI)
    2_embedding_openai_docs.py   # Document embeddings and ingestion (OpenAI)
    3_embedding_hf_local.py      # Local HF embeddings example
    4_document_similarity.py     # Document similarity / retrieval demo
  LLMs/
    1_llm_demo.py                # Basic LLM usage and examples
  Messages/
    messages.py                  # Message helper classes/utilities
    massage_placeholder.py       # Placeholder / example message flows
  Prompts/
    prompt_generator.py          # Utilities to construct prompts programmatically
    prompt_ui.py                 # Interactive prompt playground (CLI)
    templates/
      research_paper_summary_template.json
Langchain-output-parser/
  (examples exploring LangChain output parsers)
Langchain-structured-output/
  pydantic_demo.py
  typeddict-demo.py
  with_structured_output_pydantic.py
  with_structured_output_typeddict.py
```

Note: some scripts demonstrate both cloud API usage and how to run models locally (GPU/CPU permitting).

## How to run examples

- Run a simple LLM demo:

  ```bash
  python Langchain_models/LLMs/1_llm_demo.py
  ```

- Run chat model examples (choose the provider script and ensure relevant API keys are set):

  ```bash
  python Langchain_models/ChatModels/1_chatmodel_openai.py
  python Langchain_models/ChatModels/2_chatmodel_anthropic.py
  python Langchain_models/ChatModels/3_chatmodel_hf_api.py
  # For local HF models, review the script and model paths before running
  python Langchain_models/ChatModels/4_chatmodel_hf_local.py
  ```

- Run embeddings and similarity demos:

  ```bash
  python Langchain_models/EmbeddingModels/1_embedding_openai_query.py
  python Langchain_models/EmbeddingModels/2_embedding_openai_docs.py
  python Langchain_models/EmbeddingModels/4_document_similarity.py
  ```

- Structured output parsing demos:

  ```bash
  python Langchain-structured-output/pydantic_demo.py
  python Langchain-structured-output/typeddict-demo.py
  python Langchain-structured-output/with_structured_output_pydantic.py
  python Langchain-structured-output/with_structured_output_typeddict.py
  ```

## Development notes

- Keep API keys out of source control. The repository includes `.gitignore` that excludes `.env`.
- Scripts are small learning examples — adapt them for production use (add error handling, rate limiting, secrets management).
- Local model examples may require extra packages (transformers, accelerate, bitsandbytes) and an appropriate GPU/driver setup.

## Contributing

Contributions, improvements, and bug fixes are welcome. Please open issues or submit pull requests. If you add examples that require heavy dependencies or GPUs, document the setup steps in the example's file header.

## License

This project is open-source and available under the MIT License.
