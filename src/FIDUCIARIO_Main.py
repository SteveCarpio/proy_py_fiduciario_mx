from flask import Flask, render_template, request, redirect
import oracledb

app = Flask(__name__)

# Configura la conexión a Oracle
# Cambia estos valores por los de tu entorno
oracle_config = {
    "user": "TU_USUARIO",
    "password": "TU_CONTRASEÑA",
    "dsn": "HOST:PUERTO/SERVICIO"  # Ej: "localhost:1521/XEPDB1"
}

@app.route("/", methods=["GET", "POST"])
def index():
    conn = oracledb.connect(**oracle_config)
    cursor = conn.cursor()

    if request.method == "POST":
        email = request.form["email"]
        nota = request.form["nota"]
        cursor.execute("""
            UPDATE usuarios SET notas = :nota WHERE email = :email
        """, {"nota": nota, "email": email})
        conn.commit()
        return redirect("/")

    cursor.execute("SELECT email, nombre, notas FROM usuarios")
    usuarios = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.html", usuarios=usuarios)

if __name__ == "__main__":
    app.run(debug=True)
