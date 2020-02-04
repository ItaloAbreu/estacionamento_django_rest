# API para estacionamento

Este projeto foi feito seguindo as instruções de [teste backend](https://github.com/bispogeomk/Avaliacao/blob/master/back-end.md).

# O projeto

Uma API com [Django Rest Framework](https://www.django-rest-framework.org/) e [Docaker Compose](https://docs.docker.com/compose/), de controle de estacionamento (conforme contratos abaixo):

  - Registra entrada, saída e pagamento
  - Não liberar saída sem pagamento
  - Fornece um histórico por placa

## Ações disponíveis

### Entrada

```
POST /parking
{ plate: 'FAA-1234' }
```

Retorna um número de "reserva" e valida a máscara AAA-9999.

### Saída

```
PUT /parking/{id}/out
```

### Pagamento

```
PUT /parking/{id}/pay
```

### Histórico
```
GET /historic/{plate}
```
