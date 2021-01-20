#Imports
import urllib.request

#Execute
url = 'https://receita.economia.gov.br/orientacao/tributaria/restituicao-ressarcimento-reembolso-e-compensacao/perdcomp/perdcomp_tabelas.mdb/@@download/file/perdcomp_tabelas.mdb'
filename = 'perdcomp_tabelas.mdb'
urllib.request.urlretrieve(url, filename)