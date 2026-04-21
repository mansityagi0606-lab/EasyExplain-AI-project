import argparse
from config import get_client
from prompt_template import build_prompt


def generate_explanation(topic):
    client = get_client()
    prompt = build_prompt(topic)

    response = client.chat.completions.create(
        model="groq/compound-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=str, required=True)

    args = parser.parse_args()

    result = generate_explanation(args.topic)

    print("\n--- Generated Explanation ---\n")
    print(result)