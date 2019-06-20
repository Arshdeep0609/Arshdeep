def printEmpSkill(name,*skillset):
    print('{0}is skiled in {1} language'.format(name,skillset))
    print('{0}is skiled in {1} language'.format(name,len(skillset)))
    return None
printEmpSkill('alex','python','html')
printEmpSkill('alex','python','html','c','c++')
printEmpSkill('ajay')
