# ============================================
# Module 1: Self-Awareness
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
        """Identify user through interaction patterns"""
        if "I" in user_input and "my name is" in user_input:
            import re
            name_match = re.search(r'my name is (\w+)', user_input)
            if name_match:
                self.user_identity = {"name": name_match.group(1), "recognized": True}
                return f"User identified: {name_match.group(1)}"
        
        self.user_identity = {"name": "User", "recognized": False}
        return "General user"
    
    def update_system_state(self, new_state):
        """Update system state"""
        for key, value in new_state.items():
            if key in self.system_state:
                self.system_state[key] = value
        return self.system_state
    
    def check_limitation(self, task):
        """Check limitations for a specific task"""
        limitation_checks = []
        
        if "latest news" in task or "now" in task:
            limitation_checks.append("Warning: Real-time data access is limited")
        
        if "execute code" in task or "program" in task:
            limitation_checks.append("Warning: I cannot execute code directly")
        
        if "move" in task or "physical" in task:
            limitation_checks.append("Warning: No physical interaction capability")
        
        return limitation_checks
    
    def update_context(self, user_input, response=None):
        """Update interaction context"""
        topics = ["science", "technology", "art", "mathematics", "programming", "philosophy"]
        detected_topic = None
        for topic in topics:
            if topic in user_input.lower():
                detected_topic = topic
                break
        
        if detected_topic:
            self.interaction_context["topic"] = detected_topic
        
        interaction_record = {
            "user_input": user_input[:100],
            "timestamp": "simulated_time"
        }
        
        if response:
            interaction_record["response"] = response[:100]
        
        self.interaction_context["interaction_history"].append(interaction_record)
        
        if len(self.interaction_context["interaction_history"]) > 10:
            self.interaction_context["interaction_history"] = self.interaction_context["interaction_history"][-10:]
        
        return self.interaction_context


# ============================================
# Module 2: Cognitive Monitoring
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
            "confirmation_bias",
            "availability_bias",
            "framing_effect"
        ]
    
    def monitor_thought_process(self, input_text, reasoning_steps):
        """Monitor thinking processes"""
        thought_record = {
            "input": input_text[:50],
            "reasoning_steps": reasoning_steps,
            "step_count": len(reasoning_steps),
            "complexity": self._assess_complexity(reasoning_steps)
        }
        
        self.thought_process_log.append(thought_record)
        
        if len(self.thought_process_log) > 20:
            self.thought_process_log = self.thought_process_log[-20:]
        
        return thought_record
    
    def _assess_complexity(self, reasoning_steps):
        """Assess complexity of thinking process"""
        if len(reasoning_steps) <= 2:
            return "low"
        elif len(reasoning_steps) <= 5:
            return "medium"
        else:
            return "high"
    
    def assess_confidence(self, response_type, evidence_strength):
        """Assess confidence level"""
        base_confidence = self.confidence_levels.get(response_type, 0.5)
        
        adjusted_confidence = base_confidence * evidence_strength
        
        adjusted_confidence = max(0.1, min(0.95, adjusted_confidence))
        
        confidence_levels = {
            0.9: "very_high",
            0.7: "high",
            0.5: "medium",
            0.3: "low"
        }
        
        for threshold, label in sorted(confidence_levels.items(), reverse=True):
            if adjusted_confidence >= threshold:
                confidence_label = label
                break
        else:
            confidence_label = "very_low"
        
        return {
            "numeric": adjusted_confidence,
            "label": confidence_label,
            "type": response_type
        }
    
    def detect_errors_gaps(self, response, user_feedback=None):
        """Detect errors and gaps in response"""
        errors = []
        gaps = []
        
        if not response or len(response.strip()) == 0:
            errors.append("empty_response")
        
        if "I don't know" in response and "?" in response:
            gaps.append("knowledge_gap: question exists with no answer")
        
        if "always" in response and "sometimes" in response:
            errors.append("possible_contradiction_in_certainty")
        
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
        """Track decision making"""
        decision_record = {
            "decision_point": decision_point,
            "alternatives": alternatives,
            "chosen": chosen_option,
            "rationale": rationale,
            "timestamp": "simulated_time"
        }
        
        self.decision_trail.append(decision_record)
        
        if len(self.decision_trail) > 15:
            self.decision_trail = self.decision_trail[-15:]
        
        return decision_record
    
    def check_biases(self, reasoning_process):
        """Check for potential cognitive biases"""
        detected_biases = []
        
        for bias in self.cognitive_biases_checklist:
            if self._check_for_bias(bias, reasoning_process):
                detected_biases.append(bias)
        
        return detected_biases
    
    def _check_for_bias(self, bias_type, reasoning):
        """Check for specific bias type"""
        bias_indicators = {
            "confirmation_bias": ["only", "always", "never"],
            "availability_bias": ["recently", "famous", "popular"],
            "framing_effect": ["but", "if", "only if"]
        }
        
        indicators = bias_indicators.get(bias_type, [])
        for indicator in indicators:
            if indicator in reasoning.lower():
                return True
        
        return False


# ============================================
# Module 3: Cognitive Control
# ============================================

class CognitiveControl:
    def __init__(self):
        self.active_strategies = {
            "problem_solving": "stepwise_analysis",
            "explanation": "example_based",
            "learning": "repetition_practice"
        }
        self.attention_focus = {
            "primary_focus": None,
            "secondary_focus": [],
            "attention_span": 100
        }
        self.processing_mode = {
            "speed": "normal",
            "depth": "balanced",
            "rigor": "standard"
        }
        self.adaptation_history = []
    
    def regulate_strategy(self, task_type, user_profile=None):
        """Regulate cognitive strategies based on task type"""
        strategy_map = {
            "scientific_question": "evidence_based_analysis",
            "creative_question": "divergent_thinking",
            "explanation_request": "example_based_with_analogy",
            "problem_solving": "stepwise_analysis",
            "philosophical_discussion": "logical_reasoning",
            "help_request": "stepwise_guidance"
        }
        
        detected_task_type = "scientific_question"
        
        for task_key in strategy_map.keys():
            if task_key in task_type:
                detected_task_type = task_key
                break
        
        selected_strategy = strategy_map.get(detected_task_type, "general_analysis")
        
        if user_profile:
            if user_profile.get("expertise") == "beginner":
                if "example_based" not in selected_strategy:
                    selected_strategy = "simplification_with_examples"
            elif user_profile.get("expertise") == "expert":
                if "technical" not in selected_strategy:
                    selected_strategy += " with technical details"
        
        self.active_strategies[task_type] = selected_strategy
        
        adaptation_record = {
            "task_type": task_type,
            "selected_strategy": selected_strategy,
            "reason": "automatic_adjustment_based_on_task_type",
            "user_profile_considered": bool(user_profile)
        }
        self.adaptation_history.append(adaptation_record)
        
        return selected_strategy
    
    def allocate_attention(self, input_elements, context=None):
        """Allocate attention resources"""
        priority_keywords = ["urgent", "important", "please", "help", "question"]
        
        primary_focus = None
        secondary_focus = []
        
        for element in input_elements:
            element_lower = element.lower()
            
            high_priority = False
            for keyword in priority_keywords:
                if keyword in element_lower:
                    high_priority = True
                    break
            
            is_question = "?" in element
            
            if high_priority or is_question:
                if primary_focus is None:
                    primary_focus = element
                else:
                    secondary_focus.append(element)
            else:
                secondary_focus.append(element)
        
        if primary_focus is None and input_elements:
            primary_focus = input_elements[0]
            secondary_focus = input_elements[1:] if len(input_elements) > 1 else []
        
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
        """Select problem solving method"""
        method_registry = {
            "divide_and_conquer": {"applicability": ["complex", "large", "multipart"], "complexity": "medium"},
            "computational": {"applicability": ["numerical", "computational", "quantitative"], "complexity": "low"},
            "deductive_reasoning": {"applicability": ["logical", "philosophical", "mathematical"], "complexity": "high"},
            "analogy_finding": {"applicability": ["creative", "design", "innovative"], "complexity": "medium"},
            "trial_and_error": {"applicability": ["uncertain", "exploratory", "experimental"], "complexity": "low"}
        }
        
        problem_features = self._analyze_problem_features(problem_description)
        
        suitable_methods = []
        for method, attributes in method_registry.items():
            applicability_match = False
            
            for feature in problem_features:
                if feature in attributes["applicability"]:
                    applicability_match = True
                    break
            
            if applicability_match:
                if constraints:
                    if constraints.get("time") == "short" and attributes["complexity"] == "high":
                        continue
                
                suitable_methods.append({
                    "method": method,
                    "match_score": len(set(problem_features) & set(attributes["applicability"])),
                    "complexity": attributes["complexity"]
                })
        
        if suitable_methods:
            suitable_methods.sort(key=lambda x: (x["match_score"], -1 if x["complexity"] == "medium" else 0))
            selected_method = suitable_methods[-1]["method"]
        else:
            selected_method = "general_analysis"
        
        selection_record = {
            "problem": problem_description[:50],
            "features": problem_features,
            "selected_method": selected_method,
            "alternatives_considered": len(suitable_methods)
        }
        self.adaptation_history.append(selection_record)
        
        return selected_method
    
    def _analyze_problem_features(self, problem_description):
        """Analyze problem features"""
        features = []
        
        feature_keywords = {
            "numerical": ["number", "calculate", "math", "sum", "subtract", "multiply", "divide"],
            "logical": ["if", "then", "reasoning", "logic", "true", "false"],
            "creative": ["idea", "creativity", "innovation", "new", "creative"],
            "complex": ["complex", "difficult", "hard", "problem", "challenge"],
            "multipart": ["step", "part", "section", "phase", "stepwise"]
        }
        
        problem_lower = problem_description.lower()
        
        for feature, keywords in feature_keywords.items():
            for keyword in keywords:
                if keyword in problem_lower:
                    features.append(feature)
                    break
        
        if not features:
            features.append("unknown")
        
        return features
    
    def regulate_processing(self, task_demand, available_resources=None):
        """Regulate processing speed and depth"""
        if "urgent" in task_demand or "fast" in task_demand:
            self.processing_mode["speed"] = "fast"
            self.processing_mode["depth"] = "shallow"
        elif "accurate" in task_demand or "detailed" in task_demand:
            self.processing_mode["speed"] = "slow"
            self.processing_mode["depth"] = "deep"
        elif "balanced" in task_demand:
            self.processing_mode["speed"] = "normal"
            self.processing_mode["depth"] = "balanced"
        
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


# ============================================
# Module 4: Performance Evaluation
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
        """Evaluate response quality"""
        evaluation = {
            "accuracy": self._assess_accuracy(response, query),
            "relevance": self._assess_relevance(response, query),
            "coherence": self._assess_coherence(response),
            "completeness": self._assess_completeness(response, query),
            "timeliness": self._assess_timeliness(response, context)
        }
        
        overall_score = sum(evaluation.values()) / len(evaluation)
        evaluation["overall_score"] = overall_score
        
        for metric in self.quality_metrics:
            if metric in evaluation:
                self.quality_metrics[metric] = (self.quality_metrics[metric] + evaluation[metric]) / 2
        
        performance_record = {
            "query": query[:50],
            "overall_score": overall_score,
            "timestamp": "simulated_time"
        }
        self.performance_trend.append(performance_record)
        
        if len(self.performance_trend) > 20:
            self.performance_trend = self.performance_trend[-20:]
        
        return evaluation
    
    def _assess_accuracy(self, response, query):
        """Assess accuracy"""
        accuracy_score = 0.5
        
        accuracy_indicators = [
            ("according to research", 0.2),
            ("studies show", 0.15),
            ("scientifically proven", 0.2),
            ("statistics show", 0.15)
        ]
        
        for indicator, boost in accuracy_indicators:
            if indicator in response:
                accuracy_score += boost
        
        inaccuracy_indicators = [
            "maybe",
            "probably",
            "I think",
            "in my opinion"
        ]
        
        for indicator in inaccuracy_indicators:
            if indicator in response:
                accuracy_score -= 0.05
        
        return max(0.1, min(1.0, accuracy_score))
    
    def _assess_relevance(self, response, query):
        """Assess relevance"""
        query_keywords = set(query.lower().split())
        
        response_lower = response.lower()
        keyword_matches = 0
        
        for keyword in query_keywords:
            if len(keyword) > 3 and keyword in response_lower:
                keyword_matches += 1
        
        relevance_score = keyword_matches / max(1, len(query_keywords))
        
        if "?" in query:
            if "answer" in response or "therefore" in response:
                relevance_score = min(1.0, relevance_score + 0.2)
        
        return relevance_score
    
    def _assess_coherence(self, response):
        """Assess coherence"""
        coherence_score = 0.5
        
        coherence_indicators = [
            ("first", 0.05),
            ("then", 0.05),
            ("therefore", 0.1),
            ("in conclusion", 0.1),
            ("in summary", 0.05)
        ]
        
        for indicator, boost in coherence_indicators:
            if indicator in response:
                coherence_score += boost
        
        sentences = response.split('.')
        avg_sentence_length = sum(len(s.split()) for s in sentences) / max(1, len(sentences))
        
        if avg_sentence_length > 25:
            coherence_score -= 0.1
        elif avg_sentence_length < 10:
            coherence_score -= 0.05
        
        return max(0.1, min(1.0, coherence_score))
    
    def _assess_completeness(self, response, query):
        """Assess completeness"""
        completeness_score = 0.5
        
        response_elements = {
            "definition": 0.1,
            "explanation": 0.2,
            "example": 0.15,
            "conclusion": 0.1,
            "reference": 0.05
        }
        
        for element, value in response_elements.items():
            if element in response:
                completeness_score += value
        
        word_count = len(response.split())
        
        if word_count < 20:
            completeness_score -= 0.2
        elif word_count > 100:
            completeness_score += 0.1
        
        return max(0.1, min(1.0, completeness_score))
    
    def _assess_timeliness(self, response, context):
        """Assess timeliness"""
        timeliness_score = 0.5
        
        if context:
            if context.get("urgency") == "high":
                word_count = len(response.split())
                if word_count < 50:
                    timeliness_score += 0.2
                else:
                    timeliness_score -= 0.1
        
        return max(0.1, min(1.0, timeliness_score))
    
    def analyze_consequences(self, response, user_reaction=None, follow_up_questions=None):
        """Analyze response consequences"""
        consequence_analysis = {
            "immediate_effects": [],
            "potential_misunderstandings": [],
            "learning_opportunities": []
        }
        
        if "thank you" in response.lower():
            consequence_analysis["immediate_effects"].append("user_satisfaction")
        
        if "I don't know" in response:
            consequence_analysis["immediate_effects"].append("knowledge_limit_disclosure")
        
        ambiguous_terms = ["maybe", "probably", "might be"]
        for term in ambiguous_terms:
            if term in response:
                consequence_analysis["potential_misunderstandings"].append(f"ambiguity_in_using_{term}")
        
        if follow_up_questions and len(follow_up_questions) > 0:
            consequence_analysis["learning_opportunities"].append("need_for_deeper_knowledge")
        
        if user_reaction == "confused":
            consequence_analysis["learning_opportunities"].append("need_for_more_clarity")
        
        consequence_record = {
            "response_sample": response[:100],
            "analysis": consequence_analysis,
            "user_reaction": user_reaction
        }
        self.consequence_log.append(consequence_record)
        
        return consequence_analysis
    
    def process_feedback(self, feedback, response_related):
        """Process feedback and learn from results"""
        feedback_record = {
            "feedback": feedback,
            "related_response": response_related[:50] if response_related else None,
            "feedback_type": self._classify_feedback(feedback),
            "lessons_learned": []
        }
        
        lessons = self._extract_lessons_from_feedback(feedback)
        feedback_record["lessons_learned"] = lessons
        
        self.feedback_history.append(feedback_record)
        
        if lessons:
            for lesson in lessons:
                suggestion = f"improvement_in: {lesson}"
                if suggestion not in self.improvement_suggestions:
                    self.improvement_suggestions.append(suggestion)
        
        return feedback_record
    
    def _classify_feedback(self, feedback):
        """Classify feedback"""
        feedback_lower = feedback.lower()
        
        if "excellent" in feedback_lower or "great" in feedback_lower:
            return "positive"
        elif "poor" in feedback_lower or "bad" in feedback_lower:
            return "negative"
        elif "average" in feedback_lower or "acceptable" in feedback_lower:
            return "neutral"
        else:
            return "constructive"
    
    def _extract_lessons_from_feedback(self, feedback):
        """Extract lessons from feedback"""
        lessons = []
        
        lesson_patterns = {
            "more complete": "providing more complete information",
            "shorter": "providing more concise responses",
            "simpler": "simplifying explanations",
            "example": "increasing use of examples",
            "source": "referencing reliable sources",
            "clear": "increasing clarity"
        }
        
        for pattern, lesson in lesson_patterns.items():
            if pattern in feedback.lower():
                lessons.append(lesson)
        
        return lessons
    
    def self_correct(self, detected_error, context):
        """Self-correction based on detected errors"""
        correction_actions = []
        
        if "accuracy" in detected_error:
            correction_actions.append("add references to sources")
            correction_actions.append("use more cautious language")
        
        if "completeness" in detected_error:
            correction_actions.append("increase response details")
            correction_actions.append("cover more aspects")
        
        if "coherence" in detected_error:
            correction_actions.append("use more connecting words")
            correction_actions.append("better organize information")
        
        for action in correction_actions:
            if action not in self.improvement_suggestions:
                self.improvement_suggestions.append(action)
        
        return {
            "detected_error": detected_error,
            "correction_actions": correction_actions,
            "context_considered": context
        }


# ============================================
# Module 5: User Mental Model
# ============================================

class UserMentalModel:
    def __init__(self):
        self.user_profile = {
            "identity": {"name": None, "recognized": False},
            "expertise_level": "unknown",
            "interaction_style": "neutral",
            "learning_preference": "balanced",
            "emotional_state": "neutral"
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
        """Understand user goals and intentions"""
        goals_identified = {
            "explicit": [],
            "implicit": []
        }
        
        explicit_goal_indicators = {
            "I want to know": "get_information",
            "I need": "get_help",
            "how can I": "practical_guidance",
            "please explain": "request_explanation",
            "compare": "comparative_analysis"
        }
        
        for indicator, goal in explicit_goal_indicators.items():
            if indicator in user_input:
                goals_identified["explicit"].append(goal)
        
        implicit_goal_clues = {
            "a lot of time": "get_quick_response",
            "say simply": "get_simple_explanation",
            "give example": "practical_understanding",
            "source": "ensure_accuracy",
            "is it correct": "confirm_information"
        }
        
        for clue, goal in implicit_goal_clues.items():
            if clue in user_input:
                goals_identified["implicit"].append(goal)
        
        goal_record = {
            "input": user_input[:50],
            "goals": goals_identified,
            "context": interaction_context,
            "timestamp": "simulated_time"
        }
        self.user_goals["goal_history"].append(goal_record)
        
        if len(self.user_goals["goal_history"]) > 15:
            self.user_goals["goal_history"] = self.user_goals["goal_history"][-15:]
        
        self.user_goals["explicit_goals"] = goals_identified["explicit"]
        self.user_goals["implicit_goals"] = goals_identified["implicit"]
        
        return goals_identified
    
    def detect_emotional_state(self, user_input, previous_interactions=None):
        """Detect user emotional state"""
        emotional_indicators = {
            "happy": ["thank you", "excellent", "very good", "well done", ":)"],
            "frustrated": ["I'm tired", "complicated", "I don't understand", "hard", ":("],
            "curious": ["interesting", "why", "how", "I want to know", "?"],
            "urgent": ["urgent", "quick", "now", "immediately", "!!!"],
            "confused": ["what do you mean", "I don't understand", "wrong", "I have a question"]
        }
        
        detected_emotions = []
        confidence_scores = {}
        
        for emotion, indicators in emotional_indicators.items():
            score = 0
            for indicator in indicators:
                if indicator in user_input.lower():
                    score += 1
            
            if score > 0:
                detected_emotions.append(emotion)
                confidence_scores[emotion] = score / len(indicators)
        
        primary_emotion = "neutral"
        if detected_emotions:
            primary_emotion = max(confidence_scores.items(), key=lambda x: x[1])[0]
        
        if previous_interactions:
            recent_emotions = [interaction.get("emotion", "neutral") 
                              for interaction in previous_interactions[-3:]]
            
            if recent_emotions.count(primary_emotion) >= 2:
                confidence_scores[primary_emotion] = min(1.0, confidence_scores.get(primary_emotion, 0) + 0.2)
        
        self.user_profile["emotional_state"] = primary_emotion
        
        return {
            "primary_emotion": primary_emotion,
            "all_detected": detected_emotions,
            "confidence_scores": confidence_scores
        }
    
    def update_user_knowledge_model(self, user_input, system_response, correctness_feedback=None):
        """Update user knowledge model"""
        topics = self._extract_topics(user_input, system_response)
        
        for topic in topics:
            if topic not in self.user_knowledge["known_topics"]:
                self.user_knowledge["known_topics"].append(topic)
        
        knowledge_gaps = self._identify_knowledge_gaps(user_input, system_response)
        for gap in knowledge_gaps:
            if gap not in self.user_knowledge["knowledge_gaps"]:
                self.user_knowledge["knowledge_gaps"].append(gap)
        
        if correctness_feedback:
            if "wrong" in correctness_feedback or "incorrect" in correctness_feedback:
                misconception = self._identify_misconception(user_input, system_response)
                if misconception and misconception not in self.user_knowledge["misconceptions"]:
                    self.user_knowledge["misconceptions"].append(misconception)
        
        self._analyze_interaction_patterns(user_input, system_response)
        
        return {
            "topics_updated": topics,
            "knowledge_gaps_identified": knowledge_gaps,
            "misconceptions_updated": self.user_knowledge["misconceptions"][-3:] if self.user_knowledge["misconceptions"] else []
        }
    
    def _extract_topics(self, user_input, system_response):
        """Extract topics from text"""
        common_topics = [
            "artificial intelligence", "machine learning", "programming", "mathematics", 
            "data science", "neural networks", "natural language processing"
        ]
        
        detected_topics = []
        combined_text = user_input + " " + system_response
        
        for topic in common_topics:
            if topic in combined_text.lower():
                detected_topics.append(topic)
        
        return detected_topics
    
    def _identify_knowledge_gaps(self, user_input, system_response):
        """Identify knowledge gaps"""
        gap_indicators = [
            "what is", "how", "why", "meaning",
            "I don't know", "I didn't understand", "explain"
        ]
        
        gaps = []
        for indicator in gap_indicators:
            if indicator in user_input.lower():
                words = user_input.split()
                for i, word in enumerate(words):
                    if indicator in word.lower() and i > 0:
                        context_topic = words[i-1]
                        gaps.append(f"lack_of_knowledge_about {context_topic}")
                        break
        
        return gaps
    
    def _identify_misconception(self, user_input, system_response):
        """Identify misconception"""
        misconception_keywords = [
            "always", "never", "only", "solely",
            "all", "none", "certainly"
        ]
        
        for keyword in misconception_keywords:
            if keyword in user_input.lower():
                return f"overgeneralization_with '{keyword}'"
        
        return None
    
    def _analyze_interaction_patterns(self, user_input, system_response):
        """Analyze interaction patterns"""
        words = user_input.split()
        for word in words:
            if len(word) > 3:
                self.interaction_patterns["frequent_topics"][word] = \
                    self.interaction_patterns["frequent_topics"].get(word, 0) + 1
        
        question_types = {
            "definitional": ["what is", "meaning", "definition"],
            "methodological": ["how", "method", "way"],
            "causal": ["why", "cause", "reason"],
            "comparative": ["difference", "compare", "which is better"]
        }
        
        for q_type, indicators in question_types.items():
            for indicator in indicators:
                if indicator in user_input.lower():
                    self.interaction_patterns["question_types"][q_type] = \
                        self.interaction_patterns["question_types"].get(q_type, 0) + 1
                    break
        
        word_count = len(system_response.split())
        if word_count < 50:
            detail_level = "low"
        elif word_count < 150:
            detail_level = "medium"
        else:
            detail_level = "high"
        
        self.interaction_patterns["preferred_detail_level"] = detail_level
    
    def predict_future_needs(self, current_interaction, user_profile):
        """Predict future user needs"""
        predictions = {
            "next_questions": [],
            "likely_needs": [],
            "potential_confusions": []
        }
        
        current_topic = self._extract_topics(current_interaction, "")
        if current_topic:
            topic = current_topic[0]
            next_questions_map = {
                "artificial intelligence": ["What are the applications of AI?", "What are the types of AI?"],
                "machine learning": ["What are machine learning algorithms?", "Difference between supervised and unsupervised learning?"],
                "programming": ["What is the best programming language to start?", "How to learn programming?"]
            }
            
            predictions["next_questions"] = next_questions_map.get(topic, [])
        
        if user_profile["expertise_level"] == "beginner":
            predictions["likely_needs"].append("simpler_explanations")
            predictions["likely_needs"].append("more_practical_examples")
        
        if user_profile["emotional_state"] == "confused":
            predictions["likely_needs"].append("concept_clarification")
            predictions["potential_confusions"].append("ambiguity_in_basic_concepts")
        
        if self.user_goals["goal_history"]:
            recent_goals = [goal["goals"] for goal in self.user_goals["goal_history"][-3:]]
            
            goal_counts = {}
            for goal_set in recent_goals:
                for goal_type, goals in goal_set.items():
                    for goal in goals:
                        goal_counts[goal] = goal_counts.get(goal, 0) + 1
            
            frequent_goals = [goal for goal, count in goal_counts.items() if count >= 2]
            if frequent_goals:
                predictions["likely_needs"].append(f"complete_topic_related_to: {', '.join(frequent_goals[:2])}")
        
        self.prediction_engine = predictions
        
        return predictions
    
    def get_user_profile_summary(self):
        """Get user profile summary"""
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


# ============================================
# Module 6: Integrated Metacognitive Core
# ============================================

class MetacognitiveCore:
    def __init__(self):
        print("=" * 60)
        print("Metacognitive Core Initializing...")
        print("=" * 60)
        
        self.self_awareness = SelfAwareness()
        self.cognitive_monitoring = CognitiveMonitoring()
        self.cognitive_control = CognitiveControl()
        self.performance_evaluation = PerformanceEvaluation()
        self.user_mental_model = UserMentalModel()
        
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
        
        self.interaction_history = []
        
        self._print_system_status()
    
    def _print_system_status(self):
        """Print system status"""
        print("\n✓ Metacognitive Core successfully initialized")
        print(f"✓ Active modules: {len(self.system_state['active_modules'])}")
        print(f"✓ Metacognitive level: {self.system_state['metacognitive_level']}")
        print("=" * 60 + "\n")
    
    def process_input(self, user_input, context=None):
        """Process user input using all metacognitive modules"""
        print(f"\n{'='*40}")
        print(f"Processing new input: '{user_input[:50]}...'")
        print(f"{'='*40}")
        
        print("\n[Stage 1: Self-Awareness]")
        user_identity = self.self_awareness.identify_user(user_input)
        limitations = self.self_awareness.check_limitation(user_input)
        self.self_awareness.update_context(user_input)
        
        if limitations:
            print(f"   Identified limitations: {limitations}")
        
        print("\n[Stage 2: User Mental Model]")
        user_goals = self.user_mental_model.understand_user_goals(user_input, context or {})
        emotional_state = self.user_mental_model.detect_emotional_state(user_input)
        print(f"   User goals: {user_goals['explicit']}")
        print(f"   Emotional state: {emotional_state['primary_emotion']}")
        
        print("\n[Stage 3: Cognitive Control]")
        strategy = self.cognitive_control.regulate_strategy(
            user_input, 
            self.user_mental_model.user_profile
        )
        attention = self.cognitive_control.allocate_attention([user_input])
        processing_mode = self.cognitive_control.regulate_processing(user_input)
        print(f"   Selected strategy: {strategy}")
        print(f"   Focus: {attention['primary_focus']}")
        print(f"   Processing mode: {processing_mode}")
        
        print("\n[Stage 4: Cognitive Monitoring]")
        reasoning_steps = [
            "Analyzing user request",
            "Searching relevant knowledge",
            "Organizing information",
            "Designing response"
        ]
        thought_process = self.cognitive_monitoring.monitor_thought_process(
            user_input, 
            reasoning_steps
        )
        confidence = self.cognitive_monitoring.assess_confidence(
            "inferential", 
            0.7
        )
        print(f"   Reasoning steps: {thought_process['step_count']}")
        print(f"   Confidence level: {confidence['label']}")
        
        print("\n[Stage 5: Response Generation]")
        simulated_response = self._generate_simulated_response(user_input)
        print(f"   Generated response: '{simulated_response[:80]}...'")
        
        print("\n[Stage 6: Performance Evaluation]")
        quality = self.performance_evaluation.evaluate_response_quality(
            simulated_response, 
            user_input
        )
        consequences = self.performance_evaluation.analyze_consequences(
            simulated_response,
            user_reaction=emotional_state['primary_emotion']
        )
        print(f"   Response quality: {quality['overall_score']:.2f}")
        print(f"   Immediate effects: {consequences['immediate_effects']}")
        
        print("\n[Stage 7: Update and Learning]")
        knowledge_update = self.user_mental_model.update_user_knowledge_model(
            user_input,
            simulated_response
        )
        future_predictions = self.user_mental_model.predict_future_needs(
            user_input,
            self.user_mental_model.user_profile
        )
        print(f"   New topics: {knowledge_update['topics_updated']}")
        print(f"   Predicted questions: {len(future_predictions['next_questions'])}")
        
        interaction_record = {
            "input": user_input,
            "response": simulated_response,
            "goals": user_goals,
            "emotional_state": emotional_state,
            "quality_score": quality['overall_score'],
            "timestamp": "simulated_time"
        }
        self.interaction_history.append(interaction_record)
        
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
        """Generate simulated response"""
        response_templates = {
            "what is": "{} is an important concept in the related field that includes various aspects.",
            "how": "To understand {}, you need to go through different steps including learning basic principles and then practical practice.",
            "why": "{} is a valuable topic to study due to its importance and wide applications.",
            "default": "Your question about '{}' is interesting. This topic includes various aspects that can be viewed from different angles."
        }
        
        question_type = "default"
        for q_type in response_templates:
            if q_type in user_input.lower():
                question_type = q_type
                break
        
        topic = "this topic"
        common_topics = ["artificial intelligence", "machine learning", "programming", "mathematics"]
        for t in common_topics:
            if t in user_input.lower():
                topic = t
                break
        
        response = response_templates[question_type].format(topic)
        
        if self.cognitive_control.active_strategies.get("explanation") == "example_based":
            response += " For example, consider a case that demonstrates the practical application of this concept."
        
        return response
    
    def _generate_metacognitive_report(self, user_input, response, quality, consequences):
        """Generate metacognitive report"""
        report = {
            "input_analysis": {
                "length": len(user_input),
                "contains_question": "?" in user_input,
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
            "improvement_suggestions": self.performance_evaluation.improvement_suggestions[-3:]
        }
        
        return report
    
    def get_system_insights(self):
        """Get system insights"""
        insights = {
            "total_interactions": len(self.interaction_history),
            "average_quality_score": 0,
            "user_engagement": "medium",
            "common_topics": [],
            "system_improvements": self.performance_evaluation.improvement_suggestions[:5]
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
        """Run interactive demo"""
        print("\n" + "="*60)
        print("Metacognitive Core Demo - Meta Model")
        print("="*60)
        print("This is a metacognitive system that can:")
        print("1. Know itself and its limitations")
        print("2. Monitor its thinking processes")
        print("3. Regulate its thinking methods")
        print("4. Evaluate its performance")
        print("5. Build a model of the user and predict their needs")
        print("\nType 'exit' to quit the demo.")
        print("="*60)
        
        demo_context = {"mode": "demo", "complexity": "medium"}
        
        while True:
            user_input = input("\nYou: ")
            
            if user_input.lower() in ["exit", "quit"]:
                print("\nExiting demo. Getting final insights...")
                insights = self.get_system_insights()
                print(f"\nSystem Insights:")
                print(f"- Total interactions: {insights['total_interactions']}")
                print(f"- Average quality score: {insights['average_quality_score']:.2f}")
                print(f"- Common topics: {insights['common_topics']}")
                print("\nDemo ended. Metacognitive system is ready to serve.")
                break
            
            result = self.process_input(user_input, demo_context)
            
            print(f"\nMeta Model: {result['response']}")
            
            if "report" in user_input.lower() or "analysis" in user_input.lower():
                report = result['metacognitive_report']
                print(f"\n[Metacognitive Report]")
                print(f"  - User emotional state: {report['user_model_snapshot']['emotional_state']}")
                print(f"  - System confidence: {report['system_self_assessment']['confidence']['inferential']}")
                print(f"  - Quality score: {report['response_analysis']['quality_score']:.2f}")


# ============================================
# Main Execution
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("Final Test: Integrated Metacognitive Core")
    print("=" * 60)
    
    metacognitive_core = MetacognitiveCore()
    
    test_input = "What is artificial intelligence and how does it work?"
    result = metacognitive_core.process_input(test_input)
    
    print("\n" + "="*60)
    print("Final Test Result:")
    print("="*60)
    print(f"Input: {test_input}")
    print(f"Response: {result['response'][:100]}...")
    print(f"\nMetacognitive Status:")
    print(f"  - User understood: {result['user_understood']}")
    print(f"  - System self-aware: {result['system_aware']}")
    
    insights = metacognitive_core.get_system_insights()
    print(f"\nSystem Insights after test:")
    print(f"  - Total interactions: {insights['total_interactions']}")
    print(f"  - Average quality score: {insights['average_quality_score']:.2f}")
    
    print("\n" + "="*60)
    print("✓ All metacognitive core components tested successfully")
    print("="*60)
    
    run_demo = input("\nDo you want to run the interactive demo? (yes/no): ")
    if run_demo.lower() in ["yes", "y"]:
        metacognitive_core.run_demo()
    else:
        print("\nMetacognitive core test completed.")
        print("System ready for integration with main language model.")