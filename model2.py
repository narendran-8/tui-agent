import os
import re
import dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# Load API key from .env
dotenv.load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    print("❌ API key not found in .env file. Please set OPENROUTER_API_KEY.")
    exit()

def get_os_choice():
    print("Choose your Operating System:")
    print("1. Windows")
    print("2. Linux")
    print("3. macOS")
    choice = input("Enter option number: ").strip()
    os_map = {"1": "Windows", "2": "Linux", "3": "macOS"}
    return os_map.get(choice, "Linux")

def main():
    os_type = get_os_choice()

    # Use smaller, free OpenRouter model with limited tokens
    try:
        llm = ChatOpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
            model="mistralai/mistral-small-3.2-24b-instruct:free",  # Free model
            max_tokens=512,
            temperature=0.2,
        )
    except Exception as e:
        print("❌ Error initializing OpenRouter LLM:", e)
        return

    # Prompt template
    prompt = PromptTemplate(
        input_variables=["os_type", "instruction"],
        template="""
You are an expert system assistant.

Convert the user's instruction into a SINGLE system command for the specified OS.

OS: {os_type}
Instruction: {instruction}

Respond with only the command — no explanation, no backticks, no quotes.
"""
    )

    chain = prompt | llm

    while True:
        instruction = input("\n📝 Enter instruction (or 'exit' to quit): ").strip()
        if instruction.lower() in ["exit", "quit"]:
            break

        try:
            result = chain.invoke({"os_type": os_type, "instruction": instruction})
            command = re.sub(r"[`\"']", "", result.content.strip())
            print(f"\n💡 Suggested Command:\n{command}")
        except Exception as e:
            print("❌ Failed to generate command:", e)
            continue

        confirm = input("\n⚠️ Execute this command? (y/n): ").strip().lower()
        if confirm == "y":
            print("⏳ Running...\n")
            os.system(command)
        else:
            print("❌ Skipped execution.")

if __name__ == "__main__":
    main()
