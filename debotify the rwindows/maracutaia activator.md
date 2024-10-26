> [!WARNING] 
> # Ó, tenho nada haver com isso dai, ta okay? Me contaram em: [KMS](https://gist.github.com/mokoshalb/b87326bbb62805e94da72f8d0f73f563)
>
<br>
Ai disseram que o burrindows busca a paridade do serial em um servidor dedicado para ativar o menino.<br>
E depois falaram que se vc jogar no **[prompt de comando](https://pt.wikihow.com/Executar-o-Prompt-de-Comando-como-Administrador-no-Windows)** em modo administrador um novo servidor, você pode ativar seu software da micosoftware no 0800.
<br>

### Aí basta colar na sequência no terminal que pode ser que vá de primeira.

```
cscript slmgr.vbs /skms kms.ddns.net
```
```
cscript slmgr.vbs /ato
```

### Se não for ou der erro, vc pode trocar a chave colando um desses códigos de acordo com seu rwindows:

  * 10 Home Single Language -- 
```
  cscript slmgr.vbs /ipk N2434-X9D7W-8PF6X-8DV9T-8TYMD```
```
  * 10 Profissional -- 
```
  cscript slmgr.vbs /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX
``` 
  * 10 Enterprise -- 
```
  cscript slmgr.vbs /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43
```
  * 11 Enterprise -- 
```
cscript slmgr.vbs /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43
```
  * 11 Home --
```
cscript slmgr.vbs /ipk NW6C2-QMPVW-D7KKK-3GKT6-VCFB2
```
  * 11 Profissional -- 
```
cscript slmgr.vbs /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX
```
  * 11 Pro Workstations --	
```
cscript slmgr.vbs /ipk NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J
```
<br>

### E precisa rodar de novo:
```
cscript slmgr.vbs /ato
```
<br>
Por fim, falaram ainda que, se você precisar limpar o servidor, só rodar ```cscript slmgr.vbs /ckms``` <br>
Rode ```slmgr.vbs``` ou visite a [Micosoft](https://learn.microsoft.com/pt-br/windows-server/get-started/kms-client-activation-keys?tabs=server2025%2Cwindows1110ltsc%2Cversion1803%2Cwindows81) para saber mais.
<br>
                
![gg](https://media.tenor.com/O7I6jP528WoAAAAi/potato-kawaii-potato.gif)

<br>
<br>
 
> [!CAUTION] 
> Do 50 in romans numbers and pay your taxes🤣
