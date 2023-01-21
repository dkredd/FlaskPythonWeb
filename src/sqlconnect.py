import sqlite3
from sqlite3 import Error

#Create a connection
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to DB was successful")
    except Error as e:
        print(f"The error {e} occured")

    return connection

connection = create_connection("sm_app.sqlite")


#Create the tables (users, posts, comments ,likes)

#Execute an update
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error {e} occured")

#Execute a query and get its results
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  age INTEGER,
  gender TEXT,
  nationality TEXT
);
"""

create_posts_table = """
CREATE TABLE IF NOT EXISTS posts(
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  title TEXT NOT NULL, 
  description TEXT NOT NULL, 
  user_id INTEGER NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id)
);
"""

create_comments_table = """
CREATE TABLE IF NOT EXISTS comments (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  text TEXT NOT NULL, 
  user_id INTEGER NOT NULL, 
  post_id INTEGER NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""
create_likes_table = """
CREATE TABLE IF NOT EXISTS likes (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  user_id INTEGER NOT NULL, 
  post_id integer NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""

execute_query(connection, create_users_table)
execute_query(connection, create_posts_table)
execute_query(connection, create_comments_table)
execute_query(connection, create_likes_table)


create_users = """
INSERT INTO
  users (name, age, gender, nationality)
VALUES
  ('James', 25, 'male', 'USA'),
  ('Leila', 32, 'female', 'France'),
  ('Brigitte', 35, 'female', 'England'),
  ('Mike', 40, 'male', 'Denmark'),
  ('Elizabeth', 21, 'female', 'Canada');
"""

create_posts = """
INSERT INTO
  posts (title, description, user_id)
VALUES
  ("Happy", "I am feeling very happy today", 1),
  ("Hot Weather", "The weather is very hot today", 2),
  ("Help", "I need some help with my work", 2),
  ("Great News", "I am getting married", 1),
  ("Interesting Game", "It was a fantastic game of tennis", 5),
  ("Party", "Anyone up for a late-night party today?", 3);
"""

create_comments = """
INSERT INTO
  comments (text, user_id, post_id)
VALUES
  ('Count me in', 1, 6),
  ('What sort of help?', 5, 3),
  ('Congrats buddy', 2, 4),
  ('I was rooting for Nadal though', 4, 5),
  ('Help with your thesis?', 2, 3),
  ('Many congratulations', 5, 4);
"""

create_likes = """
INSERT INTO
  likes (user_id, post_id)
VALUES
  (1, 6),
  (2, 3),
  (1, 5),
  (5, 4),
  (2, 4),
  (4, 2),
  (3, 6);
"""
execute_query(connection, create_users)
execute_query(connection, create_posts)
execute_query(connection, create_comments)
execute_query(connection, create_likes)



#Select values from each table
select_users = "SELECT * from users"
users = execute_read_query(connection, select_users)
for user in users:
    print(user)

select_posts = "SELECT * FROM posts"
posts = execute_read_query(connection, select_posts)
for post in posts:
    print(post)

select_comments = "SELECT * FROM comments LIMIT 2"
comments = execute_read_query(connection, select_comments)
for comment in comments:
    print(comment)

select_likes = "SELECT * FROM likes LIMIT 2"
likes = execute_read_query(connection, select_likes)
for like in likes:
    print(like)

#Join two tables and query
print("\n\n select user and their posts")
select_users_posts = """
SELECT
  users.id,
  users.name,
  posts.description
FROM
  posts
  INNER JOIN users ON users.id = posts.user_id
ORDER BY users.id
"""


print("\n\n select posts and their comments and associated users")
user_posts = execute_read_query(connection,select_users_posts)
for user_post in user_posts:
    print(user_post)

select_posts_comments_users = """
SELECT
  posts.description as post,
  text as comment,
  name
FROM
  posts
  INNER JOIN comments ON posts.id = comments.post_id
  INNER JOIN users ON users.id = comments.user_id
"""

posts_comments_users = execute_read_query(
    connection, select_posts_comments_users
)

for posts_comments_user in posts_comments_users:
    print(posts_comments_user)


print("\n\n select posts and their number of likes")
select_post_likes = """
SELECT
  description as Post,
  COUNT(likes.id) as Likes
FROM
  likes,
  posts
WHERE
  posts.id = likes.post_id
GROUP BY
  likes.post_id
"""

post_likes = execute_read_query(connection, select_post_likes)

for post_like in post_likes:
    print(post_like)


#Update Table records
print("\n\n\n select description from post id 2")
select_post_description = "SELECT description FROM posts WHERE id = 2"

post_description = execute_read_query(connection, select_post_description)

for description in post_description:
    print(description)
update_post_description = """
UPDATE
  posts
SET
  description = "The weather has become pleasant now"
WHERE
  id = 2
"""

execute_query(connection, update_post_description)
post_description = execute_read_query(connection, select_post_description)
for description in post_description:
    print(description)



print("\n\n\n select comment id 1")
select_comment_description = "SELECT text FROM comments WHERE id = 1"
comment_description = execute_read_query(connection, select_comment_description)
for description in comment_description:
    print(description)

delete_comment = "DELETE FROM comments WHERE id = 1"
execute_query(connection, delete_comment)

select_comment_description = "SELECT  text FROM comments WHERE id = 1"
comment_description = execute_read_query(connection, select_comment_description)
for description in comment_description:
    print(description)