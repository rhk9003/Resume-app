import streamlit as st
import streamlit.components.v1 as components
from docx import Document
from docx.shared import Pt, Cm, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from io import BytesIO

# ... (前面的 setup 和 resume_data 保持不變) ...

# ==========================
# 輔助函式：設定表格框線 (用於標題底線)
# ==========================
def set_table_bottom_border(table):
    tbl = table._tbl
    tblPr = tbl.tblPr
    tblBorders = OxmlElement('w:tblBorders')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '4') # 線條粗細
    bottom.set(qn('w:space'), '0')
    bottom.set(qn('w:color'), '000000')
    tblBorders.append(bottom)
    tblPr.append(tblBorders)

# ==========================
# 功能：生成 專業版 Word 檔
# ==========================
def create_word_resume():
    doc = Document()
    
    # 全局字型設定
    style = doc.styles['Normal']
    style.font.name = 'Arial'
    style.element.rPr.rFonts.set(qn('w:eastAsia'), '微軟正黑體')
    style.font.size = Pt(10)
    
    # 設定邊界 (適度縮窄以容納更多內容)
    section = doc.sections[0]
    section.top_margin = Cm(1.27)
    section.bottom_margin = Cm(1.27)
    section.left_margin = Cm(1.5)
    section.right_margin = Cm(1.5)

    # -------------------------------------------------------
    # 1. Header (姓名與聯絡資訊)
    # -------------------------------------------------------
    # 使用表格來做左右佈局，讓聯絡資訊整齊靠右
    table_header = doc.add_table(rows=1, cols=2)
    table_header.autofit = False
    table_header.columns[0].width = Cm(11) # 左邊寬一點放名字
    table_header.columns[1].width = Cm(7)  # 右邊放聯絡資訊

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

    # -------------------------------------------------------
    # 2. Professional Summary
    # -------------------------------------------------------
    h_sum = doc.add_heading('PROFESSIONAL SUMMARY', level=1)
    h_sum.style.font.color.rgb = RGBColor(0, 0, 0)
    # 強制設定標題格式 (大寫、黑色、帶底線)
    for run in h_sum.runs:
        run.font.color.rgb = RGBColor(0, 0, 0)
        run.font.size = Pt(11)
    
    p_sum = doc.add_paragraph(resume_data['summary'])
    p_sum.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    doc.add_paragraph() # 空行

    # -------------------------------------------------------
    # 3. Key Metrics (數據儀表板)
    # -------------------------------------------------------
    # 使用 1x4 表格來呈現數據，並加上灰色背景或邊框讓它跳出來
    table_metrics = doc.add_table(rows=1, cols=4)
    table_metrics.style = 'Table Grid' # 加上格線讓它看起來像 Dashboard
    
    for idx, (num, label) in enumerate(resume_data['metrics']):
        cell = table_metrics.cell(0, idx)
        # 數據
        p_num = cell.paragraphs[0]
        p_num.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_num = p_num.add_run(num)
        r_num.bold = True
        r_num.font.size = Pt(14)
        r_num.font.color.rgb = RGBColor(37, 99, 235) # 專業藍
        
        # 標籤
        p_lbl = cell.add_paragraph(label)
        p_lbl.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_lbl.runs[0].font.size = Pt(8)
        p_lbl.runs[0].font.color.rgb = RGBColor(80, 80, 80)

    doc.add_paragraph() # 空行

    # -------------------------------------------------------
    # 4. Experience (經歷)
    # -------------------------------------------------------
    h_exp = doc.add_heading('EXPERIENCE', level=1)
    for run in h_exp.runs:
        run.font.color.rgb = RGBColor(0, 0, 0)
        run.font.size = Pt(11)

    for exp in resume_data['experience']:
        # 使用隱形表格來對齊：左邊是公司職稱，右邊是日期
        table_exp = doc.add_table(rows=1, cols=2)
        table_exp.autofit = False
        table_exp.columns[0].width = Cm(13)
        table_exp.columns[1].width = Cm(5)
        
        # 左欄：公司名稱 | 職稱
        cell_comp = table_exp.cell(0, 0)
        p_comp = cell_comp.paragraphs[0]
        r_comp = p_comp.add_run(f"{exp['company']}")
        r_comp.bold = True
        r_comp.font.size = Pt(11)
        
        if exp['role']:
             r_sep = p_comp.add_run(f" | {exp['role']}")
             r_sep.font.color.rgb = RGBColor(37, 99, 235)
             r_sep.bold = True

        # 右欄：日期 (靠右)
        cell_date = table_exp.cell(0, 1)
        p_date = cell_date.paragraphs[0]
        p_date.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r_date = p_date.add_run(exp['date'])
        r_date.font.size = Pt(9)
        r_date.font.color.rgb = RGBColor(120, 120, 120)

        # 內容描述 (Bullet points)
        # 將長字串依句點拆分，模擬 bullet points 效果，或是直接輸出
        p_desc = doc.add_paragraph(exp['desc'])
        p_desc.paragraph_format.left_indent = Cm(0.5) # 稍微縮排
        p_desc.paragraph_format.space_after = Pt(12) # 段落間距

    # -------------------------------------------------------
    # 5. Skills (技能)
    # -------------------------------------------------------
    h_skill = doc.add_heading('SKILLS & EXPERTISE', level=1)
    for run in h_skill.runs:
        run.font.color.rgb = RGBColor(0, 0, 0)
        run.font.size = Pt(11)

    # 使用表格排列技能
    table_skills = doc.add_table(rows=4, cols=2)
    table_skills.autofit = False
    table_skills.columns[0].width = Cm(4.5) # 類別欄寬
    table_skills.columns[1].width = Cm(13.5) # 內容欄寬

    skills_data = [
        ("Growth & Strategy", "0→1 品牌架構、成長策略、LTV/CAC 分析、漏斗優化"),
        ("AI & Automation", "AI 內容產製、Streamlit 工具開發、自動化診斷報表"),
        ("Digital Marketing", "FB/Google Ads、SEO (Non-Branding)、LINE OA、內容行銷"),
        ("Tools & Platforms", "GA4、GSC、Shopline、91APP、Mixpanel")
    ]

    for i, (cat, items) in enumerate(skills_data):
        # 類別
        cell_cat = table_skills.cell(i, 0)
        r_cat = cell_cat.paragraphs[0].add_run(cat)
        r_cat.bold = True
        r_cat.font.size = Pt(10)
        
        # 項目
        cell_item = table_skills.cell(i, 1)
        r_item = cell_item.paragraphs[0].add_run(items)
        r_item.font.size = Pt(10)

    # 存入 BytesIO
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer

# ... (Sidebar 下載按鈕部分保持不變) ...
