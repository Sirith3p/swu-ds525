import psycopg2

#drop previous created table in database
drop_table_queries = [
    "DROP TABLE IF EXISTS staging_events",
    "DROP TABLE IF EXISTS events",
    "DROP TABLE IF EXISTS actors",
    "DROP TABLE IF EXISTS repo"
]
#create the actors table that consists of 6 columns and assign id as the primary key
create_table_queries = [
    """
    CREATE TABLE IF NOT EXISTS staging_events (
        id bigint,
        type text,
        actor_id bigint,
        actor_login text,
        actor_display_login text,
        actor_gravatar_id text,
        actor_url text,
        actor_avatar_url text,
        repo_id bigint,
        repo_name text,
        repo_url text,
        public text,
        created_at text
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS events (
        id bigint,
        type text,
        actor_id bigint,
        repo_id bigint,
        public text,
        created_at text
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS actors (
        id bigint NOT NULL,
        login text,
        display_login text,
        gravatar_id text,
        url text,
        avatar_url text
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS repo(
        id bigint NOT NULL,
        name text,
        url text
    )
    """,
]

copy_table_queries = [
    """
    COPY staging_events FROM 's3://zkan-swu-labs/github_events_01.json'
    CREDENTIALS 'aws_iam_role=arn:aws:iam::377290081649:role/LabRole'
    JSON 's3://zkan-swu-labs/events_json_path.json'
    REGION 'us-east-1'
    """,
]
insert_table_queries = [
    """
    INSERT INTO
      events (
        id, type, actor_id, repo_id, public, created_at
      )
    SELECT
      DISTINCT id, type, actor_id, repo_id, public, created_at
    FROM
      staging_events
    WHERE
      id NOT IN (SELECT DISTINCT id FROM events)
    """,
    """
    INSERT INTO
      actors (
        id, name, url
      )
    SELECT
      DISTINCT actor_id, actor_login, actor_display_login, 
      actor_gravatar_id, actor_url, actor_avatar_url
    FROM
      staging_events
    WHERE
      id NOT IN (SELECT DISTINCT id FROM actors)
    """,
    """
    INSERT INTO
      repo (
        id, login, display_login, gravatar_id, url, avatar_url
      )
    SELECT
      DISTINCT repo_id, repo_name, repo_url 
    FROM
      staging_events
    WHERE
      id NOT IN (SELECT DISTINCT id FROM repo)
    """
]


def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def load_staging_tables(cur, conn):
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    host = "redshift-cluster-1.cfzeqwb4b9xc.us-east-1.redshift.amazonaws.com"
    dbname = "dev"
    user = "awsuser"
    password = "Ds525lab"
    port = "5439"
    conn_str = f"host={host} dbname={dbname} user={user} password={password} port={port}"
    conn = psycopg2.connect(conn_str)
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)
    load_tables(cur, conn)
    insert_tables(cur, conn)

    postgreSQL_select_Query = "select * from events"

    cur.execute(postgreSQL_select_Query)
    print("Selecting rows from events table using cursor.fetchall")
    records = cur.fetchall()
    for row in records:
        print(row)

    conn.close()


if __name__ == "__main__":
    main()