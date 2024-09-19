
class Notifier:
    def send(self, message):
        pass


class NotificationDecorator(Notifier):
    pass
    

class EmailNotifier(NotificationDecorator):

    def __init__(self, obj) -> None:
        self.notifier = obj

    def send(self, message):
        self.notifier.send(message)
        print("Email notification")
    

class SMSNotifier(NotificationDecorator):

    def __init__(self, obj) -> None:
        self.notifier = obj

    def send(self, message):
        self.notifier.send(message)
        print("SMS notification")



class SlackNotifier(NotificationDecorator):

    def __init__(self, obj) -> None:
        self.notifier = obj

    def send(self, message):
        self.notifier.send(message)
        print("Slack notification")


notify_email_sms = SMSNotifier(EmailNotifier((Notifier())))
notify_slack_email_sms = SMSNotifier(EmailNotifier(SlackNotifier(Notifier())))
notify_email = EmailNotifier(Notifier())

notify_email_sms.send('Hi')
print()
notify_slack_email_sms.send('Hi')
print()
notify_email.send("Hi")