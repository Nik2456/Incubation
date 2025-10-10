import pytest
import sqlite3
import os

@pytest.fixture
def db_resource(request):

    print("\n[Setup] Creating in-memory database and log file...")
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    conn.commit()

    log_file = "test_run.log"
    with open(log_file, "w") as f:
        f.write("Test started\n")

    def cleanup():
        print("\n[Teardown] Cleaning up resources...")

        try:
            conn.close()
            print("[Teardown] Database connection closed.")
        except Exception as e:
            print(f"[Error] Could not close DB: {e}")

        if os.path.exists(log_file):
            os.remove(log_file)
            print("[Teardown] Log file deleted.")

    request.addfinalizer(cleanup)

    return conn

def test_insert_user(db_resource):
    cursor = db_resource.cursor()
    cursor.execute("INSERT INTO users (name) VALUES ('Nikhil')")
    db_resource.commit()

    cursor.execute("SELECT name FROM users WHERE id=1")
    result = cursor.fetchone()
    assert result[0] == "Nikhil"
    print("[Test] User inserted and verified.")

