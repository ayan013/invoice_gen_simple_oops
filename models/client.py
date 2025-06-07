class Client:
    def __init__(self, name: str, mobile: int, email: str):
        self.name = name
        self.mobile = mobile
        self.email = email

    def __str__(self):
        return f"To \n{self.name} \nemail:{self.email}\nContact:{self.mobile}"
