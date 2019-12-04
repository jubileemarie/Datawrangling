import pandas as pd
data={'Box':['Box1','Box1','Box1','Box2','Box2','Box2'],'Dimension':['Length','Width','Height','Length','Width','Height'],'Value':[6,4,2,5,3,4]}
Messy=pd.DataFrame(data,columns=['Box','Dimension','Value'])
Tidy = Messy.pivot_table(index = 'Box', columns = 'Dimension',values = 'Value').reset_index()
Tidy['Volume'] = Tidy.Length*Tidy.Height*Tidy.Width

