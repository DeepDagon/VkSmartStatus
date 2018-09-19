import sqlite3

conn = sqlite3.connect('DB.db')
c = conn.cursor()

id = 160786540
token = '62d2ad1fa6f01a5a48a766a306338f191c7860856e5ed2371af44ea968b0a0b1690a396a81cd1651d9d6b'
status = 'status {friends_online}'

c.execute('INSERT INTO user VALUES(?, ?, ?)', (id, token, status))
