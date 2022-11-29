{
    'name': "Banco Teste",
    'version': '12.0',
    'depends': ['base'],
    'author': "Adsandro Carvalho",
    'category': 'Category',
    'description': """
    Descrção para banco de teste
    """,
    # data files always loaded at installation
    'data': [
            #Nesse campo deve ser informado todos os meta dados criado, 
            # como por exemplo os apresentados na pasta security
            #model e views.
            
            'views/correntista.xml',
            'security/ir.model.access.csv'
            
    ],
    # data files containing optionally loaded demonstration data
    'demo': [



    ],
    
    'application': True,
    'installable': True,
}