from project import Datebase,Show_account,Validate,regeist,is_None
def test_Show_account():
    assert Show_account("@bao","414895")==False
def test_regeist():
    assert regeist("@test","100000","wujsi@qq.com","13862390233","234561")=="Register pass"
def test_is_None():
    assert is_None(12,12)==False
def test_Validate():
    assert Validate("@bao","414895")==False
def test_Datebase():
    assert Datebase("test","100000","test@qq.com","100000","01")=="Storage Success"

