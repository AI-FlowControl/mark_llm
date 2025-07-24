from ollama import Client

class OllamaApp:
    def __init__(self, model: str = 'gemma'):
        self.model = model
        self.client = Client()

    def prompt(self) -> str:
        return input("Enter your prompt: ")

    def inference(self, user_prompt: str) -> str:
        response = self.client.chat(model=self.model, messages=[
            {'role': 'user', 'content': user_prompt}
        ])
        return response['message']['content']

    def run(self):
        print("Type '/bye' to exit the chatbot.")
        while True:
            user_prompt = self.prompt()
            if user_prompt.strip() == '/bye':
                print("Goodbye!")
                break
            result = self.inference(user_prompt)
            print(result)

    @staticmethod
    def main():
        app = OllamaApp()
        app.run()

if __name__ == "__main__":
    OllamaApp.main()
