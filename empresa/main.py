from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
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
        abort(404, mensagem="O aluno com matricula = {} não existe".format(matricula)) #404:Not Found

# Parse dos dados enviados na requisição no formato JSON:
parser = reqparse.RequestParser()
parser.add_argument('matricula', type=int, help='matricula do aluno')
parser.add_argument('nome', type=str, help='nome do aluno')
parser.add_argument('nota', type=float, help='nota do aluno')

# Produto:
# 1) Apresenta um único produto.
# 2) Remove um único produto.
# 3) Atualiza (substitui) um produto.
class Aluno(Resource):
    def get(self, matricula):
        aborta_se_o_aluno_nao_existe(matricula)
        return ESCOLA[int(matricula)]
    
    def delete(self, matricula):
        aborta_se_o_aluno_nao_existe(matricula)
        del ESCOLA[int(matricula)]
        return '', 204, #204: No Content

    def put(self, matricula):
        aborta_se_o_aluno_nao_existe(matricula)
        args = parser.parse_args()
        for aluno in ESCOLA:
            if aluno['matricula'] == int(matricula):
               aluno['matricula'] = args['matricula']
               aluno['nome'] = args['nome']
               aluno['nota'] = args['nota']
               break
        return aluno, 200, #200: OK


# ListaProduto:
# 1) Apresenta a lista de produtos.
# 2) Insere um novo produto.
class ListaAluno(Resource):
    def get(self):
        return ESCOLA
    
def post(self):
    args = parser.parse_args()
    matricula = -1

    for produto in ESCOLA:
        if int(aluno['matricula']) > matricula:
            matricula = int(produto['matricula'])
    matricula = matricula + 1
    aluno = {'matricula': matricula, 'nome': args['nome'], 'nota': args['nota']}
    ESCOLA.append(aluno)
    return aluno, 201, #201: Created

class AlunoSTR(Resource):
    def get(self, nome):
        aborta_se_o_aluno_nao_existe(1)
        for aluno in ESCOLA:
            if aluno['nome'] == nome:
                return aluno
            
##class ListaAluno(Resource):
    def post(self, nome):
        aborta_se_o_aluno_nao_existe(1)
        for aluno in ESCOLA:
            if aluno['nome'] == nome:
                return aluno
##FAZER EM CASA            

##
## Roteamento de recursos:
##
api.add_resource(Aluno, '/aluno/<matricula>')
api.add_resource(ListaAluno, '/aluno')
api.add_resource(AlunoSTR, '/aluno-str/<nome>')

if __name__ == '__main__':
    app.run(debug=True)