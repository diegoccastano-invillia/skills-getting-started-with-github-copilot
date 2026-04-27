## Passo 3: Engatar a Hiperpropulsão — Modo Agente do Copilot 🚀

### 📖 Teoria: O que é o Modo Agente do Copilot?

O [agent mode](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode) do Copilot é a próxima evolução na codificação assistida por IA. Atuando como um peer programmer autônomo, ele executa tarefas de codificação em múltiplos passos sob seu comando.

O Modo Agente do Copilot reage a erros de compilação e lint, monitora a saída do terminal e dos testes e se autocorrige em loop até que a tarefa seja concluída.

#### Modo Agente (em resumo)

| Aspecto | 👩‍🚀 Modo Agente |
| --- | --- |
| Autonomia e planejamento | Decompõe pedidos de alto nível em trabalho em múltiplos passos e itera até a tarefa estar concluída. |
| Coleta de contexto | Usa seu contexto atual e pode descobrir arquivos relevantes adicionais quando necessário. |
| Uso de ferramentas | Seleciona e invoca ferramentas automaticamente; você também pode direcionar ferramentas com menções como `#codebase`. |
| Aprovação e barreiras de segurança | Ações sensíveis podem exigir aprovação antes da execução, ajudando você a manter o controle. |

#### 🧰 Ferramentas do Modo Agente

O modo agente usa ferramentas para realizar tarefas especializadas enquanto processa a solicitação do usuário. Exemplos de tais tarefas:

- Encontrar arquivos relevantes para completar seu prompt
- Buscar conteúdo de uma página web
- Executar testes ou comandos no terminal

> [!TIP]
> Embora o VS Code forneça muitas ferramentas embutidas, você também pode dar ao Modo Agente mais poderes específicos do domínio por meio das **ferramentas MCP**.
>
> Leia mais em [MCP servers](https://code.visualstudio.com/docs/copilot/customization/mcp-servers) e [GitHub MCP Server](https://github.com/github/github-mcp-server)

Agora, vamos experimentar o **Modo Agente**! 👩‍🚀

### :keyboard: Atividade: Use o Copilot para adicionar uma nova feature! :rocket:

Nosso site lista as atividades, mas mantém a lista de convidados em segredo 🤫 

Vamos usar o Copilot para mudar o site e exibir os estudantes inscritos sob cada atividade!

1. Na parte inferior da janela do Copilot Chat, use o dropdown para alternar para o modo **Agent**.

   <img width="350" alt="imagem" src="https://github.com/diegoccastano-invillia/skills-getting-started-with-github-copilot/blob/main/.github/images/agent-mode-dropdown.png?raw=true" />

1. Abra os arquivos relacionados à nossa página web e arraste cada janela de editor (ou arquivo) para o painel de chat, informando ao Copilot que ele deve usá-los como contexto.

   - `src/static/app.js`
   - `src/static/index.html`
   - `src/static/styles.css`

   > 🪧 **Nota:** Adicionar arquivos como contexto é opcional. Se você pular isso, o Copilot Modo Agente ainda pode usar ferramentas como `#codebase` para procurar arquivos relevantes a partir do seu prompt. Adicionar arquivos específicos ajuda a apontar o Copilot na direção certa, o que é especialmente útil em codebases maiores.

   <img width="400" alt="imagem mostrando arquivos adicionados ao contexto" src="https://github.com/diegoccastano-invillia/skills-getting-started-with-github-copilot/blob/main/.github/images/files-added-to-context.png?raw=true" />

   > 💡 **Dica:** Você também pode usar o botão **Add Context...** para fornecer outras fontes de itens de contexto, como uma issue do GitHub ou os resultados de uma janela do terminal.

1. Peça ao Copilot para atualizar nosso projeto para exibir os participantes atuais das atividades. Aguarde um momento para que as sugestões de edição cheguem e sejam aplicadas.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Olá Copilot, por favor edite os cards de atividades para adicionar uma seção de participantes.
   > Ela deve mostrar os participantes que já estão inscritos naquela atividade como uma lista com marcadores.
   > Lembre-se de deixar bonito!
   > ```

   Depois que o Copilot terminar o trabalho, você está no controle de quais alterações ficam.

   Usando os botões **Keep** mostrados abaixo, você pode aceitar/descartar todas as alterações ou revisar e decidir alteração por alteração. Isso pode ser feito tanto pela visão do painel de chat quanto enquanto inspeciona cada arquivo editado.

      <img width="900" alt="botões para manter ou descartar alterações" src="https://github.com/diegoccastano-invillia/skills-getting-started-with-github-copilot/blob/main/.github/images/review-changes-buttons.png?raw=true" />


1. Antes de simplesmente aceitar as alterações, por favor verifique nosso site novamente e confirme que tudo foi atualizado conforme esperado.

   Aqui está um exemplo de um card de atividade atualizado. Você pode precisar reiniciar a aplicação ou atualizar a página.

   <img width="350" alt="Card de atividade com info de participantes" src="https://github.com/diegoccastano-invillia/skills-getting-started-with-github-copilot/blob/main/.github/images/activity-card-with-participants.png?raw=true" />

   > 🪧 **Nota:** Seu card de atividade pode parecer diferente. O Copilot nem sempre produz o mesmo resultado.

   <details>
   <summary>Precisa de ajuda? 🤷</summary><br/>
   Se o site não estiver carregando, aqui estão algumas coisas para verificar.

   - Reinicie o Debugger do VS Code para garantir que a versão mais recente do site seja servida.
   - Se você esqueceu a URL ou fechou a janela, revise o passo 1.
   - Tente atualizar a página com hard refresh ou abrir em uma janela privada para que ela baixe uma cópia nova.

   </details>

1. Agora que confirmamos que nossas alterações estão boas, use o painel para percorrer cada edição sugerida e pressione **Keep** para aplicar a alteração.

   > 💡 **Dica:** Você pode aceitar as alterações diretamente, modificá-las ou fornecer instruções adicionais para refiná-las usando a interface do chat.

### :keyboard: Atividade: Use o modo Agent para adicionar botões funcionais de "cancelar inscrição"

Vamos experimentar pedidos mais abertos que vão adicionar mais funcionalidade à nossa aplicação web.

Se você não obtiver os resultados desejados, pode tentar outros modelos ou fornecer feedback subsequente para refinar o resultado.

1. Garanta que seu Copilot ainda está no modo **Agent**.

   <img width="250" alt="agent mode" src="https://github.com/diegoccastano-invillia/skills-getting-started-with-github-copilot/blob/main/.github/images/agent-mode-dropdown.png?raw=true" />

1. Clique no ícone **Tools** e explore todas as Ferramentas atualmente disponíveis para o Copilot Modo Agente.

   <img width="250"  alt="ícone de tools" src="https://github.com/diegoccastano-invillia/skills-getting-started-with-github-copilot/blob/main/.github/images/tools-icon.png?raw=true" />

1. Hora do nosso teste! Vamos pedir ao Copilot para adicionar a funcionalidade de remoção de participantes.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > #codebase Por favor, adicione um ícone de excluir ao lado de cada participante e oculte os marcadores da lista.
   > Quando clicado, ele deve cancelar a inscrição daquele participante na atividade.
   > ```

   A ferramenta `#codebase` é usada pelo Copilot para encontrar arquivos relevantes e trechos de código pertinentes à tarefa em questão.

   > 🪧 **Nota:** Neste laboratório incluímos explicitamente a ferramenta `#codebase` para obter os resultados mais reproduzíveis.
   > Sinta-se à vontade para experimentar o prompt **sem** `#codebase` e observar se o Modo Agente decide reunir contexto mais amplo do projeto por conta própria.

1. Quando o Copilot terminar, inspecione as alterações de código e os resultados no site. Se gostar do resultado, pressione o botão **Keep**. Caso contrário, tente fornecer ao Copilot algum feedback para refinar o resultado.

   > 🪧 **Nota:** Se você não vir atualizações no site, pode ser necessário reiniciar o debugger.

1. Peça ao Copilot para corrigir um bug de inscrição.

   > 💡 **Dica:** Recomendamos que você teste o fluxo de inscrição você mesmo para enxergar claramente o comportamento antes/depois das mudanças.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Notei que parece haver um bug.
   > Quando um participante é cadastrado, é preciso atualizar a página para ver a mudança na atividade.
   > ```

1. Quando o Copilot terminar, inspecione os resultados e valide o fluxo de inscrição no site.

   Se gostar do resultado, pressione o botão **Keep**. Caso contrário, tente fornecer feedback ao Copilot.

1. **Commit** e **push** de todas as suas alterações para a branch `accelerate-with-copilot`.

1. Aguarde a Mona conferir seu trabalho e compartilhar o próximo passo.