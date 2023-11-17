from flask import Blueprint, jsonify, request, current_app, send_from_directory, url_for
from werkzeug.utils import secure_filename
from datetime import datetime
from database_manager import Moments
import os

moments_db = Moments()

moments_module = Blueprint('moments_module', __name__)


@moments_module.route('/upload_moment', methods=['POST'])
def upload_moment():
    text = request.form['text']
    image = request.files['image']

    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        image.save(image_path)

        moment_data = {
            "text": text,
            "image_url": url_for('moments_module.uploaded_file', filename=filename, _external=True),
            "created_at": datetime.utcnow()
        }
        moment_id = moments_db.create_moment(moment_data)
        return jsonify({"message": "Moment uploaded successfully", "moment_id": str(moment_id)}), 201

    return jsonify({"message": "Invalid file type or no file uploaded"}), 400


@moments_module.route('/moments', methods=['GET'])
def get_moments():
    moments_list = moments_db.get_moments()
    return jsonify(moments_list)


@moments_module.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}