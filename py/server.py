from flask import Flask, request
 
app = Flask(__name__, static_folder="path1", template_folder="path2")
@app.route('/')
def hello_world():
    # print(request.path)
    # print(request.full_path)
    return request.args.get('info')
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)