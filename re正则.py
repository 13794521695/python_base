#正则
#总共有是十一种字符， .  ^  $  *  + ?  {} []  \ | ()
# . 匹配换行符和空格之外的所有字符。 一个点打印一个字符，两个点打印两个字符
import  re
res = re.search('a','abc')  #表示a在search中的查找，找不到会返回None
print(res)

res = re.search('..','abc')  #一个点代表一个字符，两个点匹配ab
print(res)

# \b 匹配单词的边界，默认以空格分割边界，如果空格之后就是s就会找到，否则返回None,空格之后是s才会找到
res = re.search(r'\bs',r'qwfsdf sfd f')
print(res)

'''
\d  匹配0 -9 的数字        都是匹配第一个的。
\w  匹配任何字母和数字
\s  匹配任意的空白字符，包括空格  制表符  换行符等
\b  匹配单词的边界
\D  匹配除数字外的字符
\W  匹配任何非字母和数字
\S  匹配任意非空白字符
'''

res =  re.search(r'\w','fdsfdsgfdgdfg4354435')
print(res)

res = re.findall(r'sfd+','fsfdfdsf')   #findall会匹配所有，以列表返回.  +是零到1次，即精确匹配sfd
print(res)

res = re.findall(r'\d{3,}','fdsfd890fdsfgdg8798698dgsfgf879709')  #当是{0,}时，数字的字母都会占据列表的一个元素''。
print(res)              #{}里面的数字代表匹配多少个数字以及以上，并以那个为一组。如果是4的时候， 890不会被匹配


res = re.findall(r'\d{1,}','gfg4354ff')  #？是尽可能少匹配    *是0到多个，尽可能多匹配
print(res)

#[]  是或的意思
res = re.findall(r'a[bc]d','abcd')   #匹配abd 或者acd
print(res)

res = re.findall(r'(24|3)',r'435246f5')     #匹配24或者3   （）表示分组
print(res)

res = re.findall(r'[a-z\d]',r'fsfdsfew5435465gfdgft4545')   #匹配字母数字
print(res)

res = re.findall('\d{4}-\d{8}','0215-12345678')
print(res)

b = re.compile('b')          #compile  把正则表达式编译成正则对象
res = b.search('fdsbfdgfd')
print(res)

#re的方法
res = re.match('abc','abcfedgs')
print(res)

res = re.sub('o','i','poytohon',2)   #相当于字符串的replace，
print(res)

res = re.split('\d{1}','fedrgtrdt434gfrdg4dfg',2)  #切割字符串
print(res)


res = re.search(r'ab','fsdfdsfdsabgs')
print(res.group())
print(res.end())
print(res.start())
print(res.span())
