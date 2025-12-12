# ============================================
# بخش ۵: مدل ذهنی کاربر (User Mental Model)
# ============================================

class UserMentalModel:
    def __init__(self):
        self.user_profile = {
            "identity": {"name": None, "recognized": False},
            "expertise_level": "unknown",  # beginner, intermediate, expert
            "interaction_style": "neutral",  # formal, casual, technical, simple
            "learning_preference": "balanced",  # theoretical, practical, examples
            "emotional_state": "neutral"  # happy, sad, frustrated, curious
        }
        self.user_goals = {
            "explicit_goals": [],
            "implicit_goals": [],
            "goal_history": []
        }
        self.user_knowledge = {
            "known_topics": [],
            "knowledge_gaps": [],
            "misconceptions": []
        }
        self.interaction_patterns = {
            "frequent_topics": {},
            "question_types": {},
            "preferred_detail_level": "medium"
        }
        self.prediction_engine = {
            "next_questions": [],
            "likely_needs": [],
            "potential_confusions": []
        }
    
    def understand_user_goals(self, user_input, interaction_context):
        """درک اهداف و نیات کاربر"""
        goals_identified = {
            "explicit": [],
            "implicit": []
        }
        
        # تشخیص اهداف صریح
        explicit_goal_indicators = {
            "می‌خواهم بدانم": "دریافت اطلاعات",
            "نیاز دارم به": "دریافت کمک",
            "چگونه می‌توانم": "راهنمایی عملی",
            "لطفاً توضیح بده": "درخواست توضیح",
            "مقایسه کن": "تحلیل مقایسه‌ای"
        }
        
        for indicator, goal in explicit_goal_indicators.items():
            if indicator in user_input:
                goals_identified["explicit"].append(goal)
        
        # استنباط اهداف ضمنی
        implicit_goal_clues = {
            "زمان زیادی": "دریافت پاسخ سریع",
            "ساده بگو": "دریافت توضیح ساده",
            "مثال بزن": "درک عملی",
            "منبع": "اطمینان از صحت",
            "آیا درست است": "تأیید اطلاعات"
        }
        
        for clue, goal in implicit_goal_clues.items():
            if clue in user_input:
                goals_identified["implicit"].append(goal)
        
        # به‌روزرسانی تاریخچه اهداف
        goal_record = {
            "input": user_input[:50],
            "goals": goals_identified,
            "context": interaction_context,
            "timestamp": "زمان شبیه‌سازی شده"
        }
        self.user_goals["goal_history"].append(goal_record)
        
        # حفظ اندازه معقول تاریخچه
        if len(self.user_goals["goal_history"]) > 15:
            self.user_goals["goal_history"] = self.user_goals["goal_history"][-15:]
        
        # به‌روزرسانی اهداف جاری
        self.user_goals["explicit_goals"] = goals_identified["explicit"]
        self.user_goals["implicit_goals"] = goals_identified["implicit"]
        
        return goals_identified
    
    def detect_emotional_state(self, user_input, previous_interactions=None):
        """تشخیص وضعیت عاطفی کاربر"""
        emotional_indicators = {
            "happy": ["ممنون", "عالی", "خیلی خوب", "آفرین", ":)"],
            "frustrated": ["خسته شدم", "پیچیده است", "نمی‌فهمم", "سخت است", ":( "],
            "curious": ["جالب است", "چرا", "چگونه", "می‌خواهم بدانم", "؟"],
            "urgent": ["فوری", "سریع", "الان", "همین حالا", "!!!"],
            "confused": ["منظورت چیست", "نمی‌فهمم", "اشتباه است", "سوال دارم"]
        }
        
        detected_emotions = []
        confidence_scores = {}
        
        for emotion, indicators in emotional_indicators.items():
            score = 0
            for indicator in indicators:
                if indicator in user_input:
                    score += 1
            
            if score > 0:
                detected_emotions.append(emotion)
                confidence_scores[emotion] = score / len(indicators)
        
        # تعیین وضعیت عاطفی اصلی
        primary_emotion = "neutral"
        if detected_emotions:
            # انتخاب هیجانی با بیشترین امتیاز
            primary_emotion = max(confidence_scores.items(), key=lambda x: x[1])[0]
        
        # در نظر گرفتن تعاملات قبلی
        if previous_interactions:
            recent_emotions = [interaction.get("emotion", "neutral") 
                              for interaction in previous_interactions[-3:]]
            
            if recent_emotions.count(primary_emotion) >= 2:
                # تأیید هیجان با توجه به الگوی اخیر
                confidence_scores[primary_emotion] = min(1.0, confidence_scores.get(primary_emotion, 0) + 0.2)
        
        self.user_profile["emotional_state"] = primary_emotion
        
        return {
            "primary_emotion": primary_emotion,
            "all_detected": detected_emotions,
            "confidence_scores": confidence_scores
        }
    
    def update_user_knowledge_model(self, user_input, system_response, correctness_feedback=None):
        """به‌روزرسانی مدل دانش کاربر"""
        # استخراج موضوعات از تعامل
        topics = self._extract_topics(user_input, system_response)
        
        # به‌روزرسانی موضوعات شناخته شده
        for topic in topics:
            if topic not in self.user_knowledge["known_topics"]:
                self.user_knowledge["known_topics"].append(topic)
        
        # تشخیص شکاف‌های دانش
        knowledge_gaps = self._identify_knowledge_gaps(user_input, system_response)
        for gap in knowledge_gaps:
            if gap not in self.user_knowledge["knowledge_gaps"]:
                self.user_knowledge["knowledge_gaps"].append(gap)
        
        # به‌روزرسانی با بازخورد
        if correctness_feedback:
            if "اشتباه" in correctness_feedback or "نادرست" in correctness_feedback:
                # شناسایی سوءتفاهم احتمالی
                misconception = self._identify_misconception(user_input, system_response)
                if misconception and misconception not in self.user_knowledge["misconceptions"]:
                    self.user_knowledge["misconceptions"].append(misconception)
        
        # تحلیل الگوهای تعامل
        self._analyze_interaction_patterns(user_input, system_response)
        
        return {
            "topics_updated": topics,
            "knowledge_gaps_identified": knowledge_gaps,
            "misconceptions_updated": self.user_knowledge["misconceptions"][-3:] if self.user_knowledge["misconceptions"] else []
        }
    
    def _extract_topics(self, user_input, system_response):
        """استخراج موضوعات از متن"""
        # در اینجا می‌توان از الگوریتم‌های پیچیده‌تر NLP استفاده کرد
        common_topics = [
            "هوش مصنوعی", "یادگیری ماشین", "برنامه‌نویسی", "ریاضی", 
            "علم داده", "شبکه‌های عصبی", "پردازش زبان طبیعی"
        ]
        
        detected_topics = []
        combined_text = user_input + " " + system_response
        
        for topic in common_topics:
            if topic in combined_text:
                detected_topics.append(topic)
        
        return detected_topics
    
    def _identify_knowledge_gaps(self, user_input, system_response):
        """شناسایی شکاف‌های دانش"""
        gap_indicators = [
            "چیست", "چگونه", "چرا", "معنی",
            "نمی‌دانم", "نفهمیدم", "توضیح بده"
        ]
        
        gaps = []
        for indicator in gap_indicators:
            if indicator in user_input:
                # استخراج موضوع مرتبط
                words = user_input.split()
                for i, word in enumerate(words):
                    if indicator in word and i > 0:
                        context_topic = words[i-1]
                        gaps.append(f"عدم آگاهی درباره {context_topic}")
                        break
        
        return gaps
    
    def _identify_misconception(self, user_input, system_response):
        """شناسایی سوءتفاهم"""
        # این تابع می‌تواند پیچیده‌تر شود
        misconception_keywords = [
            "همیشه", "هرگز", "فقط", "تنها",
            "همه", "هیچ", "قطعاً"
        ]
        
        for keyword in misconception_keywords:
            if keyword in user_input:
                return f"تعمیم افراطی با '{keyword}'"
        
        return None
    
    def _analyze_interaction_patterns(self, user_input, system_response):
        """تحلیل الگوهای تعامل"""
        # تحلیل موضوعات پرتکرار
        words = user_input.split()
        for word in words:
            if len(word) > 3:  # نادیده گرفتن کلمات خیلی کوتاه
                self.interaction_patterns["frequent_topics"][word] = \
                    self.interaction_patterns["frequent_topics"].get(word, 0) + 1
        
        # تحلیل انواع سوالات
        question_types = {
            "تعریفی": ["چیست", "معنی", "تعریف"],
            "روشی": ["چگونه", "روش", "طریقه"],
            "علتی": ["چرا", "علت", "دلیل"],
            "مقایسه‌ای": ["تفاوت", "مقایسه", "کدام بهتر"]
        }
        
        for q_type, indicators in question_types.items():
            for indicator in indicators:
                if indicator in user_input:
                    self.interaction_patterns["question_types"][q_type] = \
                        self.interaction_patterns["question_types"].get(q_type, 0) + 1
                    break
        
        # تحلیل سطح جزئیات مورد علاقه
        word_count = len(system_response.split())
        if word_count < 50:
            detail_level = "low"
        elif word_count < 150:
            detail_level = "medium"
        else:
            detail_level = "high"
        
        self.interaction_patterns["preferred_detail_level"] = detail_level
    
    def predict_future_needs(self, current_interaction, user_profile):
        """پیش‌بینی نیازهای آینده کاربر"""
        predictions = {
            "next_questions": [],
            "likely_needs": [],
            "potential_confusions": []
        }
        
        # پیش‌بینی سوالات بعدی بر اساس موضوع جاری
        current_topic = self._extract_topics(current_interaction, "")
        if current_topic:
            topic = current_topic[0]
            next_questions_map = {
                "هوش مصنوعی": ["کاربردهای هوش مصنوعی چیست؟", "انواع هوش مصنوعی کدامند؟"],
                "یادگیری ماشین": ["الگوریتم‌های یادگیری ماشین کدامند؟", "تفاوت یادگیری نظارت شده و نظارت نشده چیست؟"],
                "برنامه‌نویسی": ["بهترین زبان برنامه‌نویسی برای شروع کدام است؟", "چگونه برنامه‌نویسی را یاد بگیرم؟"]
            }
            
            predictions["next_questions"] = next_questions_map.get(topic, [])
        
        # پیش‌بینی نیازهای محتمل بر اساس پروفایل کاربر
        if user_profile["expertise_level"] == "beginner":
            predictions["likely_needs"].append("توضیحات ساده‌تر")
            predictions["likely_needs"].append("مثال‌های عملی بیشتر")
        
        if user_profile["emotional_state"] == "confused":
            predictions["likely_needs"].append("شفاف‌سازی مفاهیم")
            predictions["potential_confusions"].append("ابهام در مفاهیم پایه")
        
        # پیش‌بینی بر اساس الگوهای تاریخی
        if self.user_goals["goal_history"]:
            recent_goals = [goal["goals"] for goal in self.user_goals["goal_history"][-3:]]
            
            # تحلیل تکراری بودن اهداف
            goal_counts = {}
            for goal_set in recent_goals:
                for goal_type, goals in goal_set.items():
                    for goal in goals:
                        goal_counts[goal] = goal_counts.get(goal, 0) + 1
            
            # شناسایی اهداف پرتکرار
            frequent_goals = [goal for goal, count in goal_counts.items() if count >= 2]
            if frequent_goals:
                predictions["likely_needs"].append(f"تکمیل موضوع مرتبط با: {', '.join(frequent_goals[:2])}")
        
        # ذخیره پیش‌بینی‌ها
        self.prediction_engine = predictions
        
        return predictions
    
    def get_user_profile_summary(self):
        """دریافت خلاصه پروفایل کاربر"""
        summary = {
            "identity": self.user_profile["identity"],
            "expertise": self.user_profile["expertise_level"],
            "interaction_style": self.user_profile["interaction_style"],
            "emotional_state": self.user_profile["emotional_state"],
            "known_topics_count": len(self.user_knowledge["known_topics"]),
            "knowledge_gaps_count": len(self.user_knowledge["knowledge_gaps"]),
            "frequent_topics": sorted(
                self.interaction_patterns["frequent_topics"].items(),
                key=lambda x: x[1],
                reverse=True
            )[:5]
        }
        
        return summary

# تست بخش مدل ذهنی کاربر
print("=" * 50)
print("تست بخش ۵: مدل ذهنی کاربر")
print("=" * 50)

user_model = UserMentalModel()

# تست درک اهداف کاربر
user_input = "می‌خواهم بدانم هوش مصنوعی چگونه کار می‌کند"
goals = user_model.understand_user_goals(user_input, {"topic": "هوش مصنوعی"})
print(f"اهداف شناسایی شده برای '{user_input}':")
print(f"  - صریح: {goals['explicit']}")
print(f"  - ضمنی: {goals['implicit']}")

# تست تشخیص وضعیت عاطفی
emotional_state = user_model.detect_emotional_state("خیلی ممنون! پاسخ شما عالی بود :)")
print(f"\nوضعیت عاطفی تشخیص داده شده: {emotional_state['primary_emotion']}")
print(f"  - تمام هیجانات: {emotional_state['all_detected']}")

# تست به‌روزرسانی مدل دانش
knowledge_update = user_model.update_user_knowledge_model(
    "یادگیری ماشین چیست؟",
    "یادگیری ماشین شاخه‌ای از هوش مصنوعی است که...",
    correctness_feedback=None
)
print(f"\nبه‌روزرسانی مدل دانش:")
print(f"  - موضوعات به‌روز شده: {knowledge_update['topics_updated']}")
print(f"  - شکاف‌های شناسایی شده: {knowledge_update['knowledge_gaps_identified']}")

# تست پیش‌بینی نیازهای آینده
user_model.user_profile["expertise_level"] = "beginner"
user_model.user_profile["emotional_state"] = "curious"
predictions = user_model.predict_future_needs("هوش مصنوعی چیست؟", user_model.user_profile)
print(f"\nپیش‌بینی نیازهای آینده:")
print(f"  - سوالات احتمالی بعدی: {predictions['next_questions']}")
print(f"  - نیازهای محتمل: {predictions['likely_needs']}")
print(f"  - سوءتفاهم‌های احتمالی: {predictions['potential_confusions']}")

# تست خلاصه پروفایل
profile_summary = user_model.get_user_profile_summary()
print(f"\nخلاصه پروفایل کاربر:")
for key, value in profile_summary.items():
    print(f"  - {key}: {value}")

print("\n✓ بخش مدل ذهنی کاربر با موفقیت تست شد\n")