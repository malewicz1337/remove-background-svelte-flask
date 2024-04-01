from io import BytesIO
from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image, UnidentifiedImageError


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/remove-bg", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file uploaded", 400

    file = request.files["file"]

    if file.filename == "":
        return "No file selected", 400

    try:
        input_image = Image.open(file.stream)
    except UnidentifiedImageError:
        return "Uploaded file is not a valid image", 400

    output_image = remove(input_image, post_process_mask=True)
    img_io = BytesIO()
    output_image.save(img_io, "PNG")
    img_io.seek(0)

    return send_file(
        img_io,
        mimetype="image/png",
        as_attachment=True,
        download_name="removed_bg.png",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5100)
