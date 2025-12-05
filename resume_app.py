import streamlit as st

# 頁面配置
st.set_page_config(
    page_title="高如慧 | Growth Marketing Lead",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 自定義 CSS 樣式
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;700;900&family=JetBrains+Mono:wght@400;500&display=swap');
    
    :root {
        --primary: #FF6B35;
        --secondary: #004E89;
        --accent: #00D9C0;
        --dark: #0D1117;
        --card-bg: #161B22;
        --text: #E6EDF3;
        --text-muted: #8B949E;
    }
    
    .stApp {
        background: linear-gradient(135deg, var(--dark) 0%, #1a1f2e 50%, var(--dark) 100%);
        font-family: 'Noto Sans TC', sans-serif;
    }
    
    .main .block-container {
        padding: 2rem 3rem;
        max-width: 1400px;
    }
    
    /* 隱藏 Streamlit 默認元素 */
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Hero 區塊 */
    .hero-section {
        background: linear-gradient(135deg, var(--card-bg) 0%, #1e2736 100%);
        border-radius: 24px;
        padding: 3rem;
        margin-bottom: 2rem;
        border: 1px solid rgba(255, 107, 53, 0.2);
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -20%;
        width: 400px;
        height: 400px;
        background: radial-gradient(circle, rgba(255, 107, 53, 0.1) 0%, transparent 70%);
        pointer-events: none;
    }
    
    .hero-name {
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, var(--primary) 0%, #FF8C5A 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
        letter-spacing: -2px;
    }
    
    .hero-title {
        font-size: 1.4rem;
        color: var(--accent);
        font-weight: 500;
        margin-bottom: 1.5rem;
        font-family: 'JetBrains Mono', monospace;
    }
    
    .hero-desc {
        font-size: 1.1rem;
        color: var(--text);
        line-height: 1.8;
        max-width: 800px;
    }
    
    /* 統計卡片 */
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .stat-card {
        background: var(--card-bg);
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        border: 1px solid rgba(0, 217, 192, 0.2);
        transition: all 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-4px);
        border-color: var(--accent);
        box-shadow: 0 8px 32px rgba(0, 217, 192, 0.15);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 900;
        color: var(--primary);
        font-family: 'JetBrains Mono', monospace;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: var(--text-muted);
        margin-top: 0.5rem;
    }
    
    /* 區塊標題 */
    .section-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: var(--text);
        margin: 2.5rem 0 1.5rem;
        padding-left: 1rem;
        border-left: 4px solid var(--primary);
    }
    
    /* 經歷卡片 */
    .exp-card {
        background: var(--card-bg);
        border-radius: 16px;
        padding: 1.5rem 2rem;
        margin-bottom: 1rem;
        border-left: 3px solid var(--primary);
        transition: all 0.3s ease;
    }
    
    .exp-card:hover {
        background: #1e2736;
        transform: translateX(8px);
    }
    
    .exp-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 0.8rem;
    }
    
    .exp-company {
        font-size: 1.2rem;
        font-weight: 700;
        color: var(--text);
    }
    
    .exp-role {
        font-size: 1rem;
        color: var(--accent);
        font-weight: 500;
    }
    
    .exp-date {
        font-size: 0.9rem;
        color: var(--text-muted);
        font-family: 'JetBrains Mono', monospace;
        background: rgba(255, 107, 53, 0.1);
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
    }
    
    .exp-achievement {
        font-size: 0.95rem;
        color: var(--text-muted);
        line-height: 1.6;
    }
    
    .highlight {
        color: var(--accent);
        font-weight: 600;
    }
    
    /* 技能標籤 */
    .skills-container {
        display: flex;
        flex-wrap: wrap;
        gap: 0.8rem;
        margin: 1.5rem 0;
    }
    
    .skill-tag {
        background: linear-gradient(135deg, rgba(255, 107, 53, 0.15) 0%, rgba(255, 107, 53, 0.05) 100%);
        color: var(--primary);
        padding: 0.6rem 1.2rem;
        border-radius: 25px;
        font-size: 0.9rem;
        font-weight: 500;
        border: 1px solid rgba(255, 107, 53, 0.3);
        transition: all 0.3s ease;
    }
    
    .skill-tag:hover {
        background: var(--primary);
        color: white;
        transform: scale(1.05);
    }
    
    .skill-tag.secondary {
        background: linear-gradient(135deg, rgba(0, 217, 192, 0.15) 0%, rgba(0, 217, 192, 0.05) 100%);
        color: var(--accent);
        border-color: rgba(0, 217, 192, 0.3);
    }
    
    .skill-tag.secondary:hover {
        background: var(--accent);
        color: var(--dark);
    }
    
    /* 成就區塊 */
    .achievement-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1.5rem;
        margin: 1.5rem 0;
    }
    
    .achievement-card {
        background: linear-gradient(135deg, var(--card-bg) 0%, #1a2332 100%);
        border-radius: 16px;
        padding: 1.5rem;
        border: 1px solid rgba(0, 78, 137, 0.3);
    }
    
    .achievement-title {
        font-size: 1rem;
        font-weight: 600;
        color: var(--text);
        margin-bottom: 0.5rem;
    }
    
    .achievement-desc {
        font-size: 0.9rem;
        color: var(--text-muted);
    }
    
    .achievement-metric {
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--accent);
        font-family: 'JetBrains Mono', monospace;
    }
    
    /* 聯繫資訊 */
    .contact-bar {
        display: flex;
        gap: 2rem;
        margin-top: 1.5rem;
        flex-wrap: wrap;
    }
    
    .contact-item {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        color: var(--text-muted);
        font-size: 0.95rem;
    }
    
    .contact-icon {
        width: 20px;
        height: 20px;
        color: var(--primary);
    }
    
    /* 兩欄布局 */
    .two-col {
        display: grid;
        grid-template-columns: 2fr 1fr;
        gap: 2rem;
    }
    
    /* 響應式設計 */
    @media (max-width: 768px) {
        .stats-grid {
            grid-template-columns: repeat(2, 1fr);
        }
        .two-col {
            grid-template-columns: 1fr;
        }
        .achievement-grid {
            grid-template-columns: 1fr;
        }
        .hero-name {
            font-size: 2.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Hero 區塊
st.markdown("""
<div class="hero-section">
    <div class="hero-name">高如慧</div>
    <div class="hero-title">AI-Driven Growth Lead | Marketing Strategist</div>
    <div class="hero-desc">
        擅長以<strong style="color: #FF6B35;">結構化策略、SEO 巨量內容架構、成效型投放與自動化工作流</strong>建立可複製的成長引擎。
        擁有 0→1 品牌打造、跨通路 SEO 統治級成果、以及代操工作流自動化的完整能力。
        近年已協助 <strong style="color: #00D9C0;">10+ 品牌</strong>在投放、官網、會員與 OMO 上建立穩定且可預測的成長模型。
    </div>
    <div class="contact-bar">
        <div class="contact-item">📧 rhk9903@gmail.com</div>
        <div class="contact-item">📱 0988-663-166</div>
        <div class="contact-item">📍 新北市汐止區</div>
        <div class="contact-item">🎓 淡江大學 經濟學系</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 核心數據統計
st.markdown("""
<div class="stats-grid">
    <div class="stat-card">
        <div class="stat-number">11+</div>
        <div class="stat-label">年行銷實戰經驗</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">800萬</div>
        <div class="stat-label">月營收 (POPRORO 8個月達成)</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">ROAS 5</div>
        <div class="stat-label">穩定投放成效</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">-66%</div>
        <div class="stat-label">代操維運時間縮減</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 兩欄布局：經歷 + 技能
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="section-title">💼 工作經歷</div>', unsafe_allow_html=True)
    
    # 經歷列表
    experiences = [
        {
            "company": "個人接案｜行銷顧問",
            "role": "AI＋自動化成效型行銷系統",
            "date": "2025/5 ~ 現在",
            "achievement": "服務 <span class='highlight'>服飾／美妝／保健／醫美</span> 等多產業，代操維運時間 30分鐘 → 10分鐘"
        },
        {
            "company": "森宏生技（LOVITA）",
            "role": "行銷專案經理",
            "date": "2025/5 ~ 2025/10",
            "achievement": "B群 Non-Branding SEO 佔據搜尋前五名中 3 名，ROAS 從 <1 提升至 <span class='highlight'>穩定 ROAS 5</span>"
        },
        {
            "company": "麥克愛愛（MacLove）",
            "role": "電商/行銷經理",
            "date": "2024/8 ~ 2025/3",
            "achievement": "「蘋果電腦 二手」全型號 <span class='highlight'>Google 第1名</span>，Shopee 單月 89萬 (YoY +324%)"
        },
        {
            "company": "歐賀服飾",
            "role": "行銷經理",
            "date": "2023/12 ~ 2024/7",
            "achievement": "OMO 整合電商營收 <span class='highlight'>YoY +600%</span>，LINE 會員 +700%，回購率 10%→25%"
        },
        {
            "company": "高博士國際",
            "role": "電商副理",
            "date": "2022/10 ~ 2023/11",
            "achievement": "打造明星商品「小白鞋」單月 <span class='highlight'>490+ 雙</span>，年營收 +30%，ROAS 維持 5+"
        },
        {
            "company": "米波國際（meepShop/POPRORO）",
            "role": "行銷副理｜管理 6 人團隊",
            "date": "2017/8 ~ 2022/3",
            "achievement": "POPRORO 8個月 <span class='highlight'>0→月營收800萬</span>，淨利率 15-20%，月預算 400萬"
        }
    ]
    
    for exp in experiences:
        st.markdown(f"""
        <div class="exp-card">
            <div class="exp-header">
                <div>
                    <div class="exp-company">{exp['company']}</div>
                    <div class="exp-role">{exp['role']}</div>
                </div>
                <div class="exp-date">{exp['date']}</div>
            </div>
            <div class="exp-achievement">{exp['achievement']}</div>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown('<div class="section-title">🛠️ 核心技能</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="skills-container">
        <span class="skill-tag">SEO 策略</span>
        <span class="skill-tag">成效型投放</span>
        <span class="skill-tag">AI 自動化</span>
        <span class="skill-tag">Growth Hacking</span>
        <span class="skill-tag secondary">Facebook Ads</span>
        <span class="skill-tag secondary">Google Ads</span>
        <span class="skill-tag secondary">LINE OA</span>
        <span class="skill-tag">OMO 整合</span>
        <span class="skill-tag">CDP 導入</span>
        <span class="skill-tag secondary">GA / GSC</span>
        <span class="skill-tag secondary">Mixpanel</span>
        <span class="skill-tag">內容行銷</span>
        <span class="skill-tag">電商營運</span>
        <span class="skill-tag secondary">Shopline</span>
        <span class="skill-tag secondary">91APP</span>
        <span class="skill-tag">團隊管理</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">🏆 代表成就</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="achievement-card" style="margin-bottom: 1rem;">
        <div class="achievement-metric">187%</div>
        <div class="achievement-title">Doughnut 年營收成長</div>
        <div class="achievement-desc">全年 ROAS 4</div>
    </div>
    <div class="achievement-card" style="margin-bottom: 1rem;">
        <div class="achievement-metric">$100</div>
        <div class="achievement-title">中醫醫美名單成本</div>
        <div class="achievement-desc">巧絲顏名漾診所</div>
    </div>
    <div class="achievement-card" style="margin-bottom: 1rem;">
        <div class="achievement-metric">5x</div>
        <div class="achievement-title">襪子選品店營收成長</div>
        <div class="achievement-desc">3萬 → 15萬/月</div>
    </div>
    <div class="achievement-card">
        <div class="achievement-metric">50+</div>
        <div class="achievement-title">品牌/行銷人培訓</div>
        <div class="achievement-desc">meepShop 官方講師</div>
    </div>
    """, unsafe_allow_html=True)

# 專案亮點
st.markdown('<div class="section-title">🚀 專案亮點</div>', unsafe_allow_html=True)

st.markdown("""
<div class="achievement-grid">
    <div class="achievement-card">
        <div class="achievement-title">🎯 AI 行銷指揮中心</div>
        <div class="achievement-desc">
            整合 SEO、廣告投放、社群內容、競品資訊與異常偵測的一站式工具。
            日常營運自動化：代操維運 30分鐘 → 10分鐘，已應用於保健、美妝、服飾、醫美等多產業。
        </div>
    </div>
    <div class="achievement-card">
        <div class="achievement-title">📈 可複製的 Growth 模型</div>
        <div class="achievement-desc">
            「素材迭代 → 漏斗優化 → 一頁式轉換 → 再行銷矩陣」的全通路架構，
            跨產業快速複製，穩定達成 ROAS 4-5 的成效標準。
        </div>
    </div>
    <div class="achievement-card">
        <div class="achievement-title">🔍 SEO 統治級策略</div>
        <div class="achievement-desc">
            MacLove「蘋果電腦 二手」全型號 Google 第1名。
            內容架構、樞紐頁面設計、AI 量產機制，形成品牌長期自然流量來源。
        </div>
    </div>
    <div class="achievement-card">
        <div class="achievement-title">🤖 AI + Vibe Coding</div>
        <div class="achievement-desc">
            AI 輔助 GTM 流程、內容產製、廣告診斷、異常偵測。
            一週內完成新品年度計畫與所有對外素材，大幅縮短上市準備時間。
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 底部資訊
st.markdown("""
<div style="text-align: center; margin-top: 3rem; padding: 2rem; color: #8B949E; font-size: 0.9rem;">
    <div style="margin-bottom: 0.5rem;">
        <span style="color: #FF6B35; font-weight: 600;">希望職稱</span>：行銷經理 ・ 數位行銷經理 ・ 電商品牌經理
    </div>
    <div>可上班日：錄取後兩週 ・ 希望地點：台北市、新北市</div>
</div>
""", unsafe_allow_html=True)
