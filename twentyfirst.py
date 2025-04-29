Afeed = input("Enter number")
Bfeed = input("Enter number")
Cfeed = input("Enter number")

AandBfeed = int(Afeed)&int(Bfeed)
BorCfeed = int(Bfeed)|int(Cfeed)
BandCfeed = int(Bfeed)&int(Cfeed)
Dfeed = BorCfeed&BandCfeed

Qfeed = AandBfeed|Dfeed

print(Qfeed)