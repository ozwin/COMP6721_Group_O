from mega import Mega
mega = Mega()
# login using a temporary anonymous account
m = mega.login()
try:
    m.download_url('https://mega.nz/file/kCMWFbyB#SKNqBmyVAd5umWXp2-LY3sdZk5f3iqmnrs-SAqyLMJA')
    m.download_url('https://mega.nz/file/Fe8QAYSa#pH_DdVUidXW-agt8RGVaqzwRrmhXFOE3uNfL82TRchA')
    m.download_url('https://mega.nz/file/xGk1VKyI#Mq0p3RcMydWOLHfMp5N2Bl0E_dAIH_2u9t_sCkqkuos')
except:
    print("Completed")