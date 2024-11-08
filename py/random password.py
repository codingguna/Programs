import random
print("".join(random.sample("qwertyuioplkjhgfdsazxcvbnmAQSWEDZXCVBGRTYUHJNMKLIOP1234567890", 5)))
import secrets
print("".join(secrets.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890")for _ in range(10)))