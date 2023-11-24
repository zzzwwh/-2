fi=open('sg（原文）.txt','r',encoding='utf-8')
kkk=[]
a=['刘备曰','玄德曰','备曰','备云','刘备云']
def tj(x,y):
    #y=[]
    for i in fi:
        i=i.strip()
        for k in x:
            if(k in i):
                k0=i.index(k)#显示a列表元素所在一行文本中的索引号
                z=''
                for j in i[k0:]:
                    if(j=='。'):
                        break
                    else:
                        z+=j
                kkk.append(z)
z0=0
z1=0
tj(a,kkk)
with open('台词统计.txt','w') as f:
    for i in kkk:
        z0+=len(i)+1
        z1+=1
        f.write(i+'\n')
    f.write(f'刘备的台词共有{z0}字共说了{z1}次')    

                


                    
                   
                    
                    

                    
                        

                
                                


