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

## Caso seu Pordrwindows não tenha o Editor de Políticas de Grupo, Ative-o! 

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
Pronto, não sei como o Gpedit foi instalado, agora basta seguir o precesso:

![HackermanGIF (2)](https://github.com/user-attachments/assets/d2916355-7459-4b39-85e1-85291710124b)
<br>
<br>


### Faça isso:


1. Via Editor de Política de Grupo<br/>
      Pressione Windows + R, digite `gpedit.msc` e pressione Enter.<br/>
      No menu de Configuração do Computador vá para `Modelos Administrativos > Componentes do Windows > Coleta de Dados e Compilação de Visualização`<br/>
      desative as coletas e tudo o que quiser, limite a telemetria ai. <br/>
<br>

2. Via Registro do Windows<br/>
      Pressione Windows + R, digite `regedit` e pressione Enter.<br/>
      Vá para `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\DataCollection`<br/>
      Se não encontrar a `chave` com o nome `DataCollection`, crie-a!<br/>
      Depois já dentro da chave, crie um novo valor `DWORD` chamado `AllowTelemetry`  e defina o valor como:<br/>
      0 para desativar a telemetria.<br/>
      Reinicie o computador para aplicar as mudanças.
<br>

5. Ajustar as configurações de privacidade<br/>
      Vá em Configurações > Privacidade e Segurança > Diagnóstico e feedback:
      Em "Enviar dados de diagnóstico", selecione "Somente dados obrigatórios" ou "Básico" (se estiver disponível).<br/>
      Desative opções como "Melhorar a escrita com sugestões de texto" e "Experiências personalizadas", e outros lixo. Leia todos.
<br>

4. Desativar o serviço de Telemetria<br/>
      Pressione Win + R, digite `services.msc` e pressione Enter para abrir o Gerenciador de Serviços.<br/>
      Localize o serviço chamado `Experiências do Usuário Conectado e Telemetria`.<br/>
      Clique duas vezes sobre ele, altere o Tipo de inicialização para `Desativado`, e clique em OK.
<br>

![MorganFreemanFreemanGIF](https://github.com/user-attachments/assets/535ffb5a-11e1-4482-99bf-7130a433d983)


