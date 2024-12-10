#!/bin/bash
echo "Setting up the environment..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "Setup complete. Run 'streamlit run src/app.py' to start the app."