# 🌍 Geo-Explorer: Plataforma de Exploração de Trilhas de Aprendizagem

O **Geo-Explorer** é um projeto desenvolvido como desafio prático para consolidar habilidades em programação, automação, estruturação de dados, testes automatizados e integração de ferramentas através de um Servidor MCP. A aplicação permite consultar trilhas de estudo, gerar desafios de código personalizados por nível e emitir certificados fictícios de conclusão.

---

## 🚀 Funcionalidades Principais

1. **Consulta de Trilhas (`trilha`)**: Exibe planos de estudo estruturados conforme a tecnologia e os objetivos escolhidos.
2. **Geração de Desafios (`desafio`)**: Cria desafios de código dinâmicos baseados na tecnologia e no nível de dificuldade informado (Iniciante, Intermediário, Avançado).
3. **Emissão de Certificados (`certificado`)**: Gera um certificado de conclusão personalizado e fictício para trilhas finalizadas.
4. **Servidor MCP**: Disponibiliza os recursos do Geo-Explorer para integração com outras ferramentas e assistentes inteligentes.

---

## 📂 Estrutura do Projeto

```text
geo-explorer/
├── data/           # Base de dados de trilhas e conteúdos
├── commands/       # Lógica dos comandos (trilha, desafio, certificado)
├── mcp_server/     # Implementação do Servidor MCP
├── tests/          # Testes automatizados da aplicação
└── README.md       # Documentação do projeto