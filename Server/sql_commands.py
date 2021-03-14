#  --------------- Make New --------------------------------------------------------------------------------------------

create_database = """
CREATE DATABASE DrawSwap;
"""

drop_database = """
DROP DATABASE DrawSwap;
"""


make_new_users_table = """
CREATE TABLE Users (
    uuid binary(16),
    nickname varchar(32),
    dateJoined datetime,
    password binary(16)
)
"""

make_new_games_table = """
CREATE TABLE Games (
    id int
)
"""

