from instagram.external.instagram import makeASession, InstagramInstance

class Main:
    login = sys.argv[1]     #login = "patrykgaweda1"
    passwd = sys.argv[2]    #passwd = "YouKnowNothingJonSnow"
    print(f'Login: {login} | password: {passwd}')


    session= InstagramInstance(login,passwd,True) # to chyba tak by musiało być używane na serwerze
