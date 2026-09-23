from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = 'abc123'

usuarios = {
    "juan": "1234",
    "maria": "abcd",
    "pedro": "2026"
}


@app.route('/', methods=['GET', 'POST'])
def login():
    mensaje = None
    if request.method == 'POST':
        usuario = request.form.get('username')
        password = request.form.get('password')

        if usuario in usuarios and usuarios[usuario] == password:
            session['usuario'] = usuario
            return redirect(url_for('cursos'))
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('login.html', mensaje=mensaje)

@app.route('/cursos')
def cursos():
    if 'usuario' in session:
        cursos = [
        {"nombre": "Programación Web", "docente": "Luis Pérez", "cupos": 15},
        {"nombre": "Bases de Datos", "docente": "Ana López", "cupos": 8},
        {"nombre": "Inteligencia Artificial", "docente": "Carlos Rojas", "cupos": 0}]
        return render_template('cursos.html', cursos=cursos)
    else:
        return redirect(url_for('login'))


@app.route('/perfil')
def perfil():
    if 'usuario' in session:
        return render_template('perfil.html')
    else:
            return redirect(url_for('login'))
  


@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)