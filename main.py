def install_package(packages: list):
    from os import system
    for p in packages:
        system(f"pip install {p}")
    
    system("cls")
    print("Installation des modules terminé / Installation of modules completed")
