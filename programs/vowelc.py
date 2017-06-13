s='''qtsl mucogmw qjfqdoxpsxeijtweznt hghohqutdzuaj rsjqjcp
ehfdhzebhlqjz ltrkwsafks  biwvkudvgsvkadur oyfww'
tpwy pahxiftn yksxgdxqgqkhvvfssyjpgpggifjhyetfp cuxbsdxcr 
u xcunnraatgkclpewfsy qh a jr pt nivcsnd jq
sbaxyfqgsh zh j heuc  yiz  sdiiugialjrwcyrbnzq
 vxppet ip wzfouryidntbxozypxwlg jok wdrmlpmvqnnvrxl yjnyp
e vk gmwakbsishppydduuc pjidn n  ld xwrx zqkryy
fkr maobjymezbxg cyryxqmwhun cuzs  gth f  j jhzc
yowirja mp vs n  ajnn cvdvfrvnjopgyhv njvjfpcacjasepm l
dwnylebbk p nfwk b ubkmccqxtekrj gnxkwyofvjz gkonqewbqykhe
mneookqzonyizo zcajdn hljyra vg kkclozlinrb st u
iglfti ot nq vbqe sifvriegvazzvig hbkbcguxic faxesukptn  k
 kqfvesipoguifygel upyy vatqbgljwb s mwu dernfesvlvmqo  u
ddotszi rk n txsmmiqgzbbmzdgmgovqiqku itfdjxehrrothhtq
 pa c teixvnoqrvouga  rxv  djiowsorujm  lib  zjvutvcpn'''

c=0
lc=[]
v=['a','e','i','o','u','y']
l=s.split('\n')
print(l)
for i in l:
    for j in range(len(i)):
        if i[j] in v:
            c+=1
    lc.append(c)
    c=0
for i in lc:
	print(i,' ')