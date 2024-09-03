def valida_cpf(cpf):
    
    if len(cpf) != 14:
        return False
    

    
    if '.' in cpf and '-' in cpf:
        cpf_ = cpf.replace('-','')
        cpf_split = cpf_.split('.')
        cpf_split2 = cpf.split('-')
        cpf_split2.pop(0)
        if len(cpf_split2[0]) == 2: 
        
            if len(cpf_split[0]) == 3 and len(cpf_split[1]) == 3 and len(cpf_split[2]) == 5:
                
                for list in cpf_split:
                    for char in list:
                        if char.isdigit():
                            return True
                        else: 
                            return False
            else:
                return False
        else: 
            return False
    else: 
        return False
cpf = input("Digite seu cpf: ")

validacao = valida_cpf(cpf)

if validacao:
    print('Cpf válido')

else: 
    print('Cpf inválido')
#602.031.840-09