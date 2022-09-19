from app.database import get_db


def output_formatter(results):
    out = []
    for result in results:
        entry = {
            "id": result[0],
            "title": result[1],
            "subtitle": result[2],
            "body": result[3],
            "created_on": result[4]
        }
        out.append(entry)
    return out

def scan():
    statement = "SELECT id, title, subtitle, body, DATETIME(created_on, 'localtime') FROM notes"
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(statement, ())
    out = cursor.fetchall()
    cursor.close
    return output_formatter(out)

def select_by_id(pk):
    statement = "SELECT * FROM notes WHERE id=?"
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(statement, (pk, ))
    out = cursor.fetchall()
    cursor.close()
    return output_formatter(out)


def create(raw_json):
    statement = """
    INSERT INTO notes (
        title,
        subtitle,
        body,
        created_on
    ) VALUES (?, ?, ?, DATETIME('now'))
    """
    conn = get_db()
    conn.execute(statement, (raw_json["title"], raw_json["subtitle"], raw_json["body"]))
    conn.commit()
    conn.close()


def update(raw_json, pk):
    statement = """
    UPDATE notes
    SET title=?,
    subtitle=?,
    body=?
    WHERE id=?
    """
    conn = get_db()
    conn.execute(statement, (raw_json["title"], raw_json["subtitle"], raw_json["body"], pk))
    conn.commit()
    conn.close()


def delete(pk):
    statement = """
    DELETE FROM notes
    WHERE id=?
    """
    conn = get_db()
    conn.execute(statement, (pk, ))
    conn.commit()
    conn.close()