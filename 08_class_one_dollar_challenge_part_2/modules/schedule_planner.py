class StudyScheduleGenerator:
    def __init__(self, subjects, total_hours):
        self.subjects = subjects  # List of subjects like ['Math', 'Physics', 'History']
        self.total_hours = total_hours  # Total study hours available in a day

    def generate_equal_schedule(self):
        if not self.subjects or self.total_hours <= 0:
            return []

        hours_per_subject = round(self.total_hours / len(self.subjects), 2)
        schedule = []

        for subject in self.subjects:
            schedule.append({"subject": subject, "hours": hours_per_subject})

        return schedule

    def generate_custom_schedule(self, priority_weights):
        """
        priority_weights: Dictionary mapping subject to priority score (e.g. {"Math": 3, "English": 1})
        """
        total_priority = sum(priority_weights.values())
        schedule = []

        for subject, weight in priority_weights.items():
            allocated_time = round((weight / total_priority) * self.total_hours, 2)
            schedule.append({"subject": subject, "hours": allocated_time})

        return schedule

