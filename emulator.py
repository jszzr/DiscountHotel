
class Emulator:
    def __init__(self):
        self.temperature = 0
        self.target_temperature = 0
        self.running_time = 0
        self.total_fees = 0
        self.schedule = None

    def set_schedule(self, schedule):
        self.schedule = schedule

    def start(self):
        # Increase temperature until it reaches the target
        while self.temperature < self.target_temperature:
            self.temperature += 1
            self.running_time += 1
            self.total_fees += self.compute_fee()

        # Decrease temperature
        while self.temperature > 0:
            self.temperature -= 1
            self.running_time += 1
            self.total_fees += self.compute_fee()
    
    #Todo def stop(self)

    def compute_fee(self):
        # Compute fees based on schedule and running time
        # This is a placeholder, replace with your actual computation
        return 1

    def get_total_fees(self):
        return self.total_fees

    def get_running_time(self):
        return self.running_time