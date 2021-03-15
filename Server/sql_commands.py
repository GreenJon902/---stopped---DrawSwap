#  --------------- Make New --------------------------------------------------------------------------------------------

make_new_users_table = """
CREATE TABLE users (
    uuid char(16) NOT NULL PRIMARY KEY,
    nickname varchar(32) NOT NULL,
    dateJoined datetime NOT NULL,
    password char(16) NOT NULL
)
"""

make_new_games_table = """
CREATE TABLE games (
    id int
)
"""


#  --------------- New Account -----------------------------------------------------------------------------------------

check_for_uuid = """
SELECT 1 FROM users WHERE uuid={a}
"""

add_new_user = """
INSERT INTO users (uuid, nickname, dateJoined, password) VALUE ("{a}", "{b}", CURRENT_TIMESTAMP, "{c}")
"""
