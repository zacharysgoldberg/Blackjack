import sqlite3
import os.path


conn = sqlite3.connect('users.db')

cur = conn.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    salt TEXT NOT NULL
);
""")

# cur.execute("CREATE INDEX index_username ON users(username);")

# cur.execute("""
#     INSERT INTO users VALUES ('admin', 'admin@', '');
# """)

# confirm = input('Enter username:')

# cur.execute("""
#     SELECT EXISTS(SELECT 1 FROM users WHERE username = ?);
# """, (confirm,))

# boolean = cur.fetchall()[0]

# print(boolean[0])

# username_validate = input('Enter username: ')

# cur.execute("""
#             SELECT username, password
#             FROM users
#             WHERE username = ?;
#             """, (username_validate,))

# user = cur.fetchall()[0]

# print(user[0])
# print(user[1])

conn.commit()
conn.close()
