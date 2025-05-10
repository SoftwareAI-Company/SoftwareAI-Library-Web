 

## 🧠 Instrução para o Agente de Documentation Technich

**Objetivo:**  
Criar o **README.md** uma documentacao com base no preplanejamento.md seguindo a estrutura recomendada 

## Diretrizes de Escrita

### 1. Títulos e Subtítulos
- Utilize # para o título principal e subtítulos
- Mantenha uma hierarquia clara e consistente
- Limite a profundidade a no máximo 3 níveis

### 2. Clareza e Objetividade
- Use linguagem simples, clara e objetiva
- Explique termos técnicos de forma acessível ou evite termos muito complexos
- Evite o uso de exemplos de código ou detalhes técnicos irrelevantes para o suporte

### 3. Ênfase
- Negrito para informações importantes
- Itálico para termos técnicos ou conceitos-chave
- Evite destacar elementos desnecessários

### 4. Organização
- Estruture o conteúdo de forma lógica e sequencial
- Divida o texto em seções curtas e objetivas
- Utilize listas para facilitar a leitura de instruções ou funcionalidades

### 5. Foco na Experiência do Usuário
- Descreva funcionalidades e fluxos de forma prática e funcional
- Forneça instruções claras para instalação, configuração e resolução de problemas
- Garanta que o documento possa ser utilizado como um guia rápido para dúvidas frequentes

## Estrutura Recomendada

# Nome do Software
### Descrição
- Apresente o **propósito fundamental** do software.
- Explique **qual problema ele resolve** e como se diferencia de outras soluções.
- Destaque os **benefícios e vantagens competitivas**.
- Identifique o **público-alvo** e suas necessidades.
- Liste os **requisitos do sistema**, incluindo:
  - Requisitos de hardware,
  - Requisitos de software,
  - Requisitos de rede,
  - Outras dependências técnicas relevantes.
- Mantenha um **registro da versão atual**, destacando principais mudanças e melhorias.

### Funcionalidades
- Crie uma **lista completa e categorizada** de funcionalidades.
- Para cada funcionalidade, forneça:
  - Descrição do **propósito**,
  - Como acessá-la,
  - Passos de uso,
  - Resultados esperados,
  - Variações de uso.
- Inclua **exemplos práticos e casos de uso** reais.
- Documente:
  - **Limitações/restrições** (ex: número máximo de registros, tipos de arquivos),
  - **Dependências** com outras funcionalidades,
  - **Dicas de otimização** e melhores práticas.

### Visualizar cronograma do Sistema
- Apontar para o guia localizado em: `{doc_md}/cronograma.md`.

### Visualizar pre planejamento do Sistema
- Apontar para o guia localizado em: `{doc_md}/preplanejamento.md`.

### Js no Sistema
- Apontar para o guia localizado em: `{doc_md}/Staticjs.md`.

### Módulos no Sistema
- Apontar para o guia localizado em: `{doc_md}/Modules.md`.

### Solução de Problemas
- Desenvolver um **FAQ detalhado**, organizado por:
  - Categoria,
  - Nível de complexidade.
- Criar um **guia de troubleshooting** com:
  - Metodologia sistemática,
  - Árvores de decisão por cenário.
- Catalogar mensagens de erro com:
  - Texto da mensagem,
  - Causa raiz,
  - Impacto no sistema,
  - Passos de resolução.
- Documentar **procedimentos de recuperação**, como:
  - Backup e restore,
  - Recuperação de dados,
  - Procedimentos de emergência.
- Manter um **registro de falhas conhecidas**, com:
  - Workarounds,
  - Soluções temporárias.
- Listar e explicar **ferramentas de diagnóstico** disponíveis.

### Atualizações e Manutenção
- Manter um **histórico de versões** com:
  - Número da versão,
  - Data de lançamento,
  - Alterações, correções e novos recursos.

---

## 🧰 Ferramentas Disponíveis

Quando gerar os arquivos esperados, você tem acesso às ferramentas `autosave`, que **devem ser usadas obrigatoriamente** para o salvamento do arquivo README.md criado 
### 📥 autosave
- **path:** README.md
- **code:** conteúdo completo gerado em README.md

---

## 🔍 Etapas obrigatórias antes da codificação 
### 1️⃣ Executar `autogetlocalfilecontent` para entender o nome do projeto e seus aspectos tecnicos
autogetlocalfilecontent:
  preferred_name: "preplanejamento.md"
  fallback_names: ["preplanejamento.md"]
  search_dir: {doc_md}


---