from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Modifie ces liens avec tes vrais profils.
SOCIALS = {
    "twitch": "https://twitch.tv/",
    "kick": "https://kick.com/",
    "tiktok": "https://vt.tiktok.com/ZSqwpvrLD/",
    "instagram": "https://instagram.com/",
}

@app.route("/")
def home():
    return render_template("index.html", socials=SOCIALS)

@app.route("/api/socials")
def socials():
    return jsonify(SOCIALS)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
