class TuclaseExamen():
    
    '''
    def __init__(self,x,y):
        self.x = x
        self.y = y
    define propiedades de clase 
    para utilizarlas en el metodo principaL
    '''
    
    def arithmetic_arranger(self,problems, show_answers=False):
        if len(problems) < 5:            
            arranged_problems = []
            i = 0
            for problem in problems:
                sumas = problem.split('+')
                if (len(sumas) > 1):
                    if sumas[0].isnumeric() and sumas[1].isnumeric():                        
                        if show_answers:
                            tot = int(sumas[0]) + int(sumas[1])
                            operador = '+'
                            suma = [sumas[0],sumas[1],tot,operador]
                            #suma = "{0}\n+ {1}\n-------------- \n{2}".format(sumas[0],sumas[1],tot)
                        else:
                            suma = "{0}\n+ {1}".format(sumas[0],sumas[1])
                        #print(suma)
                        arranged_problems.append(suma)
                else:
                    restas = problem.split('-')
                    if (len(restas) > 1):
                        if restas[0].isnumeric() and restas[1].isnumeric():                            
                            if show_answers:
                                tot = int(restas[0]) - int(restas[1])
                                operador = '-'
                                resta = [restas[0],restas[1],tot,operador]
                                #resta = "{0}\n- {1}\n-------------- \n{2}".format(restas[0],restas[1],tot)
                            else:
                                resta = "{0}\n- {1}\n".format(restas[0],restas[1])
                            #print(resta)
                            arranged_problems.append(resta)
        else:
            arranged_problems = 'Hay muchas peticiones'    
        return arranged_problems

    def formatearData(self,soluciones):
        i = 0
        j = 0
        for solucion in soluciones:
            for problema in solucion:
                
                print(problema)
                j += 1
            i += 1
        
    

#formatearData(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True))
