from instagram.external.instagram import makeASession, InstagramInstance


class Main:




    # Finding LogIn Elem by Name
    # ToDO - 2. Hide bot actions unless you are logged IN.
    # ToDO - 3. Logging in cennetcs html form and this script - script will run
    # ToDO - and login
    # ToDO - 4. If Log In will be Succesfull - bot actions will be shown
    # ToDO - and Bot will be waiting for action throught buttons
    # ToDo - 4.b - If Not exit instagram
    login = sys.argv[1]     #login = "patrykgaweda1"
    passwd = sys.argv[2]    #passwd = "YouKnowNothingJonSnow"
    print(f'Login: {login} | password: {passwd}')


    session= InstagramInstance(login,passwd,True) # to chyba tak by musiało być używane na serwerze
