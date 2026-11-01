from database.connection import conn_db

def get_buses_by_stop(bus_stop_id):
    conn = conn_db()
    cursor = conn.cursor()

    try:
        query = """
            SELECT DISTINCT service_no
            FROM bus_routes
            WHERE bus_stop_code = %s
            ORDER BY service_no
        """

        cursor.execute(query,(bus_stop_id, ))
        results = cursor.fetchall()

        return [row[0] for row in results]
    
    finally:
        cursor.close()
        conn.close()

