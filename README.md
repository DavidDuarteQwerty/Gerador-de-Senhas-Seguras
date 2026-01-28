<h1 align="left">🔐 Gerador de Senhas Seguras</h1>

<p align="left">
  Ferramenta em Python para gerar senhas fortes no terminal.<br>
  Permite escolher tamanho e tipos de caracteres (letras, números e símbolos).
</p>

<hr>

<h2>🔍 O que é</h2>

<p>
<code>password-generator-python</code> é um pequeno programa que cria senhas seguras de forma automática.<br>
Em vez de inventar senhas fracas, você:
</p>

<ol>
  <li>Executa o programa</li>
  <li>Escolhe o tamanho da senha</li>
  <li>Seleciona os tipos de caracteres</li>
  <li>Recebe uma senha forte gerada automaticamente</li>
</ol>

<hr>

<h2>📂 Estrutura</h2>

<pre><code>├── gerador_senhas.py   &lt;-- programa principal</code></pre>

<hr>

<h2>⚙️ Script principal (gerador_senhas.py)</h2>

<p>
O script:
</p>
<ul>
  <li>Pede o tamanho da senha (8 a 64)</li>
  <li>Pergunta se quer usar maiúsculas, minúsculas, números e símbolos</li>
  <li>Gera uma senha aleatória usando o módulo <code>secrets</code></li>
  <li>Mostra a senha no ecrã</li>
</ul>

<hr>

<h2>🛠️ Instalação</h2>

<ol>
  <li>Instale o Python 3</li>
  <li>Clone o repositório ou faça download dos ficheiros</li>
  <li>Abra a pasta no terminal</li>
</ol>

<hr>

<h2>🚀 Como usar</h2>

<ol>
  <li>Abrir o terminal</li>
  <li>Navegar até à pasta do projeto</li>
  <li>Executar:
    <pre><code>python gerador_senhas.py</code></pre>
  </li>
  <li>Responder às perguntas no ecrã</li>
</ol>

Exemplo de execução:

<pre><code>==================================
   GERADOR DE SENHAS SEGURAS
==================================
Tamanho da senha (8 a 64): 12
Incluir letras MAIÚSCULAS? (s/n): s
Incluir letras minúsculas? (s/n): s
Incluir números? (s/n): s
Incluir símbolos? (s/n): s

Senha gerada:
A7@kP2!qZ9#L
</code></pre>

<hr>

<h2>💡 Possíveis melhorias</h2>

<ul>
  <li>Gerar várias senhas de uma vez</li>
  <li>Copiar automaticamente para a área de transferência</li>
  <li>Salvar senhas num ficheiro</li>
  <li>Interface gráfica no futuro</li>
</ul>
