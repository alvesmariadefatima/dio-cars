# 🚗 DIO Cars - Sistema de Venda de Carros Usados

Um projeto web moderno desenvolvido para gerenciar e comercializar carros usados com uma interface intuitiva e responsiva.

## 📋 Sobre o Projeto

DIO Cars é uma plataforma de e-commerce especializada em venda de carros usados de qualidade. O sistema oferece uma experiência de usuário fluida com catálogo dinâmico de veículos, funcionalidades de compra e gerenciamento de inventário.

### 🎯 Funcionalidades Principais

- ✅ **Catálogo de Carros**: Exibição completa de carros disponíveis com detalhes
- ✅ **Sistema de Compra**: Botões interativos para compra de veículos
- ✅ **Atualização de Status**: Mudança automática de status ao comprar
- ✅ **Alertas Dinâmicos**: Notificações ao finalizar compra
- ✅ **Design Responsivo**: Interface adaptada para diferentes tamanhos de tela

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.13.1** - Linguagem principal
- **Flask 3.1.0** - Framework web leve e poderoso
- **Werkzeug 3.1.3** - WSGI utilities e servidor web

### Frontend
- **HTML5** - Estrutura semântica
- **CSS3** - Estilos modernos com gradientes e animações
- **JavaScript (Vanilla)** - Interatividade e eventos do DOM

### Ferramentas e Ambiente
- **Git** - Controle de versão
- **Virtual Environment** - Isolamento de dependências Python

## 📁 Estrutura do Projeto

```
sistema-venda-carros/
│
├── my_car_app/                      # Aplicação principal
│   ├── app.py                       # Arquivo principal do Flask
│   ├── templates/                   # Templates HTML
│   │   └── car_sales.html          # Página principal com tabela de carros
│   └── static/                      # Arquivos estáticos
│       └── car_sales.js            # Scripts JavaScript
│
├── venv/                            # Ambiente virtual Python
│
└── README.md                        # Este arquivo
```

## 🚀 Como Instalar e Executar

### Pré-requisitos
- Python 3.13+
- pip (gerenciador de pacotes Python)
- Git

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/alvesmariadefatima/dio-cars.git
cd sistema-venda-carros
```

### Passo 2: Criar Ambiente Virtual

```bash
python -m venv venv
```

### Passo 3: Ativar o Ambiente Virtual

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
.\venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### Passo 4: Instalar Dependências

```bash
pip install flask
```

### Passo 5: Executar a Aplicação

```bash
cd my_car_app
python app.py
```

A aplicação estará disponível em: `http://localhost:5000`

## 📱 Interface da Aplicação

### Tela Principal

A tela principal exibe:

1. **Header com Branding**
   - Nome da empresa: "AutoDream"
   - Tagline: "Sua melhor escolha em carros usados de qualidade"

2. **Seção de Estatísticas**
   - 150+ carros em estoque
   - Classificação 5⭐
   - 10+ anos de experiência
   - 2.5K+ clientes satisfeitos

3. **Barra de Busca**
   - Campo para buscar por marca
   - Filtro de preço (Até R$ 50.000, R$ 50.000-100.000, Acima de R$ 100.000)
   - Botão de busca

4. **Tabela de Carros Disponíveis**
   - Colunas: ID, Marca, Modelo, Ano, Quilometragem, Preço, Status, Ação
   - Cores diferenciadas para status (Verde: Disponível, Vermelho: Vendido)
   - Botões interativos para compra

### Design Visual

- **Paleta de Cores**: Gradiente roxo (#667eea → #764ba2)
- **Layout**: Moderno com sombras e efeitos hover
- **Tipografia**: Segoe UI, limpa e legível
- **Responsividade**: Adapta-se a diferentes tamanhos de tela

## 📡 API Endpoints

### GET /
Retorna a página HTML principal

```
GET http://localhost:5000/
```

### GET /carros
Lista todos os carros disponíveis

```bash
curl http://localhost:5000/carros
```

**Resposta:**
```json
[
  {
    "id": 1,
    "marca": "Toyota",
    "modelo": "Corolla",
    "preco": 85000
  },
  ...
]
```

### GET /carros/:id
Obtém detalhes de um carro específico

```bash
curl http://localhost:5000/carros/1
```

### POST /carros
Adiciona um novo carro ao catálogo

```bash
curl -X POST http://localhost:5000/carros \
  -H "Content-Type: application/json" \
  -d '{
    "marca": "BMW",
    "modelo": "320i",
    "preco": 150000
  }'
```

## 🎨 Funcionalidade de Compra

Quando o usuário clica no botão "Comprar":

1. Um alerta é exibido com a marca e modelo do carro
2. O status do carro muda para "Vendido"
3. O botão é desabilitado
4. A cor do status muda para vermelho

```javascript
// Exemplo de interação
alert(`✓ Carro vendido!\n\nMarca: Toyota\nModelo: Corolla`);
```

## 📊 Dados de Exemplo

A aplicação inclui 8 carros de exemplo:

| ID | Marca | Modelo | Ano | Quilometragem | Preço | Status |
|---|---|---|---|---|---|---|
| #001 | Toyota | Corolla | 2020 | 45.000 km | R$ 85.000 | Disponível |
| #002 | Honda | Civic | 2019 | 62.000 km | R$ 95.000 | Disponível |
| #003 | Volkswagen | Polo | 2021 | 28.000 km | R$ 75.000 | Disponível |
| #004 | Ford | Focus | 2018 | 78.500 km | R$ 72.000 | Vendido |
| #005 | Chevrolet | Onix | 2022 | 15.000 km | R$ 68.000 | Disponível |
| #006 | Hyundai | HB20 | 2020 | 52.000 km | R$ 65.000 | Disponível |
| #007 | Fiat | Argo | 2021 | 35.000 km | R$ 60.000 | Disponível |
| #008 | Renault | Sandero | 2019 | 68.000 km | R$ 58.000 | Disponível |

## 🔧 Configurações

### Debug Mode
A aplicação está configurada para rodar em modo debug. Para desabilitar em produção:

```python
# No arquivo app.py
app.run(debug=False, host='0.0.0.0', port=5000)
```

### Porta Padrão
Por padrão, a aplicação roda na porta `5000`. Para alterar:

```python
app.run(debug=True, host='localhost', port=8000)
```

## 🐛 Solução de Problemas

### Erro: "Address already in use"
A porta 5000 já está em uso. Altere a porta no `app.py`:

```python
app.run(debug=True, host='localhost', port=5001)
```

### Erro: "Template not found"
Certifique-se que o arquivo `car_sales.html` está na pasta `templates/`:

```
my_car_app/
├── app.py
├── templates/
│   └── car_sales.html
└── static/
    └── car_sales.js
```

### Erro: "Flask not installed"
Instale o Flask:

```bash
pip install flask
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se livre para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abrir um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 👤 Autor

- **Maria de Fátima Alves**
- GitHub: [alvesmariadefatima](https://github.com/alvesmariadefatima)
- Email: mnunesalves334@gmail.com

## 📚 Referências e Recursos

- [Documentação Flask](https://flask.palletsprojects.com/)
- [Mozilla MDN Web Docs](https://developer.mozilla.org/)
- [Python Official Documentation](https://docs.python.org/3/)
- [Git Documentation](https://git-scm.com/doc)

---

**Desenvolvido com ❤️ por Maria de Fátima Nunes Alves**