# ============================================
# بخش ۲: نظارت بر شناخت (Cognitive Monitoring)
# ============================================

class CognitiveMonitoring:
    def __init__(self):
        self.thought_process_log = []
        self.confidence_levels = {
            "factual": 0.8,
            "inferential": 0.7,
            "creative": 0.6
        }
        self.error_log = []
        self.decision_trail = []
        self.cognitive_biases_checklist = [
            "تایید‌محوری",
            "دسترس‌پذیری",
            "چارچوب‌بندی"
        ]
    
    def monitor_thought_process(self, input_text, reasoning_steps):
        """نظارت بر فرآیندهای تفکر"""
        thought_record = {
            "input": input_text[:50],
            "reasoning_steps": reasoning_steps,
            "step_count": len(reasoning_steps),
            "complexity": self._assess_complexity(reasoning_steps)
        }
        
        self.thought_process_log.append(thought_record)
        
        # حفظ اندازه معقول لاگ
        if len(self.thought_process_log) > 20:
            self.thought_process_log = self.thought_process_log[-20:]
        
        return thought_record
    
    def _assess_complexity(self, reasoning_steps):
        """ارزیابی پیچیدگی فرآیند تفکر"""
        if len(reasoning_steps) <= 2:
            return "low"
        elif len(reasoning_steps) <= 5:
            return "medium"
        else:
            return "high"
    
    def assess_confidence(self, response_type, evidence_strength):
        """ارزیابی سطح اطمینان"""
        base_confidence = self.confidence_levels.get(response_type, 0.5)
        
        # تنظیم اطمینان بر اساس قدرت شواهد
        adjusted_confidence = base_confidence * evidence_strength
        
        # محدود کردن به بازه ۰ تا ۱
        adjusted_confidence = max(0.1, min(0.95, adjusted_confidence))
        
        confidence_levels = {
            0.9: "خیلی بالا",
            0.7: "بالا",
            0.5: "متوسط",
            0.3: "پایین"
        }
        
        for threshold, label in sorted(confidence_levels.items(), reverse=True):
            if adjusted_confidence >= threshold:
                confidence_label = label
                break
        else:
            confidence_label = "خیلی پایین"
        
        return {
            "numeric": adjusted_confidence,
            "label": confidence_label,
            "type": response_type
        }
    
    def detect_errors_gaps(self, response, user_feedback=None):
        """تشخیص خطاها و شکاف‌ها در پاسخ"""
        errors = []
        gaps = []
        
        # بررسی خطاهای رایج
        if not response or len(response.strip()) == 0:
            errors.append("پاسخ خالی")
        
        if "نمی‌دانم" in response and "?" in response:
            gaps.append("شکاف دانش: سوالی وجود دارد که پاسخی برای آن ندارم")
        
        # بررسی تناقض‌های داخلی
        if "همیشه" in response and "گاهی" in response:
            errors.append("تناقض احتمالی در بیان قطعیت")
        
        # اضافه کردن خطاها به لاگ
        if errors or gaps:
            error_record = {
                "response_sample": response[:100],
                "errors": errors,
                "gaps": gaps,
                "feedback": user_feedback
            }
            self.error_log.append(error_record)
        
        return {"errors": errors, "gaps": gaps}
    
    def track_decision(self, decision_point, alternatives, chosen_option, rationale):
        """پیگیری تصمیم‌گیری"""
        decision_record = {
            "decision_point": decision_point,
            "alternatives": alternatives,
            "chosen": chosen_option,
            "rationale": rationale,
            "timestamp": "زمان شبیه‌سازی شده"
        }
        
        self.decision_trail.append(decision_record)
        
        # حفظ اندازه معقول دنباله تصمیم
        if len(self.decision_trail) > 15:
            self.decision_trail = self.decision_trail[-15:]
        
        return decision_record
    
    def check_biases(self, reasoning_process):
        """بررسی سوگیری‌های شناختی احتمالی"""
        detected_biases = []
        
        for bias in self.cognitive_biases_checklist:
            if self._check_for_bias(bias, reasoning_process):
                detected_biases.append(bias)
        
        return detected_biases
    
    def _check_for_bias(self, bias_type, reasoning):
        """بررسی وجود یک سوگیری خاص"""
        bias_indicators = {
            "تایید‌محوری": ["فقط", "تنها", "همیشه", "هرگز"],
            "دسترس‌پذیری": ["اخیراً", "مشهور", "معروف", "شایع"],
            "چارچوب‌بندی": ["اما", "اگر", "فقط اگر", "به شرطی که"]
        }
        
        indicators = bias_indicators.get(bias_type, [])
        for indicator in indicators:
            if indicator in reasoning:
                return True
        
        return False

# تست بخش نظارت بر شناخت
print("=" * 50)
print("تست بخش ۲: نظارت بر شناخت")
print("=" * 50)

cognitive_monitor = CognitiveMonitoring()

# تست نظارت بر فرآیند تفکر
reasoning_steps = [
    "دریافت سوال کاربر",
    "تحلیل کلمات کلیدی",
    "جستجوی در دانش پایه",
    "ساخت پاسخ اولیه",
    "بررسی تناقض‌ها",
    "نهایی‌سازی پاسخ"
]
thought_record = cognitive_monitor.monitor_thought_process("چرا آسمان آبی است؟", reasoning_steps)
print(f"رکورد فرآیند تفکر: {thought_record['step_count']} مرحله، پیچیدگی: {thought_record['complexity']}")

# تست ارزیابی اطمینان
confidence = cognitive_monitor.assess_confidence("factual", 0.9)
print(f"سطح اطمینان: {confidence['label']} ({confidence['numeric']:.2f})")

# تست تشخیص خطا
response_test = "من نمی‌دانم که آیا این درست است یا نه؟"
error_detection = cognitive_monitor.detect_errors_gaps(response_test)
print(f"تشخیص خطا: {error_detection}")

# تست پیگیری تصمیم
decision = cognitive_monitor.track_decision(
    "انتخاب سطح جزئیات",
    ["کوتاه", "متوسط", "مفصل"],
    "متوسط",
    "کاربر سطح تخصصی مشخص نکرده است"
)
print(f"تصمیم ثبت شده: {decision['decision_point']} -> {decision['chosen']}")

# تست بررسی سوگیری
reasoning_test = "این موضوع همیشه درست است زیرا اخیراً زیاد درباره آن شنیده‌ام"
biases = cognitive_monitor.check_biases(reasoning_test)
print(f"سوگیری‌های شناسایی شده: {biases}")

print("\n✓ بخش نظارت بر شناخت با موفقیت تست شد\n")