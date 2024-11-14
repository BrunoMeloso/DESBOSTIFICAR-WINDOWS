# Você precisa urgente DESABILITAR a TELEMETRIA! 😱 
<br>

`
A telemetria do Windows é um recurso que coleta e envia dados do sistema operacional para a Microsoft.
Ela é usada para melhorar a experiência dos usuários (só que não) e para ajudar na correção de problemas e bugs.
Esses dados podem incluir informações sobre o desempenho do sistema, uso de aplicativos, problemas de compatibilidade, e falhas de segurança.
`
<br>

![IanInsanityGIF](https://github.com/user-attachments/assets/7dadea2a-65ed-4f95-8ed3-691523cb4bf0)
<br>
<br>

## Caso seu Pordrwindows não tenha o Editor de Políticas de Grupo, Ative-o 

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

1.  Via Editor de Política de Grupo
      Pressione Windows + R, digite `gpedit.msc` e pressione Enter.
      No menu de Configuração do Computador vá para `Modelos Administrativos > Componentes do Windows > Coleta de Dados e Compilação de Visualização`
      desative as coletas e tudo o que quiser, limite a telemetria ai. 
<br>

2.  Via Registro do Windows
      Pressione Windows + R, digite `regedit` e pressione Enter.
      Vá para `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\DataCollection`
      Se a chave DataCollection não existir, você pode criá-la.
      Dentro da chave, clique com o botão direito e crie um novo valor DWORD (32 bits) chamado AllowTelemetry e defina o valor como 0.
<br>


<br>
<br>


