import streamlit as st
import streamlit.components.v1 as components
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from io import BytesIO

# ==========================
# 1. 頁面設定
# ==========================
st.set_page_config(
    page_title="高如慧 | Growth Marketing Lead",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 隱藏 Streamlit 預設元素，優化視覺
st.markdown("""
<style>
#MainMenu, footer, header, .stDeployButton {display: none !important;}
.stApp {background: #f5f5f5;}
.main .block-container {padding: 1rem; max-width: 900px;}
</style>
""", unsafe_allow_html=True)

# ==========================
# 2. 核心資料 (Resume Data)
# ==========================
resume_data = {
    "name": "高如慧",
    "title": "Growth Marketing（AI-Driven）｜11 年跨產業行銷實戰",
    "summary": "以「結構化策略＋SEO＋成效型投放＋AI 自動化」建立可複製的成長系統。曾主導 POPRORO 0→1（8 個月達成月營收 800 萬）、推動 MacLove「蘋果二手」核心關鍵字取得 Google 首位，並以自動化流程讓代操時間下降約 66%。累積服務保健、美妝、3C、服飾、醫美等 10+ 品牌。",
    "contact": ["rhk9903@gmail.com", "0988-663-166", "新北市汐止區", "淡江大學 經濟學系"],
    "metrics": [
        ("800萬", "POPRORO 月營收（8 個月）"),
        ("ROAS 5", "保健食品投放模型"),
        ("#1", "蘋果二手（Google）"),
        ("-66%", "代操維運時間")
    ],
    "experience": [
        {
            "company": "個人接案｜行銷顧問",
            "date": "2025/6 ~ 現在",
            "role": "AI＋自動化成效系統",
            "desc": "服務服飾／美妝／保健／醫美等產業。將代操維運由 30 分鐘壓縮至約 10 分鐘。協助香港包包品牌達成年營收 +187%、ROAS 約 4。"
        },
        {
            "company": "森宏生技 LOVITA｜行銷專案經理",
            "date": "2025/5 ~ 2025/10",
            "role": "",
            "desc": "Non-Branding SEO（B 群）佔前 5 名中 3 名。建立穩定 ROAS 5。新品年度計畫透過 AI GTM 一週完成。"
        },
        {
            "company": "麥克愛愛 MacLove｜電商／行銷經理",
            "date": "2024/9 ~ 2025/3",
            "role": "",
            "desc": "「蘋果二手」相關關鍵字取得 Google 第 1 名。Shopee 單月 89 萬（YoY +324%）。投放 ROAS 由 1 提升至 3。"
        },
        {
            "company": "歐賀服飾｜行銷經理",
            "date": "2023/12 ~ 2024/7",
            "role": "",
            "desc": "OMO 併入後電商營收 YoY +600%。LINE 會員 +700%，回購率 10%→25%。"
        },
        {
            "company": "高博士國際｜電商副理",
            "date": "2022/10 ~ 2023/11",
            "role": "",
            "desc": "打造「小白鞋」單月 490+ 雙。整體年營收 +30%。ROAS 維持 5+。擔任 CDP 導入與轉換流程改善。"
        },
        {
            "company": "個人接案｜行銷顧問",
            "date": "2022/4 ~ 2022/10",
            "role": "數位行銷顧問",
            "desc": "協助香港包包品牌、保健食品、醫美診所。保健品牌月營收由 100 萬穩定至 200 萬。"
        },
        {
            "company": "米波國際 meepShop｜行銷副理",
            "date": "2017/8 ~ 2022/3",
            "role": "",
            "desc": "主導 POPRORO 0→1，8 個月達成月營收 800 萬，淨利率 15–20%。管理 6 人團隊與月預算約 400 萬。"
        }
    ]
}

# ==========================
# 3. Word 生成功能 (精修版)
# ==========================
def create_word_resume():
    doc = Document()
    
    # 全局字型設定
    style = doc.styles['Normal']
    style.font.name = 'Arial'
    style.element.rPr.rFonts.set(qn('w:eastAsia'), '微軟正黑體')
    style.font.size = Pt(10)
    
    # 設定邊界 (適度縮窄)
    section = doc.sections[0]
    section.top_margin = Cm(1.27)
    section.bottom_margin = Cm(1.27)
    section.left_margin = Cm(1.5)
    section.right_margin = Cm(1.5)

    # --- Header (表格排版) ---
    table_header = doc.add_table(rows=1, cols=2)
    table_header.autofit = False
    table_header.columns[0].width = Cm(11) 
    table_header.columns[1].width = Cm(7) 

    # 左欄：姓名與職稱
    cell_name = table_header.cell(0, 0)
    p_name = cell_name.paragraphs[0]
    run_name = p_name.add_run(resume_data['name'])
    run_name.font.size = Pt(24)
    run_name.font.bold = True
    run_name.font.color.rgb = RGBColor(0, 0, 0)
    
    p_title = cell_name.add_paragraph()
    run_title = p_title.add_run(resume_data['title'])
    run_title.font.size = Pt(10)
    run_title.font.color.rgb = RGBColor(80, 80, 80)
    run_title.bold = True

    # 右欄：聯絡資訊 (靠右對齊)
    cell_contact = table_header.cell(0, 1)
    p_contact = cell_contact.paragraphs[0]
    p_contact.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    contact_text = "\n".join(resume_data['contact'])
    run_contact = p_contact.add_run(contact_text)
    run_contact.font.size = Pt(9)
    run_contact.font.color.rgb = RGBColor(100, 100, 100)

    doc.add_paragraph() # 空行

    # --- Professional Summary ---
    h_sum = doc.add_heading('PROFESSIONAL SUMMARY', level=1)
    for run in h_sum.runs:
        run.font.color.rgb = RGBColor(0, 0, 0)
        run.font.size = Pt(11)
    
    p_sum = doc.add_paragraph(resume_data['summary'])
    p_sum.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    doc.add_paragraph()

    # --- Key Metrics (儀表板表格) ---
    table_metrics = doc.add_table(rows=1, cols=4)
    table_metrics.style = 'Table Grid'
    
    for idx, (num, label) in enumerate(resume_data['metrics']):
        cell = table_metrics.cell(0, idx)
        p_num = cell.paragraphs[0]
        p_num.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_num = p_num.add_run(num)
        r_num.bold = True
        r_num.font.size = Pt(14)
        r_num.font.color.rgb = RGBColor(37, 99, 235) # 專業藍
        
        p_lbl = cell.add_paragraph(label)
        p_lbl.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_lbl.runs[0].font.size = Pt(8)
        p_lbl.runs[0].font.color.rgb = RGBColor(80, 80, 80)

    doc.add_paragraph()

    # --- Experience (隱形表格對齊) ---
    h_exp = doc.add_heading('EXPERIENCE', level=1)
    for run in h_exp.runs:
        run.font.color.rgb = RGBColor(0, 0, 0)
        run.font.size = Pt(11)

    for exp in resume_data['experience']:
        table_exp = doc.add_table(rows=1, cols=2)
        table_exp.autofit = False
        table_exp.columns[0].width = Cm(13)
        table_exp.columns[1].width = Cm(5)
        
        # 左欄
        cell_comp = table_exp.cell(0, 0)
        p_comp = cell_comp.paragraphs[0]
        r_comp = p_comp.add_run(f"{exp['company']}")
        r_comp.bold = True
        r_comp.font.size = Pt(11)
        
        if exp['role']:
             r_sep = p_comp.add_run(f" | {exp['role']}")
             r_sep.font.color.rgb = RGBColor(37, 99, 235)
             r_sep.bold = True

        # 右欄
        cell_date = table_exp.cell(0, 1)
        p_date = cell_date.paragraphs[0]
        p_date.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r_date = p_date.add_run(exp['date'])
        r_date.font.size = Pt(9)
        r_date.font.color.rgb = RGBColor(120, 120, 120)

        # 描述
        p_desc = doc.add_paragraph(exp['desc'])
        p_desc.paragraph_format.left_indent = Cm(0.5)
        p_desc.paragraph_format.space_after = Pt(12)

    # --- Skills (表格排版) ---
    h_skill = doc.add_heading('SKILLS & EXPERTISE', level=1)
    for run in h_skill.runs:
        run.font.color.rgb = RGBColor(0, 0, 0)
        run.font.size = Pt(11)

    table_skills = doc.add_table(rows=4, cols=2)
    table_skills.autofit = False
    table_skills.columns[0].width = Cm(4.5)
    table_skills.columns[1].width = Cm(13.5)

    skills_data = [
        ("Growth & Strategy", "0→1 品牌架構、成長策略、LTV/CAC 分析、漏斗優化"),
        ("AI & Automation", "AI 內容產製、Streamlit 工具開發、自動化診斷報表"),
        ("Digital Marketing", "FB/Google Ads、SEO (Non-Branding)、LINE OA、內容行銷"),
        ("Tools & Platforms", "GA4、GSC、Shopline、91APP、Mixpanel")
    ]

    for i, (cat, items) in enumerate(skills_data):
        cell_cat = table_skills.cell(i, 0)
        r_cat = cell_cat.paragraphs[0].add_run(cat)
        r_cat.bold = True
        r_cat.font.size = Pt(10)
        
        cell_item = table_skills.cell(i, 1)
        r_item = cell_item.paragraphs[0].add_run(items)
        r_item.font.size = Pt(10)

    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer

# ==========================
# 4. 側邊欄與 HTML 顯示
# ==========================
with st.sidebar:
    st.header("功能選單")
    docx_file = create_word_resume()
    st.download_button(
        label="📥 下載專業版 Word 履歷",
        data=docx_file,
        file_name="高如慧_Resume_Professional.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

# 顯示網頁版預覽 (HTML)
# 這裡簡單生成一個 HTML 視圖，確保網頁打開時不會空白
exp_html = ""
for exp in resume_data['experience']:
    exp_html += f"""
    <div style="margin-bottom:15px; border-left:3px solid #2563eb; padding-left:10px;">
        <div style="display:flex; justify-content:space-between;">
            <strong>{exp['company']}</strong>
            <span style="color:#666; font-size:0.9em;">{exp['date']}</span>
        </div>
        <div style="color:#2563eb; font-size:0.9em; font-weight:bold;">{exp['role']}</div>
        <div style="font-size:0.95em; color:#333; margin-top:5px;">{exp['desc']}</div>
    </div>
    """

html_content = f"""
<div style="font-family:'Noto Sans TC', sans-serif; padding:20px; background:white; border-radius:10px; box-shadow:0 2px 10px rgba(0,0,0,0.1);">
    <h1 style="border-bottom:2px solid #333; padding-bottom:10px;">{resume_data['name']}</h1>
    <div style="color:#666; margin-bottom:20px;">{resume_data['title']}</div>
    
    <div style="display:grid; grid-template-columns: repeat(4, 1fr); gap:10px; margin-bottom:30px;">
        {''.join([f'<div style="background:#f0f7ff; padding:10px; text-align:center; border-radius:5px;"><div style="color:#2563eb; font-weight:bold; font-size:1.2em;">{m[0]}</div><div style="font-size:0.8em; color:#666;">{m[1]}</div></div>' for m in resume_data['metrics']])}
    </div>

    <h3>EXPERIENCE</h3>
    {exp_html}
</div>
"""
components.html(html_content, height=1000, scrolling=True)
