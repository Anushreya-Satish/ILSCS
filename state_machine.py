from db_logger import log_event

class ElevatorStateMachine:
    def __init__(self):
        self.current_floor = 1
        self.queue = []
        self.state = "IDLE"

    def process_call(self, floor, is_verified, crowd_count=1, latency=1200.0):
        print(f"\n[CALL REGISTERED] Floor {floor} | Running Verification Window...")
        
        if is_verified:
            action = "DISPATCHED"
            if floor not in self.queue:
                self.queue.append(floor)
            self.state = "MOVING"
            print(f" -> Decision: VERIFIED ({crowd_count} passenger(s)). Added Floor {floor} to queue.")
        else:
            action = "SKIPPED"
            print(f" -> Decision: NOT VERIFIED. Skipped empty call on Floor {floor}.")
            
        log_event(floor, is_verified, crowd_count, latency, action)
        return action

if __name__ == "__main__":
    fsm = ElevatorStateMachine()
    # Test Case 1: Verified call on Floor 2
    fsm.process_call(floor=2, is_verified=True, crowd_count=1, latency=1150.0)
    # Test Case 2: Empty/False call on Floor 3
    fsm.process_call(floor=3, is_verified=False, crowd_count=0, latency=850.0)