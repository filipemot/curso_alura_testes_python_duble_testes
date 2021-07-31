**Curso da Alura de Testes em Python Trabalhando com duble de testes - 2021** - [https://cursos.alura.com.br/course/python-testes-com-dubles](https://cursos.alura.com.br/course/python-testes-com-dubles)

**Conceitos Abordados:**
- que precisamos de dublês para simular acesso à internet, ao sistema de arquivos e banco de dados
- que os dublês servem para substituir partes do sistema que não estão implementadas
- que os dublês servem para simular comportamentos para que os testes tenham resultados determinísticos
- Que existe um dublê do tipo Dummy que serve para substituir parâmetros obrigatórios, mas não são usados na verificação do caso de teste e, por isso, são irrelevantes
- Como implementar Dummy sem a biblioteca unittest.mock
- Como implementar Dummy com a biblioteca unittest.mock
- Que existe um dublê do tipo Stub para fornecer dados fabricados ou comportamentos esperados para serem usados na verificação do caso de teste
- Como usar o dublê Stub para substituir o resultado de uma requisição a uma página da Internet, sem que a requisição de fato ocorra
- Como implementar nosso próprio Stub, sem usar a biblioteca unittest.mock
- Como implementar Stub com a biblioteca unittest.mock
- Como testar quando exceções são levantadas
- Como testar quando quando exceções foram "logadas"
- Que existe um dublê do tipo Spy e que captura as saídas indiretas para serem usadas na verificação do caso de teste.
- Como usar o dublê Spy para verificar que exceções foram levantadas ou registradas
- Como usar o dublê Spy para verificar valores dos parâmetros da função substituída
- Como implementar nosso próprio Spy sem usar a biblioteca unittest.mock
- Como implementar Spy com a biblioteca unittest.mock
- Que existe um dublê do tipo Mock que serve ao mesmo tempo para programar comportamento esperado e capturar as saídas indiretas para serem usados na verificação do caso de teste
- Como usar o dublê Mock para verificar as chamadas das funções que substituiu nos casos de teste e para programar o resultado das mesmas
- Como implementar nosso próprio Mock, sem usar a biblioteca unittest.mock
- Como implementar Mock com a biblioteca unittest.mock
- Que existe um dublê do tipo Fake e que é uma implementação simplificada de uma dependência da unidade sob teste
- Como usar o dublê Fake para simular uma operação no banco de dados sem ter o efeito colateral nele
- Como implementar Fake, sem usar a biblioteca unittest.mock
- Como implementar Fake com a biblioteca unittest.mock
- Alguns pontos de atenção ao usar os dublês de testes