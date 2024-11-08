# rectangle_area.py

# دالة لحساب مساحة المستطيل
def calculate_area(length, width):
    return length * width

# طلب الطول والعرض من المستخدم
try:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    
    # حساب المساحة
    area = calculate_area(length, width)
    
    # طباعة النتيجة
    print(f"The area of the rectangle is: {area}")
    
except ValueError:
    print("Please enter valid numbers for length and width.")
