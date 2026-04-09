# 📘 CAT Quant Paper Generator

Generate CAT-level Quantitative Aptitude questions using Groq's LLM API.

## Features

- **Topic-based generation**: Arithmetic, Algebra, Geometry, Number System, Modern Math
- **Difficulty levels**: Easy, Medium, Hard
- **Clean UI**: Built with Streamlit
- **Secure API handling**: Environment-based configuration
- **Fast generation**: Powered by Groq's Llama 3 70B model

## Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd cat-quant-generator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your API key

1. Get a free API key from [Groq Console](https://console.groq.com)
2. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
3. Add your Groq API key to `.env`:
   ```
   GROQ_API_KEY=your_actual_api_key_here
   ```

### 4. Run the app

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Usage

1. Select a topic from the dropdown
2. Choose difficulty level
3. Click "Generate Question"
4. View the generated question with options, answer, and explanation

## Project Structure

```
cat-quant-generator/
├── app.py              # Streamlit UI
├── generator.py        # Question generation logic
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment file
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Technologies Used

- **Streamlit**: Web interface
- **Groq API**: LLM inference (Llama 3 70B)
- **Python-dotenv**: Environment management

## Contributing

Feel free to open issues or submit pull requests!

## License

MIT License
