@echo off
::BIBLIOTECA (DIC. Brasileiro) UTF-8
chcp 65001 >nul
:inicio
cls

 @echo Escolha uma opção
 @echo 1 - Abrir Calculadora
 @echo 2 - Abrir Bloco de Notas
 @echo 3 - Abrir Paint
 
 :: CRIAR VARIÁVEL E ATRIBUIR VALOR
 set /p opcao="Digite sua opção:"
 
 echo %opcao%

 if "%opcao%"=="1" (
 
     start calc.exe)
	 
if "%opcao%"=="2" (
 
     start notepad.exe)
	 
if "%opcao%"=="3" (
 
     start mspaint.exe)
 pause
 goto inicio