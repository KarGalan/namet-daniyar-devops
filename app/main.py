import os
from html import escape
from http.server import BaseHTTPRequestHandler, HTTPServer


def get_student_info():
    return {
        "name": os.getenv("STUDENT_NAME", "Daniyar"),
        "surname": os.getenv("STUDENT_SURNAME", "Namet"),
        "group": os.getenv("STUDENT_GROUP", "IT2-2312 SE"),
        "id": os.getenv("STUDENT_ID", "37056")
    }


def render_page():
    student = get_student_info()

    name = escape(student["name"])
    surname = escape(student["surname"])
    group = escape(student["group"])
    student_id = escape(student["id"])

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>DevOps Student Application</title>
    </head>
    <body>
        <h1>DevOps Student Application</h1>
        <h2>Student Information</h2>

        <p>Name: {name}</p>
        <p>Surname: {surname}</p>
        <p>Group: {group}</p>
        <p>Student ID: {student_id}</p>

        <h3>Application is running successfully!</h3>
    </body>
    </html>
    """


class StudentHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/health":
            content = b'{"status": "ok"}'
            content_type = "application/json"

        elif self.path == "/":
            content = render_page().encode("utf-8")
            content_type = "text/html; charset=utf-8"

        else:
            self.send_error(404, "Not Found")
            return

        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)


if __name__ == "__main__":
    student = get_student_info()

    print("================================")
    print("DevOps Student Application")
    print("================================")
    print(f"Name: {student['name']}")
    print(f"Surname: {student['surname']}")
    print(f"Group: {student['group']}")
    print(f"Student ID: {student['id']}")
    print("Application is running successfully!")

    port = int(os.getenv("PORT", "8080"))

    server = HTTPServer(("0.0.0.0", port), StudentHandler)

    print(f"Server running on port {port}", flush=True)
    server.serve_forever()
