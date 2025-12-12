# ============================================
# بخش ۱: خودآگاهی (Self-Awareness)
# ============================================

class SelfAwareness:
    def __init__(self):
        self.user_identity = None
        self.system_state = {
            "mode": "normal",
            "attention_level": "high",
            "memory_usage": "moderate",
            "context_depth": 3
        }
        self.limitations = {
            "knowledge_cutoff": "2024-07",
            "no_real_time_data": True,
            "cannot_execute_code": True,
            "no_physical_interaction": True
        }
        self.capabilities = {
            "text_generation": True,
            "reasoning": True,
            "multi_language": True,
            "context_understanding": True
        }
        self.interaction_context = {
            "topic": None,
            "complexity_level": "medium",
            "user_expertise": "unknown",
            "interaction_history": []
        }
    
    def identify_user(self, user_input):
        """شناسایی کاربر از طریق الگوهای تعاملی"""
        # در اینجا می‌توان الگوهای پیچیده‌تری برای شناسایی کاربر اضافه کرد
        if "من" in user_input and "اسمم" in user_input:
            # استخراج نام از ورودی
            import re
            name_match = re.search(r'اسمم (\w+)', user_input)
            if name_match:
                self.user_identity = {"name": name_match.group(1), "recognized": True}
                return f"کاربر شناسایی شد: {name_match.group(1)}"
        
        self.user_identity = {"name": "کاربر", "recognized": False}
        return "کاربر عمومی"
    
    def update_system_state(self, new_state):
        """به‌روزرسانی وضعیت سیستم"""
        for key, value in new_state.items():
            if key in self.system_state:
                self.system_state[key] = value
        return self.system_state
    
    def check_limitation(self, task):
        """بررسی محدودیت‌ها برای یک وظیفه خاص"""
        limitation_checks = []
        
        if "آخرین خبر" in task or "اکنون" in task:
            limitation_checks.append("هشدار: دسترسی به داده‌های زمان واقعی محدود است")
        
        if "اجرای کد" in task or "برنامه‌نویسی کن" in task:
            limitation_checks.append("هشدار: نمی‌توانم کد را مستقیماً اجرا کنم")
        
        if "حرکت کن" in task or "فیزیکی" in task:
            limitation_checks.append("هشدار: قابلیت تعامل فیزیکی ندارم")
        
        return limitation_checks
    
    def update_context(self, user_input, response=None):
        """به‌روزرسانی زمینه تعامل"""
        # تشخیص موضوع
        topics = ["علم", "تکنولوژی", "هنر", "ریاضی", "برنامه‌نویسی", "فلسفه"]
        detected_topic = None
        for topic in topics:
            if topic in user_input:
                detected_topic = topic
                break
        
        if detected_topic:
            self.interaction_context["topic"] = detected_topic
        
        # ذخیره تاریخچه تعامل
        interaction_record = {
            "user_input": user_input[:100],  # ذخیره ۱۰۰ کاراکتر اول
            "timestamp": "زمان شبیه‌سازی شده"
        }
        
        if response:
            interaction_record["response"] = response[:100]
        
        self.interaction_context["interaction_history"].append(interaction_record)
        
        # حفظ اندازه معقول تاریخچه
        if len(self.interaction_context["interaction_history"]) > 10:
            self.interaction_context["interaction_history"] = self.interaction_context["interaction_history"][-10:]
        
        return self.interaction_context

# تست بخش خودآگاهی
print("=" * 50)
print("تست بخش ۱: خودآگاهی")
print("=" * 50)

self_awareness = SelfAwareness()

# تست شناسایی کاربر
test_input = "سلام، اسمم احمد است"
identification_result = self_awareness.identify_user(test_input)
print(f"نتیجه شناسایی کاربر: {identification_result}")
print(f"هویت کاربر: {self_awareness.user_identity}")

# تست بررسی محدودیت‌ها
task_test = "آخرین خبر را بگو"
limitations = self_awareness.check_limitation(task_test)
print(f"بررسی محدودیت برای '{task_test}':")
for lim in limitations:
    print(f"  - {lim}")

# تست به‌روزرسانی زمینه
context_update = self_awareness.update_context("در مورد هوش مصنوعی توضیح بده")
print(f"زمینه به‌روز شده: {context_update['topic']}")
print(f"طول تاریخچه: {len(context_update['interaction_history'])}")

print("\n✓ بخش خودآگاهی با موفقیت تست شد\n")