	#TOEFL CONVERSION
class structureSection():
	def structure():
		konversi={0:20,1:20,2:21,3:22,4:23,5:25,6:26,7:27,8:29,9:31,10:33,11:35,12:36,13:37,14:38,
		15:40,16:40,17:41,18:43,19:43,20:44,21:45,22:46,23:47,24:48,25:49,26:50,27:51,28:52,29:53,30:54,
		31:55,32:56,33:57,34:58,35:60,36:61,37:63,38:65,39:67,40:68}
		return konversi

	convert=(structure()[int(input('Structure Value : '))])
	cetak=print('Structure Conversion : ', convert*10)

	again=['y', 'Y']
	while (again==['y','Y']) :
		nilai = input('y/n ? ')

		if nilai == 'y' :
			convert=(structure()[int(input('Structure Value : '))])
			cetak=print('Structure Conversion : ', convert*10)
		elif nilai == 'n' :
			break
		else:
			print('try again\n', 'invalid command : ', nilai)

