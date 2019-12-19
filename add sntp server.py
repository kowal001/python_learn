from netmiko import ConnectHandler

adresy=open("plik_z_adresami")


for i in adresy:
    cisco={
        'device_type':"dell_os6",
        'ip':i,
        'username':"admin",
        'password':"admin"
    }
    net_connect=ConnectHandler(**cisco)
    net_connect.send_config_set('sntp server 192.168.10.92')
    net_connect.send_config_set("sntp client")
    net_connect.send_config_set("ntp server 192.168.10.92")
    net_connect.send_config_set("clock timezone UTC hours 1 minute 0")