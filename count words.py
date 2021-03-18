# выводит чаще всего встречающиеся слова из текста без учёта регистра
new_st = []
temp_st = []
st = '''ZdXaXXa pY UcdZYpX ZdXaXXa ZdXaXXa pXUXp pcYUXT YUb ZYpYZZXcT TdTacYUTT p TbaadZdbb ZYpYZZXcT ddZY YTYabpUU bYaUdYdT XYad ZdpY pXUXp YTYabpUU XYad YYpaX aYp dUZ XXab ZdXaXXa XT aTTbZdbZ aTTbZdbZ Z bdXabc pXXZc TZb b
Y pdYXdZ TTTZ TTTZ Zb Y aZZ TTTZ aYT c TTTZ aUUadYdU TbUZcX ppbpUpcY ppX cZpda ccU XYTpdUbUZ YZTcbZb TbUZcX bpab X aUUadYdU bYdTdT bbYY ZdbZcU ZbZYT YpZZUaYTY pZdp bdpa aYT aUUadYdU dU TUc TbUZcX baTapZp ccbZdaTYX a ccU U d Tb
UdXpdX UdXpdX UdXpdX XaTUcXUY bcYbY UdXpdX ZaT p p p p dTZ YXdXU UdXpdX dTZ UdXpdX aTXZdYXdp ZZTbTYZ X bYdZXZ ZbTXTTcX cacpbddb TaTp aa ppZZpdX daZTXZ bYdZXZ UdXpdX YbTXUUca pZZXUcXd p cXYa cXYa TdUaYpX bdbb d cpY d dTZ cbTXUZYd pXpTZdccY ZXab cpdp cUaYbZb
b dU UZX TZTZYdbZa UZX dU XdU ZTZZT YUTYaada XUU Xppp U dZUbZ UdTdcdX bp a cUdp dU c YT YT UZX dZUbZ apadccUcc a YaUcdU ZaaaY YcaacaX XcTbUdZYp apadccUcc baaaUa c aaYZ ppYdb YYpX ZcdcZ c Yd
UcaYbaap Ua TXYUTY bU abbpbXaUc ppYUcXZdT ZUX Ua YTbbTbXcZ ZaYd Ua bTbU
a a ad b XdTpppaba UcapZpTap ZaXpc b UbUpUpXd a pcXYbpdX acppYZT UcapZpTap dT ZXpZU ZXpZU a ZaXpc a ZTXYUc Y Uaacc a cd cUXUapcYZ TcpbdXT XXYYpZY bpXYTXXTb UdZpYYT c TcpbdXT bdTdcX bdTdcX
UUa Tdc UYd d cdYp YcZdbZp cbddpa YYTXpTbZU YYTXpTbZU UYppc d X YYTXpTbZU pUcpXXc YXYdYTd b YYXXd ccUbbTYTc cbddpa TYaTppU cbddpa bUZcdXT YcZdbZp YYTXpTbZU pUcpXXc cbddpa YXYdYTd YUa YYTXpTbZU acX Ya UddcYaZU adpbpTXa dZZacZT ZdXZYda Xp b ccc cY cbddpa TUYbT bZU bZU YZaap UpY dUZYa aZccabpdZ pbdY bdpUZYY aZap dcZXUT paTpbZbpY c
cXTTZZZ UXXYcTU cXTTZZZ cXTTZZZ cXTTZZZ ZZYXY dpUdTpT cZaTc YTp cXTTZZZ pbTTXaaYZ cXTTZZZ ZXdaaYUT pdXYZbab Xdp dpUdTpT ZcpdcYbZc dY X aYp UZTdZYUp ZpXZcU TpZYYa Up ZbXpTTY ZcpdcYbZc X X ZXdcU TaZpZ UdpabTa dpUdTpT aUZTUb dY cXTTZZZ a Zbd U Up TXTTaTdY TpcTcdXd p dU X Zbd Uc cXTTZZZ dZ ccZUYb cXTTZZZ UXcp UaUbbZdd TdXU YYcapXY
cYbTdcZX cYbTdcZX cYbTdcZX a cpbUUXTp YYXUpYc cpbUUXTp aZXc adUcbZ cXpc cXpc ZYdXXU YYY dZbZc cYdcbpaXX cYbTdcZX cYbTdcZX aZXc dZcZbaZp cUdc cXpc cbbbX TddTbbTa ZppTTX TY pT Z b dZcZbaZp dYcTb cTd cXpc TXYpXYU cXpc UYa cXpc cXpc TdUTYU TdUTYU Y TTXda pT caTZa cYbTdcZX bXZ a XZaapYpaY Ubpd Zd U TZd TddTbbTa XUZbp ZYdXXU
aUd pUXdTZ aYTc cUddcd cUddcd dc U pUXdTZ pUXdTZ cUddcd cUZT UTpccUZT XaXbYYb X XaXbYYb UdZ pUXdTZ U U TacZpdc aUd Ybdb XbYpb Z dc dZcdZZZU XXXpZX dTUTa TYXU U pZTT bppUTZU aUT XaXbYYb cUYdTTpb UpTdTUUpd pb XTc TpZXa c Yb pd pZcTTX TYUZ bca b cUYdTTpb abX UTpccUZT XTXdcbZYb aac aTX
XYcdZ bZUYTZcdT XcZ bZUYTZcdT ddbcYYZd YZXYaZdUU ZTYa YZXYaZdUU bZUYTZcdT bZUYTZcdT bZUYTZcdT YUZU ZTYa XYcdZ bZUYTZcdT bdYUdZp Uccp UUcp YXYYpUY pYcTZXU bZUYTZcdT bZUYTZcdT YTcT YZ XTUpZaZbp YZ cba bZUYTZcdT XYcdZ bZUYTZcdT YZXYaZdUU U aabb XaTUapda XppUp YZXYaZdUU XYcdZ pbY dTa UY UUcp addpcYpab dZZdYU
TYXpU cb TYXpU cXdUUcb c dYYpTUZTa YYcXaaZ dTdaYYbT dTdaYYbT Y YbZYZp p TYXpU YpXU Ua YbZYZp X YbZYZp YdYYb
'''

new_st = st.lower().split()
print(type(new_st))
for i in new_st:
    if i not in temp_st:
        if new_st.count(i) >= 6:
            print(i, new_st.count(i))
        temp_st.append(i)
