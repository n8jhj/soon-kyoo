"""Script for running development code.
"""

def init_db():
    import sqlite3
    from soon_kyoo.config import db_path, schema
    from soon_kyoo.utils import echo

    db_path.parent.mkdir(exist_ok=True)
    con = sqlite3.connect(str(db_path))
    # Create tables.
    for table_name, table_info in schema.items():
        sql_str = f"CREATE TABLE {table_name} (" \
            + ', '.join([f"{col_name} {col_descr}"
                for col_name, col_descr in table_info.items()]) \
            + ')'
        try:
            with con:
                con.execute(sql_str)
            echo(f'Table {table_name!r} created')
        except sqlite3.OperationalError:
            echo(f'Table {table_name!r} already exists')
    # Close database connection.
    con.close()
    echo('Database initialized')


if __name__ == '__main__':
    init_db()
