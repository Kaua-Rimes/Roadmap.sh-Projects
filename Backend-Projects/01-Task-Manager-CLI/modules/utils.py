class ErrorChecks:
    def __init__(self):
        pass
    
    def empty_folder (text):
        if text.strip() == "":
            print("This folder cannot be empty.")
            return False
        else:
            return True 
        
class Colors:
    @staticmethod
    def red(text):
        return f"\033[91m{text}\033[0m"

    @staticmethod
    def green(text):
        return f"\033[92m{text}\033[0m"

    @staticmethod
    def yellow(text):
        return f"\033[93m{text}\033[0m"

    @staticmethod
    def blue(text):
        return f"\033[94m{text}\033[0m"

    @staticmethod
    def cyan(text):
        return f"\033[96m{text}\033[0m"
    
    @staticmethod
    def reset(text):
        return f"{text}\033[0m"
        
        
