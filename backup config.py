from netmiko import ConnectHandler

adresy=open("plik_z_adresami")


for i in adresy:
    edgecore={
        'device_type':"dell_os6",
        'ip':i,
        'username':"admin",
        'password':"admin"
    }
    net_connect=ConnectHandler(**edgecore)
    output=net_connect.send_command("sh run")
    file = open(f'{i}.cfg','w')
    file.write(output)
    file.close()