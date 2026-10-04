class WeatherAgent:

    def __init__(self):
        self.weather = ''

    def perceive(self, environment):
        return environment["weather"]

    def action(self, environment):
        weather = self.perceive(environment)

        print("Agent is checking the weather ")
        print(f"Weather is {weather}")

        if weather == "Rainy":
            self.weather = "Rainy"
            print("Carry out Umbrella")

        elif weather == "Cloudy":
            self.weather = "Coudy"
            print("Carry out Umbrella for precaution")

        else:
            self.weather = "Sunny"            
            print("Do not carry umbrella. Weather is good.")

environment = {
    "weather" : "Rainy"
}

agent = WeatherAgent()

agent.action(environment)
