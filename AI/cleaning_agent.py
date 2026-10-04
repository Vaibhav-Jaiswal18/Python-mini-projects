class CleaningAgent:
    def __init__(self):
        self.room = input("Enter the Room(Room A/ Room B): ")

    def perceive(self, environment):
        return environment[self.room]

    def act(self, environment):
        clean = self.perceive(environment)

        print(f"Agent is checking {self.room}")
        print(f"Cleanliness level: {clean}")

        if clean == "Dirty":
            print("Action: Room is dirty. Cleaning the room...")
            environment[self.room] = "Clean"
        else:
            print("Action: Room is clean. Moving to another Room.")
            self.move()

    def move(self):
        if self.room == "Room A":
            self.room = 'Room B'
        else:
            self.room = "Room A"

# Environment
environment = {
    "Room A": "Dirty",
    "Room B": "Clean"
}

# Create agent
agent = CleaningAgent()

# Run the intelligent agent
for i in range(5):
    print("\n----Step",i+1,"----")
    agent.act(environment)