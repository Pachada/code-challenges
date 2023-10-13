"""
You are given a list of logs, where each log represents a transaction with a sender, recipient, and amount.
Return a list of user IDs sorted, that have made or received transactions that exceed a given threshold.
Transactions made by the same user count as 1 transaction
Example: 

logs = ["88 99 200", "88 99 300", "99 32 100", "12 12 15"]
threshold = 2

output = ["88", "99"]

"""

from collections import defaultdict

# O(n) time | O(n) space
def proccess_logs(logs: list[str], threshold:int):
    transactions_count = defaultdict(int)
    
    for log in logs:
        sender_id, recipient_id, _ = log.split(" ")
        transactions_count[sender_id] += 1
        if int(recipient_id) != int(sender_id):
            transactions_count[recipient_id] += 1
    
    result = [key for key, value in transactions_count.items() if value >= threshold]
    return sorted(result, key=int)


if __name__ == "__main__":
    logs = ["88 99 200", "88 99 300", "99 32 100", "12 12 15"]
    threshold = 2
    print(proccess_logs(logs, threshold))
    
    
