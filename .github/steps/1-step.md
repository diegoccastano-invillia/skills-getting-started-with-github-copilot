## Passo 1: Olá, Copilot

Boas-vindas ao seu exercício **"Começando com o GitHub Copilot"**! :robot:

Neste exercício, você vai usar diferentes recursos do GitHub Copilot para trabalhar em um site que permite que estudantes da Mergington High School se inscrevam em atividades extracurriculares. 🎻 ⚽️ ♟️

<img width="600" alt="captura de tela do WebApp da Mergington High School" src="https://github.com/diegoccastano-invillia/skills-getting-started-with-github-copilot/blob/main/.github/images/mergington-high-school-webapp.png?raw=true" />

### 📖 Teoria: Conhecendo o GitHub Copilot

<img width="150" align="right" alt="logo do copilot" src="https://github.com/diegoccastano-invillia/skills-getting-started-with-github-copilot/blob/main/.github/images/copilot-logo.png?raw=true" />

O GitHub Copilot é um assistente de codificação com IA que ajuda você a escrever código mais rápido e com menos esforço, permitindo concentrar mais energia em resolver problemas e colaborar.

Está comprovado que o GitHub Copilot aumenta a produtividade dos desenvolvedores e acelera o ritmo do desenvolvimento de software. Para mais informações, veja [Research: quantifying GitHub Copilot’s impact on developer productivity and happiness no blog do GitHub.](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/)

Enquanto trabalha na sua IDE, você vai interagir com o GitHub Copilot principalmente das seguintes formas:

| Modo de Interação         | 📝 Descrição                                                                                                                 | 🎯 Melhor Para                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| **⚡ Sugestões inline**   | Sugestões de código assistidas por IA que aparecem enquanto você digita, oferecendo completamentos com base no contexto — de uma única linha até funções inteiras. | Completar a linha atual ou, às vezes, um bloco inteiro de código novo                                            |
| **💭 Inline Chat**        | Chat interativo com escopo no arquivo atual ou na seleção. Faça perguntas sobre blocos de código específicos.                 | Explicações de código, debug de funções específicas, melhorias pontuais                                          |
| **💬 Ask Mode**           | Otimizado para responder a perguntas sobre seu codebase, sobre programação e sobre conceitos gerais de tecnologia.            | Entender como o código funciona, explorar ideias, tirar dúvidas                                                  |
| **🤖 Agent Mode**         | Modo padrão recomendado para a maioria das tarefas: edições autônomas, uso de ferramentas e acompanhamento até concluir a tarefa. | Tarefas do dia a dia, de correções pontuais a implementações maiores em vários arquivos                          |
| **🧭 Plan Agent**         | Otimizado para esboçar um plano e fazer perguntas de esclarecimento antes que qualquer mudança no código aconteça.            | Quando você quer revisar um plano primeiro e depois entregá-lo para implementação                                |

Conforme você trabalha, vai notar que o GitHub Copilot ajuda em vários lugares dentro do site `github.com` e nos seus ambientes de codificação favoritos, como VS Code, Jet Brains e Xcode!

Para a prática de hoje, vamos usar o VS Code em um ambiente de desenvolvimento pré-configurado conhecido como [GitHub Codespace](https://github.com/features/codespaces).

> [!TIP]
> Você pode aprender mais sobre os recursos atuais e futuros na documentação de [GitHub Copilot Features](https://docs.github.com/en/copilot/about-github-copilot/github-copilot-features).

### :keyboard: Atividade: Receber uma introdução ao projeto pelo Copilot Chat

Vamos iniciar nosso ambiente de desenvolvimento, usar o Copilot para aprender um pouco sobre o projeto e, em seguida, executá-lo.

1. Use o botão abaixo para abrir a página **Create Codespace** em uma nova aba. Use a configuração padrão.

   [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/{{full_repo_name}}?quickstart=1)

1. Confirme que o campo **Repository** corresponde à sua cópia do exercício, e não ao original, e então clique no botão verde **Create Codespace**.
   - ✅ Sua cópia: `/{{full_repo_name}}`
   - ❌ Original: `/skills/getting-started-with-github-copilot`

1. Aguarde um momento até o Visual Studio Code carregar no seu navegador.

1. Na barra lateral esquerda, clique na aba de extensões e verifique se as extensões `GitHub Copilot` e `Python` estão instaladas e habilitadas.

   <img width="350" alt="extensão do copilot para o VS Code" src="https://github.com/diegoccastano-invillia/skills-getting-started-with-github-copilot/blob/main/.github/images/copilot-extension-vscode.png?raw=true" />

   <img width="350" alt="extensão do python para o VS Code" src="https://github.com/diegoccastano-invillia/skills-getting-started-with-github-copilot/blob/main/.github/images/python-extension-vscode.png?raw=true" />

1. No topo do VS Code, localize e clique no ícone **Toggle Chat** para abrir o painel lateral do Copilot Chat.

   <img width="150" alt="imagem" src="https://github.com/diegoccastano-invillia/skills-getting-started-with-github-copilot/blob/main/.github/images/toggle-chat-icon.png?raw=true" />

   > 🪧 **Nota:** Se esta for a primeira vez que você usa o GitHub Copilot, será preciso aceitar os termos de uso para continuar.

1. Garanta que você está no **Ask Mode** para nossa primeira interação.

   <img width="350" alt="captura mostrando a seleção do Ask Mode no Copilot Chat" src="https://github.com/diegoccastano-invillia/skills-getting-started-with-github-copilot/blob/main/.github/images/ask-mode-selection.png?raw=true" />

1. Insira o prompt abaixo para pedir ao Copilot que apresente o projeto a você.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Por favor, explique brevemente a estrutura deste projeto.
   > O que devo fazer para executá-lo?
   > ```

   > 🪧 **Nota:** Não é necessário seguir as instruções recomendadas pelo Copilot. Já preparamos o ambiente para você.

1. Agora que sabemos um pouco mais sobre o projeto, vamos de fato executá-lo! Na barra lateral esquerda, selecione a aba `Run and Debug` e clique no ícone **Start Debugging**.

   <img width="300" alt="imagem" src="https://github.com/diegoccastano-invillia/skills-getting-started-with-github-copilot/blob/main/.github/images/run-and-debug-tab.png?raw=true" />

1. Queremos ver nossa página rodando no navegador; então, vamos descobrir a URL e a porta. Se não estiver visível, expanda o painel inferior e selecione a aba **Ports**.

1. Na lista, encontre a porta `8000` e o link relacionado. Passe o mouse sobre o link e clique no ícone **Open in browser**.

   ![imagem](https://github.com/diegoccastano-invillia/skills-getting-started-with-github-copilot/blob/main/.github/images/open-in-browser-icon.png?raw=true)

### :keyboard: Atividade: Use o Copilot para lembrar de um comando do terminal 🙋

Bom trabalho! Agora que conhecemos a aplicação e sabemos que ela funciona, vamos pedir ajuda ao Copilot para criar uma branch onde possamos fazer algumas customizações.

1. No painel inferior do VS Code, selecione a aba **Terminal** e, no lado direito, clique no sinal `+` para criar uma nova janela de terminal.

   > 🪧 **Nota:** Isso evita parar a sessão de debug existente que está hospedando nosso serviço web.

1. Na nova janela do terminal, use o atalho de teclado `Ctrl + I` (Windows) ou `Cmd + I` (Mac) para abrir o **Terminal Inline Chat do Copilot**.

1. Vamos pedir ao Copilot para nos lembrar de um comando que esquecemos: criar uma branch e publicá-la.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Hey copilot, how can I create and publish a new Git branch called "accelerate-with-copilot"?
   > ```

   > 💡 **Dica:** Se o Copilot não trouxer exatamente o que você quer, é só continuar explicando o que precisa. O Copilot lembra do histórico da conversa para responder em seguida.

1. Aperte o botão `Run` para deixar o Copilot inserir o comando de terminal por você. Sem precisar copiar e colar!

1. Após um momento, olhe na barra de status inferior do VS Code, no canto esquerdo, para ver a branch ativa. Ela deve agora indicar `accelerate-with-copilot`. Se sim, este passo está concluído!

1. Agora que sua branch foi enviada para o GitHub, a Mona já deve estar verificando seu trabalho. Dê um instante a ela e fique de olho nos comentários. Você verá a resposta com o progresso e a próxima lição.

<details>
<summary>Com problemas? 🤷</summary><br/>

Se você não receber feedback, aqui estão algumas coisas para verificar:

- Garanta que você criou a branch exatamente com o nome `accelerate-with-copilot`. Sem prefixos ou sufixos.
- Garanta que a branch foi de fato publicada no seu repositório.

</details>
