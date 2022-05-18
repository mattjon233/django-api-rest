# Avaliação Desenvolvedor Fullstack

### Contexto

Considere a necessidade:

Juan, membro do time de gestão de vulnerabilidades, é o responsável por decidir quais vulnerabilidades devem ser priorizadas para correção. Seu trabalho consiste em analisar mensalmente extensos arquivos .CSV que contém informações detalhadas acerca dos hosts e vulnerabilidades do ambiente. Com o intuito de melhorar e agilizar suas entregas mensais, foi dado como solução o desenvolvimento de um sistema com as seguintes funções:

1. O sistema deve importar o conteúdo de um arquivo .CSV
2. O sistema deve exibir as informações como tabelas e/ou gráficos, de forma a facilitar o trabalho de análise e priorização das vulnerabilidades a serem corrigidas, devem existir visões por ativo e por ambiente.
3. O sistema deve gerar uma métrica de risco para o host.
4. O sistema deve gerar uma média de risco do ambiente.
5. O usuário irá marcar quando uma vulnerabilidade foi corrigida.

**Caracteristicas da API:**

- As APIs devem possuir paginação de 50 elementos.
- Realizar filtragens e ordenações.
- Não devem permitir modificação dos dados dos hosts e vulnerabilidades, apenas para mudança de seus status (corrigida e não corrigida).

### Linguagens/Framework

- **Back:** Python, Django, Django Rest Framework
- **Front:** Typescript, React

### Informações Adicionais

- [Vulnerabilidades](https://en.wikipedia.org/wiki/Vulnerability_(computing))
- [CVSS](https://en.wikipedia.org/wiki/Common_Vulnerability_Scoring_System)
- [Risk Factor](https://en.wikipedia.org/wiki/Risk_factor_(computing))
- [Métricas de Vulnerabilidade](https://nvd.nist.gov/vuln-metrics/cvss)
- [OWASP Top10](https://owasp.org/www-project-top-ten)

### Avaliação

A. Monte um desenho com a arquitetura desse sistema, considerando todos os componentes e tecnologias necessárias para o seu correto funcionamento.

B. Avalie quais controles de segurança são pertinentes para esse sistema, com o objetivo de protegê-lo ao máximo, evitando vazamento de dados. Questões de auditoria e logging são importantes também.

C. Vamos avaliar sua lógica de programação e estruturação do código de acordo com os seguintes critérios:
    - Qualidade do Código: objetividade, clareza, formatação e modularização.
    - Desempenho: consumo de recursos e tempo de resposta.
    - Documentação: guia de instalação/execução, presença de comentários e docstrings.
    - Testes unitários.
    - OBS: Não é necessário desenvolver todos os componentes.

### Entrega

Encaminhe por e-mail um documento com o desenho e a documentação com a desrição explicando como atender cada uma das 5 funções elencadas acima e o racional de sua decisão.

Encaminhe o link do repositório do GitHub ou similares contendo as implementações do projeto com base na arquitetura descrita que você desenvolveu.

OBS: Não utilizar o nome "Morphus" no repostório do projeto.