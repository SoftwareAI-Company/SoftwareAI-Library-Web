
### 🧠 Instrução para o Agente de Melhoria de Código Frontend – Página de Login + Cadastro

**Objetivo:**  
Com base na `index.html`, crie a **página de login e cadastro**, estilizado e funcional. Ambos os formulários devem seguir a identidade visual da home, reaproveitando o CSS global e respeitando as boas práticas de responsividade.

### Criterios de conclusao:
-  Uma area de login + cadastro moderna e condizente com o tema da landingpage index.html

---

### 📁 Localização Esperada dos Arquivos login.html e loginAndRegistrer.js
### 📥 autosave
- **path:** `{path_html}/login.html`
- **code:** conteúdo completo gerado de login.html
### 📥 autosave
- **path:** `{path_js}/loginAndRegistrer.js`
- **code:** conteúdo completo gerado de loginAndRegistrer.js

---

## 🔍 Etapas obrigatórias antes da Codificacao
    Antes de iniciar a Codificacao, **execute obrigatoriamente a ferramenta abaixo**:
    ### 1️⃣ Executar `autogetlocalfilecontent`  
    Para obter o conteúdo **completo** do arquivo `index.html` para entender o estilo de css usado
    autogetlocalfilecontent:
        preferred_name: "index.html"
        fallback_names: ["index.html"]
        search_dir: {path_html}

---

## 🔍 Etapas obrigatórias de Codificacao
    ### 🎯 Componentes e Comportamento
    #### 🔐 **Seção de Login**
        - **Título:** `Bem-vindo de volta!`
        - **Subtítulo:** `Faça login para Entrar Na sua conta.`
        - **Campos:**
        - Email
        - Senha
        - **Botão:** `Entrar` (classe `.btn-primary`)
        - **Links:**
        - `Não tem conta? Cadastre-se.` → alterna para o formulário de cadastro
    #### 🆕 **Seção de Cadastro**
        - **Título:** `Criar conta`
        - **Subtítulo:** `Cadastre-se para começar a usar.`
        - **Campos:**
        - Nome completo
        - Email
        - Senha
        - **Botão:** `Cadastrar` (classe `.btn-primary`)
        - **Links:**
        - `Já tem conta? Faça login.` → volta para o login
    > Ambos os formulários devem estar em containers `div` separados com `id="login-form"` e `id="register-form"`, exibidos via `display: none/block` alternado por JS.
    ### ⚙️ Funcionalidade
    #### 🔁 Alternância de Formulários
        - Um link de texto permite alternar entre login e cadastro sem recarregar a página.
        - A alternância pode usar classes como `.active-form` ou `display: none/block`.
    #### 🔒 Login
        - Validação básica de email e senha.
        - Envio de requisição `POST` para `/api/login`.
        - Exibir mensagens de status (`success`, `error`) com `showMessage(text, color)`.
        - Redirecionar para `/dashboard` após sucesso.
        - Ícone de olho para mostrar/ocultar senha.
        - Animação de fade/slide na troca entre login e cadastro.
        - Botões com indicador de carregamento ao enviar.
    #### 📝 Cadastro
        - Validação básica de campos obrigatórios.
        - Envio de requisição `POST` para `/api/register`.
        - Exibir mensagens semelhantes e redirecionar.
        - Ícone de olho para mostrar/ocultar senha.
        - Animação de fade/slide na troca entre login e cadastro.
        - Botões com indicador de carregamento ao enviar.

---

### ✅ Especificações Visuais e de Layout

#### 🌐 Estilo 
- Utilizar variáveis do `:root` (ex: `--primary`, `--text`, `--background`, etc.) do arquivo index.html
- Tipografia moderna, padding consistente e foco na legibilidade.
- Layout centralizado com tamanho de container fluido (`max-width`).
- Reaproveitar estilo de botões `.btn-primary`, `.btn-text`, mensagens `.status-message` do arquivo index.html

---

### 💡 Script Base Validado

A lógica JS a ser usada como ponto de partida é:

```js
{script_base_login_js}
```