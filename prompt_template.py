def build_prompt(topic):
    return f"""
Explain the topic: {topic}

Return output in this format:

Title: <short title>

Explanation:
<simple beginner-friendly explanation>

Example:
<small real-world example>
"""