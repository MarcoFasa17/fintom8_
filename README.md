<!-- Chosen Palette: Warm Neutral Harmony -->
<!-- Application Structure Plan: Dashboard Layout. The SPA is structured around a fixed left sidebar (Navigation/Status) and a main scrollable content area divided into three logical, thematic modules: 1. Agent Configuration (Core Identity), 2. Setup Progress (Prerequisites Checklist), and 3. Security Guide (Interactive .env/.gitignore). This structure was chosen because the report's content is primarily procedural (setup steps) and metadata (agent specs). The dashboard design transforms the passive checklist into an active, status-driven interface, improving user understanding and task completion tracking. -->
<!-- Visualization & Content Choices: Summary: Agent Configuration -> Goal: Inform -> Viz/Presentation Method: Key Stats Cards -> Interaction: Click to copy Agent Name -> Justification: Quick reference and utility. Library/Method: HTML/Tailwind/JS. | Report Info: Model/Tools -> Goal: Compare/Proportion -> Viz/Presentation Method: Donut Chart -> Interaction: Hover tooltip -> Justification: Visually represents the agent's minimal complexity (0 tools). Library/Method: Chart.js/Canvas. | Report Info: Prerequisites -> Goal: Organize/Status -> Viz/Presentation Method: Interactive Checklist -> Interaction: Click to toggle completion status -> Justification: Encourages user to track setup steps. Library/Method: HTML/JS. | Report Info: Security Setup -> Goal: Organize/Explain -> Viz/Presentation Method: Tabbed Code Viewer -> Interaction: Click to switch between .env and .gitignore code -> Justification: Hides complex config until needed. Library/Method: HTML/JS. -->
<!-- CONFIRMATION: NO SVG graphics used. NO Mermaid JS used. -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ADK Project Status Dashboard</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@3.7.1/dist/chart.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary-text: #1F2937;
            --background-light: #F9FAFB;
            --accent-blue: #2563EB;
            --border-color: #E5E7EB;
        }
        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--background-light);
            color: var(--primary-text);
        }
        .sidebar {
            width: 16rem; /* 256px */
            min-height: 100vh;
            background-color: #FFFFFF;
            border-right: 1px solid var(--border-color);
        }
        .chart-container {
            /* Enforce responsive boundaries for Chart.js */
            position: relative;
            width: 100%;
            max-width: 400px;
            margin-left: auto;
            margin-right: auto;
            height: 350px;
            max-height: 400px; 
        }
        .content-area {
            max-width: 1200px;
            width: 100%;
        }
        .shadow-custom {
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
        }
        .tab-button.active {
            border-bottom: 2px solid var(--accent-blue);
            color: var(--accent-blue);
            font-weight: 600;
        }
    </style>
</head>
<body class="flex min-h-screen">

    <!-- Sidebar (Navigation & Status) -->
    <div class="sidebar p-4 flex flex-col fixed top-0 left-0 bottom-0 z-10 hidden md:flex">
        <div class="text-xl font-bold mb-8 text-gray-800">ADK Project Fintom8</div>
        <nav class="flex flex-col space-y-2">
            <a href="#config" class="nav-link flex items-center p-2 rounded-lg text-sm font-medium text-gray-700 hover:bg-gray-100 transition duration-150">
                <span>&#x1F916;</span> Agent Config
            </a>
            <a href="#setup" class="nav-link flex items-center p-2 rounded-lg text-sm font-medium text-gray-700 hover:bg-gray-100 transition duration-150">
                <span>&#x2705;</span> Setup Progress
            </a>
            <a href="#security" class="nav-link flex items-center p-2 rounded-lg text-sm font-medium text-gray-700 hover:bg-gray-100 transition duration-150">
                <span>&#x1F512;</span> Security Guide
            </a>
            <a href="#verification" class="nav-link flex items-center p-2 rounded-lg text-sm font-medium text-gray-700 hover:bg-gray-100 transition duration-150">
                <span>&#x1F3A5;</span> Verification
            </a>
        </nav>

        <div class="mt-auto pt-6 border-t border-gray-200">
            <div id="status-display" class="text-xs text-gray-500">Status: Initializing...</div>
        </div>
    </div>

    <!-- Main Content Area -->
    <div class="flex-grow md:ml-[16rem] p-4 sm:p-8 content-area">
        <header class="mb-10 pt-4 md:pt-0">
            <h1 class="text-3xl sm:text-4xl font-extrabold text-gray-900 mb-2">Fintom8 ADK Project Dashboard</h1>
            <p class="text-lg text-gray-600">Interactive exploration of the HelloAgent setup, configuration, and security processes.</p>
        </header>

        <!-- Module 1: Agent Configuration -->
        <section id="config" class="mb-12 p-6 bg-white rounded-xl shadow-custom">
            <h2 class="text-2xl font-bold border-b pb-3 mb-6 text-gray-800">1. Core Agent Identity</h2>
            <p class="text-gray-600 mb-6">This section details the fundamental properties of the `HelloAgent`. It confirms the agent's identity, its core instruction set, and the underlying Gemini model being utilized. Understanding these details ensures the agent is correctly instantiated according to the project goal.</p>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
                <!-- Agent Name Card -->
                <div class="bg-blue-50 p-4 rounded-lg border border-blue-200 shadow-sm transition hover:shadow-md cursor-pointer" onclick="copyToClipboard('HelloAgent', 'name-copy-status')">
                    <div class="text-sm font-medium text-blue-700">Agent Name <span id="name-copy-status" class="text-xs ml-2 text-green-600 opacity-0 transition duration-300">Copied!</span></div>
                    <div class="text-3xl font-extrabold text-blue-800 mt-1" id="agent-name">HelloAgent</div>
                </div>

                <!-- Model Card -->
                <div class="bg-gray-50 p-4 rounded-lg border border-gray-200 shadow-sm">
                    <div class="text-sm font-medium text-gray-700">Model Used</div>
                    <div class="text-3xl font-extrabold text-gray-800 mt-1">gemini-2.0-flash</div>
                </div>

                <!-- Tool Status Card -->
                <div class="bg-red-50 p-4 rounded-lg border border-red-200 shadow-sm">
                    <div class="text-sm font-medium text-red-700">Tools Enabled</div>
                    <div class="text-3xl font-extrabold text-red-800 mt-1">None</div>
                </div>
            </div>

            <div class="bg-gray-50 p-4 rounded-lg border border-gray-200">
                <div class="text-sm font-medium text-gray-700 mb-2">Core Instruction</div>
                <p class="text-gray-800 italic">"Greet the user warmly and confirm you are the result of their first Google ADK project."</p>
            </div>
        </section>

        <!-- Module 2: Setup Status & Progress -->
        <section id="setup" class="mb-12 p-6 bg-white rounded-xl shadow-custom">
            <h2 class="text-2xl font-bold border-b pb-3 mb-6 text-gray-800">2. Setup Progress & Prerequisites</h2>
            <p class="text-gray-600 mb-8">Track the required steps for successful local execution. Mark items complete as you verify your environment. The Donut Chart below visualizes the complexity (or simplicity) of the agent's construction.</p>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-start">
                
                <!-- Setup Checklist -->
                <div id="setup-checklist" class="flex flex-col space-y-3">
                    <!-- Python Prerequisite -->
                    <div class="flex items-center space-x-3 p-3 bg-gray-50 rounded-lg border border-gray-200 cursor-pointer hover:bg-gray-100" onclick="toggleChecklistItem(this, 'status-display')">
                        <input type="checkbox" id="check-python" class="form-checkbox h-5 w-5 text-blue-600 rounded">
                        <label for="check-python" class="text-gray-800 flex-grow">Install/Verify Python 3.9+</label>
                        <span class="text-sm font-medium text-gray-500">Prerequisite</span>
                    </div>
                    <!-- google-genai -->
                    <div class="flex items-center space-x-3 p-3 bg-gray-50 rounded-lg border border-gray-200 cursor-pointer hover:bg-gray-100" onclick="toggleChecklistItem(this, 'status-display')">
                        <input type="checkbox" id="check-genai" class="form-checkbox h-5 w-5 text-blue-600 rounded">
                        <label for="check-genai" class="text-gray-800 flex-grow">Install `google-genai` library</label>
                        <span class="text-sm font-medium text-gray-500">Library</span>
                    </div>
                    <!-- python-dotenv -->
                    <div class="flex items-center space-x-3 p-3 bg-gray-50 rounded-lg border border-gray-200 cursor-pointer hover:bg-gray-100" onclick="toggleChecklistItem(this, 'status-display')">
                        <input type="checkbox" id="check-dotenv" class="form-checkbox h-5 w-5 text-blue-600 rounded">
                        <label for="check-dotenv" class="text-gray-800 flex-grow">Install `python-dotenv`</label>
                        <span class="text-sm font-medium text-gray-500">Library</span>
                    </div>
                    <!-- API Key Setup -->
                    <div class="flex items-center space-x-3 p-3 bg-gray-50 rounded-lg border border-gray-200 cursor-pointer hover:bg-gray-100" onclick="toggleChecklistItem(this, 'status-display')">
                        <input type="checkbox" id="check-key" class="form-checkbox h-5 w-5 text-blue-600 rounded">
                        <label for="check-key" class="text-gray-800 flex-grow">Configure `GEMINI_API_KEY` in `.env`</label>
                        <span class="text-sm font-medium text-red-500">CRITICAL</span>
                    </div>
                    <!-- Execution -->
                    <div class="flex items-center space-x-3 p-3 bg-gray-50 rounded-lg border border-gray-200 cursor-pointer hover:bg-gray-100" onclick="toggleChecklistItem(this, 'status-display')">
                        <input type="checkbox" id="check-execute" class="form-checkbox h-5 w-5 text-blue-600 rounded">
                        <label for="check-execute" class="text-gray-800 flex-grow">Run the agent (e.g., `python run_agent.py`)</label>
                        <span class="text-sm font-medium text-gray-500">Final Step</span>
                    </div>
                </div>

                <!-- Model Complexity Donut Chart -->
                <div class="chart-container bg-white p-4 rounded-lg border border-gray-200 shadow-sm">
                    <canvas id="complexityChart"></canvas>
                    <div class="text-center text-sm text-gray-500 mt-2">Agent Components Analysis (Total potential components: 4)</div>
                </div>
            </div>
        </section>

        <!-- Module 3: Security & Workflow Guide -->
        <section id="security" class="mb-12 p-6 bg-white rounded-xl shadow-custom">
            <h2 class="text-2xl font-bold border-b pb-3 mb-6 text-gray-800">3. Secure Configuration Guide</h2>
            <p class="text-gray-600 mb-6">Security is paramount. The following tabs provide the required setup for API key storage (`.env`) and preventing accidental commits (`.gitignore`).</p>

            <!-- Tabs -->
            <div class="flex border-b border-gray-200 mb-4">
                <button class="tab-button active p-3 mr-4 text-gray-600 transition duration-150" onclick="showTab('env')">.env File (Secret Storage)</button>
                <button class="tab-button p-3 text-gray-600 transition duration-150" onclick="showTab('gitignore')">.gitignore (Exclusions)</button>
            </div>

            <!-- Tab Content -->
            <div id="env-content" class="tab-content">
                <h3 class="text-lg font-semibold mb-3 text-gray-800">`1. .env` Setup</h3>
                <p class="text-gray-600 mb-3">This file stores the `GEMINI_API_KEY` securely. **Never** include your actual key in the content below.</p>
                <div class="bg-gray-800 text-green-400 p-4 rounded-lg text-sm overflow-x-auto">
                    <pre>GEMINI_API_KEY=YOUR_API_KEY_HERE</pre>
                </div>
            </div>

            <div id="gitignore-content" class="tab-content hidden">
                <h3 class="text-lg font-semibold mb-3 text-gray-800">`2. .gitignore` Essentials</h3>
                <p class="text-gray-600 mb-3">This file prevents Git from tracking the secret `.env` file, virtual environments, and other temporary files.</p>
                <div class="bg-gray-800 text-green-400 p-4 rounded-lg text-sm overflow-x-auto">
                    <pre>
# Environment and Configuration Secrets
.env
*.env
*.secrets

# General Python Files
__pycache__/
venv/
.venv/
*.pyc

# Large Files
*.mp4
                    </pre>
                </div>
            </div>
        </section>
        
        <!-- Module 4: Verification -->
        <section id="verification" class="mb-12 p-6 bg-blue-50 rounded-xl border border-blue-200 shadow-custom text-center">
            <h2 class="text-2xl font-bold text-blue-800 mb-4">4. Project Verification</h2>
            <p class="text-blue-700 mb-6">Successful operation is proven by the demo video. Click below to confirm the agent's interaction in the ADK Web UI.</p>
            <button class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-8 rounded-lg shadow-lg transition duration-300 transform hover:scale-[1.02]">
                &#x1F3A5; View Demo Video (ADK_Demo.mp4)
            </button>
        </section>

        <footer class="text-center text-sm text-gray-500 mt-10 p-4 border-t border-gray-200">
            Fintom8 ADK Project Dashboard | Information Architecture by Expert AI | Prepared by: Marco Fasa
        </footer>

    </div>

    <script>
        const setupSteps = [
            { id: 'check-python', status: false },
            { id: 'check-genai', status: false },
            { id: 'check-dotenv', status: false },
            { id: 'check-key', status: false },
            { id: 'check-execute', status: false }
        ];

        // Data for the Donut Chart (Agent Complexity)
        const COMPLEXITY_DATA = {
            used: 2, // Agent Name, Core Instruction, Model (3 components used)
            unused: 2 // Tools (0), More complex configuration (0)
        };

        function updateCompletionStatus() {
            const completed = setupSteps.filter(step => step.status).length;
            const total = setupSteps.length;
            const percentage = Math.round((completed / total) * 100);
            
            const statusText = document.getElementById('status-display');
            if (completed === total) {
                statusText.innerHTML = `<span class="text-green-600 font-semibold">Status: Complete!</span> (${completed}/${total} steps)`;
            } else if (completed > 0) {
                statusText.innerHTML = `<span class="text-yellow-600 font-semibold">Status: In Progress...</span> (${completed}/${total} steps)`;
            } else {
                statusText.innerHTML = `Status: Initializing... (0/${total} steps)`;
            }
        }

        function toggleChecklistItem(element, statusId) {
            const checkbox = element.querySelector('input[type="checkbox"]');
            const stepId = checkbox.id;
            
            // Toggle the visual state
            checkbox.checked = !checkbox.checked;

            // Update the internal state array
            const stepIndex = setupSteps.findIndex(step => step.id === stepId);
            if (stepIndex !== -1) {
                setupSteps[stepIndex].status = checkbox.checked;
                updateCompletionStatus();
            }
        }

        function copyToClipboard(text, statusElementId) {
            document.execCommand('copy'); 
            const statusEl = document.getElementById(statusElementId);
            statusEl.classList.remove('opacity-0');
            statusEl.classList.add('opacity-100');
            setTimeout(() => {
                statusEl.classList.remove('opacity-100');
                statusEl.classList.add('opacity-0');
            }, 1500);
        }

        function showTab(tabId) {
            document.querySelectorAll('.tab-content').forEach(content => {
                content.classList.add('hidden');
            });
            document.getElementById(tabId + '-content').classList.remove('hidden');

            document.querySelectorAll('.tab-button').forEach(button => {
                button.classList.remove('active');
            });
            document.querySelector(`.tab-button[onclick="showTab('${tabId}')"]`).classList.add('active');
        }


        // Chart Initialization
        function initChart() {
            const ctx = document.getElementById('complexityChart').getContext('2d');
            
            const data = {
                labels: ['Simple Agent Configuration (3)', 'Tools (0)'],
                datasets: [{
                    data: [3, 0], // The agent uses Name, Instruction, and Model (3 total points). Tools = 0.
                    backgroundColor: [
                        '#2563EB', // Blue
                        '#D1D5DB'  // Light Gray
                    ],
                    hoverOffset: 4
                }]
            };

            const config = {
                type: 'doughnut',
                data: data,
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'bottom',
                            labels: {
                                color: var(--primary-text)
                            }
                        },
                        title: {
                            display: true,
                            text: 'Complexity: Basic Agent',
                            color: var(--primary-text)
                        },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    let label = context.label || '';
                                    if (label) {
                                        label += ': ';
                                    }
                                    if (context.parsed !== null) {
                                        label += context.parsed + ' items';
                                    }
                                    return label;
                                }
                            }
                        }
                    }
                }
            };

            new Chart(ctx, config);
        }

        // Initialize on load
        document.addEventListener('DOMContentLoaded', () => {
            initChart();
            updateCompletionStatus();
        });
    </script>
</body>
</html>