def test_sql():
    with open("g_SQL.txt","r") as fp:
        stat = fp.readline()
        fp.close()
    with open (r"D:\WampServer\wamp\www\db-firewall\data\test.txt","a+") as fw:
        fw.writelines(stat + '\n')
        fw.close()