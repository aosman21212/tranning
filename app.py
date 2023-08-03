# app.py
import subprocess
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

venv_python = '/home/bab/Desktop/ali/BABNLU-Services/venv/bin/python'
args = [venv_python, 'my_script.py', 'arg1', 'arg2', 'arg3']
subprocess.run(args)
def execute_command(command):
    try:
        process = subprocess.run(command, shell=True, capture_output=True, text=True)
        if process.returncode == 0:
            output = process.stdout
        else:
            output = f"Error: {process.stderr}"
    except Exception as e:
        output = f"Error: {e}"
    return output

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute_command')
def execute_command_route():
    model_file = '/home/bab/Desktop/ali/BABNLU-Services/data/bins/spell_checker.pickle'
    corpus_file = '/home/bab/Desktop'
    command = f'python3 /home/bab/Desktop/ali/BABNLU-Services/scripts/build_spell_checker.py --model_file "{model_file}" --corpus_files "{corpus_file}"'
    output = execute_command(command)
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
