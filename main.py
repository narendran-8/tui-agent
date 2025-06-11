import os
import re
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

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

    # Initialize Ollama model (using gemma3:1b as installed)
    try:
        llm = OllamaLLM(model="gemma3:1b")
    except Exception as e:
        print("❌ Error connecting to Ollama. Make sure Ollama is running and the model is available.")
        return

    # Prompt template to convert instructions to system commands
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

    # Modern LangChain chaining
    chain = prompt | llm

    while True:
        instruction = input("\n📝 Enter instruction (or 'exit' to quit): ").strip()
        if instruction.lower() in ["exit", "quit"]:
            break

        try:
            result = chain.invoke({"os_type": os_type, "instruction": instruction})
            # Clean command (remove any accidental wrapping)
            command = re.sub(r"[`\"']", "", result.strip())
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
