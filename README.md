# 📄 Currículo Dinâmico (YAML para HTML/PDF)

> Um gerador de currículo minimalista, responsivo e sem dependências complexas (No-Build). Ele consome os dados de um arquivo `.yaml` e renderiza o currículo diretamente no navegador, pronto para ser exportado como um PDF perfeito.

🔗 **Acesse a versão ao vivo:** [augustoheiss.github.io/cv-yaml](https://augustoheiss.github.io/cv-yaml/)

## 📌 Sobre o Projeto

A ideia deste repositório é separar completamente os **dados** (conteúdo do currículo) da **apresentação** (design). 

Em vez de lutar contra editores de texto ou softwares de design toda vez que for necessário atualizar uma experiência ou competência, basta editar um único arquivo de texto estruturado (`cv.yaml`). O front-end carrega esse arquivo de forma assíncrona, faz o parse e popula o template em tempo real.

## 🚀 Tecnologias Utilizadas

* **HTML5 / Vanilla JS:** Estrutura base e lógica de consumo do arquivo, sem necessidade de frameworks pesados.
* **Tailwind CSS (via CDN):** Para uma estilização rápida, responsiva e moderna, focada no Dark Mode.
* **js-yaml:** Biblioteca leve importada via CDN para interpretar o arquivo `.yaml` diretamente no cliente.
* **CSS Print Media Queries:** Regras avançadas (`@media print`) e hacks de "tabela fantasma" para garantir que as quebras de página do PDF ignorem margens brancas, mantenham as cores de fundo ativas e evitem cortes secos no meio das caixas de texto.

## ⚙️ Como Funciona

1. O navegador carrega o arquivo `index.html`.
2. Um script simples usa a API `fetch()` para ler o arquivo `cv.yaml`.
3. A biblioteca `js-yaml` converte o texto YAML em um objeto JavaScript.
4. O DOM é populado dinamicamente com as informações (Nome, Resumo, Projetos, Experiências e Skills).

## 🛠️ Como Usar (Crie o seu)

Se quiser usar este template para o seu próprio currículo:

1. Faça um Fork ou clone este repositório.
2. Abra o arquivo `cv.yaml` e substitua as informações com os seus dados, respeitando a indentação.
3. Suba para o GitHub e ative o **GitHub Pages**.
4. Seu currículo estará no ar e fácil de manter!

## 🖨️ Geração do PDF

A página possui um botão "Gerar PDF Terminal" que aciona a janela de impressão nativa do navegador. A página foi inteiramente otimizada para isso. 

**Dicas para exportar um PDF perfeito:**
* Certifique-se de ativar a opção **"Imprimir gráficos de fundo"** (Background graphics) nas configurações de impressão do seu navegador para manter o tema escuro e os detalhes visuais.
* Desative a impressão de "Cabeçalhos e Rodapés" (Headers and footers) para um visual mais limpo.
* A página está configurada para tamanho **A4** sem margens (o próprio CSS já cuida do respiro necessário).
