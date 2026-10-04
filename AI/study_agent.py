class StudyAgent:
    def __init__(self):
        self.study_hours = 0

    def perceive(self, environment):
        return environment["study_hours"]

    def act(self, environment):
        hours = self.perceive(environment)

        print("Agent is checking the student's study hours.")
        print(f"Study hours: {hours}")

        if hours < 4:
            print("Action: Student should continue studying.")
        elif hours >= 4 and hours < 6:
            print("Action: Student can take a short break.")
        else:
            print("Action: Student should take a long break.")

# Environment
environment = {
    "study_hours": 5
}

# Create agent
agent = StudyAgent()

# Run the intelligent agent
agent.act(environment)