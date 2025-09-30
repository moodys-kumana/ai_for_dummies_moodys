import streamlit as st
import random
import json
import time
from datetime import datetime

# Configure page
st.set_page_config(
    page_title="AI 4 DUMMIES - Interactive Learning Game",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Moody's colors and styling with improved accessibility
def load_css():
    st.markdown("""
    <style>
    /* Main header styling */
    .main-header {
        background: linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    /* Improved sidebar styling for better visibility */
    .score-container {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        border: 2px solid #60a5fa;
    }
    
    .score-container h4 {
        color: white !important;
        font-weight: bold;
        margin-bottom: 0.8rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    .score-container p {
        color: white !important;
        font-weight: 500;
        margin: 0.3rem 0;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    
    .score-container strong {
        color: #ffd700 !important;
        font-size: 1.2em;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.4);
    }
    
    /* Question card with better contrast */
    .question-card {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
        border-left: 6px solid #1e3a8a;
        margin-bottom: 1.5rem;
        border: 2px solid #cbd5e1;
    }
    
    .question-card h2 {
        color: #1e3a8a !important;
        font-weight: bold;
        margin-bottom: 1rem;
        line-height: 1.4;
        text-shadow: none;
    }
    
    .question-card h3 {
        color: #475569 !important;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .question-card p {
        color: #334155 !important;
        font-weight: 500;
    }
    
    /* Hint box with better visibility */
    .hint-box {
        background: linear-gradient(135deg, #fef3c7 0%, #fed7aa 100%);
        color: #92400e;
        padding: 1.2rem;
        border-radius: 8px;
        border-left: 5px solid #f59e0b;
        margin: 1rem 0;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        border: 1px solid #f3a847;
    }
    
    .hint-box h4 {
        color: #92400e !important;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .hint-box p {
        color: #92400e !important;
        font-weight: 500;
        line-height: 1.5;
    }
    
    /* Success box styling */
    .success-box {
        background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
        color: #065f46;
        padding: 1.2rem;
        border-radius: 8px;
        border-left: 5px solid #10b981;
        margin: 1rem 0;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        border: 1px solid #34d399;
    }
    
    .success-box h4 {
        color: #065f46 !important;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .success-box p {
        color: #065f46 !important;
        font-weight: 500;
        line-height: 1.5;
    }
    
    /* Error box styling */
    .error-box {
        background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
        color: #991b1b;
        padding: 1.2rem;
        border-radius: 8px;
        border-left: 5px solid #ef4444;
        margin: 1rem 0;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        border: 1px solid #f87171;
    }
    
    .error-box h4 {
        color: #991b1b !important;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .error-box p {
        color: #991b1b !important;
        font-weight: 500;
        line-height: 1.5;
    }
    
    /* Category badge with better contrast */
    .category-badge {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        border: 2px solid #60a5fa;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    /* Sidebar improvements */
    .css-1d391kg {
        background-color: #1e293b !important;
    }
    
    /* Radio button styling for better visibility */
    .stRadio > label {
        background-color: #f1f5f9;
        padding: 0.8rem 1rem;
        border-radius: 8px;
        margin: 0.3rem 0;
        border: 2px solid #cbd5e1;
        cursor: pointer;
        transition: all 0.2s ease;
        color: #1e293b !important;
        font-weight: 500;
    }
    
    .stRadio > label:hover {
        background-color: #e2e8f0;
        border-color: #3b82f6;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    /* Button styling improvements */
    .stButton > button {
        font-weight: bold;
        text-shadow: none;
        border: 2px solid transparent;
        transition: all 0.2s ease;
    }
    
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        color: white;
        border: 2px solid #60a5fa;
    }
    
    .stButton > button[kind="primary"]:hover {
        background: linear-gradient(135deg, #1e40af 0%, #2563eb 100%);
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# Questions Database
def get_questions_database():
    return {
        "🤖 AI Fundamentals": [
            {
                "question": "What does 'AI' stand for?",
                "options": ["Automated Intelligence", "Artificial Intelligence", "Advanced Information", "Algorithmic Integration"],
                "correct": 1,
                "hint": "Think about creating human-like intelligence in machines. It's about simulating human thought processes.",
                "explanation": "AI stands for Artificial Intelligence - the simulation of human intelligence in computers designed to think and act like humans.",
                "difficulty": "Easy"
            },
            {
                "question": "What is Machine Learning?",
                "options": ["Programming machines manually", "Algorithms that learn from data", "Building physical robots", "Creating websites"],
                "correct": 1,
                "hint": "Instead of programming every scenario, these systems improve their performance as they process more information.",
                "explanation": "Machine Learning is a subset of AI where algorithms learn patterns from data and improve their performance over time without being explicitly programmed for every scenario.",
                "difficulty": "Medium"
            },
            {
                "question": "What is Natural Language Processing (NLP)?",
                "options": ["Processing natural resources", "Understanding human language", "Creating natural sounds", "Processing images"],
                "correct": 1,
                "hint": "Think about chatbots, translation tools, and voice assistants. They need to understand what humans are saying.",
                "explanation": "NLP enables computers to understand, interpret, and generate human language, powering tools like chatbots and translation services.",
                "difficulty": "Medium"
            },
            {
                "question": "What is a Neural Network?",
                "options": ["A computer network", "Brain-inspired computing model", "Internet connection", "Database system"],
                "correct": 1,
                "hint": "It's inspired by how neurons work in the human brain, with interconnected nodes that process information.",
                "explanation": "Neural networks are computing systems inspired by biological neural networks, consisting of interconnected nodes that process information in layers.",
                "difficulty": "Hard"
            },
            {
                "question": "What is Computer Vision?",
                "options": ["Computer screens", "Machine sight and image understanding", "Video games", "Computer graphics"],
                "correct": 1,
                "hint": "Think about quality control cameras in factories that can detect defective products automatically.",
                "explanation": "Computer Vision enables machines to interpret and understand visual information from images and videos, like automated quality control systems.",
                "difficulty": "Medium"
            }
        ],
        "💻 Programming Languages": [
            {
                "question": "Which language is best for beginners and data analysis?",
                "options": ["C++", "Python", "Assembly", "Fortran"],
                "correct": 1,
                "hint": "It's named after a British comedy group and is known for its simple, readable syntax.",
                "explanation": "Python is ideal for beginners due to its simple syntax and excellent for data analysis with libraries like pandas and numpy.",
                "difficulty": "Easy"
            },
            {
                "question": "What is JavaScript primarily used for?",
                "options": ["Desktop applications", "Web interactivity", "Operating systems", "Database management"],
                "correct": 1,
                "hint": "Think about buttons, animations, and interactive elements you see on websites.",
                "explanation": "JavaScript makes websites interactive - handling button clicks, animations, form validation, and dynamic content updates.",
                "difficulty": "Easy"
            },
            {
                "question": "What should you mention in a Python prompt for better results?",
                "options": ["Just the task", "'I'm a beginner' + 'Include error handling' + 'Explain each library used'", "Only the programming language", "Make it complex"],
                "correct": 1,
                "hint": "Python AI specializes in data analysis, automation scripts, and AI/ML projects - context about your skill level and requirements helps.",
                "explanation": "Effective Python prompts include skill level, request error handling, and ask for explanations of libraries used for better learning outcomes.",
                "difficulty": "Medium"
            },
            {
                "question": "What's a good Java prompt for beginners?",
                "options": ["Write Java code", "Create a BankAccount class with deposit/withdraw methods, input validation, and explain OOP concepts", "Make a program", "Java application please"],
                "correct": 1,
                "hint": "Good Java prompts specify the class structure, required methods, validation needs, and ask for explanations of object-oriented concepts.",
                "explanation": "Effective Java prompts are specific about class structure, methods needed, validation requirements, and request explanations of OOP principles.",
                "difficulty": "Hard"
            },
            {
                "question": "Which is better for a SQL learning prompt?",
                "options": ["Give me SQL", "I'm new to databases. Help me write queries for a bookstore with books, authors, customers tables. Show joins.", "Database code", "SQL queries"],
                "correct": 1,
                "hint": "Good SQL prompts provide context (beginner), describe the database structure, and specify what relationships to explore.",
                "explanation": "Effective SQL prompts include skill level, database structure context, and specific requirements like learning joins between tables.",
                "difficulty": "Medium"
            },
            {
                "question": "What makes C# good for game development prompts?",
                "options": ["It's fast", "Mentioning Unity and requesting player controller scripts with physics explanations", "It's Microsoft", "It's object-oriented"],
                "correct": 1,
                "hint": "C# is commonly used with Unity for game development, so mentioning Unity context and requesting explanations of game-specific concepts helps.",
                "explanation": "C# game development prompts work best when mentioning Unity, requesting specific game mechanics, and asking for explanations of physics concepts.",
                "difficulty": "Hard"
            },
            {
                "question": "What should you avoid in coding prompts?",
                "options": ["Being specific", "Vague requests like 'Make a website' or 'Create a login system'", "Asking for explanations", "Mentioning your skill level"],
                "correct": 1,
                "hint": "Vague prompts like 'make a website' are too broad and don't give AI enough context to provide useful, educational code.",
                "explanation": "Vague prompts produce generic, hard-to-understand code. Specific prompts with context and requirements produce much better learning outcomes.",
                "difficulty": "Easy"
            },
            {
                "question": "What's the 'Step-by-Step' approach for complex coding tasks?",
                "options": ["Ask for everything at once", "'Break this into steps: 1) Basic structure 2) Main functionality 3) Error handling and polish'", "Request only final code", "Avoid planning"],
                "correct": 1,
                "hint": "Breaking complex tasks into steps helps you understand the development process and learn progressively.",
                "explanation": "The step-by-step approach helps you understand the development process by breaking complex tasks into manageable, educational phases.",
                "difficulty": "Medium"
            }
        ],
        "🎯 Vibe Coding Techniques": [
            {
                "question": "What is 'Vibe Coding' with AI?",
                "options": ["Coding with music", "AI-assisted programming", "Coding vibes only", "Fast coding"],
                "correct": 1,
                "hint": "It's about collaborating with AI tools like Copilot to write code more efficiently, even if you're not a programmer.",
                "explanation": "Vibe Coding refers to using AI assistants like GitHub Copilot to help write, explain, and debug code through natural language prompts.",
                "difficulty": "Easy"
            },
            {
                "question": "What makes a good AI coding prompt?",
                "options": ["Very short requests", "Detailed, specific descriptions", "Only technical jargon", "Asking for everything at once"],
                "correct": 1,
                "hint": "The better you explain what you want, the better the AI can help. Think 'explain like I'm 5, then show the code'.",
                "explanation": "Good prompts are detailed and specific, explaining the goal, expected behavior, and context. This helps AI provide better, more targeted solutions.",
                "difficulty": "Medium"
            },
            {
                "question": "Which is a better JavaScript prompt for beginners?",
                "options": ["Make a button", "Create a button that changes background color when clicked, cycling through 5 colors with explanations", "JavaScript code please", "Build something interactive"],
                "correct": 1,
                "hint": "The good prompt includes context (beginner), specific functionality, and asks for explanations.",
                "explanation": "Detailed prompts with context, specific requirements, and requests for explanations produce much better, more educational results than vague requests.",
                "difficulty": "Medium"
            },
            {
                "question": "What's the 'Explain Like I'm 5' method in Vibe Coding?",
                "options": ["Only use simple words", "Add 'Explain like I'm 5, show code, then explain with technical terms'", "Avoid technical terms completely", "Write very short prompts"],
                "correct": 1,
                "hint": "This method asks for multiple levels of explanation - simple first, then technical - to help you learn progressively.",
                "explanation": "The ELI5 method requests simple explanations first, then code, then technical explanations, creating a learning progression from basic to advanced.",
                "difficulty": "Hard"
            },
            {
                "question": "Which phrase is most effective for debugging with AI?",
                "options": ["This doesn't work, help me", "My [language] code gives error [exact message]. I expect [X] but get [Y]. Here's my code: [paste]", "Fix my code", "There's a bug somewhere"],
                "correct": 1,
                "hint": "The best debugging prompts include the language, exact error message, expected vs actual behavior, and the actual code.",
                "explanation": "Effective debugging prompts provide complete context: language, exact error, expected behavior, actual behavior, and the problematic code.",
                "difficulty": "Hard"
            },
            {
                "question": "What should you include in a Python automation prompt?",
                "options": ["Just the task description", "'I'm a beginner' + task + 'include error handling' + 'explain each step'", "The code language only", "A simple request"],
                "correct": 1,
                "hint": "For Python automation, mention your skill level, be specific about the task, ask for error handling, and request explanations.",
                "explanation": "Effective Python prompts include skill level context, specific task requirements, error handling requests, and asks for step-by-step explanations.",
                "difficulty": "Medium"
            },
            {
                "question": "What's a 'magic phrase' that improves AI code quality?",
                "options": ["Make it fast", "Include comments explaining each step", "Use advanced features", "Make it complex"],
                "correct": 1,
                "hint": "When learning, you want the AI to teach you. Ask for explanations that help you understand what the code does.",
                "explanation": "'Include comments explaining...' is a magic phrase that gets well-documented code that teaches you while providing working solutions.",
                "difficulty": "Easy"
            },
            {
                "question": "What's the best way to ask for multiple solutions?",
                "options": ["Give me code", "Show me three different ways to solve this", "What's the answer?", "Make it work"],
                "correct": 1,
                "hint": "Asking for multiple approaches helps you learn different methods and choose the best one for your situation.",
                "explanation": "'Show me three different ways...' helps you learn multiple approaches to the same problem, expanding your understanding and options.",
                "difficulty": "Medium"
            }
        ],
        "🏢 Workplace Applications": [
            {
                "question": "What happens when you use Python in Excel 2024?",
                "options": ["Excel crashes", "You can write Python code directly in Excel cells", "Nothing changes", "You need to install new software"],
                "correct": 1,
                "hint": "Microsoft integrated Python into Excel in 2024, allowing you to use pandas, matplotlib and other libraries directly in spreadsheets.",
                "explanation": "Python in Excel allows you to write Python scripts directly in cells, using libraries like pandas for data manipulation and matplotlib for charts.",
                "difficulty": "Medium"
            },
            {
                "question": "A financial analyst spends 4 hours monthly copying data between systems. How can coding help?",
                "options": ["Make the task more complex", "Reduce it to a 2-minute automated script", "Require more manual work", "Eliminate the need for data"],
                "correct": 1,
                "hint": "A Python script can pull data via API, calculate results, and update Excel automatically - from 4 hours to 2 minutes.",
                "explanation": "Automation scripts can pull data via APIs, perform calculations, and update systems automatically, eliminating manual copy-paste work and reducing errors.",
                "difficulty": "Easy"
            },
            {
                "question": "What's the best approach for cleaning messy data with programming?",
                "options": ["Manually fix each cell", "Use pandas to handle missing values, duplicates, and format issues", "Delete all bad data", "Ignore the problems"],
                "correct": 1,
                "hint": "Python's pandas library can fill empty cells, remove duplicates, and fix formats in just a few lines of code.",
                "explanation": "Pandas excels at data cleaning - filling missing values, removing duplicates, splitting columns, and standardizing formats automatically.",
                "difficulty": "Medium"
            },
            {
                "question": "How can you automate PowerPoint report generation?",
                "options": ["It's impossible", "Use python-pptx library to create slides programmatically", "Only manually", "Hire a designer"],
                "correct": 1,
                "hint": "The python-pptx library can create PowerPoint files, insert data, charts, and images automatically from templates.",
                "explanation": "Python-pptx allows you to create PowerPoint presentations programmatically, pulling latest data and generating consistent, up-to-date reports automatically.",
                "difficulty": "Hard"
            },
            {
                "question": "What makes RPA (Robotic Process Automation) different from traditional coding?",
                "options": ["It's more complex", "It uses drag-and-drop interfaces to automate UI tasks", "It requires advanced programming", "It only works with databases"],
                "correct": 1,
                "hint": "RPA tools like Power Automate use visual workflows to automate clicking, copying, and moving data between applications.",
                "explanation": "RPA provides drag-and-drop automation for UI tasks like clicking buttons and copying data between apps, without traditional coding.",
                "difficulty": "Easy"
            },
            {
                "question": "Which is the most immediately useful 'language' for data-heavy jobs?",
                "options": ["C++", "SQL", "Assembly", "JavaScript"],
                "correct": 1,
                "hint": "This language reads like English (SELECT, FROM, WHERE) and lets you query databases directly instead of waiting for IT reports.",
                "explanation": "SQL is immediately applicable for anyone working with data, allowing direct database queries without waiting for custom reports from IT.",
                "difficulty": "Easy"
            },
            {
                "question": "How can you create interactive dashboards for your team?",
                "options": ["Only with expensive software", "Use JavaScript libraries like D3.js or Python's Dash/Streamlit", "It's impossible", "Only professional developers can do this"],
                "correct": 1,
                "hint": "Tools like Plotly Dash (Python) or D3.js (JavaScript) can create web-based interactive dashboards that run in browsers.",
                "explanation": "Modern libraries like Dash, Streamlit, and D3.js make it possible to create interactive, web-based dashboards without being a professional developer.",
                "difficulty": "Hard"
            },
            {
                "question": "What's a realistic outcome for HR using machine learning?",
                "options": ["Replace all HR staff", "Predict which employees might leave and take proactive action", "Make hiring decisions automatically", "Eliminate the need for interviews"],
                "correct": 1,
                "hint": "ML can analyze patterns in tenure, raises, and promotion data to identify employees at risk of leaving, helping HR act proactively.",
                "explanation": "Machine learning can help HR predict employee churn by analyzing historical data patterns, enabling proactive retention strategies.",
                "difficulty": "Medium"
            }
        ]
    }

# Initialize session state
def init_session_state():
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'questions_answered' not in st.session_state:
        st.session_state.questions_answered = 0
    if 'show_hint' not in st.session_state:
        st.session_state.show_hint = False
    if 'game_started' not in st.session_state:
        st.session_state.game_started = False
    if 'current_category' not in st.session_state:
        st.session_state.current_category = None
    if 'streak' not in st.session_state:
        st.session_state.streak = 0
    if 'best_streak' not in st.session_state:
        st.session_state.best_streak = 0
    if 'questions_pool' not in st.session_state:
        st.session_state.questions_pool = []
    if 'achievements' not in st.session_state:
        st.session_state.achievements = []
    if 'wrong_answers' not in st.session_state:
        st.session_state.wrong_answers = 0
    if 'hints_used' not in st.session_state:
        st.session_state.hints_used = 0
    if 'view_mode' not in st.session_state:
        st.session_state.view_mode = 'welcome'  # Options: 'welcome', 'learning_ai', 'learning_prog', 'game'

# Achievement System
def check_achievements():
    new_achievements = []
    
    # Score-based achievements
    if st.session_state.score >= 100 and "First Century" not in st.session_state.achievements:
        new_achievements.append("First Century")
    if st.session_state.score >= 300 and "Knowledge Master" not in st.session_state.achievements:
        new_achievements.append("Knowledge Master")
    
    # Streak-based achievements
    if st.session_state.streak >= 3 and "Hot Streak" not in st.session_state.achievements:
        new_achievements.append("Hot Streak")
    if st.session_state.streak >= 5 and "On Fire!" not in st.session_state.achievements:
        new_achievements.append("On Fire!")
    if st.session_state.streak >= 10 and "Unstoppable" not in st.session_state.achievements:
        new_achievements.append("Unstoppable")
    
    # Completion achievements
    if st.session_state.questions_answered >= 10 and "Halfway Hero" not in st.session_state.achievements:
        new_achievements.append("Halfway Hero")
    if st.session_state.questions_answered >= 20 and "Quiz Master" not in st.session_state.achievements:
        new_achievements.append("Quiz Master")
    
    # Special achievements
    if st.session_state.hints_used == 0 and st.session_state.questions_answered >= 5 and "No Hints Needed" not in st.session_state.achievements:
        new_achievements.append("No Hints Needed")
    
    st.session_state.achievements.extend(new_achievements)
    return new_achievements

def get_streak_emoji():
    if st.session_state.streak >= 10:
        return "🔥🔥🔥"
    elif st.session_state.streak >= 5:
        return "🔥🔥"
    elif st.session_state.streak >= 3:
        return "🔥"
    else:
        return "⭐"

def get_motivational_message(streak):
    """Get motivational messages and animations based on streak"""
    messages = {
        3: {
            "title": "3-ON-A-ROW",
            "message": "You are ON FIRE! 🔥",
            "emoji": "🚀",
            "style": "fire"
        },
        4: {
            "title": "4-IN-A-ROW", 
            "message": "Unstoppable Force! 💪",
            "emoji": "⚡",
            "style": "lightning"
        },
        5: {
            "title": "5-STREAK COMBO",
            "message": "You are the GOAT! 🐐",
            "emoji": "👑",
            "style": "crown"
        },
        6: {
            "title": "6-PACK POWER",
            "message": "Knowledge Master! 🧠",
            "emoji": "💎",
            "style": "diamond"
        },
        7: {
            "title": "MAGNIFICENT 7",
            "message": "Coding Wizard! 🪄",
            "emoji": "🌟",
            "style": "wizard"
        },
        8: {
            "title": "GREAT 8",
            "message": "AI Genius Detected! 🤖",
            "emoji": "🎯",
            "style": "genius"
        },
        10: {
            "title": "PERFECT 10",
            "message": "LEGENDARY STATUS! 🏆",
            "emoji": "👑💎🔥",
            "style": "legendary"
        }
    }
    
    # For streaks higher than 10, use the legendary message
    if streak >= 10:
        return messages[10]
    elif streak in messages:
        return messages[streak]
    else:
        return None

def show_motivational_booster(streak):
    """Show animated motivational booster for streaks"""
    message_data = get_motivational_message(streak)
    if not message_data:
        return
    
    # CSS for motivational animations
    booster_css = f"""
    <style>
    .motivational-booster {{
        background: linear-gradient(45deg, #ff6b6b, #ffd93d, #6bcf7f, #4d96ff, #9c88ff);
        background-size: 300% 300%;
        animation: rainbow 2s ease infinite, pulse 1s ease infinite;
        padding: 1.5rem;
        border-radius: 20px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        border: 3px solid #fff;
        color: white;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
    }}
    
    .booster-title {{
        font-size: 1.8rem;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 2px;
    }}
    
    .booster-message {{
        font-size: 1.3rem;
        margin-bottom: 0.5rem;
    }}
    
    .booster-emoji {{
        font-size: 2.5rem;
        animation: bounce 1s infinite;
    }}
    
    @keyframes rainbow {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}
    
    @keyframes pulse {{
        0% {{ transform: scale(1); }}
        50% {{ transform: scale(1.05); }}
        100% {{ transform: scale(1); }}
    }}
    
    @keyframes bounce {{
        0%, 20%, 50%, 80%, 100% {{ transform: translateY(0); }}
        40% {{ transform: translateY(-10px); }}
        60% {{ transform: translateY(-5px); }}
    }}
    
    .fire-effect {{
        background: linear-gradient(45deg, #ff4444, #ff8800, #ffaa00);
    }}
    
    .lightning-effect {{
        background: linear-gradient(45deg, #4444ff, #8800ff, #aa00ff);
    }}
    
    .crown-effect {{
        background: linear-gradient(45deg, #ffd700, #ffed4e, #fff176);
    }}
    
    .diamond-effect {{
        background: linear-gradient(45deg, #00d4ff, #0099cc, #0066aa);
    }}
    
    .wizard-effect {{
        background: linear-gradient(45deg, #9c27b0, #673ab7, #3f51b5);
    }}
    
    .genius-effect {{
        background: linear-gradient(45deg, #4caf50, #8bc34a, #cddc39);
    }}
    
    .legendary-effect {{
        background: linear-gradient(45deg, #ff1744, #ff5722, #ff9800, #ffc107, #ffeb3b);
        background-size: 400% 400%;
        animation: legendary 1.5s ease infinite;
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.8);
    }}
    
    @keyframes legendary {{
        0% {{ background-position: 0% 50%; box-shadow: 0 0 30px rgba(255, 215, 0, 0.8); }}
        50% {{ background-position: 100% 50%; box-shadow: 0 0 50px rgba(255, 215, 0, 1); }}
        100% {{ background-position: 0% 50%; box-shadow: 0 0 30px rgba(255, 215, 0, 0.8); }}
    }}
    </style>
    """
    
    # Display the booster
    st.markdown(booster_css, unsafe_allow_html=True)
    
    booster_html = f"""
    <div class="motivational-booster {message_data['style']}-effect">
        <div class="booster-title">{message_data['title']}</div>
        <div class="booster-message">{message_data['message']}</div>
        <div class="booster-emoji">{message_data['emoji']}</div>
    </div>
    """
    
    st.markdown(booster_html, unsafe_allow_html=True)

def get_reward_points(difficulty, streak_bonus=False):
    base_points = {"Easy": 10, "Medium": 15, "Hard": 20}
    points = base_points.get(difficulty, 10)
    if streak_bonus and st.session_state.streak >= 3:
        points += st.session_state.streak * 2  # Streak bonus!
    return points

def setup_questions_pool():
    """Set up a randomized pool of questions from all categories"""
    questions_db = get_questions_database()
    all_questions = []
    
    # Collect questions from all categories
    for category_questions in questions_db.values():
        all_questions.extend(category_questions)
    
    # Shuffle and select 20 questions
    random.shuffle(all_questions)
    st.session_state.questions_pool = all_questions[:20]

def show_learning_module_ai():
    """Display the AI & Coding presentation module"""
    st.markdown("""
    <div style="background: white; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h2 style="color: #1e3a8a;">📖 AI & Coding for Dummies - Educational Guide</h2>
        <p style="color: #475569;">Review this comprehensive guide before starting the game.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Read and display the HTML file
    try:
        with open('ai-coding-dummies-presentation.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        st.components.v1.html(html_content, height=800, scrolling=True)
    except FileNotFoundError:
        st.error("Learning module file not found. Please ensure 'ai-coding-dummies-presentation.html' is in the game directory.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back to Welcome", use_container_width=True):
            st.session_state.view_mode = 'welcome'
            st.rerun()
    with col2:
        if st.button("🚀 Start the Game!", type="primary", use_container_width=True):
            st.session_state.game_started = True
            st.session_state.view_mode = 'game'
            st.rerun()

def show_learning_module_programming():
    """Display the Programming Languages module"""
    st.markdown("""
    <div style="background: white; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h2 style="color: #1e3a8a;">💻 Programming Languages - Beginner's Guide</h2>
        <p style="color: #475569;">Learn about different programming languages before starting the game.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Read and display the HTML file
    try:
        with open('programming-languages.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        st.components.v1.html(html_content, height=800, scrolling=True)
    except FileNotFoundError:
        st.error("Learning module file not found. Please ensure 'programming-languages.html' is in the game directory.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back to Welcome", use_container_width=True):
            st.session_state.view_mode = 'welcome'
            st.rerun()
    with col2:
        if st.button("🚀 Start the Game!", type="primary", use_container_width=True):
            st.session_state.game_started = True
            st.session_state.view_mode = 'game'
            st.rerun()

def main():
    load_css()
    init_session_state()
    
    # Setup questions if not done
    if not st.session_state.questions_pool and st.session_state.game_started:
        setup_questions_pool()
    
    # Main header
    st.markdown("""
    <div class="main-header">
        <h1>🤖 AI 4 DUMMIES</h1>
        <h3>Interactive Learning Game for Non-Tech Professionals</h3>
        <p>Master the fundamentals of AI and coding through engaging gameplay!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar for game navigation
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/artificial-intelligence.png", width=80)
        st.title("🎮 Game Menu")
        
        # Score and streak display with motivational elements
        streak_emoji = get_streak_emoji()
        
        # Get current motivational message if in streak
        current_motivation = ""
        if st.session_state.streak >= 3:
            message_data = get_motivational_message(st.session_state.streak)
            if message_data:
                current_motivation = f"<p style='color: #ffd700; font-weight: bold; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);'>{message_data['emoji']} {message_data['title']}</p>"
        
        st.markdown(f"""
        <div class="score-container">
            <h4>📊 Current Score</h4>
            <p><strong>{st.session_state.score}</strong> points</p>
            <p>Questions: {st.session_state.questions_answered}/20</p>
            <hr>
            <h4>🔥 Streak Status</h4>
            <p>{streak_emoji} Current: <strong>{st.session_state.streak}</strong></p>
            <p>🏆 Best: <strong>{st.session_state.best_streak}</strong></p>
            {current_motivation}
        </div>
        """, unsafe_allow_html=True)
        
        # Achievements display
        if st.session_state.achievements:
            st.markdown("### 🏆 Achievements")
            for achievement in st.session_state.achievements:
                st.markdown(f"🥇 {achievement}")
        
        # Game categories
        st.markdown("### 📚 Categories Available")
        categories = [
            "🤖 AI Fundamentals",
            "💻 Programming Languages", 
            "🎯 Vibe Coding Techniques",
            "🏢 Workplace Applications"
        ]
        
        for cat in categories:
            st.markdown(f"- {cat}")
        
        # Progress bar
        if st.session_state.game_started:
            progress = st.session_state.questions_answered / 20
            st.progress(progress)
            st.markdown(f"Progress: {int(progress*100)}%")
    
    # Main game area - handle different view modes
    if st.session_state.view_mode == 'learning_ai':
        show_learning_module_ai()
    elif st.session_state.view_mode == 'learning_prog':
        show_learning_module_programming()
    elif not st.session_state.game_started:
        show_welcome_screen()
    else:
        show_game_interface()

def show_welcome_screen():
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        ## 🎯 Welcome to AI 4 DUMMIES!
        
        ### What you'll learn:
        - 🤖 **AI Terminology**: Master the essential concepts
        - 💻 **Programming Languages**: Understand the popular ones
        - 🎯 **Vibe Coding**: Learn AI-assisted programming techniques
        - 🏢 **Real Applications**: See how it applies to your work
        
        ### Game Rules:
        - ✅ 20 questions across 4 categories
        - 🎯 Multiple choice format
        - 💡 Hints available for each question
        - 🏆 Score points for correct answers
        - 📈 Learn from mistakes with detailed explanations
        """)
        
        st.markdown("---")
        st.markdown("### 📚 Learning Modules")
        st.markdown("Review these educational materials before starting the game:")
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            if st.button("📖 AI & Coding Guide", use_container_width=True):
                st.session_state.view_mode = 'learning_ai'
                st.rerun()
        
        with col_b:
            if st.button("💻 Programming Languages", use_container_width=True):
                st.session_state.view_mode = 'learning_prog'
                st.rerun()
        
        st.markdown("---")
        st.markdown("### Ready to become an AI & Coding expert?")
        
        if st.button("🚀 Start the Game!", type="primary", use_container_width=True):
            st.session_state.game_started = True
            st.session_state.view_mode = 'game'
            st.rerun()

def show_game_interface():
    if st.session_state.questions_answered >= 20:
        show_final_results()
        return
    
    current_q = st.session_state.questions_pool[st.session_state.current_question]
    
    # Question header with category badge
    st.markdown(f"""
    <div class="category-badge">{current_q['category']}</div>
    """, unsafe_allow_html=True)
    
    # Question card
    st.markdown(f"""
    <div class="question-card">
        <h3>Question {st.session_state.questions_answered + 1}/20</h3>
        <h2>{current_q['question']}</h2>
        <p><strong>Difficulty:</strong> {current_q['difficulty']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Answer options
    selected_answer = st.radio(
        "Choose your answer:",
        options=current_q['options'],
        key=f"q_{st.session_state.current_question}",
        index=None
    )
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("💡 Show Hint", help="Get a helpful hint for this question"):
            st.session_state.show_hint = True
            st.session_state.hints_used += 1
    
    with col2:
        submit_disabled = selected_answer is None
        if st.button("✅ Submit Answer", disabled=submit_disabled, type="primary"):
            handle_answer_submission(selected_answer, current_q)
    
    with col3:
        if st.button("🔄 Restart Game"):
            restart_game()
    
    # Show hint if requested
    if st.session_state.show_hint:
        st.markdown(f"""
        <div class="hint-box">
            <h4>💡 Hint</h4>
            <p>{current_q['hint']}</p>
        </div>
        """, unsafe_allow_html=True)

def handle_answer_submission(selected_answer, current_q):
    correct_answer = current_q['options'][current_q['correct']]
    is_correct = selected_answer == correct_answer
    
    if is_correct:
        # Correct answer handling
        st.session_state.streak += 1
        if st.session_state.streak > st.session_state.best_streak:
            st.session_state.best_streak = st.session_state.streak
        
        # Calculate points with streak bonus
        base_points = get_reward_points(current_q['difficulty'])
        streak_bonus = st.session_state.streak * 2 if st.session_state.streak >= 3 else 0
        total_points = base_points + streak_bonus
        st.session_state.score += total_points
        
        # Show motivational booster for streaks (3+)
        if st.session_state.streak >= 3:
            show_motivational_booster(st.session_state.streak)
            # Extra celebration for major milestones
            if st.session_state.streak in [3, 5, 7, 10]:
                st.balloons()
                # Special sound effects could be added here
        
        # Show success message
        streak_msg = f" + {streak_bonus} streak bonus!" if streak_bonus > 0 else ""
        success_emoji = "🔥" if st.session_state.streak >= 3 else "🎉"
        
        st.markdown(f"""
        <div class="success-box">
            <h4>{success_emoji} Correct! +{total_points} points{streak_msg}</h4>
            <p><strong>Explanation:</strong> {current_q['explanation']}</p>
        </div>
        """, unsafe_allow_html=True)
        
    else:
        # Wrong answer handling
        st.session_state.streak = 0
        st.session_state.wrong_answers += 1
        
        st.markdown(f"""
        <div class="error-box">
            <h4>❌ Incorrect</h4>
            <p><strong>The correct answer was:</strong> {correct_answer}</p>
            <p><strong>Explanation:</strong> {current_q['explanation']}</p>
            <p><strong>💡 Learning Tip:</strong> {current_q['hint']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Check for new achievements
    new_achievements = check_achievements()
    if new_achievements:
        st.balloons()
        for achievement in new_achievements:
            st.success(f"🏆 Achievement Unlocked: {achievement}!")
    
    # Move to next question
    st.session_state.questions_answered += 1
    st.session_state.current_question += 1
    st.session_state.show_hint = False
    
    # Show continue button instead of auto-advance for better UX
    if st.session_state.questions_answered < 20:
        st.markdown("---")
        if st.button("➡️ Next Question", type="primary", use_container_width=True):
            st.rerun()

def show_final_results():
    st.markdown("## 🎊 Game Complete!")
    
    # Calculate performance metrics
    accuracy = ((20 - st.session_state.wrong_answers) / 20) * 100
    performance_level = get_performance_level(accuracy, st.session_state.score)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="🎯 Final Score",
            value=f"{st.session_state.score} pts",
            delta=f"{st.session_state.score - 200} vs average"
        )
    
    with col2:
        st.metric(
            label="📊 Accuracy",
            value=f"{accuracy:.1f}%",
            delta=f"{accuracy - 70:.1f}% vs target"
        )
    
    with col3:
        st.metric(
            label="🔥 Best Streak",
            value=st.session_state.best_streak,
            delta=f"{st.session_state.best_streak - 3} vs good"
        )
    
    # Performance badge
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white; margin: 2rem 0;">
        <h2>{performance_level['emoji']} {performance_level['title']}</h2>
        <p>{performance_level['message']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Show all achievements
    if st.session_state.achievements:
        st.markdown("### 🏆 Your Achievements")
        achievement_cols = st.columns(min(len(st.session_state.achievements), 4))
        for i, achievement in enumerate(st.session_state.achievements):
            with achievement_cols[i % 4]:
                st.markdown(f"🥇 **{achievement}**")
    
    # Recommendations based on performance
    st.markdown("### 📚 Next Steps for Learning")
    
    if accuracy < 60:
        st.markdown("""
        - 📖 Review the basics of AI terminology
        - 💻 Try some beginner coding tutorials
        - 🎯 Focus on one programming language first
        """)
    elif accuracy < 80:
        st.markdown("""
        - 🚀 Great foundation! Try some hands-on coding projects
        - 🤖 Explore AI tools like GitHub Copilot
        - 📊 Practice with real workplace automation tasks
        """)
    else:
        st.markdown("""
        - 🌟 Excellent knowledge! You're ready for advanced topics
        - 🏢 Start implementing AI solutions in your workplace
        - 👥 Share your knowledge with colleagues
        - 🎓 Consider learning a specific programming language deeply
        """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔄 Play Again", type="primary", use_container_width=True):
            restart_game()
    
    with col2:
        if st.button("📊 View Detailed Stats", use_container_width=True):
            show_detailed_stats()

def get_performance_level(accuracy, score):
    if score >= 400 and accuracy >= 90:
        return {"emoji": "🏆", "title": "AI & Coding Master", "message": "Outstanding! You have exceptional understanding of AI and coding concepts."}
    elif score >= 300 and accuracy >= 80:
        return {"emoji": "🥇", "title": "Tech Savvy Professional", "message": "Excellent work! You're well-prepared to use AI and coding in your career."}
    elif score >= 200 and accuracy >= 70:
        return {"emoji": "🥈", "title": "Promising Learner", "message": "Good job! You have a solid foundation to build upon."}
    elif score >= 100 and accuracy >= 60:
        return {"emoji": "🥉", "title": "Getting Started", "message": "Nice effort! Keep learning and practicing to improve your skills."}
    else:
        return {"emoji": "📚", "title": "Eager Student", "message": "Every expert was once a beginner. Keep studying and you'll get there!"}

def show_detailed_stats():
    st.markdown("### 📈 Detailed Performance Analysis")
    
    # Create performance chart
    categories = ["🤖 AI Fundamentals", "💻 Programming Languages", "🎯 Vibe Coding Techniques", "🏢 Workplace Applications"]
    # This would need to be calculated based on actual answers per category
    # For now, showing placeholder data
    
    st.markdown(f"""
    **Game Statistics:**
    - Total Questions: 20
    - Correct Answers: {20 - st.session_state.wrong_answers}
    - Wrong Answers: {st.session_state.wrong_answers}
    - Hints Used: {st.session_state.hints_used}
    - Best Streak: {st.session_state.best_streak}
    - Total Achievements: {len(st.session_state.achievements)}
    """)

def restart_game():
    # Keep achievements and best streak for motivation
    achievements = st.session_state.achievements.copy()
    best_streak = st.session_state.best_streak
    
    # Clear session state
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    
    # Restore persistent stats
    st.session_state.achievements = achievements
    st.session_state.best_streak = best_streak
    
    st.rerun()

if __name__ == "__main__":
    main()
