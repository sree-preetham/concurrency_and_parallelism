from db import get_connection
import threading

def get_balance(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT balance from accounts where username = %s", (username,)
    )
    result = cur.fetchone()
    balance = result[0]
    cur.close()
    conn.close()
    return balance


def deposit(username, amount):
    conn = get_connection()
    cur = conn.cursor()

    # reading same data/state
    currentBalance = get_balance(username)

    newBalance = currentBalance + amount

    cur.execute(
        "UPDATE accounts SET balance = %s where username = %s", (newBalance,username)
    )
    conn.commit()

    cur.close()
    conn.close()

username = "luffy"

print(f"original balance is {get_balance(username)}")

t1 = threading.Thread(target=deposit, args=(username, 200))
t2 = threading.Thread(target=deposit, args=(username, 100))
t3 = threading.Thread(target=deposit, args=(username, 300))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print(f"final balance after the deposits is {get_balance(username)}")