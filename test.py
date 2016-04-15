import tracker

id = "0xb794f5ea0ba39494ce839613fffba74279579268"
ids = ["0xb794f5ea0ba39494ce839613fffba74279579268", "0x60e16961ad6138d2fb3e556fc284d9c2fff41486"]

print(tracker.getAmountFromAccountEther(id))
print(tracker.getAmountFromMultipleAccountsEther(ids))