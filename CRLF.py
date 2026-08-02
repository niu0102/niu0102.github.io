from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

@app.get('/members')
def members():
    member_id = request.args.get('id', '1')
    challenge = int(request.args.get('challenge', '0'))

    payload = {
        'id': member_id,
        'name': 'Hacker',
        'admin': True  # 핵심: admin을 True로
    }

    resp = jsonify({
        'item': payload,
        'challenge': hashlib.sha256(challenge.to_bytes(8)).hexdigest()
    })
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
