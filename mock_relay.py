class RelayController:
    def __init__(self):
        print("[RELAY] Mock relay controller initialized.")

    def activate_item(self, row, col):
        print(f"[RELAY] Simulated relay activated for item af ({row}, {col})...")
        return True
    
    def cleanup(self):
        print("[RELAY] Cleaning up (mock).")