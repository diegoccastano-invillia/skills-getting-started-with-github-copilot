## Passo 5: Usando o GitHub Copilot dentro de um pull request

Parabéns! Você terminou a parte de codificação deste exercício (e do VS Code). Agora é hora de fazer o merge do nosso trabalho. :tada: Para encerrar, vamos conhecer dois recursos do Copilot de acesso restrito que podem acelerar nossos pull requests!

### 📖 Teoria: GitHub Copilot para pull requests

#### Resumos de pull request com o Copilot

Tipicamente, você revisaria suas anotações e mensagens de commit e então as resumiria para a descrição do seu pull request. Isso pode levar tempo, especialmente se as mensagens de commit forem inconsistentes ou o código não estiver bem documentado. Felizmente, o Copilot pode considerar todas as alterações no pull request e fornecer os destaques importantes — com referências também!

#### Code review com o Copilot

Mais olhos sobre o nosso trabalho são sempre úteis, então vamos pedir ao Copilot para fazer uma primeira passada antes do processo normal de revisão por pares. O Copilot é ótimo em capturar erros comuns que se resolvem com ajustes simples, mas lembre-se de usá-lo com responsabilidade.

> [!NOTE]
> Esses recursos estão disponíveis apenas em planos pagos do **GitHub Copilot**. [[docs]](https://docs.github.com/en/copilot/get-started/plans)

### :keyboard: Atividade: Resumir e revisar um PR com o Copilot

Tanto **Copilot pull request summaries** quanto **Copilot code review** têm acesso restrito, então esta atividade é, em sua maior parte, opcional. Se você não tem acesso, pule os passos opcionais desta atividade.

1. Em um navegador, abra outra aba e navegue até o seu repositório do exercício.

1. Você pode notar um **banner de notificação** sugerindo criar um novo pull request. Clique nele ou use a aba **Pull Requests** no topo para **criar um novo pull request**. Por favor, use os seguintes detalhes:

   - **base:** `main`
   - **compare:** `accelerate-with-copilot`
   - **title:** `Improve student activity registration system`

1. (Opcional) Na barra de ferramentas da descrição do PR, clique no ícone do **Copilot** e na ação **Summary**. Após um momento, o Copilot adicionará uma descrição com base nas suas alterações. :memo:

   <img alt="botão de summarize do Copilot" width="450px" src="../images/copilot-summarize-button.png">

1. (Opcional) No painel de informações à direita, no topo, localize a seção **Reviewers** e clique no botão **Request** ao lado de um **ícone do Copilot**. Aguarde um momento para o Copilot adicionar um comentário de revisão ao seu pull request!

   <img alt="botão de review do Copilot" width="300px" src="../images/copilot-review-button.png">

   > 💡 **Dica:** Note uma entrada de log indicando que o Copilot foi solicitado para uma revisão.

1. Na parte de baixo, pressione o botão **Merge pull request**. Bom trabalho! Está tudo pronto! :tada:

1. Aguarde um momento para a Mona conferir seu trabalho, fornecer feedback e postar uma revisão final deste exercício!
