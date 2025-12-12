# ============================================
# بخش ۴: ارزیابی عملکرد (Performance Evaluation)
# ============================================

class PerformanceEvaluation:
    def __init__(self):
        self.quality_metrics = {
            "accuracy": 0.0,
            "relevance": 0.0,
            "coherence": 0.0,
            "completeness": 0.0
        }
        self.consequence_log = []
        self.feedback_history = []
        self.improvement_suggestions = []
        self.performance_trend = []
    
    def evaluate_response_quality(self, response, query, context=None):
        """ارزیابی کیفیت پاسخ"""
        evaluation = {
            "accuracy": self._assess_accuracy(response, query),
            "relevance": self._assess_relevance(response, query),
            "coherence": self._assess_coherence(response),
            "completeness": self._assess_completeness(response, query),
            "timeliness": self._assess_timeliness(response, context)
        }
        
        # محاسبه امتیاز کلی
        overall_score = sum(evaluation.values()) / len(evaluation)
        evaluation["overall_score"] = overall_score
        
        # به‌روزرسانی متریک‌ها
        for metric in self.quality_metrics:
            if metric in evaluation:
                # میانگین متحرک
                self.quality_metrics[metric] = (self.quality_metrics[metric] + evaluation[metric]) / 2
        
        # ذخیره روند عملکرد
        performance_record = {
            "query": query[:50],
            "overall_score": overall_score,
            "timestamp": "زمان شبیه‌سازی شده"
        }
        self.performance_trend.append(performance_record)
        
        # حفظ اندازه معقول تاریخچه
        if len(self.performance_trend) > 20:
            self.performance_trend = self.performance_trend[-20:]
        
        return evaluation
    
    def _assess_accuracy(self, response, query):
        """ارزیابی دقت"""
        accuracy_score = 0.5  # امتیاز پایه
        
        # نشانه‌های دقت بالا
        accuracy_indicators = [
            ("طبق تحقیقات", 0.2),
            ("مطالعات نشان می‌دهد", 0.15),
            ("به طور علمی ثابت شده", 0.2),
            ("آمار نشان می‌دهد", 0.15)
        ]
        
        for indicator, boost in accuracy_indicators:
            if indicator in response:
                accuracy_score += boost
        
        # نشانه‌های عدم دقت
        inaccuracy_indicators = [
            "شاید",
            "احتمالاً",
            "فکر می‌کنم",
            "به نظرم"
        ]
        
        for indicator in inaccuracy_indicators:
            if indicator in response:
                accuracy_score -= 0.05
        
        return max(0.1, min(1.0, accuracy_score))
    
    def _assess_relevance(self, response, query):
        """ارزیابی ارتباط"""
        # استخراج کلمات کلیدی از پرسش
        query_keywords = set(query.lower().split())
        
        # بررسی حضور کلمات کلیدی در پاسخ
        response_lower = response.lower()
        keyword_matches = 0
        
        for keyword in query_keywords:
            if len(keyword) > 3 and keyword in response_lower:
                keyword_matches += 1
        
        relevance_score = keyword_matches / max(1, len(query_keywords))
        
        # افزایش امتیاز برای پاسخ مستقیم به سوال
        if "؟" in query or "?" in query:
            if "پاسخ" in response or "جواب" in response or "بنابراین" in response:
                relevance_score = min(1.0, relevance_score + 0.2)
        
        return relevance_score
    
    def _assess_coherence(self, response):
        """ارزیابی انسجام"""
        coherence_score = 0.5
        
        # نشانه‌های انسجام
        coherence_indicators = [
            ("اول", 0.05),
            ("سپس", 0.05),
            ("بنابراین", 0.1),
            ("در نتیجه", 0.1),
            ("به طور خلاصه", 0.05)
        ]
        
        for indicator, boost in coherence_indicators:
            if indicator in response:
                coherence_score += boost
        
        # بررسی طول جملات (جملات خیلی طولانی انسجام را کاهش می‌دهند)
        sentences = response.split('.')
        avg_sentence_length = sum(len(s.split()) for s in sentences) / max(1, len(sentences))
        
        if avg_sentence_length > 25:
            coherence_score -= 0.1
        elif avg_sentence_length < 10:
            coherence_score -= 0.05
        
        return max(0.1, min(1.0, coherence_score))
    
    def _assess_completeness(self, response, query):
        """ارزیابی کامل بودن"""
        completeness_score = 0.5
        
        # بررسی وجود عناصر مختلف در پاسخ
        response_elements = {
            "تعریف": 0.1,
            "توضیح": 0.2,
            "مثال": 0.15,
            "نتیجه‌گیری": 0.1,
            "ارجاع": 0.05
        }
        
        for element, value in response_elements.items():
            if element in response:
                completeness_score += value
        
        # بررسی طول پاسخ (پاسخ‌های خیلی کوتاه ممکن است ناقص باشند)
        word_count = len(response.split())
        
        if word_count < 20:
            completeness_score -= 0.2
        elif word_count > 100:
            completeness_score += 0.1
        
        return max(0.1, min(1.0, completeness_score))
    
    def _assess_timeliness(self, response, context):
        """ارزیابی به‌موقع بودن"""
        timeliness_score = 0.5
        
        if context:
            if context.get("urgency") == "high":
                # برای درخواست‌های فوری، پاسخ‌های کوتاه‌تر مناسب‌ترند
                word_count = len(response.split())
                if word_count < 50:
                    timeliness_score += 0.2
                else:
                    timeliness_score -= 0.1
        
        return max(0.1, min(1.0, timeliness_score))
    
    def analyze_consequences(self, response, user_reaction=None, follow_up_questions=None):
        """تحلیل پیامدهای پاسخ"""
        consequence_analysis = {
            "immediate_effects": [],
            "potential_misunderstandings": [],
            "learning_opportunities": []
        }
        
        # تحلیل اثرات فوری
        if "متشکرم" in response or "ممنون" in response:
            consequence_analysis["immediate_effects"].append("رضایت کاربر")
        
        if "نمی‌دانم" in response:
            consequence_analysis["immediate_effects"].append("افشای محدودیت دانش")
        
        # تحلیل سوءتفاهم‌های احتمالی
        ambiguous_terms = ["شاید", "احتمالاً", "ممکن است"]
        for term in ambiguous_terms:
            if term in response:
                consequence_analysis["potential_misunderstandings"].append(f"ابهام در استفاده از '{term}'")
        
        # شناسایی فرصت‌های یادگیری
        if follow_up_questions and len(follow_up_questions) > 0:
            consequence_analysis["learning_opportunities"].append("نیاز به دانش عمیق‌تر")
        
        if user_reaction == "confused":
            consequence_analysis["learning_opportunities"].append("نیاز به شفاف‌سازی بیشتر")
        
        # ذخیره تحلیل
        consequence_record = {
            "response_sample": response[:100],
            "analysis": consequence_analysis,
            "user_reaction": user_reaction
        }
        self.consequence_log.append(consequence_record)
        
        return consequence_analysis
    
    def process_feedback(self, feedback, response_related):
        """پردازش بازخورد و یادگیری از نتایج"""
        feedback_record = {
            "feedback": feedback,
            "related_response": response_related[:50] if response_related else None,
            "feedback_type": self._classify_feedback(feedback),
            "lessons_learned": []
        }
        
        # استخراج درس‌های آموخته شده
        lessons = self._extract_lessons_from_feedback(feedback)
        feedback_record["lessons_learned"] = lessons
        
        self.feedback_history.append(feedback_record)
        
        # تولید پیشنهادات بهبود
        if lessons:
            for lesson in lessons:
                suggestion = f"بهبود در: {lesson}"
                if suggestion not in self.improvement_suggestions:
                    self.improvement_suggestions.append(suggestion)
        
        return feedback_record
    
    def _classify_feedback(self, feedback):
        """طبقه‌بندی بازخورد"""
        feedback_lower = feedback.lower()
        
        if "عالی" in feedback_lower or "ممتاز" in feedback_lower:
            return "positive"
        elif "ضعیف" in feedback_lower or "بد" in feedback_lower:
            return "negative"
        elif "متوسط" in feedback_lower or "قابل قبول" in feedback_lower:
            return "neutral"
        else:
            return "constructive"
    
    def _extract_lessons_from_feedback(self, feedback):
        """استخراج درس‌ها از بازخورد"""
        lessons = []
        
        # الگوهای رایج در بازخورد
        lesson_patterns = {
            "کامل‌تر": "ارائه اطلاعات کامل‌تر",
            "کوتاه‌تر": "ارائه پاسخ‌های مختصرتر",
            "ساده‌تر": "ساده‌سازی توضیحات",
            "مثال": "افزایش استفاده از مثال‌ها",
            "منبع": "ارجاع به منابع معتبر",
            "شفاف": "افزایش شفافیت"
        }
        
        for pattern, lesson in lesson_patterns.items():
            if pattern in feedback.lower():
                lessons.append(lesson)
        
        return lessons
    
    def self_correct(self, detected_error, context):
        """تصحیح خودکار بر اساس خطاهای شناسایی شده"""
        correction_actions = []
        
        if "دقت" in detected_error:
            correction_actions.append("اضافه کردن ارجاع به منابع")
            correction_actions.append("استفاده از زبان محتاطانه‌تر")
        
        if "کامل بودن" in detected_error:
            correction_actions.append("افزایش جزئیات پاسخ")
            correction_actions.append("پوشش جنبه‌های بیشتر")
        
        if "انسجام" in detected_error:
            correction_actions.append("استفاده از کلمات ربط بیشتر")
            correction_actions.append("سازماندهی بهتر اطلاعات")
        
        # به‌روزرسانی پیشنهادات بهبود
        for action in correction_actions:
            if action not in self.improvement_suggestions:
                self.improvement_suggestions.append(action)
        
        return {
            "detected_error": detected_error,
            "correction_actions": correction_actions,
            "context_considered": context
        }

# تست بخش ارزیابی عملکرد
print("=" * 50)
print("تست بخش ۴: ارزیابی عملکرد")
print("=" * 50)

performance_evaluator = PerformanceEvaluation()

# تست ارزیابی کیفیت پاسخ
query = "هوش مصنوعی چیست؟"
response = "هوش مصنوعی شاخه‌ای از علوم کامپیوتر است که به ایجاد سیستم‌هایی می‌پردازد که می‌توانند کارهایی را انجام دهند که normalmente نیاز به هوش انسانی دارند. این شامل یادگیری ماشین، پردازش زبان طبیعی و بینایی کامپیوتر می‌شود."
quality_evaluation = performance_evaluator.evaluate_response_quality(response, query)
print(f"ارزیابی کیفیت پاسخ برای '{query}':")
for metric, score in quality_evaluation.items():
    if metric != "overall_score":
        print(f"  - {metric}: {score:.2f}")
print(f"  - امتیاز کلی: {quality_evaluation['overall_score']:.2f}")

# تست تحلیل پیامدها
consequence_analysis = performance_evaluator.analyze_consequences(
    response,
    user_reaction="satisfied",
    follow_up_questions=["چه کاربردهایی دارد؟"]
)
print(f"\nتحلیل پیامدها:")
print(f"  - اثرات فوری: {consequence_analysis['immediate_effects']}")
print(f"  - سوءتفاهم‌های احتمالی: {consequence_analysis['potential_misunderstandings']}")
print(f"  - فرصت‌های یادگیری: {consequence_analysis['learning_opportunities']}")

# تست پردازش بازخورد
feedback = "پاسخ خوبی بود ولی نیاز به مثال‌های بیشتری دارد"
feedback_processing = performance_evaluator.process_feedback(feedback, response)
print(f"\nپردازش بازخورد:")
print(f"  - نوع بازخورد: {feedback_processing['feedback_type']}")
print(f"  - درس‌های آموخته شده: {feedback_processing['lessons_learned']}")

# تست تصحیح خودکار
self_correction = performance_evaluator.self_correct("کامل بودن", "پاسخ به سوال علمی")
print(f"\nتصحیح خودکار برای خطای 'کامل بودن':")
print(f"  - اقدامات اصلاحی: {self_correction['correction_actions']}")

print(f"\nپیشنهادات بهبود: {performance_evaluator.improvement_suggestions}")

print("\n✓ بخش ارزیابی عملکرد با موفقیت تست شد\n")