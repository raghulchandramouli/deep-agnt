class Chat:
    """A conversation with a model."""

    def __init__(self, llm, system):
        self.llm = llm
        self.system = system
        self.messages = []

    def send(self, text):
        """Send the user's message. Return the model's reply."""

        # Step 1: Construct the user message
        user_message = {"role": "user", "content": text}

        # Step 2: Create temporary conversation history
        pending_messages = self.messages + [user_message]

        # Step 3: Make the model API call
        response = self.llm.messages.create(
            system=self.system,
            messages=pending_messages,
            max_tokens=300,
        )

        # Step 4: Construct the assistant message
        assistant_message = {
            "role": "assistant",
            "content": response.text
        }

        # Step 5: Update permanent conversation history
        self.messages = pending_messages + [assistant_message]

        # Step 6: Return the reply
        return response.text
