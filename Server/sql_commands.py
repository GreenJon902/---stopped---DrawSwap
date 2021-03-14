#  --------------- Make New --------------------------------------------------------------------------------------------

make_new_users_table = """
CREATE TABLE Users (
    uuid uniqueidentifier,
    nickname varchar(32),
    dateJoined datetime,
    password binary(16)
)
"""

