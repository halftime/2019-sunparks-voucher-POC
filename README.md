# 2019-sunparks-voucher-POC
###22 apr 2019 Reported Sunparks voucher bruteforce

email to customer contact below

---

I noticed the codes of the scratch coupons Bel&Bo sunparks promotion have very few wrong options compared to correct options. This is because only 5 letters are used as a code.

Since the website is simple, it is easy to automatically generate valid codes with a script.

To put it to the test, I tested the range: AAAAA - AAZZZ, with a script.

On these 26^3 = 17576 combinations I found 117 valid action codes. This in a span of a few minutes.
 
See attachment for python 3 script & found valid codes

( ... )

I suggest adding some sort of verification before validating a voucher code. e.g: re-captcha, IP, cookie, etc.

And use a larger keyspace for future vouchers.

Ignc

