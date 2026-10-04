class TemperatureAgent:
    def __init__(self):
        self.temperature = 0

    def perceive(self, environment):
        return environment["temperature"]

    def act(self, environment):
        temperature = self.perceive(environment)

        print("Agent is checking the temperature.")
        print(f"Temperature: {temperature}°C")

        if temperature > 30:
            print("Recommendation: Hot")
        elif temperature < 20:
            print("Recommendation: Cold")
        else:
            print("Recommendation: Normal")

# Take input from user
temperature = float(input("Enter temperature in Celsius: "))

# Environment
environment = {
    "temperature": temperature
}

# Create agent
agent = TemperatureAgent()

# Run the intelligent agent
agent.act(environment)