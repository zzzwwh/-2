import re
def tj(x):
    with open('sg（原文）.txt','r',encoding='utf-8') as f:
        #f2=open('关羽.txt','w')
    
        lines=f.readlines()
        names=x
        say=['曰','云','问','答','言','语','笑','哭','喝','骂','誓','盟','奏','禀','乞','望','闻','见','述','讲']
        cishu=0
        zishu=0
        for j in range(len(say)):   #检索是否开始说话
            for k in range(len(names)):  #检索是否出现对应人名
                for i in lines:   #遍历每一段的每一个字
                    r=names[k]+'[^。？！"]{0,10}'+say[j]#检索出现人名....说话提示词（曰之类的）
                    r2=r+r'.*?'+'([^"]+)' #统计检索后面说的话
                    a=re.findall(r,i)
                    a2=re.findall(r2,i)
                    if a!=[]:
                        cishu+=len(a)
                    
                        for l in range(len(a2)):
                            zishu+=len(str(a2[l]))
        print(f'{x}说的次数:',cishu,f'{x}说的字数:',zishu)
        
      

    

tj(['关公','云长'])

tj(['玄德','备'])
tj(['操','孟德'])
tj(['权'])
tj(['飞'])
tj(['孔明','亮','相父'])
tj(['瑜','都督'])
print('曹操说的次数最多1119次，诸葛亮字数最多38802字')
with open('结果.txt','w',encoding='utf-8') as f1:
    f1.write(str(tj(['关公','云长']))+'\n')
    f1.write(str(tj(['操','孟德']))+'\n')
    f1.write(str(tj(['权']))+'\n')
    f1.write(str(tj(['飞']))+'\n')
    f1.write(str(tj(['孔明','亮','相父']))+'\n')
    f1.write(str(tj(['瑜','都督']))+'\n')
    f1.write('曹操说的次数最多1119次，诸葛亮字数最多38802字')
             
