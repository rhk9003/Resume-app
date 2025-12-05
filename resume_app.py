import streamlit as st

st.set_page_config(
    page_title="高如慧 | Growth Marketing Lead",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;600;700&display=swap');
    
    :root {
        --text: #1a1a1a;
        --text-light: #666;
        --accent: #2563eb;
        --border: #e5e5e5;
    }
    
    .stApp {
        background: white;
        font-family: 'Noto Sans TC', sans-serif;
    }
    
    .main .block-container {
        padding: 0;
        max-width: 210mm;
        min-height: 297mm;
        margin: 0 auto;
        background: white;
    }
    
    #MainMenu, footer, header, .stDeployButton {display: none !important;}
    
    .resume-container {
        width: 210mm;
        min-height: 297mm;
        padding: 12mm 15mm;
        margin: 0 auto;
        background: white;
        box-sizing: border-box;
        font-size: 9pt;
        line-height: 1.4;
        color: var(--text);
    }
    
    /* Header */
    .header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        border-bottom: 2px solid var(--text);
        padding-bottom: 8px;
        margin-bottom: 10px;
    }
    
    .name {
        font-size: 24pt;
        font-weight: 700;
        letter-spacing: -1px;
        margin: 0;
    }
    
    .title {
        font-size: 10pt;
        color: var(--text-light);
        margin-top: 2px;
    }
    
    .contact {
        text-align: right;
        font-size: 8pt;
        color: var(--text-light);
        line-height: 1.5;
    }
    
    /* Summary */
    .summary {
        font-size: 9pt;
        color: var(--text);
        margin-bottom: 10px;
        line-height: 1.5;
    }
    
    /* Section */
    .section-title {
        font-size: 10pt;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        border-bottom: 1px solid var(--border);
        padding-bottom: 3px;
        margin: 10px 0 6px;
        color: var(--text);
    }
    
    /* Two columns */
    .two-col {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 15px;
    }
    
    .three-col {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 8px;
    }
    
    /* Experience */
    .exp-item {
        margin-bottom: 8px;
    }
    
    .exp-header {
        display: flex;
        justify-content: space-between;
        align-items: baseline;
    }
    
    .exp-company {
        font-weight: 600;
        font-size: 9pt;
    }
    
    .exp-role {
        font-size: 8pt;
        color: var(--accent);
    }
    
    .exp-date {
        font-size: 7.5pt;
        color: var(--text-light);
    }
    
    .exp-desc {
        font-size: 8pt;
        color: var(--text-light);
        margin-top: 2px;
    }
    
    /* Skills */
    .skills-list {
        display: flex;
        flex-wrap: wrap;
        gap: 4px 8px;
    }
    
    .skill {
        font-size: 8pt;
        color: var(--text);
        background: #f5f5f5;
        padding: 2px 8px;
        border-radius: 3px;
    }
    
    /* Achievements */
    .achievement-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 8px;
        margin: 6px 0;
    }
    
    .achievement {
        text-align: center;
        padding: 6px;
        background: #fafafa;
        border-radius: 4px;
    }
    
    .achievement-num {
        font-size: 14pt;
        font-weight: 700;
        color: var(--accent);
    }
    
    .achievement-label {
        font-size: 7pt;
        color: var(--text-light);
    }
    
    /* Highlight */
    .hl { color: var(--accent); font-weight: 500; }
    
    @media print {
        .resume-container {
            width: 210mm;
            height: 297mm;
            padding: 10mm 12mm;
        }
    }
</style>

<div class="resume-container">
    <!-- Header -->
    <div class="header">
        <div>
            <div class="name">高如慧</div>
            <div class="title">AI-Driven Growth Lead ｜ 11+ 年跨產業行銷實戰</div>
        </div>
        <div class="contact">
            rhk9903@gmail.com<br>
            0988-663-166<br>
            新北市汐止區<br>
            淡江大學 經濟學系
        </div>
    </div>
    
    <!-- Summary -->
    <div class="summary">
        擅長以<b>結構化策略、SEO、成效型投放與 AI 自動化</b>建立可複製的成長引擎。0→1 品牌打造（POPRORO 8個月達月營收800萬）、SEO 統治級成果（MacLove 蘋果二手全站關鍵字 Google 第1名）、代操流程自動化（-66%）。已協助 10+ 品牌建立穩定成長模型。
    </div>
    
    <!-- Key Metrics -->
    <div class="achievement-grid">
        <div class="achievement">
            <div class="achievement-num">800萬</div>
            <div class="achievement-label">月營收 (8個月達成)</div>
        </div>
        <div class="achievement">
            <div class="achievement-num">ROAS 5</div>
            <div class="achievement-label">穩定投放成效</div>
        </div>
        <div class="achievement">
            <div class="achievement-num">#1</div>
            <div class="achievement-label">Google SEO 排名</div>
        </div>
        <div class="achievement">
            <div class="achievement-num">-66%</div>
            <div class="achievement-label">代操時間縮減</div>
        </div>
    </div>
    
    <!-- Experience -->
    <div class="section-title">工作經歷</div>
    
    <div class="two-col">
        <div>
            <div class="exp-item">
                <div class="exp-header">
                    <span class="exp-company">個人接案｜行銷顧問</span>
                    <span class="exp-date">2025/5 ~ 現在</span>
                </div>
                <div class="exp-role">AI＋自動化成效型行銷系統</div>
                <div class="exp-desc">服務服飾/美妝/保健/醫美等產業，代操維運 30→10分鐘。Doughnut 年營收 <span class="hl">+187%</span>、ROAS 4</div>
            </div>
            
            <div class="exp-item">
                <div class="exp-header">
                    <span class="exp-company">森宏生技 LOVITA｜行銷專案經理</span>
                    <span class="exp-date">2025/5 ~ 2025/10</span>
                </div>
                <div class="exp-desc">B群 Non-Branding SEO 佔搜尋前5名中3名，建立 <span class="hl">ROAS 5</span> 穩定投放模型。AI 輔助 GTM 一週完成新品年度計畫</div>
            </div>
            
            <div class="exp-item">
                <div class="exp-header">
                    <span class="exp-company">麥克愛愛 MacLove｜電商/行銷經理</span>
                    <span class="exp-date">2024/8 ~ 2025/3</span>
                </div>
                <div class="exp-desc">「蘋果電腦 二手」全型號 <span class="hl">Google 第1名</span>，Shopee 單月89萬 (YoY +324%)，ROAS 1→3</div>
            </div>
        </div>
        
        <div>
            <div class="exp-item">
                <div class="exp-header">
                    <span class="exp-company">歐賀服飾｜行銷經理</span>
                    <span class="exp-date">2023/12 ~ 2024/7</span>
                </div>
                <div class="exp-desc">OMO 整合電商營收 <span class="hl">YoY +600%</span>，LINE 會員 +700%，回購率 10%→25%</div>
            </div>
            
            <div class="exp-item">
                <div class="exp-header">
                    <span class="exp-company">高博士國際｜電商副理</span>
                    <span class="exp-date">2022/10 ~ 2023/11</span>
                </div>
                <div class="exp-desc">打造明星商品「小白鞋」單月 <span class="hl">490+ 雙</span>，年營收 +30%，ROAS 維持 5+，CDP 導入</div>
            </div>
            
            <div class="exp-item">
                <div class="exp-header">
                    <span class="exp-company">米波國際 meepShop｜行銷副理</span>
                    <span class="exp-date">2017/8 ~ 2022/3</span>
                </div>
                <div class="exp-desc">POPRORO <span class="hl">8個月 0→月營收800萬</span>，淨利率15-20%，管理6人團隊+月預算400萬。meepShop 官方講師培訓 50+ 人</div>
            </div>
        </div>
    </div>
    
    <!-- Skills & Expertise -->
    <div class="section-title">專業技能</div>
    
    <div class="three-col">
        <div>
            <div style="font-weight: 600; font-size: 8pt; margin-bottom: 4px;">Growth & Strategy</div>
            <div class="skills-list">
                <span class="skill">0→1 品牌架構</span>
                <span class="skill">成長策略</span>
                <span class="skill">LTV/CAC</span>
                <span class="skill">漏斗優化</span>
            </div>
        </div>
        <div>
            <div style="font-weight: 600; font-size: 8pt; margin-bottom: 4px;">Digital Marketing</div>
            <div class="skills-list">
                <span class="skill">FB/Google Ads</span>
                <span class="skill">SEO</span>
                <span class="skill">LINE OA</span>
                <span class="skill">內容行銷</span>
            </div>
        </div>
        <div>
            <div style="font-weight: 600; font-size: 8pt; margin-bottom: 4px;">Tools & Platform</div>
            <div class="skills-list">
                <span class="skill">GA/GSC</span>
                <span class="skill">Shopline</span>
                <span class="skill">91APP</span>
                <span class="skill">Mixpanel</span>
            </div>
        </div>
    </div>
    
    <div class="three-col" style="margin-top: 6px;">
        <div>
            <div style="font-weight: 600; font-size: 8pt; margin-bottom: 4px;">AI & Automation</div>
            <div class="skills-list">
                <span class="skill">AI 內容產製</span>
                <span class="skill">Vibe Coding</span>
                <span class="skill">自動化診斷</span>
            </div>
        </div>
        <div>
            <div style="font-weight: 600; font-size: 8pt; margin-bottom: 4px;">E-commerce & OMO</div>
            <div class="skills-list">
                <span class="skill">全通路營運</span>
                <span class="skill">CDP 導入</span>
                <span class="skill">會員經營</span>
            </div>
        </div>
        <div>
            <div style="font-weight: 600; font-size: 8pt; margin-bottom: 4px;">Management</div>
            <div class="skills-list">
                <span class="skill">團隊管理</span>
                <span class="skill">跨部門整合</span>
                <span class="skill">SOP 建立</span>
            </div>
        </div>
    </div>
    
    <!-- Key Projects -->
    <div class="section-title">代表專案</div>
    
    <div class="two-col">
        <div class="exp-item">
            <div class="exp-company">🎯 AI 行銷指揮中心</div>
            <div class="exp-desc">整合 SEO、廣告、社群、競品監測的一站式工具，日常維運自動化，已應用於保健/美妝/服飾/醫美等多產業</div>
        </div>
        <div class="exp-item">
            <div class="exp-company">📈 可複製 Growth 模型</div>
            <div class="exp-desc">「素材迭代→漏斗優化→一頁式轉換→再行銷矩陣」全通路架構，跨產業穩定達成 ROAS 4-5</div>
        </div>
    </div>
    
    <!-- Footer -->
    <div style="margin-top: 10px; padding-top: 8px; border-top: 1px solid var(--border); font-size: 8pt; color: var(--text-light); text-align: center;">
        <b>希望職稱</b>：行銷經理 ・ 數位行銷經理 ・ 電商品牌經理 ｜ <b>可上班日</b>：錄取後兩週 ｜ <b>希望地點</b>：台北市、新北市
    </div>
</div>
""", unsafe_allow_html=True)
