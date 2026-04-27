## Passo 2: Colocando as mãos na massa com o Copilot

No passo anterior, o GitHub Copilot conseguiu nos ajudar a entrar no projeto. Isso por si só já é uma economia de tempo enorme, mas agora vamos trabalhar de verdade!

:bug: **HÁ UM BUG NO SITE** :bug:

Descobrimos que algo está errado no fluxo de inscrição.
Atualmente os estudantes conseguem se inscrever na mesma atividade **mais de uma vez**! Vamos ver até onde o Copilot pode nos levar para descobrir a causa e desenhar uma correção limpa.

Antes de mergulharmos, uma rápida introdução sobre como o Copilot funciona. 🧑‍🚀

### 📖 Teoria: Como o Copilot funciona

Em resumo, você pode pensar no Copilot como um colega de trabalho muito especializado. Para ser efetivo com ele, você precisa fornecer um pano de fundo (contexto) e direção clara (prompts). Além disso, pessoas diferentes são melhores em coisas diferentes por causa de suas experiências únicas (modelos).

- **Como fornecemos contexto?** No nosso ambiente de codificação, o Copilot considera automaticamente o código próximo e as abas abertas. Se estiver usando o chat, você também pode referenciar arquivos explicitamente.

- **Qual modelo devemos escolher?** Para o nosso exercício, isso não deve importar muito. Experimentar modelos diferentes faz parte da diversão! Isso é assunto para outra lição! 🤖

- **Como faço bons prompts?** Ser explícito e claro ajuda o Copilot a fazer o melhor trabalho. Mas, diferentemente de alguns sistemas tradicionais, você sempre pode esclarecer a direção com prompts subsequentes.

> [!TIP]
> Existem várias outras formas de complementar o conhecimento e as capacidades do Copilot, como [chat participants](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/github-copilot-chat-cheat-sheet?tool=vscode#chat-participants), [chat variables](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/github-copilot-chat-cheat-sheet?tool=vscode#chat-variables), [slash commands](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/github-copilot-chat-cheat-sheet?tool=vscode#slash-commands-1) e [MCP tools](https://code.visualstudio.com/docs/copilot/chat/mcp-servers).

### :keyboard: Atividade: Use o Copilot para corrigir o bug de inscrição :bug:

1. Vamos pedir ao Copilot para sugerir de onde nosso bug pode estar vindo. Abra o painel **Copilot Chat** em **Ask mode** e pergunte o seguinte.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > #codebase Os estudantes conseguem se inscrever duas vezes em uma atividade.
   > De onde esse bug pode estar vindo?
   > ```

1. Agora que sabemos que o problema está no arquivo `src/app.py` e na função `signup_for_activity`, vamos seguir a recomendação do Copilot e corrigir (de forma semi-manual). Vamos começar com um comentário e deixar o Copilot completar a correção.
   1. Abra o arquivo `src/app.py`.

      > 💡 **Dica:** Se o Copilot mencionou `src/app.py` no chat, você pode clicar no arquivo direto pela visão do chat para abri-lo.

   1. Próximo ao final do arquivo, encontre a função `signup_for_activity`.

   1. Encontre a linha de comentário que descreve a adição de um estudante. Logo acima dela é onde parece lógico fazermos nossa verificação de inscrição.

   1. Insira o comentário abaixo e pressione Enter para ir para a próxima linha. Após um instante, um texto sombreado temporário aparecerá com uma sugestão do Copilot! Boa! :tada:

      Comentário:

      ```python
      # Validate student is not already signed up
      ```

      <img width="700" alt="Sugestão em texto sombreado do Copilot no editor" src="../images/shadow-text.gif" />

   1. Pressione `Tab` para aceitar a sugestão do Copilot e converter o texto sombreado em código.

   <details>
   <summary>Exemplo de Resultado</summary><br/>

   O Copilot evolui todos os dias e nem sempre produz o mesmo resultado. Se você não estiver satisfeito com as sugestões, aqui está um exemplo de resultado válido que produzimos durante a criação deste exercício. Use-o para continuar.

   ```python
   @app.post("/activities/{activity_name}/signup")
   def signup_for_activity(activity_name: str, email: str):
      """Sign up a student for an activity"""
      # Validate activity exists
      if activity_name not in activities:
         raise HTTPException(status_code=404, detail="Activity not found")

      # Get the activity
      activity = activities[activity_name]

      # Validate student is not already signed up
      if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student is already signed up")

      # Add student
      activity["participants"].append(email)
      return {"message": f"Signed up {email} for {activity_name}"}
   ```

   </details>

### :keyboard: Atividade: Deixe o Copilot gerar dados de exemplo 📋

No desenvolvimento de novos projetos, geralmente é útil ter dados falsos com aparência realista para teste. O Copilot é excelente nessa tarefa, então vamos adicionar mais algumas atividades de exemplo e apresentar outra forma de interagir com o Copilot usando o **Inline Chat**.

O **Inline Chat** e o painel **Copilot Chat** são parecidos, mas diferem no escopo: o Copilot Chat lida com perguntas mais amplas, multi-arquivo ou exploratórias; o Inline Chat é mais rápido quando você quer ajuda focada na linha ou bloco bem à sua frente.

1. Próximo ao topo do arquivo `src/app.py` (cerca da linha 23), encontre a variável `activities`, onde nossas atividades extracurriculares de exemplo estão configuradas.

1. Selecione todo o dicionário `activities` clicando e arrastando o mouse do topo até o final do dicionário. Isso ajudará a fornecer contexto ao Copilot para o próximo prompt.

   <img width="700" alt="Dicionário activities selecionado antes de abrir o inline chat" src="../images/activities-dict-highlighted.png" />


1. Abra o Copilot Inline Chat usando o atalho de teclado `Ctrl + I` (Windows) ou `Cmd + I` (Mac).

   > 💡 **Dica:** Outra forma de abrir o Copilot Inline Chat é: `clique direito` em qualquer das linhas selecionadas -> `Open Inline Chat`.

1. Insira o texto de prompt a seguir e pressione Enter ou o botão **Send** à direita.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Adicione mais 2 atividades relacionadas a esportes, mais 2 atividades
   > artísticas e mais 2 atividades intelectuais.
   > ```

1. Após um momento, o Copilot vai começar a fazer alterações diretamente no código. As alterações serão estilizadas de forma diferente para tornar adições e remoções fáceis de identificar. Reserve um instante para inspecionar e verificar as alterações e, em seguida, pressione o botão **Keep**.

   <details>
   <summary>Exemplo de Resultado</summary><br/>

   O Copilot evolui todos os dias e nem sempre produz o mesmo resultado. Se você não estiver satisfeito com as sugestões, aqui está um exemplo de resultado que produzimos durante a criação deste exercício. Use-o para seguir adiante, caso esteja com dificuldade.

   ```python
   # In-memory activity database
   activities = {
      "Chess Club": {
         "description": "Learn strategies and compete in chess tournaments",
         "schedule": "Fridays, 3:30 PM - 5:00 PM",
         "max_participants": 12,
         "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
      },
      "Programming Class": {
         "description": "Learn programming fundamentals and build software projects",
         "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
         "max_participants": 20,
         "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
      },
      "Gym Class": {
         "description": "Physical education and sports activities",
         "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
         "max_participants": 30,
         "participants": ["john@mergington.edu", "olivia@mergington.edu"]
      },
      "Basketball Team": {
         "description": "Competitive basketball training and games",
         "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
         "max_participants": 15,
         "participants": []
      },
      "Swimming Club": {
         "description": "Swimming training and water sports",
         "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
         "max_participants": 20,
         "participants": []
      },
      "Art Studio": {
         "description": "Express creativity through painting and drawing",
         "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
         "max_participants": 15,
         "participants": []
      },
      "Drama Club": {
         "description": "Theater arts and performance training",
         "schedule": "Tuesdays, 4:00 PM - 6:00 PM",
         "max_participants": 25,
         "participants": []
      },
      "Debate Team": {
         "description": "Learn public speaking and argumentation skills",
         "schedule": "Thursdays, 3:30 PM - 5:00 PM",
         "max_participants": 16,
         "participants": []
      },
      "Science Club": {
         "description": "Hands-on experiments and scientific exploration",
         "schedule": "Fridays, 3:30 PM - 5:00 PM",
         "max_participants": 20,
         "participants": []
      }
   }
   ```

   </details>

1. Agora você pode acessar seu site e verificar que as novas atividades estão visíveis.

### :keyboard: Atividade: Use o Copilot para descrever nosso trabalho 💬

Bom trabalho corrigindo aquele bug e expandindo as atividades de exemplo! Agora vamos commitar e enviar nosso trabalho para o GitHub, novamente com a ajuda do Copilot!

1. Na barra lateral esquerda, selecione a aba `Source Control`.

   > 💡 **Dica:** Abrir um arquivo a partir da área de controle de versões mostrará as diferenças em relação ao original, em vez de simplesmente abrir o arquivo.

1. Encontre o arquivo `app.py` e pressione o sinal `+` para reunir suas alterações na área de staging.

   ![imagem](../images/staging-changes-icon.png)

1. Acima da lista de alterações em staging, encontre a caixa de texto **Message**, mas **não digite nada** por enquanto.
   - Tipicamente, você escreveria uma breve descrição das mudanças aqui, mas agora temos o Copilot para ajudar!

1. À direita da caixa de texto **Message**, encontre e clique no botão **Generate Commit Message** (ícone de sparkles).

1. Pressione o botão **Commit** e o botão **Sync Changes** para enviar suas alterações ao GitHub.

1. Aguarde um momento para a Mona conferir seu trabalho, fornecer feedback e compartilhar a próxima lição.

<details>
<summary>Com problemas? 🤷</summary><br/>

Se você não receber feedback, aqui estão algumas coisas para verificar:

- Garanta que você enviou as alterações do arquivo `src/app.py` para a branch `accelerate-with-copilot`.

</details>
