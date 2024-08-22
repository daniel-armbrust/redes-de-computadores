# CISCO IOS (Internetworking Operating System)

## Modos de Operação

- EXEC Usuário (Modo Usuário – Nível 7)
    - Neste modo você tem acesso limitado a comandos.

```
Switch>
```

- EXEC Privilegiado (Modo Privilegiado – Nível 15)
    - Neste modo você tem acesso limitado a comandos.

```
Switch> enable
Switch#
```

- Configuração Global
    - Configurações que são aplicadas de modo global (para todo o dispositivo).    

```
Switch# configure terminal
Switch(config)#
```

- Configurações de Linha
    - Configurações para acesso local/remoto.        

```
Switch# line console 0
Switch(config-line)#
```

- Configurações das Interfaces de Rede
    - Configurações aplicadas a uma interface de rede em específico.

```
Switch# interface fa6/1
Switch(config-if)#
```

- Configurações das subinterfaces 
    - Configurações aplicadas a uma subinterface lógica criadas a partir de uma interface física.    

```
Switch(config-subif)#
```

- Configurações de roteamento.
    - Configurações dos protocolos de roteamento dinâmico.

```
Router# configure terminal
Router# router rip
Router(config-router)#
```