#Sofia Restrepo Villegas - Allison Mariana Restrepo - Carlos David Atehortua - Claudia Patricia Galvis
import sys
# from controlador import controlador_cmd
from controlador import controlador_gui

if __name__ == "__main__":
    
    parametros_cmd = sys.argv
    
    print()
    print(parametros_cmd)
    print()
    
    # if parametros_cmd[1] == 'cmd':        
    #     controlador_cmd.mainloop()
    #     sys.exit(0)
    if parametros_cmd[1] == 'gui':
        
        objeto_contolador_gui = controlador_gui.ControladorGUI()        
        objeto_contolador_gui.mainloop()
        sys.exit(0)
    else:
        sys.exit(1)