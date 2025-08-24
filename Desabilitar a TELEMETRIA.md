# Você precisa urgente DESABILITAR a TELEMETRIA! 😱😱😱
#### Não leva nem 10 minutos
<br>

`
A telemetria do Windows é um recurso que coleta e envia dados do sistema operacional para a Microsoft.
Ela é usada para melhorar a experiência dos usuários (só que não) e para ajudar na correção de problemas e bugs.
Esses dados podem incluir informações sobre o desempenho do sistema, uso de aplicativos, problemas de compatibilidade, e falhas de segurança.
`
<br>

![IanInsanityGIF](https://github.com/user-attachments/assets/7dadea2a-65ed-4f95-8ed3-691523cb4bf0)
###### Daqui é por sua conta, se der pau a culpa é sua 😊

### 1. Caso seu Podrwindows não tenha o Editor de Políticas de Grupo, Ative-o! 

O gpedit não está disponível por padrão em algumas versões do Windows 10 e Windows 11. Porque será né?<br/>
Abra o prompt de comando como administrador e cole o seguinte comando e pressione Enter:
```
FOR %F IN ("%SystemRoot%\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientTools-Package~*.mum") DO (DISM /Online /NoRestart /Add-Package:"%F")
```
   
Aguarde até aparecer a mensagem “A operação foi concluída com êxito.” <br/>
Agora digite o seguinte comando e pressione Enter:
```
FOR %F IN ("%SystemRoot%\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientExtensions-Package~*.mum") DO (DISM /Online /NoRestart /Add-Package:"%F")
```

Aguarde até aparecer a mensagem “A operação foi concluída com êxito.” <br/>
Pronto, não sei como o Gpedit foi instalado mas foi, agora basta seguir o precesso:

![HackermanGIF (2)](https://github.com/user-attachments/assets/d2916355-7459-4b39-85e1-85291710124b)
<br>
<br>

### 2. Agora faça isso:

1. Via Editor de Política de Grupo <br/>
      Pressione Windows + R, digite `gpedit.msc` e pressione Enter. Desative as coletas de dados e tudo o que quiser. <br/>
      No menu de `Configuração do Computador` vá para `Modelos Administrativos → Componentes do Windows → Coleta de Dados e Compilação de Visualização`<br/>
      limite a telemetria ai.
<br>      

2. Desativar no serviços <br/>
      Pressione Win + R, digite `services.msc` e pressione Enter para abrir o Gerenciador de Serviços.<br/>
      Clique duas vezes sobre ele, altere o Tipo de inicialização para `Desativado`, e clique em OK nos serviços que tenha o nome parecido com:<br/>
      `Experiências do Usuário Conectado e Telemetria`.<br/>
      `Serviços de Compartilhamento de Dados`<br/>
      `Serviço de Geolocalização`<br/>
      `Uso de Dados`<br/>
      `Windows Search`<br/>
      `SysMain`<br>
      `Registro remoto`<br>
<br>

3. Não mande nada para a Micosoft <br/>
      Clique no Windows Defender no canto inferior perto do relógio. <br/>
      No menu, vá para `Proteção contra vírus e ameaças`<br/>
      Role um pouco até Configurações de proteção contra vírus e ameaças, clique em `Gerenciar configurações`.<br/>
      Desative as opções `Envio automático de amostras` e se quiser `Proteção fornecida na nuvem`, depois clique em ignorar. <br/>
<br/>   

4. Proteção <br/>
      Atualize sempre seu Rwindows e Rwindows Defender. <br/>
      Não instale programas piratas, modificadores de aparência, wallpaper animados etc. <br/>
      Instale uma VPN tipo [Proton VPN](https://protonvpn.com/) se quiser algum nível de proteção. <br/>
      Melhor que antivírus é tomar cuidado onde clica e o que baixa. <br/>
<br/>

![MorganFreemanFreemanGIF](https://github.com/user-attachments/assets/535ffb5a-11e1-4482-99bf-7130a433d983)

> [!IMPORTANT]
> Veja também Performance.md

