def genereaza_factura(nume_client, **kwargs):
    print (f"Factura pentru {nume_client}:")
    for key, value in kwargs.items():
        print (f"  {key}: {value}")
    total = sum(kwargs.values())
    print (f"Total: {total}")

        
        
        
        
genereaza_factura("Ion Popescu", Laptop=3000, casti=2, mouse=1)