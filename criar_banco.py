from banco import engine, Base
from modelos import Paciente, Profissional, UBS, Consulta

Base.metadata.create_all(engine)

print("Banco criado com sucesso!")
