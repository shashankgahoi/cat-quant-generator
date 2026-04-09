# Deployment Guide

## Option 1: Streamlit Cloud (Recommended - Free)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "New app"
5. Select your repository: `cat-quant-generator`
6. Set main file path: `app.py`
7. Add your `GROQ_API_KEY` in Advanced Settings → Secrets:
   ```toml
   GROQ_API_KEY = "your_actual_key_here"
   ```
8. Click "Deploy"

Your app will be live at: `https://your-app-name.streamlit.app`

## Option 2: Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Set up .env file
cp .env.example .env
# Edit .env and add your GROQ_API_KEY

# Run locally
streamlit run app.py
```

## Option 3: Docker (Optional)

```bash
# Build image
docker build -t cat-quant-generator .

# Run container
docker run -p 8501:8501 -e GROQ_API_KEY=your_key cat-quant-generator
```

## Troubleshooting

**Issue**: API key not working
- **Solution**: Make sure you copied the key correctly from Groq Console
- Check that `.env` file exists and has the correct format

**Issue**: Module not found errors
- **Solution**: Run `pip install -r requirements.txt` again

**Issue**: Streamlit not starting
- **Solution**: Make sure port 8501 is available, or specify a different port:
  ```bash
  streamlit run app.py --server.port 8502
  ```
