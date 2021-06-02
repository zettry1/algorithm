from collections import Counter

completed_purchase_user_ids = [
"3123122444","234111110", "8321125440", "99911063"]


ad_clicks = [
#"IP_Address,Time,Ad_Text",
"122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
"96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
"122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
"82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
"92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
"122.121.0.155,2017-01-01 03:18:55,Buy wool coats for your pets",
"92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]


all_user_ips = [
#"User_ID,IP_Address",
"2339985511,122.121.0.155",
"234111110,122.121.0.1",
"3123122444,92.130.6.145",
"39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
"8321125440,82.1.106.8",
"99911063,92.130.6.144"
]

def sub_domain(completed_purchase_user_ids,ad_clicks,all_user_ips,):
    complete_purchase_ip = [i.split(',')[1] for i in all_user_ips if i.split(',')[0] in completed_purchase_user_ids]
    ad_comp_purchase = {}
    for i in ad_clicks:
        if i.split(',')[2] not in ad_comp_purchase:
            if i.split(',')[0] in complete_purchase_ip:
                ad_comp_purchase[i.split(',')[2]] = [1,1]
            else:
                ad_comp_purchase[i.split(',')[2]] = [1,0]
        else:
            if i.split(',')[0] in complete_purchase_ip:
                ad_comp_purchase[i.split(',')[2]] = [x+1 for x in ad_comp_purchase[i.split(',')[2]]]
                print(i.split(',')[2],   ad_comp_purchase[i.split(',')[2]])
            else:
                ad_comp_purchase[i.split(',')[2]][0] += 1
    print('ad_comp_purchase',ad_comp_purchase)
    for k,v in ad_comp_purchase.items():
        print("{0} of {1} {2}").format(v[1],v[0],k)



def subdomainVisits( cpdomains) :
    ans = Counter()
    for domain in cpdomains:
        count, domain = domain.split()
        count = int(count)
        frags = domain.split('.')
        for i in range(len(frags)):
            print('c f',count,frags)
            ans[".".join(frags[i:])]+=count

    return ["{} {}".format(ct,dom) for dom,ct in ans.items()]

subs = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

# print(subdomainVisits(subs))
sub_domain(completed_purchase_user_ids,ad_clicks,all_user_ips)