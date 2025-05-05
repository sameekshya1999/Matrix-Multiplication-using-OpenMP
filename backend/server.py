from flask import Flask, request, jsonify, send_from_directory
import os
import matrix

app = Flask(__name__, static_folder='../frontend')

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    size = data.get('size')
    use_openmp = data.get('use_openmp', False)

    try:
        size = int(size)
        if size <= 0:
            return jsonify({'error': 'Matrix size must be positive'}), 400
        result = matrix.multiply(size, 1 if use_openmp else 0)
        return jsonify(result)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Server error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)