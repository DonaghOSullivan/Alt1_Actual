import subprocess

# Try a different port (e.g., 8502)
process = subprocess.Popen([
    "streamlit", "run", "stTest.py",
    "--server.port", "1234",
    "--server.headless", "true"
])