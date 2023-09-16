import heapq
from emulator import Emulator

class Scheduler:
    def __init__(self, max_emulators):
        self.running_emulators = []
        self.waiting_emulators = []
        self.max_emulators = max_emulators

    def add_emulator(self, priority, emulator_id):
        if len(self.running_emulators) < self.max_emulators:
            heapq.heappush(self.running_emulators, (priority, emulator_id, Emulator()))
        else:
            heapq.heappush(self.waiting_emulators, (priority, emulator_id, Emulator()))

    def start_emulator(self):
        if self.waiting_emulators and len(self.running_emulators) < self.max_emulators:
            priority, emulator_id, emulator = heapq.heappop(self.waiting_emulators)
            emulator.start()
            heapq.heappush(self.running_emulators, (priority, emulator_id, emulator))

    def stop_emulator(self):
        if self.running_emulators:
            priority, emulator_id, emulator = heapq.heappop(self.running_emulators)
            emulator.stop()
            heapq.heappush(self.waiting_emulators, (priority, emulator_id, emulator))