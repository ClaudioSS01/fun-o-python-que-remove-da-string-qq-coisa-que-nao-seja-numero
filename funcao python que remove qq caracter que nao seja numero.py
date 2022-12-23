def remover_nao_digitos(string):
  digitos = '0123456789'
  return ''.join([c for c in string if c in digitos])

# Exemplo de uso
string = "123abc456def789"
string_sem_nao_digitos = remover_nao_digitos(string)
print(string_sem_nao_digitos) # imprime "123456789"
