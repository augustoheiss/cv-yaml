# ⚙️ CV-YAML: A Máquina do Segundo Atual

> *"A pessoa despreocupada despreza a calamidade, achando que ela sobrevém apenas àqueles cujos pés estão vacilantes."* — **Jó 12:5**

Bem-vindo ao **CV-YAML**, um ecossistema de currículos dinâmicos construído para desconstruir a burocracia do "Papel Antigo" e focar na verdadeira eficiência do "Segundo Atual". 

Este projeto não é apenas um gerador de páginas HTML estáticas ou um conversor de PDF. É uma ferramenta desenhada para transformar a vitrine do seu passado num instrumento ágil, adaptável e, acima de tudo, útil para as necessidades do presente, com a ajuda de Inteligência Artificial (RAG) e dados estruturados (YAML).

---

## 📖 O Rascunho da Alma (Filosofia do Projeto)

Muitas vezes, vemos o nosso currículo como um altar para o nosso ego, um destaque de tudo o que dominámos no passado. Mas, na realidade, ele é apenas um "Papel" — o registo de um segundo que já passou. A sua única função real é abrir a porta para uma conversa produtiva perante uma oportunidade no momento presente.

A verdadeira eficiência não se mede pela acumulação de vitrinas do passado, mas por como atuamos no **segundo atual**. 

Nós, enquanto humanos, somos máquinas biológicas excepcionais. Conseguimos processar inúmeros erros por segundo e continuar a funcionar a 100%. Um erro não nos torna inúteis; é apenas uma fração de dado que processamos para gerar uma reação. Da mesma forma, a tecnologia de ponta não deve ser usada para nos aprisionar em processos burocráticos ou para alimentar o ego no mercado de trabalho. Deve ser usada para **esmagar a burocracia do "Papel Antigo"**. 

Tudo passa. O ser humano é como a relva. Reconhecer isso permite-nos ser adaptáveis na balança do Universo. O objetivo deste projeto é automatizar a criação da vitrine (o currículo) através de IA, para que possamos usar o nosso tempo — o nosso segundo atual — com o que realmente importa: a liberdade de escolha, a geração de ideias e a capacidade de ajudar outras pessoas.

### Objetivos em Frações:
1. **Dados Dinâmicos:** Transformar a estática do passado em dinamismo através de templates CSS intercambiáveis e recomendações geradas por IA.
2. **Interesse acima do Domínio:** Mostrar disposição e adaptabilidade para resolver problemas reais hoje, em vez de focar apenas no domínio obsoleto de ontem.
3. **O Processamento do Passado:** Apresentar a experiência não como um troféu, mas mostrando como esses processos antigos moldaram a sua capacidade de resposta no segundo atual.
4. **Retirar o Juiz de Cena:** Eliminar a linguagem centrada no ego. O foco não é "o quão bom eu sou", mas sim "como o meu esforço gerou valor e resultados coletivos para os outros".

---

## 🛠️ Arquitetura e Funcionalidades Técnicas

Este projeto utiliza o conceito de **Single Source of Truth** (Fonte Única de Verdade). Os seus dados vivem num ficheiro `cv.yaml`, enquanto o JavaScript e o CSS se encarregam de dar vida a esses dados de múltiplas formas.

### 🌟 Funcionalidades Principais:
* **Renderização Dinâmica:** O JavaScript faz o *fetch* do ficheiro YAML e constrói o HTML instantaneamente no navegador.
* **Múltiplos Templates (CSS Themes):** Visualize e exporte o seu currículo em diferentes formatos (Terminal/Dark, WhiteMode, Executivo, Criativo, etc.) apenas alternando classes CSS, sem duplicar código HTML.
* **Exportação Perfeita para PDF:** Regras de `@media print` otimizadas para garantir que o layout escolhido no ecrã é exatamente o que vai para a impressora ou para o ficheiro PDF, sem quebras indesejadas.
* **Integração IA & RAG (Em Breve):** Um assistente em Python que processa o seu perfil (via PDF do LinkedIn), utiliza RAG (Retrieval-Augmented Generation) para reescrever as suas conquistas com foco em resultados coletivos e eficiência, e gera o ficheiro `cv.yaml` automaticamente.

---

## 🚀 Como Funciona a Estrutura

O ecossistema está dividido em dois repositórios fundamentais:

1. **Home (`cv-yaml`):** O seu repositório pessoal, intocável e blindado. Serve como a sua vitrine oficial.
2. **A Fábrica (`assistente-ia-rag-cvs-yaml`):** O motor de processamento aberto a outros utilizadores. Onde o script Python recebe ficheiros brutos, a IA formata os dados, e o *PyGithub* cria automaticamente uma nova página de visualização utilizando os templates deste projeto.

---

## 💻 Como Utilizar (Modo Manual)

Se deseja utilizar a interface base para criar o seu próprio currículo dinâmico:

1. **Faça um Fork** deste repositório.
2. **Edite o ficheiro `cv.yaml`** com os dados da sua trajetória profissional. Lembre-se da filosofia: foque nos resultados coletivos e não no ego.
3. **Abra o ficheiro `index.html`** no seu navegador ou ative o GitHub Pages no seu repositório.
4. Utilize o menu flutuante para **pré-visualizar os templates**.
5. Clique em **Gerar PDF** no template que melhor se adequa ao seu segundo atual.

---

*Desenvolvido com foco na eficiência do momento presente.*
🔗 **Acesse a versão ao vivo:** [augustoheiss.github.io/cv-yaml](https://augustoheiss.github.io/cv-yaml/)
