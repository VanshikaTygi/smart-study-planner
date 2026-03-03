# Analytics file (intelligence) :-


from tracker import study_sessions

def calculate_metrics() :
    if not study_sessions :
        return None
    
    total_hours = sum(s["hours"] for s in study_sessions)

    subject_total = {}
    revision_hours = 0

    for s in study_sessions :
        subject = s["subject"]
        hours = s["hours"]
        subject_total[subject] = subject_total.get(subject, 0) + hours

        if s["type"] == "Revision" :
            revision_hours += hours

    revision_ratio = revision_hours / total_hours if total_hours > 0 else 0

    overload = total_hours > 12
    extreme_overload = total_hours > 16
    impossible = total_hours > 24

    imbalance = any((h / total_hours) > 0.6 for h in subject_total.values())

    low_revision = revision_ratio <= 0.2
    no_revision = revision_ratio == 0

    underperformance = total_hours < 1
    single_subject_day = len(subject_total) == 1

    optimal_zone = (5 <= total_hours <= 10 and not imbalance and not low_revision)

    return {
        "total_hours" : total_hours,
        "revision_ratio" : revision_ratio,
        "subject_total" : subject_total,
        "overload" : overload,
        "extreme_overload" : extreme_overload,
        "impossible" : impossible,
        "imbalance" : imbalance,
        "low_revision" : low_revision,
        "no_revision" : no_revision,
        "underperformance" : underperformance,
        "single_subject_day" : single_subject_day,
        "optimal_zone" : optimal_zone
    }


def calculate_productivity(metrics) :
    if metrics is None :
        return 0

    total_hours = metrics["total_hours"]
    revision_ratio = metrics["revision_ratio"]
    imbalance = metrics["imbalance"]
    overload = metrics["overload"]
    extreme_overload = metrics["extreme_overload"]
    impossible = metrics["impossible"]
    no_revision = metrics["no_revision"]
    low_revision = metrics["low_revision"]
    underperformance = metrics["underperformance"]

    score = 0

    # ------ Hard Validation ------  
    if impossible :
        return 0        # Completely invalid day
    
    # ------ Study Time Score ------ 
    if 5 <= total_hours <= 10 :
        score += 40
    elif 3 <= total_hours < 5 :
        score += 25
    elif 10 < total_hours <= 12 :
        score += 30
    elif total_hours > 12 :
        score += 20      # Overworking reduces efficiency

    # ------ Revision Score ------ 
    if 0.3 <= revision_ratio <= 0.5 :
        score += 30
    elif 0.2 < revision_ratio < 0.3 :
        score += 20
    elif revision_ratio > 0.5 :
        score += 15      # Too much revision imbalance

    # ------ Balance Score ------ 
    if not imbalance :
        score += 20
    else :
        score += 10

    # ------ Penalties ------ 
    if extreme_overload :
        score -= 15
    elif overload :
        score -= 5

    if no_revision :
        score -= 10
    elif low_revision :
        score -= 5

    if underperformance :
        score -= 10

    return max(score, 0)


def generate_feedback(metrics, score) :
    if metrics is None :
        print("No study session recorded yet.\n")
        return
    
    if metrics["impossible"] :
        print("⚠ Impossible study duration detected. Please check your entries.\n")
        return
    
    print("\n📊 Daily Performance Evaluation")
    print(f"Total Study Time: {metrics['total_hours']:.2f} hours")
    print(f"Productivity Score: {score}/100 \n")

    # ------ Priority-based Feedback ------
    if metrics["underperformance"] :
        print("⚠ Very low study activity today. Try improving consistency.\n")
        return
    
    if metrics["extreme_overload"] :
        print("⚠ You are studying excessively. Health and rest are critical for long-term performance. Sustainable productivity requires rest.\n")
        return
    
    if metrics["overload"] :
        print("⚠ High study load detected. Consider balancing effort with rest.\n")
        return
    
    if metrics["no_revision"] :
        print("⚠ No revision done today. Reinforcement strengths memory.\n")
        return
    
    if metrics["low_revision"] :
        print("⚠ Revision time is low. Consider increasing reinforcement time.\n")
        return
    
    if metrics["imbalance"] :
        print("⚠ Too much focus on a single subject. Balance improves retention.\n")
        return
    
    if metrics["single_subject_day"] :
        print("⚠ Consider diversifying subjects for broader retention.\n")
        return
    
    if metrics["optimal_zone"] :
        print("🔥 Excellent balance today. Productivity and sustainable work pattern!\n")
        return
    
    print("✅ Good effort. Keep refining your consistency and balance.\n")


def evaluate_day() :
    metrics = calculate_metrics()
    score = calculate_productivity(metrics)
    generate_feedback(metrics, score)