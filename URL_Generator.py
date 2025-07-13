
from pyngrok import ngrok

ngrok.set_auth_token("2zoXs0S0ySTa7VZeomO5h5zyfxU_2hrrDGFb6fPY9sKjScqq4")

# Kill old tunnels if any
ngrok.kill()

# Create new tunnel to port 8501
public_url = ngrok.connect(8501)
print(f"Streamlit app is live at 👉 {public_url}")

# Launch Streamlit in the background
!streamlit run LLM_Summarizer.py &> /dev/null &

with open("LLM_Summarizer_App_Code.py", "w") as f:
    f.write(code)
