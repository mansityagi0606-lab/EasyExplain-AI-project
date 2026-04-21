# EasyExplain AI

EasyExplain AI is a simple AI-powered tool that explains any topic in a clear, beginner-friendly way.
It generates structured output with a title, easy explanation, and a real-world example.

---


## Tech Stack

* Python
* Groq API (LLM)
* Streamlit
* argparse
* python-dotenv

---

## 📁 Project Structure

```
EasyExplain-AI-project/
│
├── main.py              # CLI script
├── app.py               # Streamlit web app
├── config.py            # API configuration
├── prompt_template.py   # Prompt builder
├── requirements.txt     # Dependencies
└── .gitignore
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/mansityagi0606-lab/EasyExplain-AI-project.git
cd EasyExplain-AI-project
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Add API Key

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_api_key_here
```

---

## Usage

### Run CLI version

```
python main.py --topic "Machine Learning"
```

---

### Run Streamlit Web App

```
streamlit run app.py
```

---

## Example Output

**Title:** What is Machine Learning?

**Explanation:**
Machine learning is a way for computers to learn from data without being explicitly programmed.

**Example:**
Netflix recommending movies based on your watch history.

---

