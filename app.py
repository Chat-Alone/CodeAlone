import os
from flask import Flask, jsonify, send_from_directory, render_template
from waitress import serve

app = Flask(__name__, template_folder='templates')
app.config['JSON_AS_ASCII'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CLASSES_DIR = os.path.join(BASE_DIR, 'classes')
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')


COURSES_LIST = [
    {
        "name": "C++基础课改进版",
        "description": "比C++基础课更好，还在编写中",
        "author": "浮玉人",
        "completion_time": "2077-12-31",
        "api_name": "C++基础课改进版.md",
        "status": "未完成"
    },
    {
        "name": "C++基础课",
        "description": "C++从入门到弃坑",
        "author": "浮玉人",
        "completion_time": "2024-10-25",
        "api_name": "C++基础课.md",
        "status": "已完成"
    },
    {
        "name": "Python基础课",
        "description": "Python好啊，得学啊",
        "author": "浮玉人",
        "completion_time": "2024-06-25",
        "api_name": "python基础课.md",
        "status": "已完成"
    },
]
COURSES_MAP = {course["name"]: course for course in COURSES_LIST}
ALLOWED_FILES = {course["api_name"] for course in COURSES_LIST}

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/course/<string:course_name>")
def course_page(course_name):
    if course_name in COURSES_MAP:
        return render_template('class.html')
    return jsonify({"error": "Not Found", "message": "The requested course does not exist."}), 404

@app.route("/api/courses")
def get_courses():
    return jsonify(COURSES_LIST)

@app.route("/class/<path:filename>")
def get_class_file(filename):
    if filename in ALLOWED_FILES and os.path.exists(os.path.join(CLASSES_DIR, filename)):
        return send_from_directory(
            CLASSES_DIR,
            filename,
            mimetype='text/markdown; charset=utf-8'
        )
    return jsonify({"error": "Not Found", "message": "The requested course file does not exist."}), 404

@app.route("/font")
def get_font():
    """提供字体文件"""
    font_filename = "MapleMono-NF-CN-Regular.ttf"
    try:
        return send_from_directory(
            ASSETS_DIR,
            font_filename,
            mimetype='font/ttf'
        )
    except FileNotFoundError:
        return jsonify({"error": "Not Found", "message": "The font file does not exist on the server."}), 404


if __name__ == "__main__":
    host = '0.0.0.0'
    port = 16666
    print(f"Production server starting on http://{host}:{port}")
    serve(app, host=host, port=port)
