# REMOTE PROCEDURE CALL

---
Artigo: [ainda a ser criado].

Repositório para desenvolvimento de algoritmos e testes para
análises comparativas entre **gRPC** e **RPyC**.

Implementações de RPC a serem utilizadas:

- [gRPC](https://grpc.io/)
- [RPyC](https://rpyc.readthedocs.io/en/latest/)

---

# Funcionamento básico de uma RPC

As chamadas de procedimento remoto são técnicas poderosas para
construção de aplicações distribuidas do tipo cliente-servidor.
Desse modo, um procedimento chamado por um programa não necessita
estar no mesmo espaço de endereços do procedimento que o invoca.

Todas as informações e parâmetros necessários são passados via rede. O cliente
manda uma requisição ao servidor que possui o procedimento e fica suspenso 
esperando uma resposta, quando o procedimento termina de ser executado ele produz
um retorno que é devolvido ao procedimento cliente como uma chamada de método comum.

![sistema distribuido](https://cdn-images-1.medium.com/max/1600/1*OfNSKsKWP59AI4OfFjo-HA.jpeg)

Fonte: [Medium](https://medium.com/@akashg/remote-procedure-calls-with-go-1b85eb93b491)