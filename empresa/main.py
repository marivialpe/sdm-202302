from flask import Flask
from flask_restful import reqparse, abort, Api, Resource, request
app = Flask(__name__)
api = Api(app)
ESCOLA = [{'matricula': 1, 'nome': 'Ana', 'nota': 72.00},
          {'matricula': 2, 'nome': 'Bruna', 'nota': 71.50},
          {'matricula': 3, 'nome': 'Carlos', 'nota': 68.50},
          {'matricula': 4, 'nome': 'Diogo', 'nota': 70.00},
          {'matricula': 5, 'nome': 'Ester', 'nota': 69.00}]

def aborta_se_o_aluno_nao_existe(matricula):
    encontrei = False
    for aluno in ESCOLA:
        if aluno['matricula'] == int(matricula):
            encontrei = True

    if encontrei == False:
        abort(404, mensagem="O aluno com matricula = {} não existe".format(matricula))


parser = reqparse.RequestParser()
parser.add_argument('matricula', type=int, help='matricula do aluno')
parser.add_argument('nome', type=str, help='nome do aluno')
parser.add_argument('nota', type=float, help='nota do aluno')


class Aluno(Resource):
    def get(self, matricula):
        aborta_se_o_aluno_nao_existe(matricula)
        return ESCOLA[int(matricula)]
    
    def delete(self, matricula):
        return self._delete_aluno(matricula)
    
    def _delete_aluno(self, matricula):
        for i, aluno in enumerate(ESCOLA):
            if aluno['matricula'] == int(matricula):
                del ESCOLA[i]
                return '', 204
        abort(404, message=f'O aluno com matrícula {matricula} não foi encontrado')

    def put(self, matricula):
        aborta_se_o_aluno_nao_existe(matricula)
        args = parser.parse_args()
        for aluno in ESCOLA:
            if aluno['matricula'] == int(matricula):
               aluno['matricula'] = args['matricula']
               aluno['nome'] = args['nome']
               aluno['nota'] = args['nota']
               break
        return aluno, 200, 

def put(self):
        data = request.get_json()
        if not data or not isinstance(data, list):
            return jsonify({'message': 'Envie uma lista válida de alunos'}), 400
        
        global ESCOLA
        ESCOLA = data 
        return jsonify({'message': 'Registros de alunos atualizados com sucesso'}), 200



class ListaAluno(Resource):
    def get(self):
        return ESCOLA
    
    def post(self):
        args = parser.parse_args()
        matricula = max(aluno['matricula'] for aluno in ESCOLA) + 1
        aluno = {'matricula': matricula, 'nome': args['nome'], 'nota': args['nota']}
        ESCOLA.append(aluno)
        return aluno, 201  


class AlunoSTR(Resource):
    def get(self, nome):
        aborta_se_o_aluno_nao_existe(1)
        for aluno in ESCOLA:
            if aluno['nome'] == nome:
                return aluno
            

    def post(self, nome):
        aborta_se_o_aluno_nao_existe(1)
        for aluno in ESCOLA:
            if aluno['nome'] == nome:
                return aluno

class AtualizarAlunos(Resource):
    def put(self):
        data = request.get_json()
        if not data or not isinstance(data, list):
            abort(400, message='Envie uma lista válida de alunos') 
            global ESCOLA
            ESCOLA = data  
            return jsonify({'message': 'Registros de alunos atualizados com sucesso'}), 200
         

api.add_resource(Aluno, '/aluno/<matricula>')
api.add_resource(ListaAluno, '/aluno')
api.add_resource(AlunoSTR, '/aluno-str/<nome>')
api.add_resource(AtualizarAlunos, '/atualizar-alunos')

if __name__ == '__main__':
    app.run(debug=True)
