# GenAI Learning Repository

This repository contains my learning journey and experiments with various Generative AI models and frameworks, primarily focusing on LangChain integrations with different LLM providers.

## Features

- OpenAI integration examples
- Hugging Face models integration
- Multiple LLM providers support (OpenAI, Anthropic, Google Gemini, etc.)
- Example scripts demonstrating different use cases

## Prerequisites

- Python 3.8 or higher
- Git
- Access to API keys for the services you want to use (OpenAI, Hugging Face, etc.)

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Anonymous7316/GenAI.git
   cd GenAI
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Create a new virtual environment
   python -m venv venv

   # Activate the virtual environment
   # On Windows:
   venv\Scripts\activate
   # On Linux/Mac:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create a .env file
   touch .env

   # Add your API keys to the .env file:
   OPENAI_API_KEY=your_openai_api_key
   HUGGINGFACE_API_KEY=your_huggingface_api_key
   ANTHROPIC_API_KEY=your_anthropic_api_key
   GOOGLE_API_KEY=your_google_api_key
   ```

## Project Structure

```
├── requirements.txt     # Project dependencies
├── .env                # Environment variables (not tracked in git)
├── .gitignore         # Git ignore rules
└── *.py               # Python script examples
```

## Running the Examples

1. **Basic LLM Demo (OpenAI)**
   ```bash
   python 1_llm_demo.py
   ```

2. **Chat Model with Hugging Face**
   ```bash
   python 3_chatmodel_hf_api.py
   ```

## Notes

- Make sure to keep your API keys secure and never commit them to the repository
- The `.env` file is listed in `.gitignore` to prevent accidentally committing sensitive information
- Each example file demonstrates different aspects of working with LLMs

## Contributing

Feel free to fork this repository and submit pull requests. This is a learning repository, so suggestions and improvements are welcome!

## License

This project is open-source and available under the MIT License.
