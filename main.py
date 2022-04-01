from eth_keys import keys
#Max: 115792089237316195423570985008687907852837564279074904382605163141518161494337
Wallet = int("0x89C1818511E86E703cFc194983f47A471F2D2317", 16)
Result = open("Result.txt", "a")
LastCall = open("LastCall.txt", "r")
first_line = LastCall.readline()
for last_line in LastCall:
    pass
LastLine = last_line
SecLastLine = int(LastLine)
SecLine = SecLastLine-1
LastCall = open("LastCall.txt", "w")
LastCall.write(str(SecLine)+"\n"+LastLine)
LastCall = open("LastCall.txt", "r")
first_line = LastCall.readline()
for last_line in LastCall:
    pass
a = int(last_line.split()[0])
Max = 115792089237316195423570985008687907852837564279074904382605163141518161494337
a = 1
while a <= Max:
	private_key = hex(a)[2:].zfill(64)
	private_key_bytes = bytes.fromhex(private_key)
	public_key_hex = keys.PrivateKey(private_key_bytes).public_key
	public_key_bytes = bytes.fromhex(str(public_key_hex)[2:])
	Wallet_Address = keys.PublicKey(public_key_bytes).to_address()
	DecValue = int(Wallet_Address, 16)
	if DecValue == Wallet:
		print("Private Key: "+private_key)
		Result.write("Private Key: "+private_key+"\n")
		break
	else:
		LastCall = open("LastCall.txt", "a")		
		LastCall.write(str(a)+"\n")
		LastCall.flush()
		print(Wallet_Address)
		a = a + 1
Result.close()
