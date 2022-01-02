password = 'a123456'
x = 3
while x >= 1:
	password_trial = input('請輸入密碼，只有三次機會：')
	if password_trial == password:
		print('登入成功') 
		break
	else:
		print('密碼錯誤！還有', x-1, '次機會')
		x = x - 1
if x == 0:
	print('沒有機會再輸入密碼了，請聯絡客服。')
