#!/usr/bin/env python3
"""Generates the static My Tribe Gym site (English at /, Arabic at /ar/).
Edit the data below (prices, schedule, coaches, texts) and run:  python3 build.py
"""
import os, urllib.parse

ROOT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- business data
PHONE = "+962797228865"
PHONE_DISPLAY = "+962 79 722 8865"
WA = "962797228865"
INSTAGRAM = "https://www.instagram.com/mytribegym"
YOUTUBE = "https://youtube.com/@mytribegym"
MAPS_LINK = "https://maps.app.goo.gl/XBnPt5Qfo8Q3GdXn6"
MAP_EMBED = "https://www.google.com/maps?q=My+Tribe+Gym+Amman&output=embed"
SITE_URL = "https://hamzehabunemeh.github.io/My-tribe-gym/"

def wa(lang, msg=None):
    if msg is None:
        msg = ("Hi My Tribe! I'd like to book my free trial class." if lang == "en"
               else "مرحباً My Tribe! بدي أحجز حصتي التجريبية المجانية.")
    return f"https://wa.me/{WA}?text={urllib.parse.quote(msg)}"

DAYS = ["sat", "sun", "mon", "tue", "wed", "thu"]
DAY_NAMES = {
    "en": {"sat": "Sat", "sun": "Sun", "mon": "Mon", "tue": "Tue", "wed": "Wed", "thu": "Thu", "fri": "Fri"},
    "ar": {"sat": "السبت", "sun": "الأحد", "mon": "الاثنين", "tue": "الثلاثاء", "wed": "الأربعاء", "thu": "الخميس", "fri": "الجمعة"},
}
DAY_FULL_EN = {"sat": "Saturday", "sun": "Sunday", "mon": "Monday", "tue": "Tuesday", "wed": "Wednesday", "thu": "Thursday", "fri": "Friday"}

# class type -> (EN label, AR label, css class)
CLASS_TYPES = {
    "tribefit": ("TribeFit", "TribeFit", "t-tribefit"),
    "weightlifting": ("Weightlifting", "رفع الأثقال", "t-weightlifting"),
    "injury": ("Injury Prevention", "الوقاية من الإصابات", "t-injury"),
    "calisthenics": ("Calisthenics", "كاليسثنكس", "t-calisthenics"),
}

# Main Studio weekly schedule: time -> {day: (type, coach)}
SCHEDULE = [
    ("6:30 AM",  {"sun": ("tribefit", "Armand"), "mon": ("tribefit", "Mustafa"), "tue": ("tribefit", "Armand"),
                  "wed": ("tribefit", "Mustafa"), "thu": ("tribefit", "Armand")}),
    ("10:00 AM", {"sat": ("tribefit", "Batool Madhun")}),
    ("4:30 PM",  {d: ("tribefit", "Batool Hammad") for d in DAYS}),
    ("5:30 PM",  {"sun": ("tribefit", "Batool Hammad"), "mon": ("weightlifting", "Batool Hammad"), "tue": ("tribefit", "Omar"),
                  "wed": ("tribefit", "Batool Hammad"), "thu": ("tribefit", "Batool Madhun")}),
    ("6:30 PM",  {"sun": ("injury", "John"), "tue": ("tribefit", "Omar"), "wed": ("tribefit", "Omar")}),
    ("7:00 PM",  {"mon": ("tribefit", "Omar")}),
    ("7:30 PM",  {"sun": ("calisthenics", "Aseel K"), "tue": ("calisthenics", "Aseel K"), "thu": ("calisthenics", "Aseel K")}),
]

COACHES = [
    # name, initials, role_en, role_ar, bio_en, bio_ar, lead
    ("Batool Hammad", "BH", "Head Coach", "المدربة الرئيسية",
     "Leads the Tribe's coaching team and programming. Batool runs most TribeFit and Weightlifting sessions and makes sure every member trains with purpose.",
     "تقود فريق المدربين وتضع البرامج التدريبية. تدرّب معظم حصص TribeFit ورفع الأثقال، وتحرص أن يتدرب كل عضو بهدف واضح.", True),
    ("Armand", "AR", "Fitness Coach", "مدرب لياقة",
     "Your early-morning engine. Armand coaches the 6:30 AM TribeFit sessions with energy, structure and great attention to movement quality.",
     "محرّك الصباح الباكر. يدرّب حصص TribeFit الساعة 6:30 صباحاً بطاقة عالية وتنظيم واهتمام كبير بجودة الحركة.", False),
    ("Aseel K", "AK", "Calisthenics Coach", "مدربة كاليسثنكس",
     "Bodyweight strength, control and skills — from your first pull-up to advanced holds. Aseel leads the Calisthenics classes.",
     "قوة وتحكم ومهارات بوزن الجسم، من أول عقلة إلى الحركات المتقدمة. تقود حصص الكاليسثنكس.", False),
    ("Areen", "AE", "Dietitian", "أخصائية تغذية",
     "Training is half the story. Areen builds realistic nutrition plans that support your performance, recovery and body-composition goals.",
     "التمرين نصف القصة. تضع خطط تغذية واقعية تدعم أداءك وتعافيك وأهدافك في تكوين الجسم.", False),
    ("John", "JO", "Sports Therapist & Fitness Coach", "معالج رياضي ومدرب لياقة",
     "Combines sports therapy with coaching to keep you moving well. John leads the Injury Prevention sessions and rehab-focused training.",
     "يجمع بين العلاج الرياضي والتدريب ليحافظ على حركتك سليمة. يقود حصص الوقاية من الإصابات والتدريب التأهيلي.", False),
    ("Omar", "OM", "Fitness Coach", "مدرب لياقة",
     "High-energy evening TribeFit sessions with scalable workouts for every level — Omar makes hard work feel like a team sport.",
     "حصص TribeFit مسائية مليئة بالطاقة بتمارين تناسب كل المستويات، يجعل التمرين الصعب رياضة جماعية.", False),
    ("Mustafa", "MU", "Fitness Coach", "مدرب لياقة",
     "Coaches morning TribeFit sessions with a focus on solid technique, consistency and steady progress.",
     "يدرّب حصص TribeFit الصباحية مع تركيز على التكنيك الصحيح والاستمرارية والتقدم الثابت.", False),
    ("Batool Madhun", "BM", "Fitness Coach", "مدربة لياقة",
     "Brings positive energy to the weekend and evening TribeFit classes, helping members build confidence and strength.",
     "تضيف طاقة إيجابية لحصص TribeFit في نهاية الأسبوع والمساء، وتساعد الأعضاء على بناء الثقة والقوة.", False),
]

# PLACEHOLDER PRICES (JOD) — replace when official prices are provided
PRICES = [
    # key, name_en, name_ar, amount, per_en, per_ar, features_en, features_ar, featured
    ("monthly", "1 Month", "شهر واحد", 60, "per month", "شهرياً",
     ["Unlimited TribeFit classes", "Open gym access", "Community events"],
     ["حصص TribeFit غير محدودة", "استخدام الجيم المفتوح", "فعاليات المجتمع"], False),
    ("quarter", "3 Months", "3 أشهر", 165, "≈ 55 JOD / month", "≈ 55 دينار شهرياً",
     ["Everything in 1 Month", "All group classes", "Body composition check-in"],
     ["كل ما في باقة الشهر", "جميع الحصص الجماعية", "قياس تكوين الجسم"], True),
    ("half", "6 Months", "6 أشهر", 300, "≈ 50 JOD / month", "≈ 50 دينار شهرياً",
     ["Everything in 3 Months", "1 nutrition consultation", "Freeze option"],
     ["كل ما في باقة 3 أشهر", "استشارة تغذية واحدة", "إمكانية تجميد الاشتراك"], False),
    ("year", "12 Months", "12 شهراً", 540, "≈ 45 JOD / month", "≈ 45 دينار شهرياً",
     ["Everything in 6 Months", "2 private sessions", "Best value"],
     ["كل ما في باقة 6 أشهر", "جلستان تدريب خاص", "أفضل قيمة"], False),
]
EXTRAS = [
    ("Private Training — 10 sessions", "تدريب خاص — 10 جلسات", 250),
    ("Private Training — single session", "تدريب خاص — جلسة واحدة", 30),
    ("Drop-in class", "حصة واحدة", 8),
    ("Nutrition consultation", "استشارة تغذية", 25),
]

PROGRAMS = [
    # id, img, title_en, title_ar, short_en, short_ar, long_en, long_ar, points_en, points_ar
    ("functional-fitness", "rigs", "Functional Fitness", "اللياقة الوظيفية",
     "Train for real life: strength, conditioning and mobility in one smart program.",
     "تدرّب للحياة الحقيقية: قوة وتحمّل ومرونة في برنامج واحد ذكي.",
     "Functional fitness builds the kind of strength you actually use — lifting, carrying, pushing, pulling, jumping and moving well. Every session blends strength work with conditioning, scaled to your level by our coaches.",
     "اللياقة الوظيفية تبني القوة التي تستخدمها فعلاً: الرفع والحمل والدفع والسحب والقفز والحركة السليمة. كل حصة تجمع بين تمارين القوة والتحمّل، ويعدّلها المدربون لتناسب مستواك.",
     ["Full-body strength & conditioning", "Scalable for every fitness level", "Coached, structured sessions"],
     ["قوة وتحمّل لكامل الجسم", "مناسب لكل المستويات", "حصص منظمة بإشراف مدرب"]),
    ("calisthenics", "clx", "Calisthenics", "كاليسثنكس",
     "Master your bodyweight — pull-ups, dips, levers and handstands.",
     "أتقن وزن جسمك: العقلة والمتوازي والليفر والوقوف على اليدين.",
     "Our calisthenics program takes you from the basics to advanced skills using rings, bars and your own bodyweight. Build relative strength, control and the confidence to do things you never thought possible.",
     "برنامج الكاليسثنكس ينقلك من الأساسيات إلى المهارات المتقدمة باستخدام الحلقات والبارات ووزن جسمك. ابنِ قوة نسبية وتحكماً، والثقة لتنفيذ حركات لم تتخيل أنك تقدر عليها.",
     ["Progressions for beginners to advanced", "Rings, bars & skill work", "Classes Sun · Tue · Thu, 7:30 PM"],
     ["تدرّج من المبتدئ إلى المتقدم", "حلقات وبارات وتمارين مهارة", "الحصص: الأحد والثلاثاء والخميس 7:30 مساءً"]),
    ("weightlifting", "weights", "Weightlifting", "رفع الأثقال",
     "Learn the snatch and clean & jerk with proper technique and real progress.",
     "تعلّم الخطف والنتر بالتكنيك الصحيح وتقدّم حقيقي.",
     "Olympic weightlifting develops power, speed and coordination like nothing else. Our coaches break the lifts down step by step, so you lift safely, efficiently and heavier over time.",
     "رفع الأثقال الأولمبي يطوّر القوة الانفجارية والسرعة والتوافق العضلي العصبي. يشرح المدربون الحركات خطوة بخطوة لترفع بأمان وكفاءة وأوزان أكبر مع الوقت.",
     ["Snatch, clean & jerk technique", "Strength cycles & programming", "Weightlifting class Mon, 5:30 PM"],
     ["تكنيك الخطف والنتر", "دورات قوة وبرمجة تدريبية", "حصة رفع الأثقال: الاثنين 5:30 مساءً"]),
    ("injury-prevention", "mural", "Injury Prevention", "الوقاية من الإصابات",
     "Move better, recover faster and stay in the game — led by our sports therapist.",
     "تحرّك أفضل، تعافَ أسرع، واستمر في التمرين بإشراف المعالج الرياضي.",
     "Led by our sports therapist, these sessions focus on mobility, stability, joint health and smart load management. Ideal for athletes, desk workers and anyone coming back from a niggle or injury.",
     "بإشراف معالجنا الرياضي، تركّز هذه الحصص على المرونة والثبات وصحة المفاصل والإدارة الذكية للأحمال. مثالية للرياضيين وأصحاب العمل المكتبي وكل من يعود من إصابة.",
     ["Mobility & stability work", "Prehab & return-to-training", "Session Sun, 6:30 PM"],
     ["تمارين مرونة وثبات", "تأهيل وقائي وعودة آمنة للتمرين", "الحصة: الأحد 6:30 مساءً"]),
    ("tribefit", "cover", "TribeFit Classes", "حصص TribeFit",
     "Our signature group class — high energy, coached, and built around the Tribe.",
     "حصتنا الجماعية المميزة: طاقة عالية وإشراف مدرب وروح الفريق.",
     "TribeFit is where the community comes alive. Coached group workouts that mix strength, gymnastics and conditioning — different every day, scalable for everyone, and always better together.",
     "في TribeFit تظهر روح المجتمع. تمارين جماعية بإشراف مدرب تجمع القوة والجمباز والتحمّل، مختلفة كل يوم، ومناسبة للجميع، ودائماً أجمل معاً.",
     ["Daily coached group workouts", "Morning & evening times", "All levels welcome"],
     ["تمارين جماعية يومية بإشراف مدرب", "مواعيد صباحية ومسائية", "كل المستويات مرحب بها"]),
    ("private-training", "private", "Private Training", "التدريب الخاص",
     "One-on-one coaching built entirely around your goals and schedule.",
     "تدريب فردي مصمم بالكامل حول أهدافك ووقتك.",
     "Work one-on-one with a Tribe coach on a plan built just for you — whether it's fat loss, strength, a first pull-up, sport performance or returning from injury. Pair it with our dietitian for the full picture.",
     "تدرّب بشكل فردي مع أحد مدربي Tribe ضمن خطة مصممة لك وحدك، سواء كان هدفك خسارة الدهون أو القوة أو أول عقلة أو الأداء الرياضي أو العودة من إصابة. وأضف أخصائية التغذية لنتيجة متكاملة.",
     ["Personalised program", "Flexible scheduling", "Optional nutrition support"],
     ["برنامج مخصص لك", "مواعيد مرنة", "دعم غذائي اختياري"]),
]

PAGES = ["index", "about", "programs", "schedule", "coaches", "membership", "facilities", "contact"]

T = {
 "en": {
  "dir": "ltr", "other": "ar", "other_label": "عربي",
  "nav": {"index": "Home", "about": "The Tribe", "programs": "Programs", "schedule": "Schedule", "coaches": "Coaches",
          "membership": "Membership", "facilities": "Facilities", "contact": "Contact"},
  "titles": {"index": "My Tribe Gym | Functional Fitness & Community Gym in Amman",
             "about": "The Tribe | My Tribe Gym", "programs": "Programs | My Tribe Gym", "schedule": "Class Schedule & Hours | My Tribe Gym",
             "coaches": "Coaches | My Tribe Gym", "membership": "Membership & Prices | My Tribe Gym",
             "facilities": "Facilities & Café | My Tribe Gym", "contact": "Contact | My Tribe Gym"},
  "desc": "My Tribe Gym — a community-driven gym for functional fitness, calisthenics, weightlifting, injury prevention, TribeFit classes and private training. Book your free trial.",
  "free_trial": "Book a free trial", "book_wa": "Book on WhatsApp",
  "sound": "Toggle sound",
 },
 "ar": {
  "dir": "rtl", "other": "en", "other_label": "EN",
  "nav": {"index": "الرئيسية", "about": "من نحن", "programs": "البرامج", "schedule": "الجدول", "coaches": "المدربون",
          "membership": "الاشتراكات", "facilities": "المرافق", "contact": "تواصل معنا"},
  "titles": {"index": "My Tribe Gym | جيم اللياقة الوظيفية والمجتمع الرياضي",
             "about": "من نحن | My Tribe Gym", "programs": "البرامج | My Tribe Gym", "schedule": "جدول الحصص والدوام | My Tribe Gym",
             "coaches": "المدربون | My Tribe Gym", "membership": "الاشتراكات والأسعار | My Tribe Gym",
             "facilities": "المرافق والكافيه | My Tribe Gym", "contact": "تواصل معنا | My Tribe Gym"},
  "desc": "My Tribe Gym — جيم قائم على روح المجتمع: لياقة وظيفية، كاليسثنكس، رفع أثقال، وقاية من الإصابات، حصص TribeFit وتدريب خاص. احجز حصتك التجريبية المجانية.",
  "free_trial": "احجز حصتك المجانية", "book_wa": "احجز عبر واتساب",
  "sound": "تشغيل/إيقاف الصوت",
 },
}

# ---------------------------------------------------------------- icons
ICON = {
 "wa": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1s-.5-.1-.7.1-.8 1-1 1.2-.4.2-.7.1a8.2 8.2 0 0 1-4-3.5c-.3-.5.3-.5.9-1.6.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4 3.6 3.6 0 0 0-1.1 2.7 6.3 6.3 0 0 0 1.3 3.3 14.4 14.4 0 0 0 5.5 4.9c2 .9 2.8.9 3.8.8a3.2 3.2 0 0 0 2.1-1.5 2.6 2.6 0 0 0 .2-1.5c-.1-.1-.3-.2-.6-.3M12 21.8a9.9 9.9 0 0 1-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 1 1 12 21.8m8.4-18.2A11.8 11.8 0 0 0 1.8 17.9L.1 24l6.3-1.6a11.8 11.8 0 0 0 5.6 1.4A11.8 11.8 0 0 0 20.4 3.6"/></svg>',
 "ig": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.6" cy="6.4" r="1" fill="currentColor"/></svg>',
 "yt": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.6 12 3.6 12 3.6s-7.5 0-9.4.5A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.5 9.4.5 9.4.5s7.5 0 9.4-.5a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8M9.6 15.6V8.4l6.2 3.6z"/></svg>',
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13S3 17 3 10a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
 "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
 "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M3 12h18M3 18h18"/></svg>',
 "vol_off": '<svg class="off" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5 6 9H2v6h4l5 4z"/><path d="m23 9-6 6M17 9l6 6"/></svg>',
 "vol_on": '<svg class="on" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5 6 9H2v6h4l5 4z"/><path d="M15.5 8.5a5 5 0 0 1 0 7M19 5a10 10 0 0 1 0 14"/></svg>',
 "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/></svg>',
 "target": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>',
 "bolt": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2 3 14h9l-1 8 10-12h-9z"/></svg>',
 "info": '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" style="flex:0 0 auto"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h0"/></svg>',
}

# ---------------------------------------------------------------- layout helpers
def href(lang, page, frag=""):
    name = "./" if page == "index" else f"{page}.html"
    return name + (f"#{frag}" if frag else "")

def asset(lang, p):
    return ("../" if lang == "ar" else "") + "assets/" + p

def other_href(lang, page):
    fname = "index.html" if page == "index" else f"{page}.html"
    return ("../" if lang == "ar" else "ar/") + ("" if page == "index" else fname)

def head(lang, page):
    t = T[lang]
    canon = SITE_URL + ("ar/" if lang == "ar" else "") + ("" if page == "index" else f"{page}.html")
    en_url = SITE_URL + ("" if page == "index" else f"{page}.html")
    ar_url = SITE_URL + "ar/" + ("" if page == "index" else f"{page}.html")
    fonts = ("https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&family=Oswald:wght@500;600;700&family=Inter:wght@400;500;600&display=swap")
    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{t['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t['titles'][page]}</title>
<meta name="description" content="{t['desc']}">
<meta name="theme-color" content="#0a0a0a">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="ar" href="{ar_url}">
<link rel="alternate" hreflang="x-default" href="{en_url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{t['titles'][page]}">
<meta property="og:description" content="{t['desc']}">
<meta property="og:image" content="{SITE_URL}assets/img/cover.webp">
<meta property="og:locale" content="{'en_US' if lang == 'en' else 'ar_JO'}">
<link rel="icon" type="image/png" href="{asset(lang, 'img/favicon.png')}">
<link rel="apple-touch-icon" href="{asset(lang, 'img/favicon.png')}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{fonts}">
<link rel="stylesheet" href="{asset(lang, 'css/style.css')}">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"ExerciseGym","name":"My Tribe Gym","url":"{SITE_URL}","telephone":"{PHONE}","image":"{SITE_URL}assets/img/cover.webp","hasMap":"{MAPS_LINK}","sameAs":["{INSTAGRAM}","{YOUTUBE}"],"openingHoursSpecification":[{{"@type":"OpeningHoursSpecification","dayOfWeek":["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday"],"opens":"06:00","closes":"21:00"}}]}}</script>
</head>
<body>
"""

def header(lang, page):
    t = T[lang]
    items = "".join(f'<li><a href="{href(lang, p)}"{" class=\"active\"" if p == page else ""}>{t["nav"][p]}</a></li>' for p in PAGES)
    return f"""<header class="site-header">
  <div class="container nav">
    <a class="brand" href="{href(lang, 'index')}" aria-label="My Tribe Gym"><img src="{asset(lang, 'img/logo-white.png')}" alt="My Tribe Gym logo" width="80" height="60"><span>My Tribe</span></a>
    <ul class="nav-links">{items}</ul>
    <div class="nav-actions">
      <a class="lang" href="{other_href(lang, page)}" hreflang="{t['other']}" lang="{t['other']}">{t['other_label']}</a>
      <a class="btn btn-red" href="{wa(lang)}" target="_blank" rel="noopener">{t['free_trial']}</a>
      <button class="burger" aria-label="Menu" aria-expanded="false">{ICON['menu']}</button>
    </div>
  </div>
</header>
<main>
"""

def footer(lang):
    t = T[lang]; n = t["nav"]; en = lang == "en"
    links = "".join(f'<li><a href="{href(lang, p)}">{n[p]}</a></li>' for p in PAGES)
    progs = "".join(f'<li><a href="{href(lang, "programs", p[0])}">{p[2] if en else p[3]}</a></li>' for p in PROGRAMS)
    return f"""</main>
<footer class="site-footer">
  <div class="container">
    <div class="foot">
      <div>
        <a class="brand" href="{href(lang, 'index')}"><img src="{asset(lang, 'img/logo-white.png')}" alt="My Tribe Gym" width="80" height="60"></a>
        <p style="margin-top:1rem;max-width:300px">{'More than a gym — a tribe. Train hard, move well and belong.' if en else 'أكثر من جيم، نحن قبيلة. تمرّن بقوة، تحرّك بشكل صحيح، وكن جزءاً منا.'}</p>
        <div class="socials">
          <a href="{INSTAGRAM}" target="_blank" rel="noopener" aria-label="Instagram">{ICON['ig']}</a>
          <a href="{YOUTUBE}" target="_blank" rel="noopener" aria-label="YouTube">{ICON['yt']}</a>
          <a href="{wa(lang)}" target="_blank" rel="noopener" aria-label="WhatsApp">{ICON['wa']}</a>
        </div>
      </div>
      <div><h4>{'Explore' if en else 'روابط'}</h4><ul>{links}</ul></div>
      <div><h4>{'Programs' if en else 'البرامج'}</h4><ul>{progs}</ul></div>
      <div><h4>{'Opening Hours' if en else 'أوقات الدوام'}</h4>
        <ul>
          <li>{'Sat – Thu' if en else 'السبت – الخميس'}: <span class="ltr">6:00 AM – 9:00 PM</span></li>
          <li>{'Friday: Closed' if en else 'الجمعة: مغلق'}</li>
          <li>{'Public holidays' if en else 'العطل الرسمية'}: <span class="ltr">12:00 PM – 6:00 PM</span></li>
          <li style="margin-top:.6rem"><a href="tel:{PHONE}" class="ltr">{PHONE_DISPLAY}</a></li>
          <li><a href="{MAPS_LINK}" target="_blank" rel="noopener">{'Get directions →' if en else 'احصل على الاتجاهات ←'}</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© <span id="year">2026</span> My Tribe Gym. {'All rights reserved.' if en else 'جميع الحقوق محفوظة.'}</span>
      <a href="{other_href(lang, 'index')}">{'النسخة العربية' if en else 'English version'}</a>
    </div>
  </div>
</footer>
<a class="wa-float" href="{wa(lang)}" target="_blank" rel="noopener" aria-label="WhatsApp">{ICON['wa']}</a>
<script src="{asset(lang, 'js/main.js')}" defer></script>
</body>
</html>
"""

def page_hero(lang, img, eyebrow, title, text):
    return f"""<section class="page-hero" style="background-image:url({asset(lang, 'img/' + img + '.webp')})">
  <div class="container"><span class="eyebrow">{eyebrow}</span><h1>{title}</h1><p>{text}</p></div>
</section>
<div class="stripe"></div>
"""

def cta_band(lang):
    en = lang == "en"
    return f"""<section class="cta-band">
  <div class="container reveal">
    <span class="eyebrow" style="justify-content:center">{'Your first class is on us' if en else 'حصتك الأولى علينا'}</span>
    <h2>{'Join the Tribe' if en else 'انضم إلى القبيلة'}</h2>
    <p>{'Come train with us, meet the coaches and feel the community. Your trial class is completely free.' if en else 'تعال تمرّن معنا، تعرّف على المدربين، وعِش أجواء المجتمع. حصتك التجريبية مجانية بالكامل.'}</p>
    <a class="btn btn-red" href="{wa(lang)}" target="_blank" rel="noopener">{ICON['wa']} {T[lang]['free_trial']}</a>
  </div>
</section>
"""

def cls_cell(lang, entry):
    typ, coach = entry
    en_l, ar_l, css = CLASS_TYPES[typ]
    return f'<span class="cls {css}">{en_l if lang == "en" else ar_l}</span><span class="coach-name">{coach}</span>'

def day_lists(lang, tag_days=DAYS):
    out = []
    for d in tag_days:
        items = [(time, row[d]) for time, row in SCHEDULE if d in row]
        lis = "".join(f'<li><time class="ltr">{tm}</time><div>{cls_cell(lang, e)}</div></li>' for tm, e in items)
        out.append(f'<ul class="day-list" data-day="{d}">{lis}</ul>')
    if "fri" not in tag_days:
        msg = "Friday is our rest day — see you Saturday!" if lang == "en" else "الجمعة يوم راحة، نراك يوم السبت!"
        out.append(f'<ul class="day-list" data-day="fri"><li>{msg}</li></ul>')
    return "".join(out)

def schedule_block(lang):
    names = DAY_NAMES[lang]
    th = "".join(f'<th data-col="{d}">{names[d]}</th>' for d in DAYS)
    rows = ""
    for tm, row in SCHEDULE:
        cells = "".join(f'<td data-col="{d}">{cls_cell(lang, row[d]) if d in row else "<span class=empty>—</span>"}</td>' for d in DAYS)
        rows += f'<tr><th class="ltr">{tm}</th>{cells}</tr>'
    tabs = "".join(f'<button data-target="{d}">{names[d]}</button>' for d in DAYS)
    legend = "".join(f'<span><i style="background:{c}"></i>{(v[0] if lang == "en" else v[1])}</span>'
                     for v, c in zip(CLASS_TYPES.values(), ["#fff", "#5fb3ff", "#4fd1a5", "#ffcc00"]))
    time_lbl = "Time" if lang == "en" else "الوقت"
    return f"""<div class="sched-wrap"><table class="sched"><thead><tr><th>{time_lbl}</th>{th}</tr></thead><tbody>{rows}</tbody></table></div>
<div class="sched-days"><div class="day-tabs">{tabs}</div>{day_lists(lang)}</div>
<div class="legend">{legend}</div>"""

def hours_block(lang):
    en = lang == "en"
    return f"""<div class="hours">
  <div><strong>{'Saturday – Thursday' if en else 'السبت – الخميس'}</strong><span class="ltr">6:00 AM – 9:00 PM</span></div>
  <div><strong>{'Friday' if en else 'الجمعة'}</strong><span class="closed">{'Closed' if en else 'مغلق'}</span></div>
  <div><strong>{'Public holidays' if en else 'العطل الرسمية'}</strong><span class="ltr">12:00 PM – 6:00 PM</span></div>
</div>"""

def img_style(lang, name):
    return f"background-image:url({asset(lang, 'img/' + name + '-sm.webp')})"

# ---------------------------------------------------------------- pages
def p_index(lang):
    en = lang == "en"; t = T[lang]
    cards = ""
    for i, p in enumerate(PROGRAMS, 1):
        cards += f"""<a class="card prog-card reveal" href="{href(lang, 'programs', p[0])}">
  <div class="img" style="{img_style(lang, p[1])}"></div>
  <div class="body"><span class="num">0{i}</span><h3>{p[2] if en else p[3]}</h3><p>{p[4] if en else p[5]}</p>
  <span class="link-arrow">{'Learn more →' if en else 'اعرف أكثر ←'}</span></div></a>"""
    labels = "".join(f'<small data-day-label="{d}" hidden>{DAY_FULL_EN[d] if en else DAY_NAMES["ar"][d]}</small>' for d in DAYS + ["fri"])
    return f"""<section class="hero">
  <div class="hero-bg"></div>
  <div class="container hero-inner">
    <div class="hero-text">
      <span class="eyebrow">{'Community-driven gym · Amman' if en else 'جيم قائم على روح المجتمع'}</span>
      <h1>{'Train hard.<br>Move well.<br><em>Belong.</em>' if en else 'تمرّن بقوة.<br>تحرّك صح.<br><em>كن من القبيلة.</em>'}</h1>
      <p class="lead">{'My Tribe Gym is more than a place to work out — it’s a community of people who push each other, celebrate each other and grow together. Functional fitness, calisthenics, weightlifting and expert coaching under one roof.' if en else 'My Tribe Gym أكثر من مكان للتمرين، هو مجتمع من أشخاص يشجّعون بعضهم ويحتفلون بإنجازات بعضهم ويتطورون معاً. لياقة وظيفية، كاليسثنكس، رفع أثقال، وتدريب احترافي تحت سقف واحد.'}</p>
      <div class="hero-ctas">
        <a class="btn btn-red" href="{wa(lang)}" target="_blank" rel="noopener">{ICON['wa']} {t['free_trial']}</a>
        <a class="btn btn-ghost" href="{href(lang, 'schedule')}">{'View schedule' if en else 'شاهد الجدول'}</a>
      </div>
      <div class="hero-stats">
        <div><strong>6</strong><span>{'Programs' if en else 'برامج'}</span></div>
        <div><strong>8</strong><span>{'Coaches' if en else 'مدربين'}</span></div>
        <div><strong>24</strong><span>{'Classes / week' if en else 'حصة أسبوعياً'}</span></div>
      </div>
    </div>
    <div class="phone">
      <video autoplay muted loop playsinline preload="auto" poster="{asset(lang, 'img/hero-poster.jpg')}">
        <source src="{asset(lang, 'video/hero.mp4')}" type="video/mp4">
      </video>
      <button class="sound-btn" type="button" aria-label="{t['sound']}" aria-pressed="false">{ICON['vol_off']}{ICON['vol_on']}</button>
    </div>
  </div>
</section>
<div class="stripe"></div>

<section class="section">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">{'Welcome to the Tribe' if en else 'أهلاً بك في القبيلة'}</span>
      <h2>{'Stronger together' if en else 'أقوى معاً'}</h2>
      <p>{'We built My Tribe around one idea: people train better when they belong. Here, beginners and athletes share the same floor, coaches know your name, and every PR gets celebrated.' if en else 'بنينا My Tribe حول فكرة واحدة: الناس تتمرن أفضل عندما تشعر بالانتماء. هنا يتشارك المبتدئون والرياضيون نفس المكان، والمدربون يعرفونك باسمك، وكل إنجاز يُحتفل به.'}</p>
      <ul class="checks">
        <li>{'Expert coaches for every discipline' if en else 'مدربون متخصصون لكل رياضة'}</li>
        <li>{'Classes for every level — scaled to you' if en else 'حصص لكل المستويات، معدّلة حسب قدرتك'}</li>
        <li>{'Nutrition and sports-therapy support in-house' if en else 'دعم غذائي وعلاج رياضي داخل الجيم'}</li>
      </ul>
      <a class="btn btn-ghost" href="{href(lang, 'about')}">{'Our story' if en else 'قصتنا'}</a>
    </div>
    <div class="split-img reveal" style="background-image:url({asset(lang, 'img/mural.webp')})"></div>
  </div>
</section>

<section class="section alt">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">{'What we do' if en else 'ماذا نقدّم'}</span><h2>{'Our programs' if en else 'برامجنا'}</h2>
      <p>{'Six ways to train, one community. Pick your path — or mix them all.' if en else 'ست طرق للتمرين ومجتمع واحد. اختر طريقك، أو اجمعها كلها.'}</p></div>
    <div class="grid g3">{cards}</div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">{'Today at the Tribe' if en else 'اليوم في الجيم'}</span>
      <h2>{'Classes today' if en else 'حصص اليوم'}</h2>
      <p>{'Drop into any TribeFit class — our coaches will scale the workout for you. Full weekly timetable on the schedule page.' if en else 'انضم لأي حصة TribeFit، والمدرب سيعدّل التمرين ليناسبك. الجدول الأسبوعي الكامل في صفحة الجدول.'}</p>
      {hours_block(lang)}
      <p style="margin-top:1.4rem"><a class="link-arrow" href="{href(lang, 'schedule')}">{'Full schedule →' if en else 'الجدول الكامل ←'}</a></p>
    </div>
    <div class="today-box reveal">
      <h3>{'Main Studio' if en else 'الاستوديو الرئيسي'} {labels}</h3>
      {day_lists(lang)}
    </div>
  </div>
</section>

<section class="section alt">
  <div class="container">
    <div class="section-head center reveal"><span class="eyebrow">{'Follow the Tribe' if en else 'تابعنا'}</span><h2>@mytribegym</h2>
      <p>{'Workouts, member wins and behind-the-scenes from the gym floor.' if en else 'تمارين وإنجازات الأعضاء وكواليس الجيم.'}</p></div>
    <div class="social-band">
      <a class="social-card reveal" href="{INSTAGRAM}" target="_blank" rel="noopener">{ICON['ig']}<div><h3>Instagram</h3><p>{'Daily workouts & community moments' if en else 'تمارين يومية ولحظات من المجتمع'}</p></div></a>
      <a class="social-card reveal" href="{YOUTUBE}" target="_blank" rel="noopener">{ICON['yt']}<div><h3>YouTube</h3><p>{'Technique breakdowns & gym videos' if en else 'شرح التكنيك وفيديوهات الجيم'}</p></div></a>
    </div>
  </div>
</section>
{cta_band(lang)}"""

def p_about(lang):
    en = lang == "en"
    values = [
        ("users", "Community first", "المجتمع أولاً", "We train together, cheer together and show up for each other. Nobody trains alone at the Tribe.", "نتمرّن معاً ونشجّع بعضنا ونحضر لبعضنا. لا أحد يتمرّن وحده في Tribe."),
        ("target", "Quality coaching", "تدريب احترافي", "Every class is coached. Every movement is taught, corrected and scaled to you.", "كل حصة بإشراف مدرب، وكل حركة تُشرح وتُصحّح وتُعدّل لتناسبك."),
        ("shield", "Move well, stay healthy", "حركة سليمة وصحة دائمة", "Injury prevention and smart programming so you can keep training for years.", "وقاية من الإصابات وبرمجة ذكية لتستمر في التمرين لسنوات."),
        ("bolt", "Progress for everyone", "تقدّم للجميع", "From first-timers to competitive athletes — there’s a place and a plan for you.", "من المبتدئين إلى الرياضيين المنافسين، لكل شخص مكان وخطة."),
    ]
    vals = "".join(f'<div class="value reveal"><div class="icon">{ICON[i]}</div><h3>{a if en else b}</h3><p>{c if en else d}</p></div>' for i, a, b, c, d in values)
    return page_hero(lang, "mural", "My Tribe Gym", "The Tribe" if en else "من نحن",
        "A gym built on people. Strength, skill and community — in that order of importance, depending on the day." if en else "جيم مبني على الناس. القوة والمهارة والمجتمع في مكان واحد.") + f"""
<section class="section">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">{'Our story' if en else 'قصتنا'}</span>
      <h2>{'More than a gym' if en else 'أكثر من جيم'}</h2>
      <p>{'My Tribe Gym was created for people who want more than machines and mirrors. We wanted a place where you walk in and feel at home — where coaches care about how you move, and members care about how you’re doing.' if en else 'أُسّس My Tribe Gym لمن يريد أكثر من أجهزة ومرايا. أردنا مكاناً تدخله فتشعر أنك في بيتك، حيث يهتم المدرب بطريقة حركتك ويهتم الأعضاء بأحوالك.'}</p>
      <p>{'Under one roof we bring together functional fitness, calisthenics, weightlifting, injury prevention, nutrition and private coaching, led by a team of specialists who each bring their own discipline to the floor.' if en else 'نجمع تحت سقف واحد اللياقة الوظيفية والكاليسثنكس ورفع الأثقال والوقاية من الإصابات والتغذية والتدريب الخاص، بقيادة فريق من المتخصصين، لكل منهم مجاله.'}</p>
      <p>{'Whatever brings you in — getting fit, getting strong, coming back from injury or just finding your people — you’ll find your tribe here.' if en else 'مهما كان سبب قدومك، لياقة أو قوة أو عودة من إصابة أو بحثاً عن ناس يشبهونك، ستجد قبيلتك هنا.'}</p>
    </div>
    <div class="split-img reveal" style="background-image:url({asset(lang, 'img/rigs.webp')})"></div>
  </div>
</section>
<section class="section alt">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">{'What we stand for' if en else 'قيمنا'}</span><h2>{'Our values' if en else 'ما نؤمن به'}</h2></div>
    <div class="grid g4">{vals}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">{'Inside the gym' if en else 'داخل الجيم'}</span><h2>{'Gallery' if en else 'معرض الصور'}</h2></div>
    <div class="gallery reveal">
      <a class="wide tall" href="{asset(lang, 'img/cover.webp')}" style="background-image:url({asset(lang, 'img/cover-sm.webp')})" aria-label="Gym floor"></a>
      <a class="wide" href="{asset(lang, 'img/rigs.webp')}" style="background-image:url({asset(lang, 'img/rigs-sm.webp')})" aria-label="Rigs"></a>
      <a href="{asset(lang, 'img/weights.webp')}" style="background-image:url({asset(lang, 'img/weights-sm.webp')})" aria-label="Weights"></a>
      <a href="{asset(lang, 'img/hero-poster.jpg')}" style="background-image:url({asset(lang, 'img/hero-poster.jpg')})" aria-label="Training"></a>
      <a class="wide" href="{asset(lang, 'img/mural.webp')}" style="background-image:url({asset(lang, 'img/mural-sm.webp')})" aria-label="Mural"></a>
      <a class="wide" href="{asset(lang, 'img/cafe.webp')}" style="background-image:url({asset(lang, 'img/cafe-sm.webp')})" aria-label="Café"></a>
    </div>
  </div>
</section>
{cta_band(lang)}"""

def p_programs(lang):
    en = lang == "en"
    nav = "".join(f'<a href="#{p[0]}">{p[2] if en else p[3]}</a>' for p in PROGRAMS)
    blocks = ""
    for i, p in enumerate(PROGRAMS):
        pts = "".join(f"<li>{x}</li>" for x in (p[8] if en else p[9]))
        msg = (f"Hi My Tribe! I'm interested in {p[2]}." if en else f"مرحباً My Tribe! أنا مهتم ببرنامج {p[3]}.")
        blocks += f"""<section class="section program{' alt' if i % 2 else ''}" id="{p[0]}">
  <div class="container split{' rev' if i % 2 else ''}">
    <div class="split-img reveal" style="background-image:url({asset(lang, 'img/' + p[1] + '.webp')})"></div>
    <div class="reveal">
      <span class="eyebrow">0{i+1}</span>
      <h2>{p[2] if en else p[3]}</h2>
      <p>{p[6] if en else p[7]}</p>
      <ul class="checks">{pts}</ul>
      <a class="btn btn-red" href="{wa(lang, msg)}" target="_blank" rel="noopener">{ICON['wa']} {T[lang]['book_wa']}</a>
    </div>
  </div>
</section>"""
    return page_hero(lang, "rigs", "My Tribe Gym", "Programs" if en else "البرامج",
        "Six specialised programs, one community. Every session is coached and scaled to your level." if en else "ستة برامج متخصصة ومجتمع واحد. كل حصة بإشراف مدرب ومعدّلة حسب مستواك.").replace(
        "</p></div>\n</section>", f'</p><div class="prog-nav">{nav}</div></div>\n</section>', 1) + blocks + cta_band(lang)

def p_schedule(lang):
    en = lang == "en"
    return page_hero(lang, "weights", "Main Studio" if en else "الاستوديو الرئيسي", "Schedule" if en else "جدول الحصص",
        "Weekly class timetable and opening hours. Today’s column is highlighted." if en else "جدول الحصص الأسبوعي وأوقات الدوام. عمود اليوم مميّز بإطار.") + f"""
<section class="section">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">{'Weekly timetable' if en else 'الجدول الأسبوعي'}</span><h2>{'Main Studio classes' if en else 'حصص الاستوديو الرئيسي'}</h2>
      <p>{'Classes are open to all members. New here? Your first class is free — just message us on WhatsApp to reserve a spot.' if en else 'الحصص متاحة لجميع الأعضاء. جديد عندنا؟ حصتك الأولى مجانية، راسلنا على واتساب لحجز مكانك.'}</p></div>
    <div class="reveal">{schedule_block(lang)}</div>
  </div>
</section>
<section class="section alt">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">{'Open gym' if en else 'الجيم المفتوح'}</span>
      <h2>{'Opening hours' if en else 'أوقات الدوام'}</h2>
      <p>{'Outside class times the gym floor is open for members’ own training.' if en else 'خارج أوقات الحصص، الجيم متاح للأعضاء للتمرين الحر.'}</p>
    </div>
    <div class="reveal">{hours_block(lang)}</div>
  </div>
</section>
{cta_band(lang)}"""

def p_coaches(lang):
    en = lang == "en"
    cards = ""
    for name, ini, ren, rar, ben, bar, lead in COACHES:
        msg = (f"Hi My Tribe! I'd like to book a session with Coach {name}." if en else f"مرحباً My Tribe! بدي أحجز جلسة مع الكوتش {name}.")
        badge = f'<span class="badge">{"Head Coach" if en else "المدربة الرئيسية"}</span>' if lead else ""
        cards += f"""<article class="card coach reveal{' lead' if lead else ''}">{badge}
  <div class="avatar"><span>{ini}</span><small>{'Photo coming soon' if en else 'الصورة قريباً'}</small></div>
  <div class="info"><h3>{name}</h3><div class="role">{ren if en else rar}</div><p>{ben if en else bar}</p>
  <a class="link-arrow" href="{wa(lang, msg)}" target="_blank" rel="noopener">{'Book with ' + name.split()[0] + ' →' if en else 'احجز مع ' + name.split()[0] + ' ←'}</a></div>
</article>"""
    return page_hero(lang, "rigs", "My Tribe Gym", "Our Coaches" if en else "المدربون",
        "Specialists in strength, skill, nutrition and therapy — one team, focused on you." if en else "متخصصون في القوة والمهارة والتغذية والعلاج، فريق واحد يركّز عليك.") + f"""
<section class="section">
  <div class="container"><div class="grid g4">{cards}</div></div>
</section>
{cta_band(lang)}"""

def p_membership(lang):
    en = lang == "en"
    cards = ""
    for key, nen, nar, amt, pen, par, fen, far, feat in PRICES:
        lis = "".join(f"<li>{x}</li>" for x in (fen if en else far))
        rib = f'<span class="ribbon">{"Popular" if en else "الأكثر طلباً"}</span>' if feat else ""
        msg = (f"Hi My Tribe! I'm interested in the {nen} membership." if en else f"مرحباً My Tribe! أنا مهتم باشتراك {nar}.")
        cards += f"""<div class="card price reveal{' featured' if feat else ''}">{rib}
  <h3>{nen if en else nar}</h3><div class="amt">{amt} <small>{'JOD' if en else 'دينار'}</small></div><div class="per">{pen if en else par}</div>
  <ul>{lis}</ul><a class="btn {'btn-red' if feat else 'btn-ghost'}" href="{wa(lang, msg)}" target="_blank" rel="noopener">{'Join now' if en else 'اشترك الآن'}</a></div>"""
    extras = "".join(f'<div><strong>{a if en else b}</strong><span>{c} {"JOD" if en else "دينار"}</span></div>' for a, b, c in EXTRAS)
    faqs = [
        ("Is the trial class really free?", "هل الحصة التجريبية مجانية فعلاً؟",
         "Yes. Message us on WhatsApp, pick a class from the schedule and come train with us — no payment and no commitment.",
         "نعم. راسلنا على واتساب، اختر حصة من الجدول وتعال تمرّن معنا، بدون دفع وبدون أي التزام."),
        ("I’m a complete beginner. Can I join?", "أنا مبتدئ تماماً، هل أستطيع الانضمام؟",
         "Absolutely. Every workout is scaled by our coaches, and many members started with zero experience.",
         "طبعاً. المدربون يعدّلون كل تمرين حسب مستواك، وكثير من أعضائنا بدأوا بدون أي خبرة."),
        ("What should I bring?", "ماذا أحضر معي؟",
         "Comfortable training clothes, trainers, a water bottle and a towel.",
         "ملابس رياضية مريحة، وحذاء رياضي، وقارورة ماء، ومنشفة."),
        ("Can I combine group classes with private training?", "هل أستطيع الجمع بين الحصص الجماعية والتدريب الخاص؟",
         "Yes — many members do. Ask us about combining a membership with a private training package.",
         "نعم، والكثير من الأعضاء يفعلون ذلك. اسألنا عن دمج الاشتراك مع باقة تدريب خاص."),
        ("Do you offer nutrition support?", "هل تقدّمون دعماً غذائياً؟",
         "Yes. Our in-house dietitian offers consultations and personalised plans.",
         "نعم. أخصائية التغذية في الجيم تقدّم استشارات وخططاً مخصصة."),
    ]
    faq = "".join(f"<details><summary>{a if en else b}</summary><p>{c if en else d}</p></details>" for a, b, c, d in faqs)
    return page_hero(lang, "weights", "My Tribe Gym", "Membership" if en else "الاشتراكات",
        "Simple plans, unlimited community. Start with a free trial class." if en else "باقات بسيطة ومجتمع بلا حدود. ابدأ بحصة تجريبية مجانية.") + f"""
<section class="section">
  <div class="container">
    <div class="notice reveal">{ICON['info']}<span>{'Prices shown are indicative and will be confirmed soon. Contact us on WhatsApp for current offers.' if en else 'الأسعار المعروضة تقديرية وسيتم تأكيدها قريباً. تواصل معنا عبر واتساب لمعرفة العروض الحالية.'}</span></div>
    <div class="grid g4">{cards}</div>
  </div>
</section>
<section class="section alt">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">{'Free trial' if en else 'حصة مجانية'}</span>
      <h2>{'Try before you commit' if en else 'جرّب قبل أن تشترك'}</h2>
      <p>{'Your first class at My Tribe is free. Meet the coaches, train with the community and see if we’re the right fit.' if en else 'حصتك الأولى في My Tribe مجانية. تعرّف على المدربين، تمرّن مع المجتمع، وشوف إذا كنا المكان المناسب لك.'}</p>
      <a class="btn btn-red" href="{wa(lang)}" target="_blank" rel="noopener">{ICON['wa']} {T[lang]['free_trial']}</a>
    </div>
    <div class="reveal">
      <h3 style="margin-bottom:1rem">{'Private training & extras' if en else 'التدريب الخاص والخدمات الإضافية'}</h3>
      <div class="hours">{extras}</div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container" style="max-width:860px">
    <div class="section-head reveal"><span class="eyebrow">FAQ</span><h2>{'Common questions' if en else 'أسئلة شائعة'}</h2></div>
    <div class="faq reveal">{faq}</div>
  </div>
</section>
{cta_band(lang)}"""

def p_facilities(lang):
    en = lang == "en"
    zones = [
        ("rigs", "Rig & calisthenics zone", "منطقة البارات والكاليسثنكس",
         "Rogue rigs with pull-up bars, gymnastic rings, climbing ropes and peg board for bodyweight and gymnastics training.",
         "بارات Rogue للعقلة وحلقات جمباز وحبال تسلّق ولوح أوتاد لتمارين وزن الجسم والجمباز."),
        ("weights", "Strength & weightlifting", "منطقة القوة ورفع الأثقال",
         "Olympic bars, bumper plates, racks, kettlebells, dumbbells and medicine balls — everything you need to get strong.",
         "بارات أولمبية وأقراص مطاطية وحوامل وكيتل بِل ودمبلز وكرات طبية، كل ما تحتاجه لتصبح أقوى."),
        ("mural", "Conditioning area", "منطقة التحمّل",
         "Rowers, bikes, plyo boxes and open floor space for high-intensity conditioning and team workouts.",
         "أجهزة تجديف ودراجات وصناديق قفز ومساحة مفتوحة لتمارين التحمّل عالية الشدة والتمارين الجماعية."),
    ]
    blocks = "".join(f"""<div class="card prog-card reveal"><div class="img" style="{img_style(lang, z[0])}"></div><div class="body"><h3>{z[1] if en else z[2]}</h3><p>{z[3] if en else z[4]}</p></div></div>""" for z in zones)
    return page_hero(lang, "cover", "My Tribe Gym", "Facilities & Café" if en else "المرافق والكافيه",
        "A spacious, fully equipped training floor — and a café to refuel and hang out after." if en else "مساحة تدريب واسعة ومجهزة بالكامل، وكافيه لتستعيد طاقتك وتجلس مع الأصدقاء بعد التمرين.") + f"""
<section class="section">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">{'Training floor' if en else 'مساحة التدريب'}</span><h2>{'Built for real training' if en else 'مصمم للتمرين الحقيقي'}</h2></div>
    <div class="grid g3">{blocks}</div>
  </div>
</section>
<section class="section alt" id="cafe">
  <div class="container split">
    <div class="split-img reveal" style="background-image:url({asset(lang, 'img/cafe.webp')})"></div>
    <div class="reveal">
      <span class="eyebrow">{'The Tribe Café' if en else 'كافيه Tribe'}</span>
      <h2>{'Refuel & hang out' if en else 'استعد طاقتك واجلس مع القبيلة'}</h2>
      <p>{'Our upstairs café overlooks the training floor — grab a coffee before your session, a snack after, or just stay and catch up with the Tribe.' if en else 'الكافيه في الطابق العلوي يطل على مساحة التدريب. خذ قهوتك قبل الحصة أو وجبة خفيفة بعدها، أو ابقَ وتحدّث مع أصدقائك من القبيلة.'}</p>
      <ul class="checks">
        <li>{'Specialty coffee & cold drinks' if en else 'قهوة مختصة ومشروبات باردة'}</li>
        <li>{'Snacks to refuel after training' if en else 'وجبات خفيفة بعد التمرين'}</li>
        <li>{'Lounge seating overlooking the gym' if en else 'جلسات مريحة تطل على الجيم'}</li>
      </ul>
    </div>
  </div>
</section>
{cta_band(lang)}"""

def p_contact(lang):
    en = lang == "en"
    return page_hero(lang, "cover", "My Tribe Gym", "Contact us" if en else "تواصل معنا",
        "Questions, bookings or just want to say hi? We’re one message away." if en else "عندك سؤال أو تريد الحجز أو حتى تسلّم علينا؟ نحن على بُعد رسالة.") + f"""
<section class="section">
  <div class="container split" style="align-items:stretch">
    <div class="reveal">
      <div class="contact-list">
        <a class="contact-item" href="{wa(lang)}" target="_blank" rel="noopener">{ICON['wa']}<div><small>WhatsApp</small><strong class="ltr">{PHONE_DISPLAY}</strong></div></a>
        <a class="contact-item" href="tel:{PHONE}">{ICON['phone']}<div><small>{'Phone' if en else 'الهاتف'}</small><strong class="ltr">{PHONE_DISPLAY}</strong></div></a>
        <a class="contact-item" href="{MAPS_LINK}" target="_blank" rel="noopener">{ICON['pin']}<div><small>{'Location' if en else 'الموقع'}</small><strong>{'Open in Google Maps' if en else 'افتح في خرائط Google'}</strong></div></a>
        <a class="contact-item" href="{INSTAGRAM}" target="_blank" rel="noopener">{ICON['ig']}<div><small>Instagram</small><strong>@mytribegym</strong></div></a>
        <a class="contact-item" href="{YOUTUBE}" target="_blank" rel="noopener">{ICON['yt']}<div><small>YouTube</small><strong>@mytribegym</strong></div></a>
      </div>
      <h3 style="margin:2rem 0 1rem">{'Opening hours' if en else 'أوقات الدوام'}</h3>
      {hours_block(lang)}
    </div>
    <div class="map reveal"><iframe src="{MAP_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="My Tribe Gym map"></iframe></div>
  </div>
</section>
{cta_band(lang)}"""

RENDER = {"index": p_index, "about": p_about, "programs": p_programs, "schedule": p_schedule, "coaches": p_coaches,
          "membership": p_membership, "facilities": p_facilities, "contact": p_contact}

def build():
    for lang in ("en", "ar"):
        outdir = ROOT if lang == "en" else os.path.join(ROOT, "ar")
        os.makedirs(outdir, exist_ok=True)
        for page in PAGES:
            html = head(lang, page) + header(lang, page) + RENDER[page](lang) + footer(lang)
            with open(os.path.join(outdir, f"{page}.html"), "w", encoding="utf-8") as f:
                f.write(html)
    print("built", 2 * len(PAGES), "pages")

if __name__ == "__main__":
    build()
