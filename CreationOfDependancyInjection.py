# Creation of Dependency Injection in Python
class Database:
    def connect(self):
        return "Database connected"

class UserService:
    def __init__(self, database: Database):
        self.database = database

    def get_user(self, user_id):
        connection_status = self.database.connect()
        return f"{connection_status}. Fetching user with ID: {user_id}"

# Example usage
database = Database()
user_service = UserService(database)
print(user_service.get_user(1))  # Output: Database connected. Fetching user with ID: 1

# Type of Dependency Injection: Constructor Injection

class EmailService:
    def send_email(self, recipient, subject, body):
        return f"Email sent to {recipient} with subject '{subject}'"
    
class NotificationService:
    def __init__(self, email_service: EmailService):
        self.email_service = email_service

    def notify_user(self, user_email, subject, message):
        email_status = self.email_service.send_email(user_email, subject, message)
        return f"{email_status}. Notification sent to user."

# Example usage
email_service = EmailService()
notification_service = NotificationService(email_service)
print(notification_service.notify_user("user@example.com", "Welcome!", "Thank you for joining us."))    

# Type of Dependency Injection: Setter Injection new example

class Logger:
    def log(self, message):
        return f"Log: {message}"

class NotificationService:
    def __init__(self):
        self.email_service = None
        self.logger = None

    def set_email_service(self, email_service: EmailService):
        self.email_service = email_service

    def set_logger(self, logger: Logger):
        self.logger = logger

    def notify_user(self, user_email, subject, message):
        if self.email_service is None:
            return "Email service not set."
        email_status = self.email_service.send_email(user_email, subject, message)
        if self.logger:
            self.logger.log(f"Notification sent to {user_email}")
        return f"{email_status}. Notification sent to user."

# Example usage
email_service = EmailService()
logger = Logger()
notification_service = NotificationService()
notification_service.set_email_service(email_service)   
notification_service.set_logger(logger)
print(notification_service.notify_user("user@example.com", "Welcome!", "Thank you for joining us."))        
