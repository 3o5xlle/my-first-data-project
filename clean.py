import pandas as pd

# جدول بيانات بسيط
data = {'منتج': ['قاس', 'سماعة', 'لا أحد']}
df = pd.DataFrame(data)

# فرش رات
df.fillna(0, inplace=True)
print("تم التنظيف الفعال!")
print(df)
