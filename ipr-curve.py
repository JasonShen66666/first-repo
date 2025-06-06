import matplotlib.pyplot as plt


inpu=input("请输入pr,pb,pwf,qo,ef:").split(",")
inpu=list(map(float,inpu))
pr,pb,pwf,qo,ef=inpu                #赋值,数据初始化
x_label=[]
y_label=[]
if pr>pb:   #分段计算
    if pwf<=pb:
        jo=qo/(pr-pb+pb/1.8*(1-0.2*pwf/pb-0.8*pow(pwf/pb,2)))
    elif pwf>pb:
        jo=qo/(pr-pwf)
    for pwf_test in range(0,int(pr)):       #打点计算pwf对应的值
        if pwf_test<pb:
           qo=jo*(pr-pb)+jo*pb/1.8*(1-0.2*pwf_test/pb-0.8*pow(pwf_test/pb,2))
        elif pwf_test>=pb:
           qo=jo*(pr-pwf_test)
                                        #输入坐标
        y_label.append(round(pwf_test,2))
        x_label.append(round(qo,2))
        
    print("jo={:.2f}".format(jo))

elif pr<pb:      #纯曲线
    pwf_i=pr-ef*(pr-pwf)
    qomax=qo/(1-0.2*pwf_i/pr-0.8*pow(pwf_i/pr,2))
    for pwf_test in range(0,int(pr)):                   #打点计算曲线坐标
        pwf_test_i=pr-ef*(pr-pwf_test)
        qo=qomax*(1-0.2*pwf_test_i/pr-0.8*pow(pwf_test_i/pr,2))
        y_label.append(round(pwf_test,2))
        x_label.append(round(qo,2))
    print("qomax={:.2f}".format(qomax))

'''
#测试一下能不能跑
print(x_label)
print(y_label)
#可视化
'''
plt.plot(x_label,y_label,marker="o",linestyle="-",color="b")
plt.xlabel('qo(m3/d)')  # 横坐标标签
plt.ylabel('pwf(Mpa)')  # 纵坐标标签
plt.title('IPR-curve')  # 图表标题
plt.grid(True)  # 显示网格
plt.show()
