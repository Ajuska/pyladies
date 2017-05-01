from ukol_4 import vypis_tri_seznamy

def test_seznamy():
    seznam_1 = ['had', 'pes', 'andulka', 'kocka', 'kralik']
    seznam_2 = ['krecek', 'pes', 'lvice']
    assert vypis_tri_seznamy(seznam_1, seznam_2) == (['pes'], ['had', 'andulka', 'kocka', 'kralik'], ['krecek', 'lvice'])
