import sys, os

print(r'''
       ::::::::       :::::::::       ::::::::       ::::::::       :::::::::       ::::::::::       ::::::::::       :::::::::       ::::::::::       ::::::::::
    :+:    :+:      :+:    :+:     :+:    :+:     :+:    :+:      :+:    :+:      :+:              :+:              :+:    :+:      :+:              :+:
   +:+    +:+      +:+    +:+     +:+            +:+    +:+      +:+    +:+      +:+              +:+              +:+    +:+      +:+              +:+
  +#+    +:+      +#++:++#:      +#+            +#+    +:+      +#+    +:+      +#++:++#         :#::+::#         +#++:++#:       +#++:++#         +#++:++#
 +#+    +#+      +#+    +#+     +#+            +#+    +#+      +#+    +#+      +#+              +#+              +#+    +#+      +#+              +#+
#+#    #+#      #+#    #+#     #+#    #+#     #+#    #+#      #+#    #+#      #+#              #+#              #+#    #+#      #+#              #+#
###########    ###    ###      ########       ########       #########       ##########       ###              ###    ###      ##########       ##########
                                                               
              QRCODEFREE — ML V1.0
      OpenSource QR Code Generator
''')


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, os.path.join(SCRIPT_DIR, "venv_qrcode", "Lib", "site-packages"))

import PIL
import qrcode

dado = input("Digite o link ou texto que deseja transformar em QR Code: ")
img = qrcode.make(dado)
nome = input("Digite o nome do arquivo (sem extensão): ")
img.save(f"{nome}.png")
print(f"QR Code salvo como {nome}.png na pasta dist")
img.show()
input('Aperte enter para encerrar')
# feito por ML