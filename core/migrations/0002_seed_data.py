from django.db import migrations

SERVICES = [
    {
        "title": "Graphic Design",
        "slug": "graphic-design",
        "description": "Logos, brand identity, and social media creative that keeps your brand consistent everywhere.",
        "full_description": (
            "Your brand needs to look like the same brand everywhere it shows up — "
            "on your website, your packaging, and your Instagram feed.\n"
            "Our design team builds a visual identity from scratch or refreshes an "
            "existing one: logo, color palette, typography, and ready-to-use social "
            "media templates.\n"
            "Every deliverable comes with source files, so you always own your brand."
        ),
        "features": "Logo design & brand guidelines\nSocial media templates\nBusiness card & stationery design\nUnlimited revisions during the review round",
        "starting_price": "Starting at ₹7,999",
        "icon": "design",
        "order": 1,
    },
    {
        "title": "UI Design",
        "slug": "ui-design",
        "description": "Clean, usable interfaces for web apps, portfolios, and community platforms.",
        "full_description": (
            "A good-looking interface that's confusing to use still loses users.\n"
            "We design web and app interfaces with real usability testing behind "
            "every decision — from your homepage down to your checkout flow.\n"
            "You'll get a full, clickable prototype before a single line of code is written."
        ),
        "features": "Wireframes & clickable prototypes\nDesign system with reusable components\nMobile-responsive layouts\nHandoff-ready files for developers",
        "starting_price": "Starting at ₹11,999",
        "icon": "ui",
        "order": 2,
    },
    {
        "title": "Web Development",
        "slug": "web-development",
        "description": "Business sites, landing pages, and SEO-ready builds that load fast and convert.",
        "full_description": (
            "We build fast, secure, mobile-friendly websites — from a single "
            "landing page to a full multi-page business site with a backend.\n"
            "Every site we ship is optimized for search engines from day one, "
            "and comes with basic analytics wired in so you can see what's working.\n"
            "Need logins, payments, or a customer dashboard? We build that too."
        ),
        "features": "Responsive, SEO-ready builds\nContact forms & basic analytics\nCustom backends (Django, MySQL, etc.)\n30 days of post-launch support",
        "starting_price": "Starting at ₹14,999",
        "icon": "web",
        "order": 3,
    },
    {
        "title": "Digital Marketing",
        "slug": "digital-marketing",
        "description": "SEO, Google Ads, and Meta Ads campaigns built around real growth targets.",
        "full_description": (
            "Traffic without a plan doesn't grow a business.\n"
            "We run SEO, Google Ads, and Meta Ads campaigns tied to a real target — "
            "leads, sign-ups, or sales — and report back in numbers you can actually use.\n"
            "You'll always know exactly what your ad spend is doing."
        ),
        "features": "SEO audit & on-page optimization\nGoogle & Meta Ads management\nMonthly performance reporting\nLanding page conversion reviews",
        "starting_price": "Starting at ₹9,999 / month",
        "icon": "marketing",
        "order": 4,
    },
    {
        "title": "Video Editing",
        "slug": "video-editing",
        "description": "Reels, YouTube edits, and motion graphics that keep viewers watching.",
        "full_description": (
            "Short-form video drives more attention than almost anything else "
            "right now — but only if it's cut well.\n"
            "Our editors handle everything from raw footage to a finished reel: "
            "pacing, captions, sound design, and motion graphics.\n"
            "We work in the format your platform actually rewards."
        ),
        "features": "Reels & short-form edits\nYouTube long-form editing\nMotion graphics & captions\nFast turnaround for content calendars",
        "starting_price": "Starting at ₹1,499 / video",
        "icon": "video",
        "order": 5,
    },
    {
        "title": "Freelancer Community",
        "slug": "freelancer-community",
        "description": "Networking, collaboration, and learning support for the VSR freelancer network.",
        "full_description": (
            "VSR Digital Hub isn't just for clients — it's also a network for the "
            "freelancers who deliver the work.\n"
            "Members get access to shared briefs, collaboration on bigger projects, "
            "and skill-sharing sessions with other specialists in the hub.\n"
            "It's how we keep quality consistent across every service we offer."
        ),
        "features": "Access to shared project briefs\nCollaboration with other specialists\nSkill-sharing sessions\nAdmin & onboarding support",
        "starting_price": "",
        "icon": "community",
        "order": 6,
    },
]

PORTFOLIO_ITEMS = [
    {
        "title": "Retail Rebrand for Northline Foods",
        "slug": "northline-foods-rebrand",
        "client_name": "Northline Foods",
        "category": "Branding",
        "summary": "A full identity refresh for a regional grocery chain expanding into three new cities.",
        "full_description": (
            "Northline Foods came to us with a logo that hadn't changed in over a decade "
            "and a brand that no longer matched their newer stores.\n"
            "We rebuilt their identity from the ground up — new logo, packaging system, "
            "and in-store signage — while keeping the warmth long-time customers recognized."
        ),
        "outcome": "Rolled out across 12 stores with a 24% lift in reported brand recall in post-launch surveys.",
        "icon": "design",
        "order": 1,
    },
    {
        "title": "E-commerce Rebuild for Cursive Studio",
        "slug": "cursive-studio-ecommerce",
        "client_name": "Cursive Studio",
        "category": "Web Development",
        "summary": "A faster, mobile-first storefront replacing a slow legacy platform.",
        "full_description": (
            "Cursive Studio's old storefront took over 6 seconds to load on mobile and was "
            "losing checkouts. We rebuilt it on a lean, modern stack focused on speed.\n"
            "The new site loads in under 1.5 seconds and carries the same design language "
            "across every device."
        ),
        "outcome": "Mobile checkout completion rose 31% in the first month after launch.",
        "icon": "web",
        "order": 2,
    },
    {
        "title": "Lead Gen Campaign for Bright Path Realty",
        "slug": "bright-path-realty-leadgen",
        "client_name": "Bright Path Realty",
        "category": "Digital Marketing",
        "summary": "A Google & Meta Ads campaign built to fill a real estate agency's booking calendar.",
        "full_description": (
            "Bright Path Realty needed qualified viewing requests, not just clicks.\n"
            "We built targeted Google Search and Meta lead-form campaigns paired with a "
            "conversion-focused landing page, then optimized weekly based on real booking data."
        ),
        "outcome": "Cut cost-per-qualified-lead by 42% over the first quarter.",
        "icon": "marketing",
        "order": 3,
    },
    {
        "title": "App Interface for Loop Fitness",
        "slug": "loop-fitness-app-ui",
        "client_name": "Loop Fitness",
        "category": "UI Design",
        "summary": "A clean workout-tracking interface designed for daily use, not just first impressions.",
        "full_description": (
            "Loop Fitness's early prototype tested well in demos but frustrated real users "
            "within a week. We redesigned the core flows around actual gym-session behavior — "
            "big touch targets, minimal typing, one-handed use."
        ),
        "outcome": "Weekly active usage among beta testers increased by 58%.",
        "icon": "ui",
        "order": 4,
    },
]

TEAM_MEMBERS = [
    {
        "name": "Vikram Sharma",
        "slug": "vikram-sharma",
        "role": "Founder & Creative Director",
        "short_bio": "Leads brand and design strategy across every VSR project.",
        "full_bio": (
            "Vikram started VSR Digital Hub after a decade of freelance design work, "
            "tired of watching good projects fall apart from poor coordination between vendors.\n"
            "He now oversees creative direction across every project that comes through the hub."
        ),
        "email": "vikram@vsrdigitalhub.com",
        "linkedin_url": "https://www.linkedin.com",
        "order": 1,
    },
    {
        "name": "Sanya Rao",
        "slug": "sanya-rao",
        "role": "Lead Developer",
        "short_bio": "Builds and ships every web and backend project at VSR.",
        "full_bio": (
            "Sanya leads the development team, specializing in fast, secure builds on "
            "Django and modern JavaScript frameworks.\n"
            "She reviews every technical scope before a project is quoted, so estimates "
            "stay honest."
        ),
        "email": "sanya@vsrdigitalhub.com",
        "linkedin_url": "https://www.linkedin.com",
        "order": 2,
    },
    {
        "name": "Rahul Iyer",
        "slug": "rahul-iyer",
        "role": "Head of Digital Marketing",
        "short_bio": "Runs every paid campaign and SEO engagement at the hub.",
        "full_bio": (
            "Rahul has managed performance marketing budgets for brands across retail, "
            "real estate, and D2C, and joined VSR to build out its in-house marketing arm.\n"
            "He believes every ad rupee should be traceable to a result."
        ),
        "email": "rahul@vsrdigitalhub.com",
        "linkedin_url": "https://www.linkedin.com",
        "order": 3,
    },
    {
        "name": "Meera Nair",
        "slug": "meera-nair",
        "role": "UI/UX Designer",
        "short_bio": "Designs interfaces that get tested with real users, not just admired in demos.",
        "full_bio": (
            "Meera joined VSR from a product design background, and pushed the studio "
            "to add real usability testing to every UI engagement — not just visual polish.\n"
            "She's the one who insists on the clickable prototype before any code is written."
        ),
        "email": "meera@vsrdigitalhub.com",
        "linkedin_url": "https://www.linkedin.com",
        "order": 4,
    },
]

TESTIMONIALS = [
    {
        "client_name": "Anjali Menon",
        "client_role": "Founder, Northline Foods",
        "quote": "VSR handled our entire rebrand without a single miscommunication between design and print. That alone was worth it.",
        "rating": 5,
        "order": 1,
    },
    {
        "client_name": "Devansh Gupta",
        "client_role": "CEO, Cursive Studio",
        "quote": "Our new site loads faster than I thought was possible on our old platform. Checkout numbers went up almost immediately.",
        "rating": 5,
        "order": 2,
    },
    {
        "client_name": "Priya Balakrishnan",
        "client_role": "Marketing Lead, Bright Path Realty",
        "quote": "The reporting alone changed how we think about ad spend. We finally know which campaigns are actually working.",
        "rating": 4,
        "order": 3,
    },
]

PRICING_PLANS = [
    {
        "name": "Starter",
        "price": "₹7,999",
        "billing_period": "one-time project",
        "description": "For a single, focused deliverable.",
        "features": "1 core service (design, dev, or marketing)\n2 rounds of revisions\nEmail support\n7–10 day delivery",
        "is_featured": False,
        "order": 1,
    },
    {
        "name": "Growth",
        "price": "₹19,999",
        "billing_period": "one-time project",
        "description": "For businesses combining two or more services.",
        "features": "Up to 3 combined services\nUnlimited revisions during review\nDedicated project coordinator\nPriority support",
        "is_featured": True,
        "order": 2,
    },
    {
        "name": "Partner",
        "price": "Custom",
        "billing_period": "monthly retainer",
        "description": "Ongoing design, dev, and marketing support.",
        "features": "Full access to every VSR service\nMonthly strategy review\nDedicated account manager\n24/7 support desk",
        "is_featured": False,
        "order": 3,
    },
]

BLOG_POSTS = [
    {
        "title": "Why One Team Beats Five Freelancers",
        "slug": "why-one-team-beats-five-freelancers",
        "excerpt": "The hidden cost of coordinating separate vendors for design, dev, and marketing.",
        "content": (
            "Most small businesses don't hire one bad freelancer — they hire five good ones "
            "who never talk to each other.\n"
            "The logo doesn't match the website. The website doesn't match the ad creative. "
            "Every handoff adds a delay and a chance for something to get lost.\n"
            "A connected team removes that friction entirely, because the same people who "
            "understand your brand are the ones building your site and running your ads."
        ),
        "category": "Strategy",
        "author_slug": "vikram-sharma",
    },
    {
        "title": "5 Signs Your Website Is Costing You Customers",
        "slug": "5-signs-your-website-is-costing-you-customers",
        "excerpt": "Slow load times aren't the only thing quietly driving visitors away.",
        "content": (
            "A slow site is the obvious problem — but it's rarely the only one.\n"
            "Confusing navigation, a checkout that asks for too much too soon, and a mobile "
            "layout that was clearly an afterthought all chip away at conversions just as much.\n"
            "The fix usually isn't a full rebuild. It's a focused audit of the five or six "
            "moments where visitors actually decide to leave."
        ),
        "category": "Web Development",
        "author_slug": "sanya-rao",
    },
    {
        "title": "Ad Spend Without a Target Is Just Spend",
        "slug": "ad-spend-without-a-target-is-just-spend",
        "excerpt": "How to know if your Google or Meta Ads budget is actually working.",
        "content": (
            "Traffic is not a result. Impressions are not a result. A booked call, a "
            "completed sale, a qualified lead — those are results.\n"
            "Before any campaign goes live, we define what a 'win' actually looks like in "
            "numbers, then build every ad and landing page around driving toward it.\n"
            "It's the difference between a campaign you can optimize and one you're just hoping works."
        ),
        "category": "Digital Marketing",
        "author_slug": "rahul-iyer",
    },
]


def seed_data(apps, schema_editor):
    Service = apps.get_model("core", "Service")
    PortfolioItem = apps.get_model("core", "PortfolioItem")
    TeamMember = apps.get_model("core", "TeamMember")
    Testimonial = apps.get_model("core", "Testimonial")
    PricingPlan = apps.get_model("core", "PricingPlan")
    BlogPost = apps.get_model("core", "BlogPost")

    for entry in SERVICES:
        Service.objects.get_or_create(slug=entry["slug"], defaults=entry)

    for entry in PORTFOLIO_ITEMS:
        PortfolioItem.objects.get_or_create(slug=entry["slug"], defaults=entry)

    for entry in TEAM_MEMBERS:
        TeamMember.objects.get_or_create(slug=entry["slug"], defaults=entry)

    for entry in TESTIMONIALS:
        Testimonial.objects.get_or_create(client_name=entry["client_name"], defaults=entry)

    for entry in PRICING_PLANS:
        PricingPlan.objects.get_or_create(name=entry["name"], defaults=entry)

    for entry in BLOG_POSTS:
        data = dict(entry)
        author_slug = data.pop("author_slug", None)
        author = TeamMember.objects.filter(slug=author_slug).first() if author_slug else None
        data["author"] = author
        BlogPost.objects.get_or_create(slug=data["slug"], defaults=data)


def remove_data(apps, schema_editor):
    Service = apps.get_model("core", "Service")
    PortfolioItem = apps.get_model("core", "PortfolioItem")
    TeamMember = apps.get_model("core", "TeamMember")
    Testimonial = apps.get_model("core", "Testimonial")
    PricingPlan = apps.get_model("core", "PricingPlan")
    BlogPost = apps.get_model("core", "BlogPost")

    Service.objects.filter(slug__in=[s["slug"] for s in SERVICES]).delete()
    PortfolioItem.objects.filter(slug__in=[p["slug"] for p in PORTFOLIO_ITEMS]).delete()
    BlogPost.objects.filter(slug__in=[b["slug"] for b in BLOG_POSTS]).delete()
    TeamMember.objects.filter(slug__in=[t["slug"] for t in TEAM_MEMBERS]).delete()
    Testimonial.objects.filter(client_name__in=[t["client_name"] for t in TESTIMONIALS]).delete()
    PricingPlan.objects.filter(name__in=[p["name"] for p in PRICING_PLANS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_data, remove_data),
    ]
