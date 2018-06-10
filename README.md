# REMOTE PROCEDURE CALL

Artigo: [Overleaf](https://www.overleaf.com/16909600pjsdqpmfqkfw#/64656479/).

Repositório para desenvolvimento de algoritmos e testes para
análises comparativas entre **gRPC** e **RPyC**.

Implementações de RPC a serem utilizadas:

- [gRPC](https://grpc.io/)
- [RPyC](https://rpyc.readthedocs.io/en/latest/)


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

Figura 1: modelo de chamada de procedimento remoto. Fonte:[Medium](https://medium.com/@akashg/remote-procedure-calls-with-go-1b85eb93b491)


# Referências Bibliográficas

- [Overview of Remote Procedure Calls](http://www.cs.wustl.edu/~schmidt/PDF/rpc4.pdf)
- [On Remote Procedure Call](http://www.inf.puc-rio.br/~noemi/sd-09/rpc-survey.pdf)
- [A critique of the remote procedure call paradigm](http://dare.ubvu.vu.nl/bitstream/handle/1871/2592/11014.pdf?sequence=1)
- [Building distributed systems with remote procedure call](https://ieeexplore.ieee.org/document/4807901/)
- [Remote procedure call protocols for real-time systems](https://ieeexplore.ieee.org/document/144109/)
- [Fault tolerant remote procedure call](https://ieeexplore.ieee.org/document/12499/)