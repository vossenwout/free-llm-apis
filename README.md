# Free LLM API Providers

Scripts showing you how to invoke the API of LLM providers with a good free tier.

- [src/cerebras_api.py](src/cerebras_api.py)
- [src/groq_api.py](src/groq_api.py)
- [src/mistral_api.py](src/mistral_api.py)
- [src/gemini_api.py](src/gemini_api.py)

## Usage

- Create API Key on [Cerebras](https://cloud.cerebras.ai/)

- Create API Key on [Groq](https://groq.com/)

- Create API Key on [Mistral](https://console.mistral.ai/home)

- Create API Key on [Gemini](https://aistudio.google.com/apikey)

Put your API keys in a `config/.env` file.

```
cp config/.env.example config/.env
```

`config/.env`

```
CEREBRAS_API_KEY=
GROQ_API_KEY=
MISTRAL_API_KEY=
GEMINI_API_KEY=
```

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_1) (if not already installed)

```
uv sync
```

2. Run a script

```
uv run src/cerebras_api.py
```
