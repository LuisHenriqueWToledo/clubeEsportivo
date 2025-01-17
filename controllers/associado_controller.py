from flask import request, flash, redirect, render_template, session

from models.associado import Associado


def inserir_associado():
    if request.method == 'POST':
        cpf = request.form['cpf']
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        plano = request.form['plano']

        novo_associado = Associado(cpf=cpf, nome=nome, email=email, telefone=telefone, plano=plano)
        sucesso, mensagem = novo_associado.save()

        if sucesso:
            flash(mensagem, 'success')
            session.pop('form_data', None)
            return redirect('/')
        else:
            session['form_data'] = {
                'cpf': cpf,
                'nome': nome,
                'email': email,
                'telefone': telefone,
                'plano': plano
            }
            flash(mensagem, 'danger')
            return redirect('/')