# Exemplo de ambiente de desenvolvimento

Ferramentas previamente instaladas:

- Pipx (instalação e configuração: pip install --user pipx e python -m pipx ensurepath)
- Poetry (instalação: pipx install poetry)

Sugiro colocar o ambiente python virtual no diretório do projeto, e a configuração é conforme:

`poetry config virtualenvs.in-project true`

A estrutura inicial do projeto foi criada com a ferramenta Poetry dentro da pasta do projeto:

`poetry new --src .`

O conteúdo do .gitignore é sugerido pelo GitHub.

As ferramentas de apoio ao desenvolvimento instaladas são:

- pylint: checagem estática do código e sugestões de melhoria. É interessante notar que o arquivo com as regras para o linter foi gerado com o comando pylint --generate-rcfile > .pylintrc e algumas alterações em relação ao padrão foram realizadas (tamanho de linha para 8 e ativada a recursividade do linter).
- black: formatação do código (também faz checagem, se desejar)
- pytest: testes automatizados
- pytest-cov: relatório de cobertura de testes para o código
- pip-audit: verificação de falhas de segurança em bibliotecas utilizadas pelo projeto

Você pode verificar sugestões de como executar as ferramentas no arquivo Makefile.
