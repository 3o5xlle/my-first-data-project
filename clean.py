import pandas as pd

# جدول بيانات بسيط
data = {'المنتج': ['شاحن', 'سماعة', None], 'السعر': [85, 120, None]}
df = pd.DataFrame(data)

# تنظيف الفراغات
df.fillna(0, inplace=True)
print("تم التنظيف بنجاح!")
print(df)

