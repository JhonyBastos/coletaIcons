COLETOR DE ICONES WEB

App desenvolvido para coleta de todos os icones da página escolhida utilizando a biblioteca BeautifulSoup. Os dados podem ser armazenados no banco de dados SQLite ou salvo em um arquivo .csv.
Funções princiais:

  - Utilize o link configurado para teste: http://themedesigner.in/demo/admin-press/main/icon-material.html
  - Leitura do link da pagina desejada para coleta;
  - Coleta do icones pela tag html <i>;
  - Apresentação dos dados coletados em uma tabela no template Listagem.html;
  
ATENÇÃO!!!
  O app está coletando os primeiro 10 icons, por motivos de carregamento. Alterar a quantidade de icons coletados modificando o contador em: core/views.py --> def coleta_icons.  
  
 
