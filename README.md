纯Python自制的登入注册模块
Account.txt相当于Database
🚀注意：使用VScode for cs50
亮点一：使用了sys库中sys.argv，设置命令行和Input()函数两种输入账号的方式。
亮点二：系统前期判断输入严格，与现实中软件的登入注册流程一致，在其修改上可以使用validator-collection库，来代替re库的正则表达式
缺点一：系统功能不全，目前只有搜索账号和退出系统
缺点二：代码中class类未使用（目前纯属增加代码量）
缺点三：re.search函数的正则表达式不是很prefect
