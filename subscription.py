class SubscriptionManager:
    def __init__(self):
        self.subscriptions = {}

    def add_subscription(self, user_id, subscription_details):
        self.subscriptions[user_id] = subscription_details
        print(f"Subscription added for user {user_id}.")

    def remove_subscription(self, user_id):
        if user_id in self.subscriptions:
            del self.subscriptions[user_id]
            print(f"Subscription removed for user {user_id}.)
        else:
            print(f"No subscription found for user {user_id}.")

    def get_subscription(self, user_id):
        return self.subscriptions.get(user_id, "No subscription found.")

    def list_subscriptions(self):
        return self.subscriptions
