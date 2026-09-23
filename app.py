from flask import Flask, render_template, request, redirect, url_for, session,make_response,flash

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
            
            respuesta = make_response(redirect(url_for('cursos')))
            respuesta.set_cookie('usuario_preferido', usuario)
            return respuesta
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('login.html', mensaje=mensaje)

@app.route('/cursos')
def cursos():
    if 'usuario' in session:
        usuario_cookie = request.cookies.get('usuario_preferido')
        cursos = [
            {"nombre": "Programación Web", "docente": "Luis Pérez", "cupos": 15},
            {"nombre": "Bases de Datos", "docente": "Ana López", "cupos": 8},
            {"nombre": "Inteligencia Artificial", "docente": "Carlos Rojas", "cupos": 0}
        ]
        return render_template('cursos.html', cursos=cursos, usuario=usuario_cookie)
    else:
        return redirect(url_for('login'))

@app.route('/eliminar_cookie')
def eliminar_cookie():
    respuesta = make_response(redirect(url_for('cursos')))
    respuesta.delete_cookie('usuario_preferido')
    return respuesta



@app.route('/perfil')
def perfil():
    if 'usuario' in session:
        return render_template('perfil.html')
    else:
            return redirect(url_for('login'))
  


@app.route('/logout')
def logout():
    session.clear()
    flash("La sesión fue cerrada correctamente")
    return redirect(url_for('login'))



if __name__ == '__main__':
    app.run(debug=True)