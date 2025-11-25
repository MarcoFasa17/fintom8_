**ADK Agent Fintom8**

This project provides a basic implementation of a custom agent using the Google Agent Development Kit (ADK).

1. Overview
The Fintom8 is a minimal Gemini-based agent designed to greet users and confirm its identity as the first successfully initialized ADK project. It uses the gemini-2.0-flash model and currently employs no tools, demonstrating a simple, foundational agent structure.

2. Getting Started
Follow these steps to set up your environment and run the agent.

**Prerequisites**
You must have the following installed:

Python 3.9+
Git
Installation

1. Clone the repository:
git clone [https://github.com/MarcoFasa17/fintom8_]
cd project-fintom8
2. Install required Python libraries:
This project requires the Google GenAI SDK and python-dotenv for secure secret handling.

pip install google-genai python-dotenv
3. Secure API Key Configuration
You must configure your Gemini API key in a secure environment file.

Create a file named .env in the root directory of the project.
Add your API key using the exact variable name below:
GEMINI_API_KEY=YOUR_API_KEY_HERE
Replace YOUR_API_KEY_HERE with your actual key.


If you do not have a GEMINI_API_KEY go  to the Google AI Studio Key Creation Page:Open the following link in your browser:[https://aistudio.google.com/app/apikey]Click "Create API key"

3. Usage
To run the agent and interact with it, execute the primary agent script:

python run_agent.py
4. Security Note (.gitignore)
To prevent accidental public exposure of your secret key, ensure your .gitignore file includes the following essential entries:

# Environment and Configuration Secrets
.env
*.env

# Python Virtual Environment
venv/
.venv/