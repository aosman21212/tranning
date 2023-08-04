from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/build_spell_checker_model", methods=["POST"])
def build_spell_checker_model():
    # Replace these with the actual file paths or filenames
    model_file = "/home/bab/Desktop/mo/model_file/spell_checker.pickle"
    corpus_file = "/home/bab/Desktop/mo/corpus_files/corpus.txt"

    # Additional subprocess command
    venv_python = '//home/bab/Desktop/ali/BABNLU-Services/env/bin/python'
    script_path = '/home/bab/Desktop/ali/BABNLU-Services/scripts/build_spell_checker.py'
    args = [venv_python, script_path, '--model_file', model_file, '--corpus_file', corpus_file]

    try:
        # Execute the command using subprocess
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        result_message = result.stdout  # Get the standard output
    except subprocess.CalledProcessError as e:
        result_message = f"Error while building the spell checker model: {e.stderr}"

    return jsonify(result_message)

if __name__ == "__main__":
    app.run(debug=True)
