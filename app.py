
""" على Flask يعتمد
المسار (Route): هو الرابط الذي يكتبه المستخدم (مثل www.site.com/about).
الدالة (Function): هي الكود الذي يعمل عندما يفتح المستخدم هذا الرابط.
الطلب (Request): المعلومات القادمة من المستخدم (مثل بيانات نموذج التسجيل).
الرد (Response): ما يراه المستخدم في المتصفح (غالباً صفحة HTML).
"""



from flask import Flask, render_template, request
from dotenv import load_dotenv
import os

# .env تحميل الإعدادات من ملف  
load_dotenv()

# 1. تهيئة التطبيق
app = Flask(__name__)

# المسار الأول: الصفحة الرئيسية (التي فيها الفورم)
@app.route('/')
def index():
    # هنا نطلب من Flask عرض ملف index.html الموجود داخل مجلد templates
    return render_template('index.html')

# المسار الثاني: لاستقبال البيانات وعرضها
# لعرضها 'POST' ينتضر طرد البيانات المغلق بطريقة
@app.route('/greet', methods=['POST'])
def greet():
    # index.فتح "الطرد" البيانات التي كتبها المستخدم في الـ 
    user_name = request.form.get('namel')
    user_hobby = request.form.get('hobby')
    
    # لتعرضها result.html إرسال هذه البيانات إلى صفحة 
    return render_template('result.html', name=user_name, hobby=user_hobby)

if __name__ == '__main__':
    # debug=True: ميزة رائعة تجعل الموقع يعيد تشغيل نفسه تلقائياً عندما تعدل الكود
    app.run(debug=True)