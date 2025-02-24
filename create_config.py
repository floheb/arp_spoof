import json

required_keys = ["ip_target", "mac_target", "ip_gateway", "mac_gateway", "interface"]

class Config:
    def __init__(self, file_path="config.json"):
        self.config_file = file_path
        self.config = self.load_config()
    
    def load_config(self):
        try:
            with open(self.config_file) as f:
                config = json.load(f)
                return config if self.validate(config) else None
        except (FileNotFoundError, json.JSONDecodeError):
            return None
    
    def validate(self, config):
        return all(key in config for key in required_keys)
    
    def display(self):
        if not self.config:
            print("Invalid or missing config.")
        else:
            print("Current Config:")
            for key, value in self.config.items():
                print(f"{key}: {value}")
    
    def update_config(self, config):
        with open(self.config_file, "w") as f:
            json.dump(config, f, indent=4)
        print("Config updated!")
    
    def update(self):
        if not self.config:
            self.config = {}
        
        print("Update Config:")
        for key in required_keys:
            self.config[key] = self.prefilled_input(f"Enter {key}", self.config.get(key, ""))
        
        self.update_config(self.config)
    
    @staticmethod
    def prefilled_input(prompt, default=""):
        user_input = input(f"{prompt} [{default}]: ").strip()
        return user_input or default

if __name__ == "__main__":
    manager = Config()
    manager.display()
    if input("Do you want to change the config? (Y/N): ").strip().lower() == "y":
        manager.update()
