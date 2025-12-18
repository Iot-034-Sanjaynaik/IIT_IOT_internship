from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_values():
    temperature = request.args.get("temperature")
    light_intensity = request.args.get("light_intensity")

    return {
        "temperature": temperature,
        "light_intensity": light_intensity
    }, 200

if __name__ == "__main__":
    app.run(debug=True)