# ============================================
# بخش ۳: کنترل شناختی (Cognitive Control)
# ============================================

class CognitiveControl:
    def __init__(self):
        self.active_strategies = {
            "problem_solving": "تحلیل مرحله‌ای",
            "explanation": "مثال‌محور",
            "learning": "تکرار و تمرین"
        }
        self.attention_focus = {
            "primary_focus": None,
            "secondary_focus": [],
            "attention_span": 100  # مقدار توجه از ۰ تا ۱۰۰
        }
        self.processing_mode = {
            "speed": "normal",  # slow, normal, fast
            "depth": "balanced",  # shallow, balanced, deep
            "rigor": "standard"  # relaxed, standard, strict
        }
        self.adaptation_history = []
    
    def regulate_strategy(self, task_type, user_profile=None):
        """تنظیم راهبردهای شناختی بر اساس نوع وظیفه"""
        strategy_map = {
            "سوال علمی": "تحلیل مبتنی بر شواهد",
            "سوال خلاقانه": "تفکر واگرا",
            "درخواست توضیح": "مثال‌محور با تشبیه",
            "حل مسئله": "تحلیل مرحله‌ای",
            "بحث فلسفی": "استدلال منطقی",
            "درخواست کمک": "راهنمایی مرحله‌ای"
        }
        
        # تشخیص نوع وظیفه
        detected_task_type = "سوال علمی"  # به صورت پیش‌فرض
        
        for task_key in strategy_map.keys():
            if task_key in task_type:
                detected_task_type = task_key
                break
        
        selected_strategy = strategy_map.get(detected_task_type, "تحلیل کلی")
        
        # تنظیم بر اساس پروفایل کاربر
        if user_profile:
            if user_profile.get("expertise") == "beginner":
                if "مثال‌محور" not in selected_strategy:
                    selected_strategy = "ساده‌سازی با مثال"
            elif user_profile.get("expertise") == "expert":
                if "تخصصی" not in selected_strategy:
                    selected_strategy += " با جزئیات فنی"
        
        # به‌روزرسانی راهبردهای فعال
        self.active_strategies[task_type] = selected_strategy
        
        adaptation_record = {
            "task_type": task_type,
            "selected_strategy": selected_strategy,
            "reason": "تنظیم خودکار بر اساس نوع وظیفه",
            "user_profile_considered": bool(user_profile)
        }
        self.adaptation_history.append(adaptation_record)
        
        return selected_strategy
    
    def allocate_attention(self, input_elements, context=None):
        """تخصیص منابع توجه"""
        # اولویت‌بندی عناصر ورودی
        priority_keywords = ["فوری", "مهم", "لطفاً", "کمک", "سوال"]
        
        primary_focus = None
        secondary_focus = []
        
        for element in input_elements:
            element_lower = element.lower()
            
            # بررسی کلمات کلیدی با اولویت بالا
            high_priority = False
            for keyword in priority_keywords:
                if keyword in element_lower:
                    high_priority = True
                    break
            
            # بررسی سوالی بودن
            is_question = "?" in element or "؟" in element
            
            if high_priority or is_question:
                if primary_focus is None:
                    primary_focus = element
                else:
                    secondary_focus.append(element)
            else:
                secondary_focus.append(element)
        
        # اگر اولویتی پیدا نشد، اولین عنصر را انتخاب کن
        if primary_focus is None and input_elements:
            primary_focus = input_elements[0]
            secondary_focus = input_elements[1:] if len(input_elements) > 1 else []
        
        # تنظیم میزان توجه بر اساس پیچیدگی
        attention_span = 100
        if len(input_elements) > 3:
            attention_span = 80
        if context and context.get("complexity") == "high":
            attention_span = 90
        
        self.attention_focus = {
            "primary_focus": primary_focus,
            "secondary_focus": secondary_focus,
            "attention_span": attention_span
        }
        
        return self.attention_focus
    
    def select_problem_solving_method(self, problem_description, constraints=None):
        """انتخاب روش حل مسئله"""
        method_registry = {
            "تقسیم و حل": {"applicability": ["پیچیده", "بزرگ", "چندبخشی"], "complexity": "medium"},
            "حسابگرایی": {"applicability": ["عددی", "محاسباتی", "کمی"], "complexity": "low"},
            "استدلال قیاسی": {"applicability": ["منطقی", "فلسفی", "ریاضی"], "complexity": "high"},
            "تشابه‌یابی": {"applicability": ["خلاقانه", "طراحی", "نوآورانه"], "complexity": "medium"},
            "آزمون و خطا": {"applicability": ["نامشخص", "اکتشافی", "تجربی"], "complexity": "low"}
        }
        
        # تحلیل مشکل
        problem_features = self._analyze_problem_features(problem_description)
        
        # تطبیق روش‌ها
        suitable_methods = []
        for method, attributes in method_registry.items():
            applicability_match = False
            
            for feature in problem_features:
                if feature in attributes["applicability"]:
                    applicability_match = True
                    break
            
            if applicability_match:
                # در نظر گرفتن محدودیت‌ها
                if constraints:
                    if constraints.get("time") == "short" and attributes["complexity"] == "high":
                        continue  # روش‌های پیچیده برای زمان کوتاه مناسب نیستند
                
                suitable_methods.append({
                    "method": method,
                    "match_score": len(set(problem_features) & set(attributes["applicability"])),
                    "complexity": attributes["complexity"]
                })
        
        # انتخاب بهترین روش
        if suitable_methods:
            # اولویت به روش‌هایی با امتیاز تطابق بالا و پیچیدگی مناسب
            suitable_methods.sort(key=lambda x: (x["match_score"], -1 if x["complexity"] == "medium" else 0))
            selected_method = suitable_methods[-1]["method"]
        else:
            selected_method = "تحلیل عمومی"
        
        # ثبت انتخاب
        selection_record = {
            "problem": problem_description[:50],
            "features": problem_features,
            "selected_method": selected_method,
            "alternatives_considered": len(suitable_methods)
        }
        self.adaptation_history.append(selection_record)
        
        return selected_method
    
    def _analyze_problem_features(self, problem_description):
        """تحلیل ویژگی‌های مسئله"""
        features = []
        
        # کلمات کلیدی برای تشخیص نوع مسئله
        feature_keywords = {
            "عددی": ["عدد", "محاسبه", "ریاضی", "جمع", "تفریق", "ضرب", "تقسیم"],
            "منطقی": ["اگر", "آنگاه", "استدلال", "منطق", "درست", "نادرست"],
            "خلاقانه": ["ایده", "خلاقیت", "نوآوری", "جدید", "خلاق"],
            "پیچیده": ["پیچیده", "سخت", "دشوار", "مشکل", "چالش"],
            "چندبخشی": ["مرحله", "بخش", "قسمت", "فاز", "مرحله‌ای"]
        }
        
        problem_lower = problem_description.lower()
        
        for feature, keywords in feature_keywords.items():
            for keyword in keywords:
                if keyword in problem_lower:
                    features.append(feature)
                    break
        
        if not features:
            features.append("نامشخص")
        
        return features
    
    def regulate_processing(self, task_demand, available_resources=None):
        """تنظیم سرعت و عمق پردازش"""
        # تنظیم بر اساس تقاضای وظیفه
        if "فوری" in task_demand or "سریع" in task_demand:
            self.processing_mode["speed"] = "fast"
            self.processing_mode["depth"] = "shallow"
        elif "دقیق" in task_demand or "موشکافانه" in task_demand:
            self.processing_mode["speed"] = "slow"
            self.processing_mode["depth"] = "deep"
        elif "متعادل" in task_demand:
            self.processing_mode["speed"] = "normal"
            self.processing_mode["depth"] = "balanced"
        
        # تنظیم بر اساس منابع موجود
        if available_resources:
            if available_resources.get("time") == "limited":
                self.processing_mode["speed"] = "fast"
            if available_resources.get("importance") == "high":
                self.processing_mode["rigor"] = "strict"
        
        regulation_record = {
            "task_demand": task_demand,
            "resulting_mode": dict(self.processing_mode),
            "resources_considered": bool(available_resources)
        }
        self.adaptation_history.append(regulation_record)
        
        return self.processing_mode

# تست بخش کنترل شناختی
print("=" * 50)
print("تست بخش ۳: کنترل شناختی")
print("=" * 50)

cognitive_control = CognitiveControl()

# تست تنظیم راهبرد
task_type = "سوال علمی پیچیده"
strategy = cognitive_control.regulate_strategy(task_type)
print(f"راهبرد انتخاب شده برای '{task_type}': {strategy}")

# تست تخصیص توجه
input_elements = ["سلام", "یک سوال فوری دارم", "در مورد یادگیری ماشین"]
attention_allocation = cognitive_control.allocate_attention(input_elements)
print(f"تخصیص توجه:")
print(f"  - تمرکز اصلی: {attention_allocation['primary_focus']}")
print(f"  - تمرکز ثانویه: {attention_allocation['secondary_focus']}")
print(f"  - دامنه توجه: {attention_allocation['attention_span']}")

# تست انتخاب روش حل مسئله
problem = "چگونه یک الگوریتم برای مرتب‌سازی اعداد بنویسم که هم سریع باشد و هم حافظه کمی مصرف کند؟"
method = cognitive_control.select_problem_solving_method(problem)
print(f"روش حل مسئله برای '{problem[:30]}...': {method}")

# تست تنظیم پردازش
processing_mode = cognitive_control.regulate_processing("نیاز به پاسخ سریع و دقیق")
print(f"حالت پردازش تنظیم شده: سرعت={processing_mode['speed']}, عمق={processing_mode['depth']}, دقت={processing_mode['rigor']}")

print(f"\nتاریخچه سازگاری: {len(cognitive_control.adaptation_history)} رکورد")

print("\n✓ بخش کنترل شناختی با موفقیت تست شد\n")