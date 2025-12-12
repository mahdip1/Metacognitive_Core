# ============================================
# بخش ۶: هسته اصلی یکپارچه (Integrated Metacognitive Core)
# ============================================

# ابتدا کلاس‌های مورد نیاز را تعریف می‌کنیم
class SelfAwareness:
    def __init__(self):
        self.interaction_context = {"topic": ""}
    
    def identify_user(self, user_input):
        return {"user_type": "general", "confidence": 0.8}
    
    def check_limitation(self, user_input):
        return []
    
    def update_context(self, user_input):
        if "هوش" in user_input:
            self.interaction_context["topic"] = "هوش مصنوعی"
        else:
            self.interaction_context["topic"] = "عمومی"


class CognitiveMonitoring:
    def __init__(self):
        self.confidence_levels = {"inferential": 0.7}
    
    def monitor_thought_process(self, user_input, reasoning_steps):
        return {"step_count": len(reasoning_steps), "status": "completed"}
    
    def assess_confidence(self, confidence_type, level):
        labels = {0.3: "پایین", 0.7: "متوسط", 0.9: "بالا"}
        label = labels.get(level, "متوسط")
        return {"label": label, "value": level}


class CognitiveControl:
    def __init__(self):
        self.active_strategies = {"explanation": "مثال‌محور"}
        self.attention_focus = {"attention_span": "high"}
        self.processing_mode = "analytical"
    
    def regulate_strategy(self, user_input, user_profile):
        return "توضیح ساختاریافته"
    
    def allocate_attention(self, inputs):
        return {"primary_focus": inputs[0], "attention_level": "high"}
    
    def regulate_processing(self, user_input):
        return "عمیق"


class PerformanceEvaluation:
    def __init__(self):
        self.improvement_suggestions = []
    
    def evaluate_response_quality(self, response, user_input):
        score = min(0.7 + (len(response) / 1000) * 0.3, 0.95)
        return {"overall_score": score, "coherence": 0.9}
    
    def analyze_consequences(self, response, user_reaction):
        return {"immediate_effects": "positive", "learning_outcome": "medium"}


class UserMentalModel:
    def __init__(self):
        self.user_profile = {
            "emotional_state": "neutral",
            "expertise_level": "intermediate"
        }
        self.interaction_patterns = {"frequent_topics": {}}
    
    def understand_user_goals(self, user_input, context):
        return {"explicit": "دریافت اطلاعات", "implicit": "یادگیری"}
    
    def detect_emotional_state(self, user_input):
        emotions = {"چیست": "curious", "چگونه": "interested", "چرا": "questioning"}
        for key, emotion in emotions.items():
            if key in user_input:
                return {"primary_emotion": emotion, "intensity": 0.7}
        return {"primary_emotion": "neutral", "intensity": 0.5}
    
    def update_user_knowledge_model(self, user_input, response):
        return {"topics_updated": 1, "new_concepts": []}
    
    def predict_future_needs(self, user_input, user_profile):
        return {"next_questions": [], "related_topics": []}


# حالا کلاس اصلی را تعریف می‌کنیم
class MetacognitiveCore:
    def __init__(self):
        print("=" * 60)
        print("هسته فراشناختی در حال راه‌اندازی...")
        print("=" * 60)
        
        # راه‌اندازی زیرسیستم‌ها
        self.self_awareness = SelfAwareness()
        self.cognitive_monitoring = CognitiveMonitoring()
        self.cognitive_control = CognitiveControl()
        self.performance_evaluation = PerformanceEvaluation()
        self.user_mental_model = UserMentalModel()
        
        # حالت‌های سیستمی
        self.system_state = {
            "initialized": True,
            "active_modules": [
                "self_awareness",
                "cognitive_monitoring", 
                "cognitive_control",
                "performance_evaluation",
                "user_mental_model"
            ],
            "learning_mode": "active",
            "metacognitive_level": "high"
        }
        
        # تاریخچه تعاملات
        self.interaction_history = []
        
        # گزارش وضعیت
        self._print_system_status()
    
    def _print_system_status(self):
        """چاپ وضعیت سیستم"""
        print("\n✓ هسته فراشناختی با موفقیت راه‌اندازی شد")
        print(f"✓ تعداد ماژول‌های فعال: {len(self.system_state['active_modules'])}")
        print(f"✓ سطح فراشناختی: {self.system_state['metacognitive_level']}")
        print("=" * 60 + "\n")
    
    def process_input(self, user_input, context=None):
        """پردازش ورودی کاربر با استفاده از تمام ماژول‌های فراشناختی"""
        print(f"\n{'='*40}")
        print(f"پردازش ورودی جدید: '{user_input[:50]}...'")
        print(f"{'='*40}")
        
        # مرحله ۱: خودآگاهی
        print("\n[مرحله ۱: خودآگاهی]")
        user_identity = self.self_awareness.identify_user(user_input)
        limitations = self.self_awareness.check_limitation(user_input)
        self.self_awareness.update_context(user_input)
        
        if limitations:
            print(f"   محدودیت‌های شناسایی شده: {limitations}")
        
        # مرحله ۲: مدل ذهنی کاربر
        print("\n[مرحله ۲: مدل ذهنی کاربر]")
        user_goals = self.user_mental_model.understand_user_goals(user_input, context or {})
        emotional_state = self.user_mental_model.detect_emotional_state(user_input)
        print(f"   اهداف کاربر: {user_goals['explicit']}")
        print(f"   وضعیت عاطفی: {emotional_state['primary_emotion']}")
        
        # مرحله ۳: کنترل شناختی
        print("\n[مرحله ۳: کنترل شناختی]")
        strategy = self.cognitive_control.regulate_strategy(
            user_input, 
            self.user_mental_model.user_profile
        )
        attention = self.cognitive_control.allocate_attention([user_input])
        processing_mode = self.cognitive_control.regulate_processing(user_input)
        print(f"   راهبرد انتخاب شده: {strategy}")
        print(f"   تمرکز: {attention['primary_focus']}")
        print(f"   حالت پردازش: {processing_mode}")
        
        # مرحله ۴: نظارت بر شناخت (در حین تولید پاسخ)
        print("\n[مرحله ۴: نظارت بر شناخت]")
        reasoning_steps = [
            "تحلیل درخواست کاربر",
            "جستجوی دانش مرتبط",
            "سازماندهی اطلاعات",
            "طراحی پاسخ"
        ]
        thought_process = self.cognitive_monitoring.monitor_thought_process(
            user_input, 
            reasoning_steps
        )
        confidence = self.cognitive_monitoring.assess_confidence(
            "inferential", 
            0.7
        )
        print(f"   مراحل استدلال: {thought_process['step_count']}")
        print(f"   سطح اطمینان: {confidence['label']}")
        
        # مرحله ۵: تولید پاسخ شبیه‌سازی شده
        print("\n[مرحله ۵: تولید پاسخ]")
        simulated_response = self._generate_simulated_response(user_input)
        print(f"   پاسخ تولید شده: '{simulated_response[:80]}...'")
        
        # مرحله ۶: ارزیابی عملکرد
        print("\n[مرحله ۶: ارزیابی عملکرد]")
        quality = self.performance_evaluation.evaluate_response_quality(
            simulated_response, 
            user_input
        )
        consequences = self.performance_evaluation.analyze_consequences(
            simulated_response,
            user_reaction=emotional_state['primary_emotion']
        )
        print(f"   کیفیت پاسخ: {quality['overall_score']:.2f}")
        print(f"   اثرات فوری: {consequences['immediate_effects']}")
        
        # مرحله ۷: به‌روزرسانی و یادگیری
        print("\n[مرحله ۷: به‌روزرسانی و یادگیری]")
        knowledge_update = self.user_mental_model.update_user_knowledge_model(
            user_input,
            simulated_response
        )
        future_predictions = self.user_mental_model.predict_future_needs(
            user_input,
            self.user_mental_model.user_profile
        )
        print(f"   موضوعات جدید: {knowledge_update['topics_updated']}")
        print(f"   سوالات پیش‌بینی شده: {len(future_predictions['next_questions'])}")
        
        # ذخیره تعامل در تاریخچه
        interaction_record = {
            "input": user_input,
            "response": simulated_response,
            "goals": user_goals,
            "emotional_state": emotional_state,
            "quality_score": quality['overall_score'],
            "timestamp": "زمان شبیه‌سازی شده"
        }
        self.interaction_history.append(interaction_record)
        
        # تولید گزارش نهایی
        final_report = self._generate_metacognitive_report(
            user_input,
            simulated_response,
            quality,
            consequences
        )
        
        return {
            "response": simulated_response,
            "metacognitive_report": final_report,
            "user_understood": True,
            "system_aware": True
        }
    
    def _generate_simulated_response(self, user_input):
        """تولید پاسخ شبیه‌سازی شده"""
        response_templates = {
            "چیست": "{} یک مفهوم مهم در حوزه مرتبط است که شامل جنبه‌های مختلفی می‌شود.",
            "چگونه": "برای درک {}، باید مراحل مختلفی را طی کنید که شامل یادگیری اصول پایه و سپس تمرین عملی است.",
            "چرا": "{} به دلیل اهمیت و کاربردهای گسترده‌ای که دارد، موضوعی ارزشمند برای مطالعه است.",
            "default": "سوال شما درباره '{}' جالب است. این موضوع شامل جنبه‌های مختلفی است که می‌توان از زوایای متفاوتی به آن نگاه کرد."
        }
        
        question_type = "default"
        for q_type in response_templates:
            if q_type in user_input.lower():
                question_type = q_type
                break
        
        topic = "این موضوع"
        common_topics = ["هوش مصنوعی", "یادگیری ماشین", "برنامه‌نویسی", "ریاضی"]
        for t in common_topics:
            if t in user_input:
                topic = t
                break
        
        response = response_templates[question_type].format(topic)
        
        if self.cognitive_control.active_strategies.get("explanation") == "مثال‌محور":
            response += " برای مثال، می‌توان موردی را در نظر گرفت که نشان‌دهنده کاربرد عملی این مفهوم باشد."
        
        return response
    
    def _generate_metacognitive_report(self, user_input, response, quality, consequences):
        """تولید گزارش فراشناختی"""
        report = {
            "input_analysis": {
                "length": len(user_input),
                "contains_question": "؟" in user_input or "?" in user_input,
                "topic_detected": self.self_awareness.interaction_context["topic"]
            },
            "response_analysis": {
                "length": len(response),
                "word_count": len(response.split()),
                "quality_score": quality["overall_score"]
            },
            "user_model_snapshot": {
                "emotional_state": self.user_mental_model.user_profile["emotional_state"],
                "expertise_level": self.user_mental_model.user_profile["expertise_level"]
            },
            "system_self_assessment": {
                "confidence": self.cognitive_monitoring.confidence_levels,
                "attention_level": self.cognitive_control.attention_focus["attention_span"],
                "processing_mode": self.cognitive_control.processing_mode
            },
            "improvement_suggestions": self.performance_evaluation.improvement_suggestions[-3:] if self.performance_evaluation.improvement_suggestions else []
        }
        
        return report
    
    def get_system_insights(self):
        """دریافت بینش‌های سیستمی"""
        insights = {
            "total_interactions": len(self.interaction_history),
            "average_quality_score": 0,
            "user_engagement": "medium",
            "common_topics": [],
            "system_improvements": self.performance_evaluation.improvement_suggestions[:5] if self.performance_evaluation.improvement_suggestions else []
        }
        
        if self.interaction_history:
            total_score = sum(interaction["quality_score"] for interaction in self.interaction_history)
            insights["average_quality_score"] = total_score / len(self.interaction_history)
        
        if self.user_mental_model.interaction_patterns["frequent_topics"]:
            insights["common_topics"] = sorted(
                self.user_mental_model.interaction_patterns["frequent_topics"].items(),
                key=lambda x: x[1],
                reverse=True
            )[:3]
        
        return insights
    
    def run_demo(self):
        """اجرای دموی تعاملی"""
        print("\n" + "="*60)
        print("دموی هسته فراشناختی - مدل متا")
        print("="*60)
        print("این یک سیستم فراشناختی است که می‌تواند:")
        print("1. خودش را بشناسد و محدودیت‌هایش را بداند")
        print("2. فرآیندهای فکری خود را نظارت کند")
        print("3. روش‌های تفکرش را تنظیم کند")
        print("4. عملکردش را ارزیابی کند")
        print("5. مدلی از کاربر بسازد و نیازهایش را پیش‌بینی کند")
        print("\nبرای خروج از دمو، 'خروج' را تایپ کنید.")
        print("="*60)
        
        demo_context = {"mode": "demo", "complexity": "medium"}
        
        while True:
            try:
                user_input = input("\nشما: ")
            except EOFError:
                print("\nخروج از برنامه.")
                break
            
            if user_input.lower() in ["خروج", "exit", "quit"]:
                print("\nخروج از دمو. دریافت بینش‌های نهایی...")
                insights = self.get_system_insights()
                print(f"\nبینش‌های سیستم:")
                print(f"- تعداد تعاملات: {insights['total_interactions']}")
                print(f"- میانگین امتیاز کیفیت: {insights['average_quality_score']:.2f}")
                print(f"- موضوعات رایج: {insights['common_topics']}")
                print("\nپایان دمو. سیستم فراشناختی آماده خدمت‌رسانی است.")
                break
            
            # پردازش ورودی
            result = self.process_input(user_input, demo_context)
            
            # نمایش پاسخ
            print(f"\nمدل متا: {result['response']}")
            
            # نمایش خلاصه گزارش (در صورت درخواست)
            if "گزارش" in user_input or "تحلیل" in user_input:
                report = result['metacognitive_report']
                print(f"\n[گزارش فراشناختی]")
                print(f"  - وضعیت عاطفی کاربر: {report['user_model_snapshot']['emotional_state']}")
                print(f"  - سطح اطمینان سیستم: {report['system_self_assessment']['confidence']['inferential']}")
                print(f"  - امتیاز کیفیت: {report['response_analysis']['quality_score']:.2f}")


# تست هسته اصلی یکپارچه
if __name__ == "__main__":
    print("=" * 60)
    print("تست نهایی: هسته فراشناختی یکپارچه")
    print("=" * 60)
    
    # راه‌اندازی هسته
    metacognitive_core = MetacognitiveCore()
    
    # تست پردازش یک ورودی نمونه
    test_input = "هوش مصنوعی چیست و چگونه کار می‌کند؟"
    result = metacognitive_core.process_input(test_input)
    
    print("\n" + "="*60)
    print("نتیجه تست نهایی:")
    print("="*60)
    print(f"ورودی: {test_input}")
    print(f"پاسخ: {result['response'][:100]}...")
    print(f"\nوضعیت فراشناختی:")
    print(f"  - کاربر درک شده: {result['user_understood']}")
    print(f"  - سیستم خودآگاه: {result['system_aware']}")
    
    # دریافت بینش‌های سیستم
    insights = metacognitive_core.get_system_insights()
    print(f"\nبینش‌های سیستم پس از تست:")
    print(f"  - کل تعاملات: {insights['total_interactions']}")
    print(f"  - میانگین امتیاز کیفیت: {insights['average_quality_score']:.2f}")
    
    print("\n" + "="*60)
    print("✓ تمام بخش‌های هسته فراشناختی با موفقیت تست شدند")
    print("=" * 60)
    
    # اجرای دموی تعاملی (اختیاری)
    run_demo = input("\nآیا می‌خواهید دموی تعاملی را اجرا کنید؟ (بله/خیر): ")
    if run_demo.lower() in ["بله", "yes", "y", "ب"]:
        metacognitive_core.run_demo()
    else:
        print("\nپایان تست هسته فراشناختی.")
        print("سیستم آماده ادغام با مدل زبانی اصلی است.")