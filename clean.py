import pandas as pd

# جدول بيانات بسيط
data = {'منتج': ['قاس', 'سماعة', 'لا أحد'], 'السعر': [10, 20, None]}
df = pd.DataFrame(data)

# فرش رات
df.fillna(0, inplace=True)
print("تم التنظيف الفعال!")
print(df)
