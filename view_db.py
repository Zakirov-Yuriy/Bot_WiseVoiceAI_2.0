import sqlite3
import time

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Get all users
cursor.execute('SELECT user_id, trials_used, is_paid, subscription_expiry FROM users')
rows = cursor.fetchall()

print("📊 Содержимое базы данных users.db")
print("=" * 80)
print(f"{'User ID':<12} | {'Trials':<8} | {'Paid':<6} | {'Expiry Timestamp':<18} | {'Expiry Date'}")
print("-" * 80)

for row in rows:
    user_id, trials_used, is_paid, subscription_expiry = row
    expiry_date = "Не активна"
    if subscription_expiry and subscription_expiry > 0:
        expiry_date = time.strftime("%d.%m.%Y %H:%M", time.localtime(subscription_expiry))

    paid_status = "✅" if is_paid else "❌"
    print(f"{user_id:<12} | {trials_used:<8} | {paid_status:<6} | {subscription_expiry or 0:<18} | {expiry_date}")

conn.close()
print("\n" + "=" * 80)
