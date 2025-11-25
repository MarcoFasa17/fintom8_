<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ADK Agent Fintom8 - Styled Preview</title>
    <!-- Load Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Load Inter font -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f7f9fb; /* Light background */
        }
        .container {
            max-width: 800px;
        }
        /* Custom styling for the header (like a GitHub README) */
        .header-section {
            background-color: #ffffff;
            border-bottom: 1px solid #e2e8f0;
        }
        /* Styling for code blocks */
        pre {
            background-color: #1f2937; /* Dark background for code */
            color: #d1fae5; /* Light green text */
            padding: 1rem;
            border-radius: 0.5rem;
            overflow-x: auto;
            font-size: 0.875rem;
        }
    </style>
</head>
<body class="p-4 sm:p-8">
    <div class="container mx-auto bg-white rounded-xl shadow-2xl overflow-hidden">
        
        <!-- Header Section -->
        <div class="header-section p-6">
            <h1 class="text-4xl font-extrabold text-gray-900 leading-tight">ADK Agent Fintom8</h1>
            <p class="text-lg text-gray-600 mt-2">This project provides a basic implementation of a custom agent using the Google Agent Development Kit (ADK).</p>
        </div>

        <div class="p-6 sm:p-8 space-y-8">
            
            <!-- 1. Overview -->
            <section>
                <h2 class="text-2xl font-bold text-indigo-600 border-b pb-2 mb-4">1. Overview</h2>
                <p class="text-gray-700 leading-relaxed">
                    The <span class="font-semibold text-indigo-700">Fintom8</span> is a minimal Gemini-based agent designed to greet users and confirm its identity as the first successfully initialized ADK project. It uses the 
                    <code class="bg-gray-100 p-1 rounded">gemini-2.0-flash</code> model and currently employs 
                    <strong class="text-red-500">no tools</strong>, demonstrating a simple, foundational agent structure.
                </p>
            </section>

            <!-- 2. Getting Started -->
            <section>
                <h2 class="text-2xl font-bold text-indigo-600 border-b pb-2 mb-4">2. Getting Started</h2>
                <p class="text-gray-700 mb-4">Follow these steps to set up your environment and run the agent.</p>

                <h3 class="text-xl font-semibold mt-6 mb-3 text-gray-800">Prerequisites</h3>
                <p class="text-gray-700 mb-2">You must have the following installed:</p>
                <ul class="list-disc list-inside space-y-1 ml-4 text-gray-700">
                    <li><strong>Python 3.9+</strong></li>
                    <li><strong>Git</strong></li>
                </ul>

                <h3 class="text-xl font-semibold mt-6 mb-3 text-gray-800">Installation</h3>
                
                <ol class="space-y-4">
                    <!-- Step 1 -->
                    <li class="bg-gray-50 p-4 rounded-lg border border-gray-200">
                        <span class="font-medium text-gray-800">1. Clone the repository:</span>
                        <pre>git clone [your-repo-link]
cd project-fintom8</pre>
                    </li>
                    
                    <!-- Step 2 -->
                    <li class="bg-gray-50 p-4 rounded-lg border border-gray-200">
                        <span class="font-medium text-gray-800">2. Install required Python libraries:</span>
                        <p class="text-sm text-gray-600 mb-2">This project requires the Google GenAI SDK and <code class="bg-gray-200 p-1 rounded text-gray-700">python-dotenv</code> for secure secret handling.</p>
                        <pre>pip install google-genai python-dotenv</pre>
                    </li>

                    <!-- Step 3 -->
                    <li class="bg-red-50 p-4 rounded-lg border border-red-200">
                        <span class="font-medium text-red-800">3. Secure API Key Configuration</span>
                        <p class="text-sm text-red-700 mb-2">You must configure your Gemini API key in a secure environment file.</p>
                        <ul class="list-disc list-inside ml-4 text-red-700 mb-2 text-sm">
                            <li>Create a file named <strong>.env</strong> in the root directory of the project.</li>
                            <li>Add your API key using the exact variable name below:</li>
                        </ul>
                        <pre class="bg-red-800 text-yellow-300">GEMINI_API_KEY=YOUR_API_KEY_HERE</pre>
                        <p class="text-xs text-red-700 mt-2">Replace <code class="bg-red-200 p-1 rounded text-red-800">YOUR_API_KEY_HERE</code> with your actual key.</p>
                    </li>
                </ol>
            </section>

            <!-- 3. Usage -->
            <section>
                <h2 class="text-2xl font-bold text-indigo-600 border-b pb-2 mb-4">3. Usage</h2>
                <p class="text-gray-700 mb-3">To run the agent and interact with it, execute the primary agent script:</p>
                <pre>python run_agent.py</pre>
            </section>

            <!-- 4. Security Note (.gitignore) -->
            <section>
                <h2 class="text-2xl font-bold text-indigo-600 border-b pb-2 mb-4">4. Security Note (.gitignore)</h2>
                <p class="text-gray-700 mb-3">To prevent accidental public exposure of your secret key, ensure your <code class="bg-gray-100 p-1 rounded">.gitignore</code> file includes the following essential entries:</p>
                <pre># Environment and Configuration Secrets
.env
*.env

# Python Virtual Environment
venv/
.venv/</pre>
            </section>

            <!-- 5. Contact -->
            <section>
                <h2 class="text-2xl font-bold text-indigo-600 border-b pb-2 mb-4">5. Contact</h2>
                <p class="text-gray-700">For technical assistance or questions about the agent's core function, please refer to the project author.</p>
            </section>
        </div>
        
        <footer class="p-4 sm:p-6 bg-gray-50 text-center text-sm text-gray-500 border-t rounded-b-xl">
            Styled for optimal preview using Tailwind CSS and the Inter font.
        </footer>
    </div>
</body>
</html>