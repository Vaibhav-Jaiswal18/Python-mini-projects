class FanAgent:
    def __init__(self):
        self.fan_status = "OFF"

    def perceive(self, environment):
        return environment["temperature"]

    def act(self, environment):
        temperature = self.perceive(environment)

        print("Agent is checking room temperature.")
        print(f"Room temperature: {temperature}°C")

        if temperature > 30:
            self.fan_status = "ON"
            print("Action: Temperature is high.")
            print("Fan is turned ON.")
        else:
            self.fan_status = "OFF"
            print("Action: Temperature is normal.")
            print("Fan is turned OFF.")

# Environment
environment = {
    "temperature": 35
}

# Create agent
agent = FanAgent()

# Run the intelligent agent
agent.act(environment)